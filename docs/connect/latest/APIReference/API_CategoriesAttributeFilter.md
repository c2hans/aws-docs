---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CategoriesAttributeFilter.html
---

# CategoriesAttributeFilter
<a name="API_CategoriesAttributeFilter"></a>

A filter that matches category segments based on the tags assigned to the rules that create the categories. Provide exactly one of `OrConditions`, `AndCondition`, or `TagCondition`.

## Contents
<a name="API_CategoriesAttributeFilter_Contents"></a>

 ** AndCondition **   <a name="connect-Type-CategoriesAttributeFilter-AndCondition"></a>
A condition that the filter evaluates using AND logic. A category segment matches only when all of the tag conditions in the condition are met.
Type: [CategoriesAttributeAndCondition](API_CategoriesAttributeAndCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-CategoriesAttributeFilter-OrConditions"></a>
A list of conditions that the filter evaluates using OR logic. A category segment matches when at least one of the conditions in the list is met.
Type: Array of [CategoriesAttributeAndCondition](API_CategoriesAttributeAndCondition.md) objects
Required: No

 ** TagCondition **   <a name="connect-Type-CategoriesAttributeFilter-TagCondition"></a>
A single tag condition that a category segment must match. The category's rule must have the specified tag key and value.
Type: [TagCondition](API_TagCondition.md) object
Required: No

## See Also
<a name="API_CategoriesAttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CategoriesAttributeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CategoriesAttributeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CategoriesAttributeFilter)
