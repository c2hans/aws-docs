---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TimerFiredEventAttributes.html
---

# TimerFiredEventAttributes
<a name="API_TimerFiredEventAttributes"></a>

Provides the details of the `TimerFired` event.

## Contents
<a name="API_TimerFiredEventAttributes_Contents"></a>

 ** startedEventId **   <a name="SWF-Type-TimerFiredEventAttributes-startedEventId"></a>
The ID of the `TimerStarted` event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** timerId **   <a name="SWF-Type-TimerFiredEventAttributes-timerId"></a>
The unique ID of the timer that fired.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_TimerFiredEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/TimerFiredEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/TimerFiredEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/TimerFiredEventAttributes)
