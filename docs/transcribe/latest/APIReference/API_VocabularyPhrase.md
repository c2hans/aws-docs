---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_VocabularyPhrase.html
---

# VocabularyPhrase

A phrase in an inline custom vocabulary.

## Contents
<a name="API_VocabularyPhrase_Contents"></a>

 ** Text **   <a name="transcribe-Type-VocabularyPhrase-Text"></a>
The phrase to recognize in your audio.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** DisplayAs **   <a name="transcribe-Type-VocabularyPhrase-DisplayAs"></a>
How the phrase is written in your transcript. If you don't include `DisplayAs`, the phrase is written as it appears in `Text`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_VocabularyPhrase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/VocabularyPhrase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/VocabularyPhrase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/VocabularyPhrase)
