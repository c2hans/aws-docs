---
source_url: https://docs.aws.amazon.com/pricingplanmanager/latest/APIReference/API_ScheduledChange.html
---

# ScheduledChange
<a name="API_ScheduledChange"></a>

A pending change on a subscription that takes effect at the end of the current billing period, such as a tier downgrade or cancellation.

## Contents
<a name="API_ScheduledChange_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** changeType **   <a name="pricingplanmanager-Type-ScheduledChange-changeType"></a>
The type of pending change. Possible values are `DOWNGRADE` (a tier change to a lower level) and `CANCELLATION` (subscription termination).
Type: String
Valid Values: `DOWNGRADE | CANCELLATION`
Required: Yes

 ** effectiveDate **   <a name="pricingplanmanager-Type-ScheduledChange-effectiveDate"></a>
The date and time when the change takes effect, in ISO 8601 format. This value is populated after the change is confirmed by the billing system.
Type: Timestamp
Required: No

 ** planTier **   <a name="pricingplanmanager-Type-ScheduledChange-planTier"></a>
For downgrades, the tier level that the subscription will change to. Not present for cancellations.
Type: String
Required: No

 ** usageLevel **   <a name="pricingplanmanager-Type-ScheduledChange-usageLevel"></a>
For downgrades, the target usage level after the change takes effect.
Type: String
Required: No

## See Also
<a name="API_ScheduledChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-plan-manager-2025-08-05/ScheduledChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-plan-manager-2025-08-05/ScheduledChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-plan-manager-2025-08-05/ScheduledChange)
