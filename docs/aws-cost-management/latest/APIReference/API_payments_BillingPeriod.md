---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_BillingPeriod.html
---

# BillingPeriod

A billing period, as a half-open date range: `startDate` is inclusive and `endDate` is exclusive. Both members are calendar dates, carried as the timestamp of 00:00:00 UTC on that day.

## Contents
<a name="API_payments_BillingPeriod_Contents"></a>

 ** endDate **   <a name="awscostmanagement-Type-payments_BillingPeriod-endDate"></a>
The day after the last day of the billing period, exclusive, as the timestamp of 00:00:00 UTC on that day. A calendar month runs from the first of the month to the first of the next month.
Type: Timestamp
Required: Yes

 ** startDate **   <a name="awscostmanagement-Type-payments_BillingPeriod-startDate"></a>
The first day of the billing period, inclusive, as the timestamp of 00:00:00 UTC on that day.
Type: Timestamp
Required: Yes

## See Also
<a name="API_payments_BillingPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/BillingPeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/BillingPeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/BillingPeriod)
