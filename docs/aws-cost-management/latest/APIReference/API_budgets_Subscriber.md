---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Subscriber.html
---

# Subscriber
<a name="API_budgets_Subscriber"></a>

The subscriber to a budget notification. The subscriber consists of a subscription type and either an Amazon SNS topic or an email address.

For example, an email subscriber has the following parameters:
+ A `subscriptionType` of `EMAIL`
+ An `address` of `example@example.com`

## Contents
<a name="API_budgets_Subscriber_Contents"></a>

 ** Address **   <a name="awscostmanagement-Type-budgets_Subscriber-Address"></a>
The address that AWS sends budget notifications to, either an SNS topic or an email.
When you create a subscriber, the value of `Address` can't contain line breaks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2147483647.
Pattern: `(.*[\n\r\t\f\ ]?)*`
Required: Yes

 ** SubscriptionType **   <a name="awscostmanagement-Type-budgets_Subscriber-SubscriptionType"></a>
The type of notification that AWS sends to a subscriber.
Type: String
Valid Values: `SNS | EMAIL`
Required: Yes

## See Also
<a name="API_budgets_Subscriber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/Subscriber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/Subscriber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/Subscriber)
