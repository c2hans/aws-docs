---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_TextMatchItem.html
---

# TextMatchItem
<a name="API_TextMatchItem"></a>

A structure indicating matched terms for an attribute.

## Contents
<a name="API_TextMatchItem_Contents"></a>

 ** attribute **   <a name="datazone-Type-TextMatchItem-attribute"></a>
The name of the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** matchOffsets **   <a name="datazone-Type-TextMatchItem-matchOffsets"></a>
List of offsets indicating matching terms in the TextMatchItem text.
Type: Array of [MatchOffset](API_MatchOffset.md) objects
Required: No

 ** text **   <a name="datazone-Type-TextMatchItem-text"></a>
Snippet of attribute text containing highlighted content.
Type: String
Required: No

## See Also
<a name="API_TextMatchItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/TextMatchItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/TextMatchItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/TextMatchItem)
