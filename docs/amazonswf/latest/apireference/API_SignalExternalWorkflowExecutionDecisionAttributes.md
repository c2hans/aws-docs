---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_SignalExternalWorkflowExecutionDecisionAttributes.html
---

# SignalExternalWorkflowExecutionDecisionAttributes
<a name="API_SignalExternalWorkflowExecutionDecisionAttributes"></a>

Provides the details of the `SignalExternalWorkflowExecution` decision.

 **Access Control**

You can use IAM policies to control this decision's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ You cannot use an IAM policy to constrain this action's parameters.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Contents
<a name="API_SignalExternalWorkflowExecutionDecisionAttributes_Contents"></a>

 ** signalName **   <a name="SWF-Type-SignalExternalWorkflowExecutionDecisionAttributes-signalName"></a>
 The name of the signal.The target workflow execution uses the signal name and input to process the signal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** workflowId **   <a name="SWF-Type-SignalExternalWorkflowExecutionDecisionAttributes-workflowId"></a>
 The `workflowId` of the workflow execution to be signaled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** control **   <a name="SWF-Type-SignalExternalWorkflowExecutionDecisionAttributes-control"></a>
The data attached to the event that can be used by the decider in subsequent decision tasks.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** input **   <a name="SWF-Type-SignalExternalWorkflowExecutionDecisionAttributes-input"></a>
 The input data to be provided with the signal. The target workflow execution uses the signal name and input data to process the signal.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** runId **   <a name="SWF-Type-SignalExternalWorkflowExecutionDecisionAttributes-runId"></a>
The `runId` of the workflow execution to be signaled.
Type: String
Length Constraints: Maximum length of 64.
Required: No

## See Also
<a name="API_SignalExternalWorkflowExecutionDecisionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/SignalExternalWorkflowExecutionDecisionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/SignalExternalWorkflowExecutionDecisionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/SignalExternalWorkflowExecutionDecisionAttributes)
