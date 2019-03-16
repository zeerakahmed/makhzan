# corpus

An Urdu text corpus to enable research and applications for the Urdu language. All text in this repository is free to use for commercial and non-commercial projects.

## How text was selected

All text in this repository has been selected for quality of language, upholding high editorial standards. Given the poor quality of most published Urdu text in digital form, this selection criteria allows the use of this text for natural language process, and machine learning applications without the need to address fundamental quality issues in the text.

We have made efforts to ensure this text is as broadly representative as possible. Specifically we have attempted to select for as many authors as possible, and diversity in the gender of the author, as well as years and city of publication. This effort is imperfect, and we appreciate any attempts at pointing us to resources that can help diversify this text even further.

## File structure

The text repository itself is contained within `/text`. `sources.csv` contains metadata for each text file.

## Text Formatting

### Basic structure

- Each file in `/text` represents a piece of work by one author. A book with a single set of author(s) is for example, represented by one file. A magazine or journal with a separate author(s) for each piece is represented by a separate file for each piece.
- A paragraph of text is represented as a single line of text with a new line character at the end.
- Titles are presented on separate lines.
- For pieces of text with multiple sections (such as a book with multiple chapters), an empty line indicates a section break.

### Annotations

- Annotations have been made using XML syntax, using an ```<annotation>``` element.
- Due to the use of XML syntax for annotations, ```<```, ```>``` and ```&``` characters have been escaped as ```&lt;```, ```&gt```, and ```&amp``` respectively.
- A language (```lang```) attribute is added to the ```<annotation>``` element to indicate text in other languages (such as quoted text or technical vocabulary presented in other languages and scripts). The attribute value a two-character ISO 639-1 code. So the resultant annotation for an Arabic quote for example, will be ```<annotation lang="ar"></annotation>```. 

### Encoding

- All text has been converted from a variety of original formats into text files using Unicode code points in ```utf-8``` encoding.
- Unicode code points have been chosen in their fully decomposed form. 

### Textual modifications

- Typographical errors have been fixed in the text we obtained where possible to ensure a standardized typographical format. These include removing spaces before punctuation such as periods and commas, adding spaces after periods and commas, using the correct quotation characters, removing unnecessary whitespace, and fixing any obvious spelling errors. This is done to prevent downstream bugs in software that uses this corpus.
- Efforts have been made to ensure the correct usage of the zero-width non-joiner character. The character is used to break cursive without adding a space, often used in compound words. Errant spaces mid-word have been removed where necessary and noticed.

### Metadata in ```sources.csv```

There are various reasons to provide metadata on our text sourcing:
- Attribution to authors, copyright holders, and other contributors.
- Allowance for an audit of our text selection mechanism, and for suggestions to be made for this corpus to be more representative.
- For convenient selection of text when needed for research applications. 

Notes on how we have formatted this metadata:
- The number of words is calculated subtracting XML annotations, and text from languages other than Urdu. For Urdu projects this text is most likely to be ignored, and so the word count subtracting such text presents a more accurate estimate of the actual Urdu words used.

## Copyright

Each piece of text has been included with explicit permission of respective copyright holders, where available. Otherwise the text is copyright free. You are free to use this text to help with your research work, but you are not allowed to redistribute, or republish this text in any form without explicit permission of the copyright holders.

In some cases copyright free text has been digitally reproduced through the hard work of our collaborators. In such cases we have credited the appropriate people where possible in the ```Notes``` column of `sources.csv`, and we strongly encourage you to contact them before redistributing this text in any form.