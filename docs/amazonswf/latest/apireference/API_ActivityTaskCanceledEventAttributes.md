---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityTaskCanceledEventAttributes.html
---

# ActivityTaskCanceledEventAttributes
<a name="API_ActivityTaskCanceledEventAttributes"></a>

Provides the details of the `ActivityTaskCanceled` event.

## Contents
<a name="API_ActivityTaskCanceledEventAttributes_Contents"></a>

 ** scheduledEventId **   <a name="SWF-Type-ActivityTaskCanceledEventAttributes-scheduledEventId"></a>
The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** startedEventId **   <a name="SWF-Type-ActivityTaskCanceledEventAttributes-startedEventId"></a>
The ID of the `ActivityTaskStarted` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** details **   <a name="SWF-Type-ActivityTaskCanceledEventAttributes-details"></a>
Details of the cancellation.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** latestCancelRequestedEventId **   <a name="SWF-Type-ActivityTaskCanceledEventAttributes-latestCancelRequestedEventId"></a>
If set, contains the ID of the last `ActivityTaskCancelRequested` event recorded for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: No

## See Also
<a name="API_ActivityTaskCanceledEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ActivityTaskCanceledEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ActivityTaskCanceledEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ActivityTaskCanceledEventAttributes)
