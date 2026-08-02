---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityTaskStartedEventAttributes.html
---

# ActivityTaskStartedEventAttributes
<a name="API_ActivityTaskStartedEventAttributes"></a>

Provides the details of the `ActivityTaskStarted` event.

## Contents
<a name="API_ActivityTaskStartedEventAttributes_Contents"></a>

 ** scheduledEventId **   <a name="SWF-Type-ActivityTaskStartedEventAttributes-scheduledEventId"></a>
The ID of the `ActivityTaskScheduled` event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** identity **   <a name="SWF-Type-ActivityTaskStartedEventAttributes-identity"></a>
Identity of the worker that was assigned this task. This aids diagnostics when problems arise. The form of this identity is user defined.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ActivityTaskStartedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ActivityTaskStartedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ActivityTaskStartedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ActivityTaskStartedEventAttributes)
