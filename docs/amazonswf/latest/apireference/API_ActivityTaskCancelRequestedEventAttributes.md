---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityTaskCancelRequestedEventAttributes.html
---

# ActivityTaskCancelRequestedEventAttributes
<a name="API_ActivityTaskCancelRequestedEventAttributes"></a>

Provides the details of the `ActivityTaskCancelRequested` event.

## Contents
<a name="API_ActivityTaskCancelRequestedEventAttributes_Contents"></a>

 ** activityId **   <a name="SWF-Type-ActivityTaskCancelRequestedEventAttributes-activityId"></a>
The unique ID of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-ActivityTaskCancelRequestedEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `RequestCancelActivityTask` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

## See Also
<a name="API_ActivityTaskCancelRequestedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ActivityTaskCancelRequestedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ActivityTaskCancelRequestedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ActivityTaskCancelRequestedEventAttributes)
