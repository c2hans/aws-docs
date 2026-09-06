---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DefaultVocabulary.html
---

# DefaultVocabulary
<a name="API_DefaultVocabulary"></a>

Contains information about a default vocabulary.

## Contents
<a name="API_DefaultVocabulary_Contents"></a>

 ** InstanceId **   <a name="connect-Type-DefaultVocabulary-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** LanguageCode **   <a name="connect-Type-DefaultVocabulary-LanguageCode"></a>
The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html)
Type: String
Valid Values: `ar-AE | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fr-CA | fr-FR | hi-IN | it-IT | ja-JP | ko-KR | pt-BR | pt-PT | zh-CN | en-NZ | en-ZA | ca-ES | da-DK | fi-FI | id-ID | ms-MY | nl-NL | no-NO | pl-PL | sv-SE | tl-PH`
Required: Yes

 ** VocabularyId **   <a name="connect-Type-DefaultVocabulary-VocabularyId"></a>
The identifier of the custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** VocabularyName **   <a name="connect-Type-DefaultVocabulary-VocabularyName"></a>
A unique name of the custom vocabulary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

## See Also
<a name="API_DefaultVocabulary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DefaultVocabulary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DefaultVocabulary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DefaultVocabulary)
