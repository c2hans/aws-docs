---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_EventSubscription.html
---

# EventSubscription
<a name="API_EventSubscription"></a>

Contains the results of a successful invocation of the [DescribeEventSubscriptions](API_DescribeEventSubscriptions.md) action.

## Contents
<a name="API_EventSubscription_Contents"></a>

 ** CustomerAwsId **
The Amazon customer account associated with the event notification subscription.
Type: String
Required: No

 ** CustSubscriptionId **
The event notification subscription Id.
Type: String
Required: No

 ** Enabled **
A Boolean value indicating if the subscription is enabled. True indicates the subscription is enabled.
Type: Boolean
Required: No

 ** EventCategoriesList.EventCategory.N **
A list of event categories for the event notification subscription.
Type: Array of strings
Required: No

 ** EventSubscriptionArn **
The Amazon Resource Name (ARN) for the event subscription.
Type: String
Required: No

 ** SnsTopicArn **
The topic ARN of the event notification subscription.
Type: String
Required: No

 ** SourceIdsList.SourceId.N **
A list of source IDs for the event notification subscription.
Type: Array of strings
Required: No

 ** SourceType **
The source type for the event notification subscription.
Type: String
Required: No

 ** Status **
The status of the event notification subscription.
Constraints:
Can be one of the following: creating \| modifying \| deleting \| active \| no-permission \| topic-not-exist
The status "no-permission" indicates that Neptune no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.
Type: String
Required: No

 ** SubscriptionCreationTime **
The time the event notification subscription was created.
Type: String
Required: No

## See Also
<a name="API_EventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/EventSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/EventSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/EventSubscription)
