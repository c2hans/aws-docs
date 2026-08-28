---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ExternalWorkflowExecutionCancelRequestedEventAttributes.html
---

# ExternalWorkflowExecutionCancelRequestedEventAttributes
<a name="API_ExternalWorkflowExecutionCancelRequestedEventAttributes"></a>

Provides the details of the `ExternalWorkflowExecutionCancelRequested` event.

## Contents
<a name="API_ExternalWorkflowExecutionCancelRequestedEventAttributes_Contents"></a>

 ** initiatedEventId **   <a name="SWF-Type-ExternalWorkflowExecutionCancelRequestedEventAttributes-initiatedEventId"></a>
The ID of the `RequestCancelExternalWorkflowExecutionInitiated` event corresponding to the `RequestCancelExternalWorkflowExecution` decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** workflowExecution **   <a name="SWF-Type-ExternalWorkflowExecutionCancelRequestedEventAttributes-workflowExecution"></a>
The external workflow execution to which the cancellation request was delivered.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: Yes

## See Also
<a name="API_ExternalWorkflowExecutionCancelRequestedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ExternalWorkflowExecutionCancelRequestedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ExternalWorkflowExecutionCancelRequestedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ExternalWorkflowExecutionCancelRequestedEventAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
