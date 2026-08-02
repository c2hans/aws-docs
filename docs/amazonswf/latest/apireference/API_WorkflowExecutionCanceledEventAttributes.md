---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionCanceledEventAttributes.html
---

# WorkflowExecutionCanceledEventAttributes
<a name="API_WorkflowExecutionCanceledEventAttributes"></a>

Provides the details of the `WorkflowExecutionCanceled` event.

## Contents
<a name="API_WorkflowExecutionCanceledEventAttributes_Contents"></a>

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-WorkflowExecutionCanceledEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `CancelWorkflowExecution` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** details **   <a name="SWF-Type-WorkflowExecutionCanceledEventAttributes-details"></a>
The details of the cancellation.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

## See Also
<a name="API_WorkflowExecutionCanceledEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/WorkflowExecutionCanceledEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/WorkflowExecutionCanceledEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/WorkflowExecutionCanceledEventAttributes)
