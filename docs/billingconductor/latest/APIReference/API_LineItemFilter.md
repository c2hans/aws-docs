---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_LineItemFilter.html
---

# LineItemFilter
<a name="API_LineItemFilter"></a>

A representation of the line item filter for your custom line item. You can use line item filters to include or exclude specific resource values from the billing group's total cost. For example, if you create a custom line item and you want to filter out a value, such as Savings Plans discounts, you can update `LineItemFilter` to exclude it.

## Contents
<a name="API_LineItemFilter_Contents"></a>

 ** Attribute **   <a name="billingconductor-Type-LineItemFilter-Attribute"></a>
The attribute of the line item filter. This specifies what attribute that you can filter on.
Type: String
Valid Values: `LINE_ITEM_TYPE | SERVICE`
Required: Yes

 ** MatchOption **   <a name="billingconductor-Type-LineItemFilter-MatchOption"></a>
The match criteria of the line item filter. This parameter specifies whether not to include the resource value from the billing group total cost.
Type: String
Valid Values: `NOT_EQUAL | EQUAL`
Required: Yes

 ** AttributeValues **   <a name="billingconductor-Type-LineItemFilter-AttributeValues"></a>
The values of the line item filter. This specifies the values to filter on.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+`
Required: No

 ** Values **   <a name="billingconductor-Type-LineItemFilter-Values"></a>
The values of the line item filter. This specifies the values to filter on. Currently, you can only exclude Savings Plans discounts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `SAVINGS_PLAN_NEGATION`
Required: No

## See Also
<a name="API_LineItemFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/LineItemFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/LineItemFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/LineItemFilter)
