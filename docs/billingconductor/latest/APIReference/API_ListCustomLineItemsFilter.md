---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemsFilter.html
---

# ListCustomLineItemsFilter
<a name="API_ListCustomLineItemsFilter"></a>

A filter that specifies the custom line items and billing groups to retrieve FFLI information.

## Contents
<a name="API_ListCustomLineItemsFilter_Contents"></a>

 ** AccountIds **   <a name="billingconductor-Type-ListCustomLineItemsFilter-AccountIds"></a>
The AWS accounts in which this custom line item will be applied to.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Pattern: `[0-9]{12}`
Required: No

 ** Arns **   <a name="billingconductor-Type-ListCustomLineItemsFilter-Arns"></a>
A list of custom line item ARNs to retrieve information.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`
Required: No

 ** BillingGroups **   <a name="billingconductor-Type-ListCustomLineItemsFilter-BillingGroups"></a>
The billing group Amazon Resource Names (ARNs) to retrieve information.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: No

 ** Names **   <a name="billingconductor-Type-ListCustomLineItemsFilter-Names"></a>
A list of custom line items to retrieve information.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: No

## See Also
<a name="API_ListCustomLineItemsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListCustomLineItemsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListCustomLineItemsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListCustomLineItemsFilter)
