---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_EventSubscription.html
---

# EventSubscription
<a name="API_EventSubscription"></a>

This data type is used in the [Subscription](API_Subscription.md) data type.

## Contents
<a name="API_EventSubscription_Contents"></a>

 ** event **   <a name="Inspector-Type-EventSubscription-event"></a>
The event for which Amazon Simple Notification Service (SNS) notifications are sent.
Type: String
Valid Values: `ASSESSMENT_RUN_STARTED | ASSESSMENT_RUN_COMPLETED | ASSESSMENT_RUN_STATE_CHANGED | FINDING_REPORTED | OTHER`
Required: Yes

 ** subscribedAt **   <a name="Inspector-Type-EventSubscription-subscribedAt"></a>
The time at which [SubscribeToEvent](API_SubscribeToEvent.md) is called.
Type: Timestamp
Required: Yes

## See Also
<a name="API_EventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/EventSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/EventSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/EventSubscription)
