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


// read wordFrequency into dictionary
var path = "../stats/WordFrequency"
var inputStream = InputStream.init(fileAtPath: path)
inputStream?.open()
var wordFrequencyDict =  try! JSONSerialization.jsonObject(with: inputStream!, options: []) as! [String: Int]
inputStream?.close()

// read 2Gram
path = "../stats/2-Gram"
inputStream = InputStream.init(fileAtPath: path)
inputStream?.open()
var BigramDict =  try! JSONSerialization.jsonObject(with: inputStream!, options: []) as! [String: [String: Int]]
inputStream?.close()

// read approveList
let data = try String(contentsOfFile: "./Sources/wordBreakingValidator/approveList", encoding: .utf8)
let approveList = data.components(separatedBy: .newlines)

// get file URLs from ../text directory
let textDirectoryPath = "../text/"
let textDirectoryURL: URL = NSURL.fileURL(withPath: textDirectoryPath)
let files = try! FileManager.default.contentsOfDirectory(at: textDirectoryURL,
                                                         includingPropertiesForKeys: nil,
                                                         options: [.skipsHiddenFiles])

var correctionList: [Correction: Int] = [:]

func addToCorrectionList(_ c: Correction) {
    if correctionList[c] == nil {
        correctionList[c] = 1
    } else {
        correctionList[c] = correctionList[c]! + 1
    }
}

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
    text = text.replacingOccurrences(of: "\\W", with: " ", options: .regularExpression)
    text = text.replacingOccurrences(of: "\\d", with: " ", options: .regularExpression)
    text = text.replacingOccurrences(of: "\\s+", with: " ", options: .regularExpression)
    text = Naqqash.removeDiacritics(text, ofType: Naqqash.DiacriticType.NonEssential)
    
    // go through each character
    var currentWord = ""
    var lastWord: String?
    for c in text {
        
        // add to word if letter
        if Naqqash.isLetter(c) {
            currentWord += String(c)
        }
        
        // if at end of word
        if (c == " " || c == "\n") && currentWord.count > 0 {
            
            // break word into two and see if it needs to be broken
            var j = currentWord.index(after: currentWord.startIndex)
            while (j < currentWord.endIndex) {
                let s = String(currentWord[..<j])
                let t = String(currentWord[j...])
                if (wordFrequencyDict[s] != nil &&
                    wordFrequencyDict[t] != nil &&
                    s.count > 1 &&
                    t.count > 1 &&
                    wordFrequencyDict[s]! > 100 &&
                    wordFrequencyDict[t]! > 100 &&
                    BigramDict[s]?[t] ?? 0 > wordFrequencyDict[currentWord]! &&
                    !approveList.contains(currentWord)) {
                    addToCorrectionList(Correction(text: currentWord,
                                                   suggestedCorrection: "\(s) \(t)"))
                }
                j = currentWord.index(after: j)
            }
            
            if lastWord != nil {
                let s = currentWord + lastWord!
                if (wordFrequencyDict[s] != nil &&
                    !approveList.contains(s) &&
                    wordFrequencyDict[s]! > (wordFrequencyDict[currentWord] ?? 0) &&
                    wordFrequencyDict[s]! > (wordFrequencyDict[lastWord!] ?? 0)
                    ) {
                    addToCorrectionList(Correction(text: "\(currentWord) \(lastWord!)",
                                                   suggestedCorrection: s))
                }
            }
            
            lastWord = currentWord
            currentWord = ""
        }
    }
}

// format output
let sortedCorrections = correctionList.sorted { $0.value > $1.value }
var totalErrorFreq = 0
for c in sortedCorrections {
    totalErrorFreq += c.value
}
var output = ""
print("\(sortedCorrections.count) suggested corrections", to: &output)
print("\(totalErrorFreq) total frequency\n", to: &output)
for c in sortedCorrections {
    print("Text: \(c.key.text)", to: &output)
    print("Suggestion: \(c.key.suggestedCorrection)", to: &output)
    print("Frequency: \(c.value)", to: &output)
    print("", to: &output)
}

// write to file
let file = URL(fileURLWithPath: "../stats/wordBreakingErrors")
try! output.write(to: file, atomically: false, encoding: .utf8)
