---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_Subscription.html
---

# Subscription
<a name="API_Subscription"></a>

This data type is used as a response element in the [ListEventSubscriptions](API_ListEventSubscriptions.md) action.

## Contents
<a name="API_Subscription_Contents"></a>

 ** eventSubscriptions **   <a name="Inspector-Type-Subscription-eventSubscriptions"></a>
The list of existing event subscriptions.
Type: Array of [EventSubscription](API_EventSubscription.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

 ** resourceArn **   <a name="Inspector-Type-Subscription-resourceArn"></a>
The ARN of the assessment template that is used during the event for which the SNS notification is sent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** topicArn **   <a name="Inspector-Type-Subscription-topicArn"></a>
The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS notifications are sent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## See Also
<a name="API_Subscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/Subscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/Subscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/Subscription)
