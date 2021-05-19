# Text Sources

## How text was selected

All text in this repository has been selected for quality of language, upholding high editorial standards. Given the poor quality of most published Urdu text in digital form, this selection criteria allows the use of this text for natural language processing, and machine learning applications without the need to address fundamental quality issues in the text.

We have made efforts to ensure this text is as broadly representative as possible. Specifically we have attempted to select for as many authors as possible, and diversity in the gender of the author, as well as years and city of publication. This effort is imperfect, and we appreciate any attempts at pointing us to resources that can help diversify this text further.

At the moment text in Maḵẖzan is sourced from the following publications:
- [_Bunyad_](https://bunyad.lums.edu.pk/website/)
- [_IBC Urdu_](http://ibcurdu.com)
- [_Ishraq_](https://www.javedahmedghamidi.org/#!/ishraq)
- [Unicode Common Locale Data Repository](http://cldr.unicode.org)

Details of how text has been reviewed and transformed from each source is listed below.

## Review & Transformation Process

Source text is received from each publication in different formats. As a result, we create a unique transformation process for each publication with a common desired output in mind. Details of how text was reviewed and transformed from each source is listed below.

For all text we look for common spacing issues, such as: the use of spaces before and after punctuation, multiple spaces in a row, and diacritics applied to space characters instead of the characters prior.

After text is added to Maḵẖzan, we continue to improve by analyzing for word breaking errors.

### _Bunyad_

Text was received as InPage files. Through screen automation software, we read the style assigned to each line of text. These styles were used to infer markup in our XML format. Spacing errors (such as around puncutation) was then programatically fixed.

This automated process was then manually reviewed. We then manually searched for and annotated non-Urdu languages, using visual and linguistic queues. Languages were identified with the help of online translation tools where ambiguous. We searched the text for single letters which were not connected to other letters before or after in a word, and tried to fix word breaking errors where possible. For text added recently (after we added all _Bunyad_ text), we leave this step to our automated word breaking validation tools. We removed all footnote/endnotes in the text, due to their lack of linguistic diversity. Footnote/endnote markers in the body of the text were also removed. 

#### Known issues

- [Some documents do not have URLs in metadata.](https://github.com/zeerakahmed/makhzan/issues/40)
- [Some lists have nested paragraph elements. After transforming _Bunyad_ text we decided that this was perhaps not the best approach, and lists should only contain one line of text per list item. Affected documents need correction.](https://github.com/zeerakahmed/makhzan/issues/36)

### _IBC Urdu_

Text was received as a Wordpress export. This text was then programatically transformed into Maḵẖzan's format XML by inferring desired tags from HTML markup. Extraneous HTML markup and non-text content was removed. Spacing issues (such as around punctuation) were fixed programatically. Text in Latin script was automatically tagged as an English annotation (given the likelihood of text in the Latin script being in English). We manually searched for the words "پشتو" (Pashto), "پنجابی" (Panjabi), "سندھی" (Sindhi), "بلوچی" (Balochi), "عربی" (Arabi/Arabic), "فارسی" (Farsi/Persian) to identify foreign language text in the Arabic script. Author genders were inferred via name and a web search for their biographical data.

#### Known issues

- [Some documents appear to be translated (given the names of authors), but translation data is not listed.](https://github.com/zeerakahmed/makhzan/issues/11)
- [Some headings have been marked up as blockquotes.](https://github.com/zeerakahmed/makhzan/issues/25)
- [Some documents may be duplicates.](https://github.com/zeerakahmed/makhzan/issues/35)

### _Ishraq_

Text was programatically scraped from the website. A few files were manually tagged, before we wrote a script to transform the vast majority of text into our XML format. Desired tags were inferred from HTML markup, and then manually reviewed. Spacing issues (such as around punctuation) were fixed programatically. 

Text in Latin script was automatically tagged as an English annotation (given the likelihood of text in the Latin script being in English). Arabic text was identified through the use of distinct styling in the source material. Persian text was less clearly identifiable, but where possible has been annotated with identification help through online translation services. Where the original language is not clearly known but is identified to not be Urdu, the `lang` attribute in the `<annotation>` tag has been omitted. 

Where the text indicates that it has been translated, translator information and original language are called out in the `<meta>` tag. For some text the original langauge is not specified and has been ommitted from the metadata. 

At times author names were not listed in the field containing author data on most web pages, and was instead listed in the first line of text. In such instances we have inferred the author name from this first line of text. The author name was removed from the body of text in these cases, except for when it is attached to a footnote (which in almost if not all cases indicates the author's designation and organization).

Footnotes have not been removed, and generally are placed at the end of each document in a separate `<section>` tag where they have been separated in the original text with a visual indicator. As such markers in the text indicating their connection to a footnote have also not been removed. In this journal they are often indicated as * or ؂ characters.

Lists are a part of many documents. In some documents, paragraphs are numbered as if part of a large list. If each element of a list is limited to one line of text, we have marked each line of text as a list item (`<li>`) and wrapped them in a `<list>` tag. If multiple lines of text are provided after a single bullet or number, each line of text has been marked up as a paragraph (`<p>`).

#### Known issues

- Original language is not listed in some translations.
- [Some documents may be duplicates.](https://github.com/zeerakahmed/makhzan/issues/35)

### Unicode Common Locale Data Repository

The Unicode CLDR provides common translations, and locale-specific formatting information for software makers. The documents included in Maḵẖzan take the Urdu sections of some source documents. These include a significant number of unique Urdu words, including proper nouns. However they do not include prose per se. We converted source XML files into logical equivalent tags in Maḵẖzan markup. Individual data items for example, were marked as `<p>` tags.