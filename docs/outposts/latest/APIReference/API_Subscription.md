---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_Subscription.html
---

# Subscription
<a name="API_Subscription"></a>

Provides information about your AWS Outposts subscriptions.

## Contents
<a name="API_Subscription_Contents"></a>

 ** BeginDate **   <a name="outposts-Type-Subscription-BeginDate"></a>
The date your subscription starts.
Type: Timestamp
Required: No

 ** Currency **   <a name="outposts-Type-Subscription-Currency"></a>
The currency of the subscription price. Currently only `USD` is supported.
Type: String
Valid Values: `USD`
Required: No

 ** EndDate **   <a name="outposts-Type-Subscription-EndDate"></a>
The date your subscription ends.
Type: Timestamp
Required: No

 ** MonthlyRecurringPrice **   <a name="outposts-Type-Subscription-MonthlyRecurringPrice"></a>
The amount you are billed each month in the subscription period.
Type: Double
Required: No

 ** OrderIds **   <a name="outposts-Type-Subscription-OrderIds"></a>
The order ID for your subscription.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\S \n]+$`
Required: No

 ** SubscriptionId **   <a name="outposts-Type-Subscription-SubscriptionId"></a>
The ID of the subscription that appears on the AWS Billing Center console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\S \n]+$`
Required: No

 ** SubscriptionStatus **   <a name="outposts-Type-Subscription-SubscriptionStatus"></a>
The status of subscription which can be one of the following:
+  **INACTIVE** - Subscription requests that are inactive.
+  **ACTIVE** - Subscription requests that are in progress and have an end date in the future.
+  **PENDING** - Subscription has been created but billing has not yet commenced because the subscription begin date has not been reached.
+  **CANCELLED** - Subscription requests that are cancelled.
Type: String
Valid Values: `ACTIVE | PENDING | INACTIVE | CANCELLED`
Required: No

 ** SubscriptionType **   <a name="outposts-Type-Subscription-SubscriptionType"></a>
The type of subscription which can be one of the following:
+  **ORIGINAL** - The first order on the AWS Outposts.
+  **RENEWAL** - Renewal requests, both month to month and longer term.
+  **CAPACITY\_INCREASE** - Capacity scaling orders.
Type: String
Valid Values: `ORIGINAL | RENEWAL | CAPACITY_INCREASE`
Required: No

 ** UpfrontPrice **   <a name="outposts-Type-Subscription-UpfrontPrice"></a>
The amount billed when the subscription is created. This is a one-time charge.
Type: Double
Required: No

## See Also
<a name="API_Subscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/Subscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/Subscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/Subscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
