---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateCustomLineItemChargeDetails.html
---

# UpdateCustomLineItemChargeDetails
<a name="API_UpdateCustomLineItemChargeDetails"></a>

 A representation of the new charge details of a custom line item. This should contain only one of `Flat` or `Percentage`.

## Contents
<a name="API_UpdateCustomLineItemChargeDetails_Contents"></a>

 ** Flat **   <a name="billingconductor-Type-UpdateCustomLineItemChargeDetails-Flat"></a>
 An `UpdateCustomLineItemFlatChargeDetails` that describes the new charge details of a flat custom line item.
Type: [UpdateCustomLineItemFlatChargeDetails](API_UpdateCustomLineItemFlatChargeDetails.md) object
Required: No

 ** LineItemFilters **   <a name="billingconductor-Type-UpdateCustomLineItemChargeDetails-LineItemFilters"></a>
A representation of the line item filter.
Type: Array of [LineItemFilter](API_LineItemFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** Percentage **   <a name="billingconductor-Type-UpdateCustomLineItemChargeDetails-Percentage"></a>
 An `UpdateCustomLineItemPercentageChargeDetails` that describes the new charge details of a percentage custom line item.
Type: [UpdateCustomLineItemPercentageChargeDetails](API_UpdateCustomLineItemPercentageChargeDetails.md) object
Required: No

## See Also
<a name="API_UpdateCustomLineItemChargeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/UpdateCustomLineItemChargeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/UpdateCustomLineItemChargeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/UpdateCustomLineItemChargeDetails)
