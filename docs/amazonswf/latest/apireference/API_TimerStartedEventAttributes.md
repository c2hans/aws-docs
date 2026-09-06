---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TimerStartedEventAttributes.html
---

# TimerStartedEventAttributes
<a name="API_TimerStartedEventAttributes"></a>

Provides the details of the `TimerStarted` event.

## Contents
<a name="API_TimerStartedEventAttributes_Contents"></a>

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-TimerStartedEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `StartTimer` decision for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** startToFireTimeout **   <a name="SWF-Type-TimerStartedEventAttributes-startToFireTimeout"></a>
The duration of time after which the timer fires.
The duration is specified in seconds, an integer greater than or equal to `0`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Required: Yes

 ** timerId **   <a name="SWF-Type-TimerStartedEventAttributes-timerId"></a>
The unique ID of the timer that was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** control **   <a name="SWF-Type-TimerStartedEventAttributes-control"></a>
Data attached to the event that can be used by the decider in subsequent workflow tasks.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

## See Also
<a name="API_TimerStartedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/TimerStartedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/TimerStartedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/TimerStartedEventAttributes)
