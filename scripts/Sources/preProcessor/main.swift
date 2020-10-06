import Foundation
import Naqqash

// get file URLs from ../text directory
let textDirectoryPath = "../tex/"
let textDirectoryURL: URL = NSURL.fileURL(withPath: textDirectoryPath)
let files = try! FileManager.default.contentsOfDirectory(at: textDirectoryURL,
                                                         includingPropertiesForKeys: nil,
                                                         options: [.skipsHiddenFiles])

for file in files {
    print("Processing \(file)")

    let contents = try! String(contentsOf: file)

    // check if valid xml
    do {
        let _ = try XMLDocument(xmlString: contents, options: .documentIncludeContentTypeDeclaration)
    } catch {
        print("Bad xml \(file)")
        continue
    }

    var modified = ""
    // decompose any character that needs to be decombposed
    for char in contents {
        var c = char
        if Naqqash.isDecomposable(c) { c = Naqqash.decompose(c) }
        modified += String(char)
    }
    // write to file
    do {
        try modified.write(to: file,
                       atomically: true,
                       encoding: String.Encoding.utf8)
    } catch {
        print("Failed to write file \(file)")
    }
}
