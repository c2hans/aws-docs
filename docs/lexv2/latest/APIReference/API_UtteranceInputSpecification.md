---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UtteranceInputSpecification.html
---

# UtteranceInputSpecification
<a name="API_UtteranceInputSpecification"></a>

Contains information about input of an utterance.

## Contents
<a name="API_UtteranceInputSpecification_Contents"></a>

 ** audioInput **   <a name="lexv2-Type-UtteranceInputSpecification-audioInput"></a>
Contains information about the audio input for an utterance.
Type: [UtteranceAudioInputSpecification](API_UtteranceAudioInputSpecification.md) object
Required: No

 ** textInput **   <a name="lexv2-Type-UtteranceInputSpecification-textInput"></a>
A text input transcription of the utterance. It is only applicable for test-sets containing text data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_UtteranceInputSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UtteranceInputSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UtteranceInputSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UtteranceInputSpecification)
