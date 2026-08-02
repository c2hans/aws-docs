---
source_url: https://docs.aws.amazon.com/pricingplanmanager/latest/APIReference/API_SubscriptionSummary.html
---

# SubscriptionSummary
<a name="API_SubscriptionSummary"></a>

Summary information for a flat-rate pricing subscription, as returned by list operations.

## Contents
<a name="API_SubscriptionSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="pricingplanmanager-Type-SubscriptionSummary-arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies this subscription.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** createdAt **   <a name="pricingplanmanager-Type-SubscriptionSummary-createdAt"></a>
The date and time when the subscription was created, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** eTag **   <a name="pricingplanmanager-Type-SubscriptionSummary-eTag"></a>
The entity tag for concurrency control. Pass this value in the `If-Match` header when making changes to this subscription.
Type: String
Required: Yes

 ** planFamily **   <a name="pricingplanmanager-Type-SubscriptionSummary-planFamily"></a>
The pricing plan family for the subscription, such as `CloudFront`.
Type: String
Required: Yes

 ** planTier **   <a name="pricingplanmanager-Type-SubscriptionSummary-planTier"></a>
The current tier level of the pricing plan.
Type: String
Required: Yes

 ** resourceArns **   <a name="pricingplanmanager-Type-SubscriptionSummary-resourceArns"></a>
The ARNs of the AWS resources covered by this subscription.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** status **   <a name="pricingplanmanager-Type-SubscriptionSummary-status"></a>
The current status of the subscription.
Type: String
Valid Values: `PENDING_APPROVAL | ACTIVE | SYNC_IN_PROGRESS | FAILED`
Required: Yes

 ** updatedAt **   <a name="pricingplanmanager-Type-SubscriptionSummary-updatedAt"></a>
The date and time when the subscription was last modified, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** scheduledChange **   <a name="pricingplanmanager-Type-SubscriptionSummary-scheduledChange"></a>
A pending change that will take effect at the end of the current billing period, if any.
Type: [ScheduledChange](API_ScheduledChange.md) object
Required: No

 ** statusReason **   <a name="pricingplanmanager-Type-SubscriptionSummary-statusReason"></a>
A human-readable explanation of the current status, present when additional context is available.
Type: String
Required: No

 ** usageLevel **   <a name="pricingplanmanager-Type-SubscriptionSummary-usageLevel"></a>
The usage level within the plan tier.
Type: String
Required: No

## See Also
<a name="API_SubscriptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-plan-manager-2025-08-05/SubscriptionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-plan-manager-2025-08-05/SubscriptionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-plan-manager-2025-08-05/SubscriptionSummary)
