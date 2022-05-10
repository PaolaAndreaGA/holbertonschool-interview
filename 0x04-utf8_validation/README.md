# 0x04. UTF-8 Validation

## UTF-8

From Wikipedia, the free encyclopedia

[Jump to navigation](https://en.wikipedia.org/wiki/UTF-8#mw-head)[Jump to search](https://en.wikipedia.org/wiki/UTF-8#searchInput)

UTF-8

Standard

[Unicode Standard](http://www.unicode.org/versions/latest/)

Classification

[Unicode Transformation Format](https://en.wikipedia.org/wiki/Unicode_Transformation_Format "Unicode Transformation Format"),  [extended ASCII](https://en.wikipedia.org/wiki/Extended_ASCII "Extended ASCII"),  [variable-width encoding](https://en.wikipedia.org/wiki/Variable-width_encoding "Variable-width encoding")

Extends

[US-ASCII](https://en.wikipedia.org/wiki/US-ASCII "US-ASCII")

Transforms / Encodes

[ISO 10646](https://en.wikipedia.org/wiki/ISO_10646 "ISO 10646")  ([Unicode](https://en.wikipedia.org/wiki/Unicode "Unicode"))

Preceded by

[UTF-1](https://en.wikipedia.org/wiki/UTF-1 "UTF-1")

-   [v](https://en.wikipedia.org/wiki/Template:Infobox_character_encoding "Template:Infobox character encoding")
-   [t](https://en.wikipedia.org/wiki/Template_talk:Infobox_character_encoding "Template talk:Infobox character encoding")
-   [e](https://en.wikipedia.org/w/index.php?title=Template:Infobox_character_encoding&action=edit)

**UTF-8**  is a  [variable-width](https://en.wikipedia.org/wiki/Variable-width_encoding "Variable-width encoding")  [character encoding](https://en.wikipedia.org/wiki/Character_encoding "Character encoding")  used for electronic communication. Defined by the  [Unicode Standard](https://en.wikipedia.org/wiki/Unicode_Standard "Unicode Standard"), the name is derived from  _Unicode_  (or  _Universal Coded Character Set_)  _Transformation Format – 8-bit_.[[1]](https://en.wikipedia.org/wiki/UTF-8#cite_note-1)

UTF-8 is capable of encoding all 1,112,064[[nb 1]](https://en.wikipedia.org/wiki/UTF-8#cite_note-2)  valid character  [code points](https://en.wikipedia.org/wiki/Code_point "Code point")  in  [Unicode](https://en.wikipedia.org/wiki/Unicode "Unicode")  using one to four one-[byte](https://en.wikipedia.org/wiki/Byte "Byte")  (8-bit) code units. Code points with lower numerical values, which tend to occur more frequently, are encoded using fewer bytes. It was designed for  [backward compatibility](https://en.wikipedia.org/wiki/Backward_compatibility "Backward compatibility")  with  [ASCII](https://en.wikipedia.org/wiki/ASCII "ASCII"): the first 128 characters of Unicode, which correspond one-to-one with ASCII, are encoded using a single byte with the same binary value as ASCII, so that valid ASCII text is valid UTF-8-encoded Unicode as well. Since ASCII bytes do not occur when encoding non-ASCII code points into UTF-8, UTF-8 is safe to use within most programming and document languages that interpret certain ASCII characters in a special way, such as  `/`  ([slash](https://en.wikipedia.org/wiki/Slash_(punctuation) "Slash (punctuation)")) in filenames,  `\`  ([backslash](https://en.wikipedia.org/wiki/Backslash "Backslash")) in  [escape sequences](https://en.wikipedia.org/wiki/String_literal#Escape_sequences "String literal"), and  `%`  in  [printf](https://en.wikipedia.org/wiki/Printf "Printf").

UTF-8 was designed as a superior alternative to  [UTF-1](https://en.wikipedia.org/wiki/UTF-1 "UTF-1"), a proposed variable-width encoding with partial ASCII compatibility which lacked some features including  [self-synchronization](https://en.wikipedia.org/wiki/Self-synchronizing_code "Self-synchronizing code")  and fully ASCII-compatible handling of characters such as slashes.  [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson "Ken Thompson")  and  [Rob Pike](https://en.wikipedia.org/wiki/Rob_Pike "Rob Pike")  produced the first implementation for the  [Plan 9](https://en.wikipedia.org/wiki/Plan_9_from_Bell_Labs "Plan 9 from Bell Labs")  operating system in September 1992.[[2]](https://en.wikipedia.org/wiki/UTF-8#cite_note-mgk25-3)[[3]](https://en.wikipedia.org/wiki/UTF-8#cite_note-4)  This led to its adoption by  [X/Open](https://en.wikipedia.org/wiki/X/Open "X/Open")  as its specification for  _FSS-UTF_, which would first be officially presented at  [USENIX](https://en.wikipedia.org/wiki/USENIX "USENIX")  in January 1993 and subsequently adopted by the  [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force "Internet Engineering Task Force")  (IETF) in  RFC 2277  (BCP 18) for future internet standards work, replacing Single Byte Character Sets such as  [Latin-1](https://en.wikipedia.org/wiki/Latin-1 "Latin-1")  in older RFCs.

UTF-8 is the dominant encoding for the  [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web "World Wide Web")  (and internet technologies), accounting for 98% of all web pages, and up to 100.0% for some languages, as of 2022.[[4]](https://en.wikipedia.org/wiki/UTF-8#cite_note-W3TechsWebEncoding-5)
