---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CategoriesAttributeAndCondition.html
---

# CategoriesAttributeAndCondition
<a name="API_CategoriesAttributeAndCondition"></a>

A list of tag conditions that the filter evaluates together using AND logic. A category segment matches only when the tags on its rule satisfy every tag condition in the list.

## Contents
<a name="API_CategoriesAttributeAndCondition_Contents"></a>

 ** TagConditions **   <a name="connect-Type-CategoriesAttributeAndCondition-TagConditions"></a>
A list of tag conditions. All of the tag conditions must be met for the condition to match.
Type: Array of [TagCondition](API_TagCondition.md) objects
Required: No

## See Also
<a name="API_CategoriesAttributeAndCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CategoriesAttributeAndCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CategoriesAttributeAndCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CategoriesAttributeAndCondition)
