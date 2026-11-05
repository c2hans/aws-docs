---
source_url: https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_CategoriesAttributeFilter.html
---

# CategoriesAttributeFilter
<a name="API_connect-contact-lens_CategoriesAttributeFilter"></a>

A filter that matches category segments based on the tags assigned to the rules that create the categories. Provide exactly one of `OrConditions`, `AndCondition`, or `TagCondition`.

## Contents
<a name="API_connect-contact-lens_CategoriesAttributeFilter_Contents"></a>

 ** AndCondition **   <a name="connect-Type-connect-contact-lens_CategoriesAttributeFilter-AndCondition"></a>
A condition that the filter evaluates using AND logic. A category segment matches only when all of the tag conditions in the condition are met.
Type: [CategoriesAttributeAndCondition](API_connect-contact-lens_CategoriesAttributeAndCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-connect-contact-lens_CategoriesAttributeFilter-OrConditions"></a>
A list of conditions that the filter evaluates using OR logic. A category segment matches when at least one of the conditions in the list is met.
Type: Array of [CategoriesAttributeAndCondition](API_connect-contact-lens_CategoriesAttributeAndCondition.md) objects
Array Members: Maximum number of 25 items.
Required: No

 ** TagCondition **   <a name="connect-Type-connect-contact-lens_CategoriesAttributeFilter-TagCondition"></a>
A single tag condition that a category segment must match. The category's rule must have the specified tag.
Type: [TagCondition](API_connect-contact-lens_TagCondition.md) object
Required: No

## See Also
<a name="API_connect-contact-lens_CategoriesAttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-contact-lens-2020-08-21/CategoriesAttributeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-contact-lens-2020-08-21/CategoriesAttributeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-contact-lens-2020-08-21/CategoriesAttributeFilter)
