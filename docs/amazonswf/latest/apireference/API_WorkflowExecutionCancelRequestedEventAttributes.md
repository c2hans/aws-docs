---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionCancelRequestedEventAttributes.html
---

# WorkflowExecutionCancelRequestedEventAttributes
<a name="API_WorkflowExecutionCancelRequestedEventAttributes"></a>

Provides the details of the `WorkflowExecutionCancelRequested` event.

## Contents
<a name="API_WorkflowExecutionCancelRequestedEventAttributes_Contents"></a>

 ** cause **   <a name="SWF-Type-WorkflowExecutionCancelRequestedEventAttributes-cause"></a>
If set, indicates that the request to cancel the workflow execution was automatically generated, and specifies the cause. This happens if the parent workflow execution times out or is terminated, and the child policy is set to cancel child executions.
Type: String
Valid Values: `CHILD_POLICY_APPLIED`
Required: No

 ** externalInitiatedEventId **   <a name="SWF-Type-WorkflowExecutionCancelRequestedEventAttributes-externalInitiatedEventId"></a>
The ID of the `RequestCancelExternalWorkflowExecutionInitiated` event corresponding to the `RequestCancelExternalWorkflowExecution` decision to cancel this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: No

 ** externalWorkflowExecution **   <a name="SWF-Type-WorkflowExecutionCancelRequestedEventAttributes-externalWorkflowExecution"></a>
The external workflow execution for which the cancellation was requested.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: No

## See Also
<a name="API_WorkflowExecutionCancelRequestedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecutionCancelRequestedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecutionCancelRequestedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecutionCancelRequestedEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
