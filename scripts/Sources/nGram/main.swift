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

// Actual NGram Logic
func runNGram(N: Int) {

    // dictionary to store words and their frequencies
    var nGramFreq : [String:[String:Int]] = [:]

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
        text = text.replacingOccurrences(of: "\\p{P}", with: "\n", options: .regularExpression)
        text = text.replacingOccurrences(of: "\\d", with: "\n", options: .regularExpression)
        text = text.replacingOccurrences(of: "\\t", with: "\n", options: .regularExpression)
        var newText = text.replacingOccurrences(of: "\\s\\s+", with: "\n", options: .regularExpression)
        while text != newText {
            text = newText
            newText = text.replacingOccurrences(of: "\\s\\s+", with: "\n", options: .regularExpression)
        }
        
        text = Naqqash.removeDiacritics(text, ofType: Naqqash.DiacriticType.NonEssential)
        
        // go through each character
        var word = ""
        var words: [String] = []
        for char in text {
            var c = char
            
            // add to word if letter
            if Naqqash.isLetter(c) {
                if Naqqash.isDecomposable(c) { c = Naqqash.decompose(c) }
                word += String(c)
            }
            
            // if at end of words
            if c == " " || c == "\n" {
                
                // add word to buffer, if for some reason word is empty at word boundary, reset buffer
                if word == "" {
                    words = []
                } else {
                    words.append(word)
                    word = ""
                }
                
                // record nGram if of appropriate size
                if words.count == N {
                    
                    // formulate keys
                    var firstKey = ""
                    for i in 0..<words.count-1 {
                        firstKey += words[i]
                        if i != words.count-2 { firstKey += " " }
                    }
                    let secondKey = words[words.count-1]

                    // add to dictionary
                    if nGramFreq[firstKey] == nil {
                        nGramFreq[firstKey] = [secondKey: 1]
                    } else if nGramFreq[firstKey]![secondKey] == nil {
                        nGramFreq[firstKey]!.updateValue(1, forKey: secondKey)
                    } else {
                        let freq = nGramFreq[firstKey]![secondKey]!
                        nGramFreq[firstKey]!.updateValue(freq + 1, forKey: secondKey)
                    }

                    // move word buffer forward
                    words.removeFirst()
                }
            }
                
            // if nGram breaks before required length ignore
            if c == "\n" && words.count < N {
                word = ""
                words = []
            }
        }
    }

    // remove nGrams that only have one entry
    for (prefix, var suffixes) in nGramFreq {
        for (suffix, count) in suffixes {
            if count <= 1 {
                suffixes.removeValue(forKey: suffix)
            }
        }
        if suffixes.count > 0 { nGramFreq.updateValue(suffixes, forKey: prefix) }
        else { nGramFreq.removeValue(forKey: prefix) }
    }
    
    // write to file
    let outputPath = "../stats/\(N)-Gram"
    let outputStream = OutputStream.init(toFileAtPath: outputPath, append: false)
    outputStream?.open()
    JSONSerialization.writeJSONObject(nGramFreq,
                                      to: outputStream!,
                                      options: [.prettyPrinted],
                                      error: nil)
    outputStream?.close()
}

// Choices of N to run the script on
for N in 2...4 {
    runNGram(N: N)
}
