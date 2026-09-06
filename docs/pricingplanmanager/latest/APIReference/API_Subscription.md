---
source_url: https://docs.aws.amazon.com/pricingplanmanager/latest/APIReference/API_Subscription.html
---

# Subscription
<a name="API_Subscription"></a>

The full details of a flat-rate pricing subscription, including its current configuration, status, and associated resources.

## Contents
<a name="API_Subscription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="pricingplanmanager-Type-Subscription-arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies this subscription.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** createdAt **   <a name="pricingplanmanager-Type-Subscription-createdAt"></a>
The date and time when the subscription was created, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** planFamily **   <a name="pricingplanmanager-Type-Subscription-planFamily"></a>
The pricing plan family for the subscription, such as `CloudFront`.
Type: String
Required: Yes

 ** planTier **   <a name="pricingplanmanager-Type-Subscription-planTier"></a>
The current tier level of the pricing plan, such as `FREE`, `PRO`, `BUSINESS`, or `PREMIUM`.
Type: String
Required: Yes

 ** resourceArns **   <a name="pricingplanmanager-Type-Subscription-resourceArns"></a>
The ARNs of the AWS resources covered by this subscription.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** status **   <a name="pricingplanmanager-Type-Subscription-status"></a>
The current status of the subscription. For the list of possible values, see the `Status` type.
Type: String
Valid Values: `PENDING_APPROVAL | ACTIVE | SYNC_IN_PROGRESS | FAILED`
Required: Yes

 ** updatedAt **   <a name="pricingplanmanager-Type-Subscription-updatedAt"></a>
The date and time when the subscription was last modified, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** scheduledChange **   <a name="pricingplanmanager-Type-Subscription-scheduledChange"></a>
A pending change that will take effect at the end of the current billing period. This field is present only when a downgrade or cancellation is scheduled.
Type: [ScheduledChange](API_ScheduledChange.md) object
Required: No

 ** statusReason **   <a name="pricingplanmanager-Type-Subscription-statusReason"></a>
A human-readable explanation of the current status, present when additional context is available.
Type: String
Required: No

 ** usageLevel **   <a name="pricingplanmanager-Type-Subscription-usageLevel"></a>
The usage level within the plan tier. When present, indicates a specific capacity configuration beyond the base tier.
Type: String
Required: No

## See Also
<a name="API_Subscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-plan-manager-2025-08-05/Subscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-plan-manager-2025-08-05/Subscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-plan-manager-2025-08-05/Subscription)
