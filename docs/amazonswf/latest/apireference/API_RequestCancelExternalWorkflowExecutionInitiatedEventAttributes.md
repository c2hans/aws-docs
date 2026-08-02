---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RequestCancelExternalWorkflowExecutionInitiatedEventAttributes.html
---

# RequestCancelExternalWorkflowExecutionInitiatedEventAttributes
<a name="API_RequestCancelExternalWorkflowExecutionInitiatedEventAttributes"></a>

Provides the details of the `RequestCancelExternalWorkflowExecutionInitiated` event.

## Contents
<a name="API_RequestCancelExternalWorkflowExecutionInitiatedEventAttributes_Contents"></a>

 ** decisionTaskCompletedEventId **   <a name="SWF-Type-RequestCancelExternalWorkflowExecutionInitiatedEventAttributes-decisionTaskCompletedEventId"></a>
The ID of the `DecisionTaskCompleted` event corresponding to the decision task that resulted in the `RequestCancelExternalWorkflowExecution` decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** workflowId **   <a name="SWF-Type-RequestCancelExternalWorkflowExecutionInitiatedEventAttributes-workflowId"></a>
The `workflowId` of the external workflow execution to be canceled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** control **   <a name="SWF-Type-RequestCancelExternalWorkflowExecutionInitiatedEventAttributes-control"></a>
Data attached to the event that can be used by the decider in subsequent workflow tasks.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** runId **   <a name="SWF-Type-RequestCancelExternalWorkflowExecutionInitiatedEventAttributes-runId"></a>
The `runId` of the external workflow execution to be canceled.
Type: String
Length Constraints: Maximum length of 64.
Required: No

## See Also
<a name="API_RequestCancelExternalWorkflowExecutionInitiatedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/RequestCancelExternalWorkflowExecutionInitiatedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/RequestCancelExternalWorkflowExecutionInitiatedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/RequestCancelExternalWorkflowExecutionInitiatedEventAttributes)
