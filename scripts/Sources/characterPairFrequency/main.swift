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
        text.append("\n")
    }

    func parser(_ parser: XMLParser,
                foundCharacters string: String) {
        if readText { text.append(string) }
    }
}

struct Correction: Hashable {
    var text: String
    var suggestedCorrection: String
}


// dictionary to store words and their frequencies
var charFreq : [String:Int] = [:]

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
    
    // replace all punctuation, digits and tabs with new lines, replace consecutive new lines with a single new line
    text = text.replacingOccurrences(of: "[\\p{Lu}\\p{Ll}\\p{Lt}\\p{Lm}\\p{M}\\p{N}\\p{P}\\p{S}\\p{C}]", with: "\n", options: .regularExpression)
    text = text.replacingOccurrences(of: "\\n\\n+", with: "\n", options: .regularExpression)
    
    // go through each character
    var currentChar: String?
    var lastChar: String?
    for c in text {
        
        // add to word if letter
        if Naqqash.isLetter(c) {
            lastChar = currentChar
            currentChar = String(c)
        }
        
        if lastChar != nil && currentChar != nil {
            let key = lastChar! + currentChar!
            charFreq.updateValue((charFreq[key] ?? 0) + 1, forKey: key)
        }
    }
}

// format output
let sortedCharFreq = charFreq.sorted { $0.value > $1.value }
var output = ""
print("{", to: &output)
for item in sortedCharFreq {
    print("\t\"\(item.key)\" : \(item.value),", to: &output)
}
output.removeLast(2)
print("\n}", to: &output)

// write to file
let file = URL(fileURLWithPath: "../stats/characterPairFrequency")
try! output.write(to: file, atomically: false, encoding: .utf8)
