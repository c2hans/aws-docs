---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-contact-lens_CategoriesAttributeAndCondition.html
---

# CategoriesAttributeAndCondition
<a name="API_connect-contact-lens_CategoriesAttributeAndCondition"></a>

A list of tag conditions that the filter evaluates together using AND logic. A category segment matches only when the tags on its rule satisfy every tag condition in the list.

## Contents
<a name="API_connect-contact-lens_CategoriesAttributeAndCondition_Contents"></a>

 ** TagConditions **   <a name="connect-Type-connect-contact-lens_CategoriesAttributeAndCondition-TagConditions"></a>
A list of tag conditions. All of the tag conditions must be met for the condition to match.
Type: Array of [TagCondition](API_connect-contact-lens_TagCondition.md) objects
Array Members: Maximum number of 25 items.
Required: No

## See Also
<a name="API_connect-contact-lens_CategoriesAttributeAndCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-contact-lens-2020-08-21/CategoriesAttributeAndCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-contact-lens-2020-08-21/CategoriesAttributeAndCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-contact-lens-2020-08-21/CategoriesAttributeAndCondition)
