---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_VocabularyFilterSettings.html
---

# VocabularyFilterSettings

Custom vocabulary filters to apply to your transcript, and how to apply them.

## Contents
<a name="API_VocabularyFilterSettings_Contents"></a>

 ** Filters **   <a name="transcribe-Type-VocabularyFilterSettings-Filters"></a>
Custom vocabulary filters, with one entry per language. In each entry, you can reference a custom vocabulary filter you created or provide words inline. All entries must use the same type, either all by name or all inline.
If you specify `Language`, include exactly one entry, and its `Language` must match. If you use `LanguageDetectionMode`, you can include one entry for each language in `LanguageOptions`.
Type: Array of [VocabularyFilterEntry](API_VocabularyFilterEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** VocabularyFilterMethod **   <a name="transcribe-Type-VocabularyFilterSettings-VocabularyFilterMethod"></a>
Specify how you want your custom vocabulary filter applied to your transcript.
To replace words with `***`, choose `mask`.
To delete words, choose `remove`.
To flag words without changing them, choose `tag`.
Type: String
Valid Values: `remove | mask | tag`
Required: Yes

## See Also
<a name="API_VocabularyFilterSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/VocabularyFilterSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/VocabularyFilterSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/VocabularyFilterSettings)
