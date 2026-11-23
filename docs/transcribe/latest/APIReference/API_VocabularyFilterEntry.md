---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_VocabularyFilterEntry.html
---

# VocabularyFilterEntry

A custom vocabulary filter for one language. Specify exactly one of `VocabularyFilterName` or `Words`.

## Contents
<a name="API_VocabularyFilterEntry_Contents"></a>

 ** Language **   <a name="transcribe-Type-VocabularyFilterEntry-Language"></a>
The language this custom vocabulary filter applies to, as a base language code (for example, `en`). Each language can appear in only one entry.
Type: String
Valid Values: `en | es | fr | it | de | ja | pt | ko | zh-CN | zh-TW | zh-HK`
Required: Yes

 ** VocabularyFilterName **   <a name="transcribe-Type-VocabularyFilterEntry-VocabularyFilterName"></a>
The name of a custom vocabulary filter you created. The filter's language must match this entry's `Language`.
Vocabulary filter names are case sensitive.
Include either `VocabularyFilterName` or `Words` in each entry, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** Words **   <a name="transcribe-Type-VocabularyFilterEntry-Words"></a>
The words to filter, provided inline. You don't need to create the vocabulary filter first.
Include either `Words` or `VocabularyFilterName` in each entry, but not both.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_VocabularyFilterEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/VocabularyFilterEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/VocabularyFilterEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/VocabularyFilterEntry)
