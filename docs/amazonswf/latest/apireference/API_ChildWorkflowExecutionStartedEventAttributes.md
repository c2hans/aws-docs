---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ChildWorkflowExecutionStartedEventAttributes.html
---

# ChildWorkflowExecutionStartedEventAttributes
<a name="API_ChildWorkflowExecutionStartedEventAttributes"></a>

Provides the details of the `ChildWorkflowExecutionStarted` event.

## Contents
<a name="API_ChildWorkflowExecutionStartedEventAttributes_Contents"></a>

 ** initiatedEventId **   <a name="SWF-Type-ChildWorkflowExecutionStartedEventAttributes-initiatedEventId"></a>
The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution` [Decision](API_Decision.md) to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** workflowExecution **   <a name="SWF-Type-ChildWorkflowExecutionStartedEventAttributes-workflowExecution"></a>
The child workflow execution that was started.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: Yes

 ** workflowType **   <a name="SWF-Type-ChildWorkflowExecutionStartedEventAttributes-workflowType"></a>
The type of the child workflow execution.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

## See Also
<a name="API_ChildWorkflowExecutionStartedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ChildWorkflowExecutionStartedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ChildWorkflowExecutionStartedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ChildWorkflowExecutionStartedEventAttributes)
