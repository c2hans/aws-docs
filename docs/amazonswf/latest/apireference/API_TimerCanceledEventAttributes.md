---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TimerCanceledEventAttributes.html
---

# TimerCanceledEventAttributes
<a name="API_TimerCanceledEventAttributes"></a>

 Provides the details of the `TimerCanceled` event.

## Contents
<a name="API_TimerCanceledEventAttributes_Contents"></a>

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-TimerCanceledEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `CancelTimer` decision to cancel this timer. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** startedEventId **   <a name="SWF-Type-TimerCanceledEventAttributes-startedEventId"></a>
The ID of the `TimerStarted` event that was recorded when this timer was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** timerId **   <a name="SWF-Type-TimerCanceledEventAttributes-timerId"></a>
The unique ID of the timer that was canceled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_TimerCanceledEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/TimerCanceledEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/TimerCanceledEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/TimerCanceledEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
