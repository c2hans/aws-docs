---
source_url: https://docs.aws.amazon.com/transcribe/latest/dg/charsets-med.html
---

# Character set for Amazon Transcribe Medical
<a name="charsets-med"></a>

To use custom vocabularies in Amazon Transcribe Medical, use the following character set.

## English character set
<a name="char-english-med"></a>

For English custom vocabularies, you can use the following characters in the `Phrase` and `SoundsLike` columns:
+ a - z
+ A - Z
+ ' (apostrophe)
+ - (hyphen)
+ . (period)

You can use the following International Phonetic Alphabet (IPA) characters in the `IPA` column of the vocabulary input file.

| Character | Code | Character | Code |
| --- | --- | --- | --- |
| aʊ | 0061 028A | w | 0077 |
| aɪ | 0061 026A | z | 007A |
| b | 0062 | æ | 00E6 |
| d | 0064 | ð | 00F0 |
| eɪ | 0065 026A | ŋ | 014B |
| f | 0066 | ɑ | 0251 |
| g | 0067 | ɔ | 0254 |
| h | 0068 | ɔɪ | 0254 026A |
| i | 0069 | ə | 0259 |
| j | 006A | ɛ | 025B |
| k | 006B | ɝ | 025D |
| l | 006C | ɡ | 0261 |
| l̩ | 006C 0329 | ɪ | 026A |
| m | 006D | ɹ | 0279 |
| n | 006E | ʃ | 0283 |
| n̩ | 006E 0329 | ʊ | 028A |
| oʊ | 006F 028A | ʌ | 028C |
| p | 0070 | ʍ | 028D |
| s | 0073 | ʒ | 0292 |
| t | 0074 | ʤ | 02A4 |
| u | 0075 | ʧ | 02A7 |
| v | 0076 | θ | 03B8 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
