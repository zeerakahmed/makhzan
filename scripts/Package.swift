// swift-tools-version:5.1
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "scripts",
    dependencies: [
        .package(url: "https://github.com/zeerakahmed/naqqash", from: "0.1.0"),
    ],
    targets: [
        .target(
            name: "preProcessor",
            dependencies: ["Naqqash"]
        ),
        .target(
            name: "wordFrequency",
            dependencies: ["Naqqash"]
        ),
        .target(
            name: "characterFrequency",
            dependencies: ["Naqqash"]
        ),
        .target(
            name: "diacriticFrequency",
            dependencies: ["Naqqash"]
        ),
        .target(
            name: "nGram",
            dependencies: ["Naqqash"]
        ),
        .target(
            name: "wordBreakingValidator",
            dependencies: ["Naqqash"]
        ),
        .target(
            name: "stringReplacer",
            dependencies: ["Naqqash"]
        ),
        .target(
            name: "characterPairFrequency",
            dependencies: ["Naqqash"]
        ),
        .target(
            name: "urls"
        ),
    ]
)
