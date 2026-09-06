---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityTaskTimedOutEventAttributes.html
---

# ActivityTaskTimedOutEventAttributes
<a name="API_ActivityTaskTimedOutEventAttributes"></a>

Provides the details of the `ActivityTaskTimedOut` event.

## Contents
<a name="API_ActivityTaskTimedOutEventAttributes_Contents"></a>

 ** scheduledEventId **   <a name="SWF-Type-ActivityTaskTimedOutEventAttributes-scheduledEventId"></a>
The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** startedEventId **   <a name="SWF-Type-ActivityTaskTimedOutEventAttributes-startedEventId"></a>
The ID of the `ActivityTaskStarted` event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** timeoutType **   <a name="SWF-Type-ActivityTaskTimedOutEventAttributes-timeoutType"></a>
The type of the timeout that caused this event.
Type: String
Valid Values: `START_TO_CLOSE | SCHEDULE_TO_START | SCHEDULE_TO_CLOSE | HEARTBEAT`
Required: Yes

 ** details **   <a name="SWF-Type-ActivityTaskTimedOutEventAttributes-details"></a>
Contains the content of the `details` parameter for the last call made by the activity to `RecordActivityTaskHeartbeat`.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

## See Also
<a name="API_ActivityTaskTimedOutEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ActivityTaskTimedOutEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ActivityTaskTimedOutEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ActivityTaskTimedOutEventAttributes)
