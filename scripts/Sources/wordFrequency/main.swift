import Foundation

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

// get file URLs from ../text directory
let textDirectoryPath: URL = NSURL.fileURL(withPath:"../text/")
let files = try! FileManager.default.contentsOfDirectory(at: textDirectoryPath, includingPropertiesForKeys: nil, options: [.skipsHiddenFiles])

for file in files {
    
    // to test only run it on one file
    if !file.absoluteString.hasSuffix("0002.xml") {
        continue
    }
    
    let parserDelegate = ParserDelegate()
    if let parser = XMLParser(contentsOf: file) {
        parser.delegate = parserDelegate
        parser.parse()
    }
    
    let text = parserDelegate.text
    print(text)
    
}
