---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ChildWorkflowExecutionTimedOutEventAttributes.html
---

# ChildWorkflowExecutionTimedOutEventAttributes
<a name="API_ChildWorkflowExecutionTimedOutEventAttributes"></a>

Provides the details of the `ChildWorkflowExecutionTimedOut` event.

## Contents
<a name="API_ChildWorkflowExecutionTimedOutEventAttributes_Contents"></a>

 ** initiatedEventId **   <a name="SWF-Type-ChildWorkflowExecutionTimedOutEventAttributes-initiatedEventId"></a>
The ID of the `StartChildWorkflowExecutionInitiated` event corresponding to the `StartChildWorkflowExecution` [Decision](API_Decision.md) to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** startedEventId **   <a name="SWF-Type-ChildWorkflowExecutionTimedOutEventAttributes-startedEventId"></a>
The ID of the `ChildWorkflowExecutionStarted` event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** timeoutType **   <a name="SWF-Type-ChildWorkflowExecutionTimedOutEventAttributes-timeoutType"></a>
The type of the timeout that caused the child workflow execution to time out.
Type: String
Valid Values: `START_TO_CLOSE`
Required: Yes

 ** workflowExecution **   <a name="SWF-Type-ChildWorkflowExecutionTimedOutEventAttributes-workflowExecution"></a>
The child workflow execution that timed out.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: Yes

 ** workflowType **   <a name="SWF-Type-ChildWorkflowExecutionTimedOutEventAttributes-workflowType"></a>
The type of the child workflow execution.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

## See Also
<a name="API_ChildWorkflowExecutionTimedOutEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ChildWorkflowExecutionTimedOutEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ChildWorkflowExecutionTimedOutEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ChildWorkflowExecutionTimedOutEventAttributes)
