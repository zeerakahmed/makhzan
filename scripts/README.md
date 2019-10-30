This directory contains a set of scripts to conduct common analyses on the text corpus. These serve as a good starting point on how to build further scripts.

## How these scripts are structured

The collection of scripts is structured as a Swift package. You can read more about Swift packages [here](https://swift.org/package-manager/). 

While Swift is not the most common language for natural language processing, it was chosen due to a dependency on the [Naqqash package](http://github.com/zeerakahmed/naqqash) which provides necessary methods to process text in the Arabic script. Both the Naqqash package and this text repository were built in the service of [Matnsaz](https://matnsaz.net), an Urdu keyboard.

The `Package.swift` file contains the names of executables and lists dependencies. If you create a new script, add a target to this file.

## How to run

To build the scripts on your machine, run
    `swift build`

To run a script, identify the target you want to run as follows:
    `swift run <target>`

For example if you wanted to run the `wordFrequency` script, you would run it as
    `swift run wordFrequency`


