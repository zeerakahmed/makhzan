This directory contains additional software tools used to make transformations to the text in Maḵẖzan. 

Most scripts exist in [`/scripts`](../scripts). Largely these are used to conduct analyses of the text, but there are also a few scripts that are used for transformation purposes. Since the [`/scripts`](../scripts) directory is constructed as a Swift package, other tools are kept in this directory.

## How these tools are structured

These scipts are structured as individual files that can be run from the command line.

## Current tools

### wordBreakingErrorCheck

This tool goes through the [output](../stats/wordBreakingErrors) of [our word breaking validator](../scripts/Sources/wordBreakingValidator), and allows quickly making decisions on the suggestions of the validator using the command line. You can approve the suggestion from our validator, reject, or mark as a maybe.

After running this tool, run the [stringReplacer](../scripts/Sources/stringReplacer) script to make suggested replacements in the text, rerun the workBreakingValidator to update remaining word breaking errors, and ideally other stats as well so the final dataset remains accurate.

To run `python wordBreakingErrorCheck.py`. This requires Python 3.
