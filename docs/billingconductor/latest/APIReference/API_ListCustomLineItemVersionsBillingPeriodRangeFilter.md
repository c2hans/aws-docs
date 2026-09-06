---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemVersionsBillingPeriodRangeFilter.html
---

# ListCustomLineItemVersionsBillingPeriodRangeFilter
<a name="API_ListCustomLineItemVersionsBillingPeriodRangeFilter"></a>

A billing period filter that specifies the custom line item versions to retrieve.

## Contents
<a name="API_ListCustomLineItemVersionsBillingPeriodRangeFilter_Contents"></a>

 ** EndBillingPeriod **   <a name="billingconductor-Type-ListCustomLineItemVersionsBillingPeriodRangeFilter-EndBillingPeriod"></a>
The exclusive end billing period that defines a billing period range where a custom line item version is applied.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

 ** StartBillingPeriod **   <a name="billingconductor-Type-ListCustomLineItemVersionsBillingPeriodRangeFilter-StartBillingPeriod"></a>
The inclusive start billing period that defines a billing period range where a custom line item version is applied.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

## See Also
<a name="API_ListCustomLineItemVersionsBillingPeriodRangeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListCustomLineItemVersionsBillingPeriodRangeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListCustomLineItemVersionsBillingPeriodRangeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListCustomLineItemVersionsBillingPeriodRangeFilter)
