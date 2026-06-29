/*
  Used to replace strings in the entire corpus. At the moment this is specifically designed to fix word breaking errors. In the 'replacements' file, each line of text has the text to find and the text to replace it with, separated by a tab character.
*/

import Foundation
import Naqqash

// read replacements
let data = try String(contentsOfFile: "./Sources/stringReplacer/replacements", encoding: .utf8)
let replacements = data.components(separatedBy: .newlines)

// pre-compile all regex patterns once
let compiledReplacements: [(NSRegularExpression, String)] = replacements.compactMap { r in
    if r == "" { return nil }
    let parts = r.components(separatedBy: "\t")
    guard parts.count >= 2 else { return nil }
    let pattern = "(?<!\\p{Lo})\(NSRegularExpression.escapedPattern(for: parts[0]))(?!\\p{Lo})"
    guard let regex = try? NSRegularExpression(pattern: pattern) else { return nil }
    return (regex, parts[1])
}

// get file URLs from ../text directory
let textDirectoryPath = "../text/"
let textDirectoryURL: URL = NSURL.fileURL(withPath: textDirectoryPath)
let files = try! FileManager.default.contentsOfDirectory(at: textDirectoryURL,
                                                         includingPropertiesForKeys: nil,
                                                         options: [.skipsHiddenFiles])

let total = files.count
for (index, file) in files.enumerated() {
    let current = index + 1
    print("\r\(current)/\(total) \(file.lastPathComponent)", terminator: "")
    fflush(stdout)

    autoreleasepool {
        var text = try! String(contentsOf: file)

        for (regex, replace) in compiledReplacements {
            let range = NSRange(text.startIndex..., in: text)
            text = regex.stringByReplacingMatches(in: text, range: range, withTemplate: replace)
        }

        do {
            try text.write(to: file, atomically: true, encoding: .utf8)
        } catch {
            print("\nFailed to write file \(file)")
        }
    }
}
print("\nDone.")
