import Foundation
import Naqqash

// Logic for what to do as the XML parser reads the file
class ParserDelegate: NSObject, XMLParserDelegate {
    var text = ""
    var readText = false
    
    func parser(_ parser: XMLParser,
                didStartElement elementName: String,
                namespaceURI: String?,
                qualifiedName qName: String?,
                attributes attributeDict: [String : String] = [:]) {
        if elementName == "title" { readText = true }
        if elementName == "body" { readText = true }
        if elementName == "annotation" { readText = false }
    }

    func parser(_ parser: XMLParser,
                didEndElement elementName: String,
                namespaceURI: String?,
                qualifiedName qName: String?) {
        if elementName == "title" { readText = false }
        if elementName == "annotation" { readText = true }
    }

    func parser(_ parser: XMLParser,
                foundCharacters string: String) {
        if readText { text.append(string) }
    }
}

// dictionary to store words and their frequencies
var wordFreq : [String:Int] = [:]

// get file URLs from ../text directory
let textDirectoryPath = "../text/"
let textDirectoryURL: URL = NSURL.fileURL(withPath: textDirectoryPath)
let files = try! FileManager.default.contentsOfDirectory(at: textDirectoryURL,
                                                         includingPropertiesForKeys: nil,
                                                         options: [.skipsHiddenFiles])

// process every file
for file in files {
    
    // get the relevant text from the text file
    let parserDelegate = ParserDelegate()
    if let parser = XMLParser(contentsOf: file) {
        parser.delegate = parserDelegate
        parser.parse()
    }
    var text = parserDelegate.text
    
    // remove punctuation, numbers, extraneous whitespace and non-essential diacritics
    var charactersToRemove = CharacterSet()
    charactersToRemove.formUnion(.punctuationCharacters)
    charactersToRemove.formUnion(.decimalDigits)
    text.removeAll { String($0).rangeOfCharacter(from:charactersToRemove) != nil }
    text = text.replacingOccurrences(of: "\\s+", with: " ", options: .regularExpression)
    text = Naqqash.removeDiacritics(text, ofType: Naqqash.DiacriticType.NonEssential)
    
    // go through each character
    var word = ""
    for char in text {
        var c = char
        
        // add to word if letter
        if Naqqash.isLetter(c) {
            if Naqqash.isDecomposable(c) { c = Naqqash.decompose(c) }
            word += String(c)
        }
        
        // add to dictionary if end of word
        else if c == " " {
            // ignore if word is an empty string, can happen if we removed some non-letter characters that were their own words
            if word == "" { 
                continue 
            }
            // add to dictionary if not there
            if wordFreq.index(forKey: word) == nil {
                wordFreq[word] = 1
            } 

            // increment if already in dictionary
            else {
                let count = wordFreq[word]!
                wordFreq.updateValue(count + 1, forKey: word)
            }

            // reset word
            word = ""
        }
        
        // ignore any other characters
        else {
            continue
        }
    }
}

// write to file
var outputPath = "../stats/wordFrequency"
var outputStream = OutputStream.init(toFileAtPath: outputPath, append: false)
outputStream?.open()
JSONSerialization.writeJSONObject(wordFreq,
                                  to: outputStream!,
                                  options: [.prettyPrinted],
                                  error: nil)
outputStream?.close()

