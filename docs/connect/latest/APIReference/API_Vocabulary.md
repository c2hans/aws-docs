---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Vocabulary.html
---

# Vocabulary
<a name="API_Vocabulary"></a>

Contains information about a custom vocabulary.

## Contents
<a name="API_Vocabulary_Contents"></a>

 ** Arn **   <a name="connect-Type-Vocabulary-Arn"></a>
The Amazon Resource Name (ARN) of the custom vocabulary.
Type: String
Required: Yes

 ** Id **   <a name="connect-Type-Vocabulary-Id"></a>
The identifier of the custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** LanguageCode **   <a name="connect-Type-Vocabulary-LanguageCode"></a>
The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html)
Type: String
Valid Values: `ar-AE | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fr-CA | fr-FR | hi-IN | it-IT | ja-JP | ko-KR | pt-BR | pt-PT | zh-CN | en-NZ | en-ZA | ca-ES | da-DK | fi-FI | id-ID | ms-MY | nl-NL | no-NO | pl-PL | sv-SE | tl-PH`
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-Vocabulary-LastModifiedTime"></a>
The timestamp when the custom vocabulary was last modified.
Type: Timestamp
Required: Yes

 ** Name **   <a name="connect-Type-Vocabulary-Name"></a>
A unique name of the custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

 ** State **   <a name="connect-Type-Vocabulary-State"></a>
The current state of the custom vocabulary.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | CREATION_FAILED | DELETE_IN_PROGRESS`
Required: Yes

 ** Content **   <a name="connect-Type-Vocabulary-Content"></a>
The content of the custom vocabulary in plain-text format with a table of values. Each row in the table represents a word or a phrase, described with `Phrase`, `IPA`, `SoundsLike`, and `DisplayAs` fields. Separate the fields with TAB characters. For more information, see [Create a custom vocabulary using a table](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html#create-vocabulary-table).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60000.
Required: No

 ** FailureReason **   <a name="connect-Type-Vocabulary-FailureReason"></a>
The reason why the custom vocabulary was not created.
Type: String
Required: No

 ** Tags **   <a name="connect-Type-Vocabulary-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Vocabulary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Vocabulary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Vocabulary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Vocabulary)
