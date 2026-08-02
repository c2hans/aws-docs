---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CustomVocabularyItem.html
---

# CustomVocabularyItem
<a name="API_CustomVocabularyItem"></a>

The unique custom vocabulary item from the custom vocabulary list.

## Contents
<a name="API_CustomVocabularyItem_Contents"></a>

 ** itemId **   <a name="lexv2-Type-CustomVocabularyItem-itemId"></a>
The unique item identifer for the custom vocabulary item from the custom vocabulary list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** phrase **   <a name="lexv2-Type-CustomVocabularyItem-phrase"></a>
The unique phrase for the custom vocabulary item from the custom vocabulary list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** displayAs **   <a name="lexv2-Type-CustomVocabularyItem-displayAs"></a>
The DisplayAs value for the custom vocabulary item from the custom vocabulary list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** weight **   <a name="lexv2-Type-CustomVocabularyItem-weight"></a>
The weight assigned for the custom vocabulary item from the custom vocabulary list.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3.
Required: No

## See Also
<a name="API_CustomVocabularyItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CustomVocabularyItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CustomVocabularyItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CustomVocabularyItem)
