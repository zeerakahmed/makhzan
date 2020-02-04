# How to add text to this corpus

## General Instructions

Please read the *Text Formatting* section in the [respository's README](../README.md) to get a general sense of how text has been transformed into standardized format.

You can find a [base template file](base-template.xml) in this directory which is a good starting point to start adding text.

Once ready please open a pull request to add a file to the `../text` directory. File names are incrementing integers.

## Obtaining source text

We are in possession of a large anount of text that needs to be cleaned and transformed for addition to this corpus. If you would like to help by cleaning and transforming this data please reach out [through our website](https://matnsaz.net/en/contact).

If you are in the possession of Urdu text that is not already, or is not slated to be, part of this corpus please get in touch. We are especially in need of text that is not typeset in Nastaliq typefaces, which mostly contains errors detailed below.

## Modifying and correcting source text

### Common transformations:

- **Remove footnotes/endnotes:** In most source text footnotes often contain information unlikely to diversify our text corpus, and they are more difficult to encode. As such it makes it much easier to ignore them.
  - Remove footnotes/endnotes from the document. In text sourced from Bunyad, these are often at the end of each document.
  - Remove all footnote markers. These are mostly digits. Search for `\d` and remove as necessary. Note that other digits are part of the text and should not be removed.

## Spacing issues in InPage & Nastaliq text

A lot of text in the Urdu language is typeset using the InPage application. Nearly the entirety of text we have come across that is typeset in this manner has a number of common issues that need to be resolved.

- **Use the correct quotation marks**
  - Replace `’’` with `”`.
  - Replace `‘‘` with `“`.
- **Ensure spacing is correct around punctuation**
  - Remove leading space in anything that matches `\s[۔،:\(\[“‘]`.
  - Add a trailing space in anything that matches `[۔،:\(\[“‘][^\s]`.
  - Add a leading space in anything that matches `[^\s][\)\]”’]`
  - Remove trailing space in anything that matches `[\)\]”’]\s`
- **Remove double spaces**
  - Replace `\ \ ` with `\ ` until there are no more characters matching `  `. 

Further, we find that text typset in Nastaliq typefaces often has a number of spacing errors in and around words. Mostly these spaces are added to make the text more aesthetically pleasing, and due to incorrect/non-existent usage of the zero width non-joiner character. 

- **Check for floating letters:** Single characters hanging out with spaces on either side is a sign of a typographical error. A `و` character is usually ok, but anything else needs to be manually investigated.
  - Find all characters matching ` [^و] ` and investigate
- **Correct spaces with *zer* underneath**
  - Find all sequences matching ` ِ`. In most of these cases the *zer* is indicating the presence of a compound word. In such cases the *zer* needs to move to the letter preceding the space, and the space itself should be replaced with a zero width non-joiner character.