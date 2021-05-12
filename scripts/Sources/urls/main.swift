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
        if elementName == "link" { readText = true }
    }

    func parser(_ parser: XMLParser,
                didEndElement elementName: String,
                namespaceURI: String?,
                qualifiedName qName: String?) {
        if elementName == "link" { readText = false }
    }

    func parser(_ parser: XMLParser,
                foundCharacters string: String) {
        if readText { text.append(string) }
    }
}

// get file URLs from ../text directory
let textDirectoryPath = "../text/"
let textDirectoryURL: URL = NSURL.fileURL(withPath: textDirectoryPath)
let files = try! FileManager.default.contentsOfDirectory(at: textDirectoryURL,
                                                         includingPropertiesForKeys: nil,
                                                         options: [.skipsHiddenFiles])

// output string
var output = ""

// process every file
for file in files {
    
    // get the relevant text from the text file
    let parserDelegate = ParserDelegate()
    if let parser = XMLParser(contentsOf: file) {
        parser.delegate = parserDelegate
        parser.parse()
    }
    var text = parserDelegate.text
    
    // correct xml flags and add to output
    text = text.replacingOccurrences(of: "&amp;", with: "&")
    output += file.lastPathComponent + "\t" + text + "\n"
    
}

// write to file
let file = URL(fileURLWithPath: "../stats/urls")
try! output.write(to: file, atomically: false, encoding: .utf8)
