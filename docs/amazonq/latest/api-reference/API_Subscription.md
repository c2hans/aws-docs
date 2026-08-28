---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Subscription.html
---

# Subscription
<a name="API_Subscription"></a>

Information about an Amazon Q Business subscription.

Subscriptions are used to provide access for an IAM Identity Center user or a group to an Amazon Q Business application.

Amazon Q Business offers two subscription tiers: `Q_LITE` and `Q_BUSINESS`. Subscription tier determines feature access for the user. For more information on subscriptions and pricing tiers, see [Amazon Q Business pricing](https://aws.amazon.com/q/business/pricing/).

## Contents
<a name="API_Subscription_Contents"></a>

 ** currentSubscription **   <a name="qbusiness-Type-Subscription-currentSubscription"></a>
The type of your current Amazon Q Business subscription.
Type: [SubscriptionDetails](API_SubscriptionDetails.md) object
Required: No

 ** nextSubscription **   <a name="qbusiness-Type-Subscription-nextSubscription"></a>
The type of the Amazon Q Business subscription for the next month.
Type: [SubscriptionDetails](API_SubscriptionDetails.md) object
Required: No

 ** principal **   <a name="qbusiness-Type-Subscription-principal"></a>
The IAM Identity Center `UserId` or `GroupId` of a user or group in the IAM Identity Center instance connected to the Amazon Q Business application.
Type: [SubscriptionPrincipal](API_SubscriptionPrincipal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** subscriptionArn **   <a name="qbusiness-Type-Subscription-subscriptionArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q Business subscription that was updated.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** subscriptionId **   <a name="qbusiness-Type-Subscription-subscriptionId"></a>
The identifier of the Amazon Q Business subscription to be updated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1224.
Required: No

## See Also
<a name="API_Subscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/Subscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/Subscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/Subscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
