---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_VocabularySettingsEntry.html
---

# VocabularySettingsEntry

A custom vocabulary for one language. Specify exactly one of `VocabularyName` or `Phrases`.

## Contents
<a name="API_VocabularySettingsEntry_Contents"></a>

 ** Language **   <a name="transcribe-Type-VocabularySettingsEntry-Language"></a>
The language this custom vocabulary applies to, as a base language code (for example, `en`). Each language can appear in only one entry.
Type: String
Valid Values: `en | es | fr | it | de | ja | pt | ko | zh-CN | zh-TW | zh-HK`
Required: Yes

 ** Phrases **   <a name="transcribe-Type-VocabularySettingsEntry-Phrases"></a>
Up to 100 phrases to use as a custom vocabulary, provided inline. You don't need to create the vocabulary first.
Include either `Phrases` or `VocabularyName` in each entry, but not both.
Type: Array of [VocabularyPhrase](API_VocabularyPhrase.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** VocabularyName **   <a name="transcribe-Type-VocabularySettingsEntry-VocabularyName"></a>
The name of a custom vocabulary you created. The vocabulary must be in the `READY` state, and its language must match this entry's `Language`.
Vocabulary names are case sensitive.
Include either `VocabularyName` or `Phrases` in each entry, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

## See Also
<a name="API_VocabularySettingsEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/VocabularySettingsEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/VocabularySettingsEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/VocabularySettingsEntry)
