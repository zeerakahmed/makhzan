/*
  Used to replace strings in the entire corpus. At the moment this is specifically designed to fix word breaking errors. In the 'replacements' file, each line of text has the text to find and the text to replace it with, separated by a tab character.
*/

import Foundation
import Naqqash

// read replacements
let data = try String(contentsOfFile: "./Sources/stringReplacer/replacements", encoding: .utf8)
let replacements = data.components(separatedBy: .newlines)

// get file URLs from ../text directory
let textDirectoryPath = "../text/"
let textDirectoryURL: URL = NSURL.fileURL(withPath: textDirectoryPath)
let files = try! FileManager.default.contentsOfDirectory(at: textDirectoryURL,
                                                         includingPropertiesForKeys: nil,
                                                         options: [.skipsHiddenFiles])

for file in files {
    var text = try! String(contentsOf: file)
    
    for r in replacements {
        if r == "" { continue }
        let data = r.components(separatedBy: "\t")
        let find = #"(?<!\p{Lo})\#(data[0])(?!\p{Lo})"#
        let replace = data[1]
        text = text.replacingOccurrences(of: find, with: replace, options: .regularExpression)
    }
    
    // write to file
    do {
        try text.write(to: file,
                       atomically: true,
                       encoding: String.Encoding.utf8)
    } catch {
        print("Failed to write file \(file)")
    }
    
    break
}
