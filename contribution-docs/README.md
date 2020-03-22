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

### Spacing issues in InPage & Nastaliq text

A lot of text in the Urdu language is typeset using the InPage application. Nearly the entirety of text we have come across that is typeset in this manner has a number of common issues that need to be resolved.

- **Use the correct quotation marks**
  - Replace `’’` with `”`.
  - Replace `‘‘` with `“`.
- **Ensure spacing is correct around punctuation**
  - Remove leading space in anything that matches `\s[۔،:\(\[“‘]`.
  - Add a trailing space in anything that matches `[۔،:\(\[“‘][^\s]`.
  - Add a leading space in anything that matches `[^\s][\)\]”’]`.
  - Remove trailing space in anything that matches `[\)\]”’]\s`.
- **Remove double spaces**
  - Replace occurences of two consecutive spaces with a single space until there are no more occurences of two consecutive spaces.

Further, we find that text typset in Nastaliq typefaces often has a number of spacing errors in and around words. Mostly these spaces are added to make the text more aesthetically pleasing, and due to incorrect/non-existent usage of the zero width non-joiner character. 

- **Check for floating letters:** Single characters hanging out with spaces on either side is a sign of a typographical error. A `و` character is usually ok, but anything else needs to be manually investigated.
  - Find all characters matching `\s[^و]\s` and investigate
- **Correct spaces with *zer* underneath**
  - Find all sequences matching `\sِ`. In most of these cases the *zer* is indicating the presence of a compound word. In such cases the *zer* needs to move to the letter preceding the space, and the space itself should be replaced with a zero width non-joiner character.

### Using the right Unicode characters and file format

Before merging new text with the `master` branch, two precautions need to be taken:
1. Text encoding is `UTF-8`. 
2. Unicode characters are chosen in their decomposed form. 

To ensure you are doing both, run the `preProcessor` script in the [`../scripts`](/scripts) folder before merging. This runs a cleaner on all text files to ensure the correct encoding and character choices. 

## Tools to help with modification of source text

### Sublime Text 3 Plugins

To help with the arduous task of cleaning, and semantically tagging source text we are beginning to develop text editor plugins. A first draft of these is included in the [`/sublime-text-3-plugins`](/sublime-text-3-plugins) directory. As the name suggests these plugins are for the Sublime Text 3 text editor.

Using these plugins will provide a `Makhzan` menu next to the other Sublime Text menu, containing helpful commands. Using these plugins a number of time-intensive transformations are automated with one click:
- Use the `Fix Common Inpage Issues` command to fix most spacing issues identified above. Only floating letters, and spaces with a *zer* underneath need to be manually addressed.
- To add semantic tags around any text, just select the text and run the appropriate command from the menu. For example, running the `Add Paragraph Tags` command will add opening and closing `<p>` tags to the beginning and end of the lines selected. Using these commands also ensures that indentation and new-line conventions are more closely followed in the corpus.

To utilize these plugins, copy all the files in this directory to your `Sublime Text 3/Packages/User` folder. This folder will be in different places depending on your operating system. If you already have a `Main.sublime-menu` file that you have used to add a custom menu to Sublime Text, then simply append the dictionary item in this file to your existing `Main.sublime-menu` file.