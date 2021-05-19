# Text Formatting & Markup

## Markup

### Basic structure

Each file in `/text` represents a piece of work by one author. A book with a single set of author(s) is for example, represented by one file. A magazine or journal with a separate author(s) for each piece is represented by a separate file for each piece.

Text is structured and annotated using XML syntax. The ontology of elements used is loosely based around HTML, with simplifications made when HTML's specificity is not needed, and additions made to express common occurences in this corpus that would be useful for linguistic analysis. The semantic tagging of text is editorial in nature, which is to say that another person semantically tagging the text may do so differently. Effort has been made however to ensure consistency, and to retain the original meaning of the text while making it easy to parse through linguistically different pieces of text for analysis. 

The resulting structure of tags in the text documents is as follows:
- The root node is a `<document>` element.
- Each `<document>` is divided into `<meta>` and `<body>` tags. 
- The `<meta>` tag, as the name suggests, contains metadata on the document such as the document's title, information about the author and publication, as well as other potentially useful facts such as the number of Urdu words in the document and whether the document contains text in any other languages.
- The `<body>` tag is divided into `<section>` elements. In general the rule is that a clear visual demarkation in the original text (such as a page break, or a horizontal rule) is used to indicate a section break. A heading does not automatically create a new section.
- Each paragraph is a `<p>` element.
- Headings are wrapped in an `<heading>` element. 
- Blockquotes are wrapped in a `<blockquote>` element. Blockquotes may themselves contain other elements.
- Lists are wrapped in an `<list>`. Individual items in each list are wrapped in an `<li>` element. 
- Poetic verses are wrapped in a `<verse>` element. Each verse is on a separate line but is not wrapped in an individual element.
- Tables are wrapped in a `<table>` element. A table is divided into rows marked by `<tr>` and columns marked by `<td>`.
- Text not in the Urdu language is wrapped in an `<annotation>` tag (more below). 
- `<p>`, `<heading>`, `<li>`, `<td>` and `<annotation>` tags are inline with the text (i.e. there is no new line character before and after the tag). Other tags have a new line after the opening and before the closing tag. 

Due to the use of XML syntax, `<`, `>` and `&` characters have been escaped as `&lt;`, `&gt;`, and `&amp;` respectively. This includes the use of these characters in URLs inside `<meta>` tags.

### Annotations

- Annotations have been made inline using an `<annotation>` element.
- A language (`lang`) attribute is added to the `<annotation>` element to indicate text in other languages (such as quoted text or technical vocabulary presented in other languages and scripts). The attribute value a two-character ISO 639-1 code. So the resultant annotation for an Arabic quote for example, will be `<annotation lang="ar"></annotation>`. 
- A type (`type`) attributed is added to indicate text that is not in a language per se but is not Urdu text. URLs for example are wrapped in an `<annotation type="url">` tag. 

## Metadata

There are various reasons to provide metadata on our text sourcing:
- Attribution to authors, copyright holders, and other contributors.
- Allowance for an audit of our text selection mechanism, and for suggestions to be made for this corpus to be more representative.
- For convenient selection of text when needed for research applications. 

Notes on how we have formatted this metadata:
- The number of words is calculated subtracting XML annotations, and text from languages other than Urdu. For Urdu projects this text is most likely to be ignored, and so the word count subtracting such text presents a more accurate estimate of the actual Urdu words used.

## Encoding

- All text has been converted from a variety of original formats into text files using Unicode code points in `utf-8` encoding and `LF` line endings.
- We use NFD normalization for all Unicode characters, i.e. Unicode code points have been chosen in their canonical, fully decomposed form. The primary rationale for decomposition was that it allowed an easier way to remove diacritics and deal with the smallest atomic unit of Unicode characters when performing analyses. This means that rendering engines may occasionally display the wrong glyphs for characters which they expect to be precomposed, but we have compromised on accuracy of visual representation for each of processing (which is the primary goal of this dataset). If rendering this text we encourage ensuring that text is precomposed before representation. [See this discussion for details](https://github.com/zeerakahmed/makhzan/issues/15).

## Textual modifications

- Typographical errors have been fixed in the text we obtained where possible to ensure a standardized typographical format. These include removing spaces before punctuation such as periods and commas, adding spaces after periods and commas, using the correct quotation characters, removing unnecessary whitespace, and fixing any obvious spelling errors. This is done to prevent downstream bugs in software that uses this corpus.
- Egregious word breaking errors have been fixed. We use a custom algorirthm to identify such errors, then manually review candidate errors and suggestions. Original text is correct when we we are certain that there is a canonical representation of a word.
- Occassionally punctuation has been changed for clarity. For example, in one particular case repeated a number of times in this corpus, an Arabic period was used to indicate a date range. Here the period has been replaced with a hyphen so as to not break any sentence breaking code.
- In some cases source text makes both a visual demarcation of a block quotation and also uses quotation marks at the beginning and end of the blockquote. In these cases extraneous quotation marks have been removed from elements already marked as `<blockquote>`.
- Efforts have been made to ensure the correct usage of the zero-width non-joiner character. The character is used to break cursive without adding a space, often used in compound words. Errant spaces mid-word have been removed where necessary and noticed.