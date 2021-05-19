# Analysis

This [scripts directory](../scripts) contains a set of scripts to conduct common analyses on the text corpus. These serve as a good starting point on how to build further scripts.

This [tools directory](../tools) contains additional software used to make transformations to the text in Maḵẖzan. While the [`/scripts`](../scripts) directory contains most scripts, since it is constructed as a Swift package, other tools are kept in [tools directory](../tools).

## [/scripts](../scripts)

### How these scripts are structured

The collection of scripts is structured as a Swift package. You can read more about Swift packages [here](https://swift.org/package-manager/). 

While Swift is not the most common language for natural language processing, it was chosen due to a dependency on the [Naqqash package](http://github.com/zeerakahmed/naqqash) which provides necessary methods to process text in the Arabic script. Both the Naqqash package and this text repository were originally built in the service of [Matnsaz](https://matnsaz.net), an Urdu keyboard.

The `Package.swift` file contains the names of executables and lists dependencies. If you create a new script, add a target to this file. The `/Sources` directory contains executables which each perform separate analyses. Output from these analyses is stored in `../stats`. 

### How to run

To build the scripts on your machine, `cd` to `/scripts` and then run `swift build`. To run a script, identify the target you want to run by running `swift run <target>`. For example if you wanted to run the `wordFrequency` script, you would run it as `swift run wordFrequency`

### Scripts included

- `characterFrequency`: Counts how often each character classified as a letter in the Arabic script appears in the corpus.
- `characterPairFrequency`: Counts how often pairs of letters in the Arabic script appear in the corpus.
- `nGram`: Counts the frequency of sequences of words (n-Grams). The script outputs counts for 2, 3 and 4-grams.
- `preProcessor`: Goes through each character in every file, and decomposes it into multiple Unicode codepoints if needed.
- `stringReplacer`: Replaces text with associated replacements as identifed in the [companion `replacements` file](../scripts/Sources/stringReplacer/replacements). Each line of the `replacements` file lists text to be replaced, and the replacement text, separated by a tab character. The [word breaking error check tool](../tools/wordBreakingErrorCheck.py) is used to add suggested replacements to this file.
- `url`: Outputs the URL listed in the `<meta>` tag of each file.
- `wordBreakingValidator`: Reads through every word of text, and suggests words that might have word breaking errors. If a word can be split into two words where the the two suggested words occur more often than the source word, the script suggests a replacement. If two words can be put together and the resultant word occurs more often than the two source words, the script also suggests a replacement. These suggestions are intended for manual review (perhaps using the aid of the [word breaking error check tool](../tools/wordBreakingErrorCheck.py)) to accept or reject these replacements. Rejected replacements are approved as valid words and added to the [companion `approveList`](../scripts/Sources/wordBreakingValidator/approveList). The process to fix word breaking errors is to run this validator, review suggestions, then run stringReplacer to correct errors in the dataset.
- `wordFrequency`: Counts how often each word appears in the full corpus. Text in non-Urdu languages and metadata is ignored for this count.

## [/tools](../tools)

### How these tools are structured

These scipts are structured as individual files that can be run from the command line.

### Current tools

#### wordBreakingErrorCheck

This tool goes through the [output](../stats/wordBreakingErrors) of [our word breaking validator](../scripts/Sources/wordBreakingValidator), and allows quickly making decisions on the suggestions of the validator using the command line. You can approve the suggestion from our validator, reject, or mark as a maybe.

After running this tool, run the [stringReplacer](../scripts/Sources/stringReplacer) script to make suggested replacements in the text, rerun the workBreakingValidator to update remaining word breaking errors, and ideally other stats as well so the final dataset remains accurate.

To run `python wordBreakingErrorCheck.py`. This requires Python 3.