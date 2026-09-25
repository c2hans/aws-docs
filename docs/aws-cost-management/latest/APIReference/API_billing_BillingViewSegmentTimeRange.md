---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingViewSegmentTimeRange.html
---

# BillingViewSegmentTimeRange
<a name="API_billing_BillingViewSegmentTimeRange"></a>

 Specifies a time range with an inclusive begin date and an exclusive end date.

## Contents
<a name="API_billing_BillingViewSegmentTimeRange_Contents"></a>

 ** beginDateInclusive **   <a name="awscostmanagement-Type-billing_BillingViewSegmentTimeRange-beginDateInclusive"></a>
 The inclusive start of the time range. This value can't be in the future.
Type: Timestamp
Required: No

 ** endDateExclusive **   <a name="awscostmanagement-Type-billing_BillingViewSegmentTimeRange-endDateExclusive"></a>
 The exclusive end of the time range. This value must be after `beginDateInclusive`.
Type: Timestamp
Required: No

## See Also
<a name="API_billing_BillingViewSegmentTimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/BillingViewSegmentTimeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/BillingViewSegmentTimeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/BillingViewSegmentTimeRange)
