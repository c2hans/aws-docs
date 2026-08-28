---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_VocabularySummary.html
---

# VocabularySummary
<a name="API_VocabularySummary"></a>

Contains summary information about the custom vocabulary.

## Contents
<a name="API_VocabularySummary_Contents"></a>

 ** Arn **   <a name="connect-Type-VocabularySummary-Arn"></a>
The Amazon Resource Name (ARN) of the custom vocabulary.
Type: String
Required: Yes

 ** Id **   <a name="connect-Type-VocabularySummary-Id"></a>
The identifier of the custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** LanguageCode **   <a name="connect-Type-VocabularySummary-LanguageCode"></a>
The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html)
Type: String
Valid Values: `ar-AE | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fr-CA | fr-FR | hi-IN | it-IT | ja-JP | ko-KR | pt-BR | pt-PT | zh-CN | en-NZ | en-ZA | ca-ES | da-DK | fi-FI | id-ID | ms-MY | nl-NL | no-NO | pl-PL | sv-SE | tl-PH`
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-VocabularySummary-LastModifiedTime"></a>
The timestamp when the custom vocabulary was last modified.
Type: Timestamp
Required: Yes

 ** Name **   <a name="connect-Type-VocabularySummary-Name"></a>
A unique name of the custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

 ** State **   <a name="connect-Type-VocabularySummary-State"></a>
The current state of the custom vocabulary.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | CREATION_FAILED | DELETE_IN_PROGRESS`
Required: Yes

 ** FailureReason **   <a name="connect-Type-VocabularySummary-FailureReason"></a>
The reason why the custom vocabulary was not created.
Type: String
Required: No

## See Also
<a name="API_VocabularySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/VocabularySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/VocabularySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/VocabularySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
