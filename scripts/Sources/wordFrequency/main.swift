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
        if elementName == "body" { readText = true }
        if elementName == "annotation" { readText = false }
    }

    func parser(_ parser: XMLParser,
                didEndElement elementName: String,
                namespaceURI: String?,
                qualifiedName qName: String?) {
        if elementName == "annotation" { readText = true }
    }

    func parser(_ parser: XMLParser,
                foundCharacters string: String) {
        if readText { text.append(string) }
    }
}

var wordFreq: [String: Int]

// get file URLs from ../text directory
let textDirectoryPath: URL = NSURL.fileURL(withPath:"../text/")
let files = try! FileManager.default.contentsOfDirectory(at: textDirectoryPath, includingPropertiesForKeys: nil, options: [.skipsHiddenFiles])

// process every file
for file in files {
    
    // to test only run it on one file
    if !file.absoluteString.hasSuffix("0002.xml") {
        continue
    }
    
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
     
    // split into words
    print(text)
}
