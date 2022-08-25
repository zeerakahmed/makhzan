# Maḵẖzan مخزن

An Urdu text corpus to enable research and applications for the Urdu language. We believe Maḵẖzan is the best Urdu dataset to start work for Urdu NLP.

This dataset currently comprises 6.26 million words of Urdu text. We have selected source text that we believe to have gone through strong editorial standards, to preserve linguistic integrity. The text is then syntactically marked up, so that headings, paragraphs, and lists can be identified. Metadata is added to each file so data can be intelligently filtered and selected. We annotate non-Urdu text included in source publications. Data also goes through an intense cleaning process to make the text easier to read for software, as well as correcting typograghical errors.

Maḵẖzan is free to use for all commercial and non-commercial purposes. To protect writers' whose writing is part of this dataset, we ask that you not republish the raw text (please see License information below). If you end up using Maḵẖzan for your work, we'd love to hear about it.

## Navigating this repository

- [`/docs`](/docs): Documentation
- [`/scripts`](/scripts): Scripts to analyze the text, constructed as a Swift package.
- [`/stats`](/stats): Output of text analyses, which can be used out of the box to power NLP applications, such as word and n-gram frequencies.
- [`/text`](/text): The text corpus itself, consisting of XML files.
- [`/tools`](/tools): Command line tools for data cleaning. These are of use to help improve the quality of Maḵẖzan

## Contribution

We would love your help in a number of ways. Please get in touch if you:
- have any text to contribute to this repository
- spot an error in the text
- write a script that should be distributed with the corpus

Start an issue on this repository or get in touch [through our website](https://matnsaz.net/en/contact).

### Contributors

We are grateful to our current contributors

#### Engineering

- Waqas Ali
- Hassan Talat
- Shaoor Munir
- Muhammad Haroon

#### Data Editing
- Hamza Safdar
- Akbar Zaman 

Text Contributions
- Gurmani Center at LUMS
- IBC Urdu
- Al-Mawrid Institute 

## Citation

````
@misc{makhzan,
title={Maḵẖzan},
howpublished = "\url{https://github.com/zeerakahmed/makhzan/}",
}
````

## License / Copyright

### Material in the [`/text`](/text) directory

All files in the [`/text`](/text) directory are covered under standard copyright. Each piece of text has been included in this repository with explicity permission of respective copyright holders, who are identified in the `<meta>` tag for each file. You are free to use this text for analysis, research and development, but you are not allowed to redistribute or republish this text. Where possible we encourage that forks of this repository be kept private unless explicit permission is granted.

Some cases where a less restrictive license could apply to files in the [`/text`](/text) directory are presented below. 

In some cases copyright free text has been digitally reproduced through the hard work of our collaborators. In such cases we have credited the appropriate people where possible in a `<notes>` field in the file's metadata, and we strongly encourage you to contact them before redistributing this text in any form.

Where a separate license is provided along with the text, we have provided corresponding data in the `<publication>` field in a file's metadata. 

### All other materials

All other materials in this repository (such as software, aggregated analyses and documentation) in the [`/scripts`](/scripts) or [`/stats`](/stats) directory are licensed under the terms of the MIT license.

### Copyright concerns

If you feel any material has been included in this repository erroneously and/or copyright arrangements have not been respected, please file an issue on this repository or get in touch [through our website](https://matnsaz.net/en/contact). 
