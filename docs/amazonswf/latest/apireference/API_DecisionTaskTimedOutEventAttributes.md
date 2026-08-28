---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DecisionTaskTimedOutEventAttributes.html
---

# DecisionTaskTimedOutEventAttributes
<a name="API_DecisionTaskTimedOutEventAttributes"></a>

Provides the details of the `DecisionTaskTimedOut` event.

## Contents
<a name="API_DecisionTaskTimedOutEventAttributes_Contents"></a>

 ** scheduledEventId **   <a name="SWF-Type-DecisionTaskTimedOutEventAttributes-scheduledEventId"></a>
The ID of the `DecisionTaskScheduled` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** startedEventId **   <a name="SWF-Type-DecisionTaskTimedOutEventAttributes-startedEventId"></a>
The ID of the `DecisionTaskStarted` event recorded when this decision task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** timeoutType **   <a name="SWF-Type-DecisionTaskTimedOutEventAttributes-timeoutType"></a>
The type of timeout that expired before the decision task could be completed.
Type: String
Valid Values: `START_TO_CLOSE | SCHEDULE_TO_START`
Required: Yes

## See Also
<a name="API_DecisionTaskTimedOutEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/DecisionTaskTimedOutEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/DecisionTaskTimedOutEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/DecisionTaskTimedOutEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
