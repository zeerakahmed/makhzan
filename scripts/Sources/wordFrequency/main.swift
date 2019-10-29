import Foundation

// get file URLs from ../text directory
let textDirectoryPath: URL = NSURL.fileURL(withPath:"../text/")
let files = try! FileManager.default.contentsOfDirectory(at: textDirectoryPath, includingPropertiesForKeys: nil, options: [.skipsHiddenFiles])

for file in files {
    var text = try? String(contentsOf: file)
}
