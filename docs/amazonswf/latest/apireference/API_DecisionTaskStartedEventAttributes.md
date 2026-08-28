---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DecisionTaskStartedEventAttributes.html
---

# DecisionTaskStartedEventAttributes
<a name="API_DecisionTaskStartedEventAttributes"></a>

Provides the details of the `DecisionTaskStarted` event.

## Contents
<a name="API_DecisionTaskStartedEventAttributes_Contents"></a>

 ** scheduledEventId **   <a name="SWF-Type-DecisionTaskStartedEventAttributes-scheduledEventId"></a>
The ID of the `DecisionTaskScheduled` event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** identity **   <a name="SWF-Type-DecisionTaskStartedEventAttributes-identity"></a>
Identity of the decider making the request. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_DecisionTaskStartedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/DecisionTaskStartedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/DecisionTaskStartedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/DecisionTaskStartedEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
