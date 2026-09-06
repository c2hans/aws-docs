---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemChargeDetails.html
---

# ListCustomLineItemChargeDetails
<a name="API_ListCustomLineItemChargeDetails"></a>

 A representation of the charge details of a custom line item.

## Contents
<a name="API_ListCustomLineItemChargeDetails_Contents"></a>

 ** Type **   <a name="billingconductor-Type-ListCustomLineItemChargeDetails-Type"></a>
 The type of the custom line item that indicates whether the charge is a `fee` or `credit`.
Type: String
Valid Values: `CREDIT | FEE`
Required: Yes

 ** Flat **   <a name="billingconductor-Type-ListCustomLineItemChargeDetails-Flat"></a>
 A `ListCustomLineItemFlatChargeDetails` that describes the charge details of a flat custom line item.
Type: [ListCustomLineItemFlatChargeDetails](API_ListCustomLineItemFlatChargeDetails.md) object
Required: No

 ** LineItemFilters **   <a name="billingconductor-Type-ListCustomLineItemChargeDetails-LineItemFilters"></a>
A representation of the line item filter.
Type: Array of [LineItemFilter](API_LineItemFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** Percentage **   <a name="billingconductor-Type-ListCustomLineItemChargeDetails-Percentage"></a>
 A `ListCustomLineItemPercentageChargeDetails` that describes the charge details of a percentage custom line item.
Type: [ListCustomLineItemPercentageChargeDetails](API_ListCustomLineItemPercentageChargeDetails.md) object
Required: No

## See Also
<a name="API_ListCustomLineItemChargeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListCustomLineItemChargeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListCustomLineItemChargeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListCustomLineItemChargeDetails)
