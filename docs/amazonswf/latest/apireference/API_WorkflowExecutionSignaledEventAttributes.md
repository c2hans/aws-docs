---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionSignaledEventAttributes.html
---

# WorkflowExecutionSignaledEventAttributes
<a name="API_WorkflowExecutionSignaledEventAttributes"></a>

Provides the details of the `WorkflowExecutionSignaled` event.

## Contents
<a name="API_WorkflowExecutionSignaledEventAttributes_Contents"></a>

 ** signalName **   <a name="SWF-Type-WorkflowExecutionSignaledEventAttributes-signalName"></a>
The name of the signal received. The decider can use the signal name and inputs to determine how to the process the signal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** externalInitiatedEventId **   <a name="SWF-Type-WorkflowExecutionSignaledEventAttributes-externalInitiatedEventId"></a>
The ID of the `SignalExternalWorkflowExecutionInitiated` event corresponding to the `SignalExternalWorkflow` decision to signal this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event. This field is set only if the signal was initiated by another workflow execution.
Type: Long
Required: No

 ** externalWorkflowExecution **   <a name="SWF-Type-WorkflowExecutionSignaledEventAttributes-externalWorkflowExecution"></a>
The workflow execution that sent the signal. This is set only of the signal was sent by another workflow execution.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: No

 ** input **   <a name="SWF-Type-WorkflowExecutionSignaledEventAttributes-input"></a>
The inputs provided with the signal. The decider can use the signal name and inputs to determine how to process the signal.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

## See Also
<a name="API_WorkflowExecutionSignaledEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecutionSignaledEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecutionSignaledEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecutionSignaledEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
