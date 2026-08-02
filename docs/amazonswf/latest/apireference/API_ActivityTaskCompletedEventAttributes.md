---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityTaskCompletedEventAttributes.html
---

# ActivityTaskCompletedEventAttributes
<a name="API_ActivityTaskCompletedEventAttributes"></a>

Provides the details of the `ActivityTaskCompleted` event.

## Contents
<a name="API_ActivityTaskCompletedEventAttributes_Contents"></a>

 ** scheduledEventId **   <a name="SWF-Type-ActivityTaskCompletedEventAttributes-scheduledEventId"></a>
The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** startedEventId **   <a name="SWF-Type-ActivityTaskCompletedEventAttributes-startedEventId"></a>
The ID of the `ActivityTaskStarted` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** result **   <a name="SWF-Type-ActivityTaskCompletedEventAttributes-result"></a>
The results of the activity task.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

## See Also
<a name="API_ActivityTaskCompletedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ActivityTaskCompletedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ActivityTaskCompletedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ActivityTaskCompletedEventAttributes)
