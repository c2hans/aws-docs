---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_SignalExternalWorkflowExecutionInitiatedEventAttributes.html
---

# SignalExternalWorkflowExecutionInitiatedEventAttributes
<a name="API_SignalExternalWorkflowExecutionInitiatedEventAttributes"></a>

Provides the details of the `SignalExternalWorkflowExecutionInitiated` event.

## Contents
<a name="API_SignalExternalWorkflowExecutionInitiatedEventAttributes_Contents"></a>

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-SignalExternalWorkflowExecutionInitiatedEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `SignalExternalWorkflowExecution` decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** signalName **   <a name="SWF-Type-SignalExternalWorkflowExecutionInitiatedEventAttributes-signalName"></a>
The name of the signal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** workflowId **   <a name="SWF-Type-SignalExternalWorkflowExecutionInitiatedEventAttributes-workflowId"></a>
The `workflowId` of the external workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** control **   <a name="SWF-Type-SignalExternalWorkflowExecutionInitiatedEventAttributes-control"></a>
Data attached to the event that can be used by the decider in subsequent decision tasks.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** input **   <a name="SWF-Type-SignalExternalWorkflowExecutionInitiatedEventAttributes-input"></a>
The input provided to the signal.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** runId **   <a name="SWF-Type-SignalExternalWorkflowExecutionInitiatedEventAttributes-runId"></a>
The `runId` of the external workflow execution to send the signal to.
Type: String
Length Constraints: Maximum length of 64.
Required: No

## See Also
<a name="API_SignalExternalWorkflowExecutionInitiatedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/SignalExternalWorkflowExecutionInitiatedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/SignalExternalWorkflowExecutionInitiatedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/SignalExternalWorkflowExecutionInitiatedEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
