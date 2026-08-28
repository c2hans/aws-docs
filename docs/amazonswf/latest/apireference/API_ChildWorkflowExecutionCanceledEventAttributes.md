---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ChildWorkflowExecutionCanceledEventAttributes.html
---

# ChildWorkflowExecutionCanceledEventAttributes
<a name="API_ChildWorkflowExecutionCanceledEventAttributes"></a>

Provide details of the `ChildWorkflowExecutionCanceled` event.

## Contents
<a name="API_ChildWorkflowExecutionCanceledEventAttributes_Contents"></a>

 ** initiatedEventId **   <a name="SWF-Type-ChildWorkflowExecutionCanceledEventAttributes-initiatedEventId"></a>
The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution` [Decision](API_Decision.md) to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** startedEventId **   <a name="SWF-Type-ChildWorkflowExecutionCanceledEventAttributes-startedEventId"></a>
The ID of the `ChildWorkflowExecutionStarted` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** workflowExecution **   <a name="SWF-Type-ChildWorkflowExecutionCanceledEventAttributes-workflowExecution"></a>
The child workflow execution that was canceled.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: Yes

 ** workflowType **   <a name="SWF-Type-ChildWorkflowExecutionCanceledEventAttributes-workflowType"></a>
The type of the child workflow execution.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

 ** details **   <a name="SWF-Type-ChildWorkflowExecutionCanceledEventAttributes-details"></a>
Details of the cancellation (if provided).
Type: String
Length Constraints: Maximum length of 32768.
Required: No

## See Also
<a name="API_ChildWorkflowExecutionCanceledEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ChildWorkflowExecutionCanceledEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ChildWorkflowExecutionCanceledEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ChildWorkflowExecutionCanceledEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
