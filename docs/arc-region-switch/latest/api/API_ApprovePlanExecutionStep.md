---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ApprovePlanExecutionStep.html
---

# ApprovePlanExecutionStep
<a name="API_ApprovePlanExecutionStep"></a>

Approves a step in a plan execution that requires manual approval. When you create a plan, you can include approval steps that require manual intervention before the execution can proceed. This operation allows you to provide that approval.

You must specify the plan ARN, execution ID, step name, and approval status. You can also provide an optional comment explaining the approval decision.

## Request Parameters
<a name="API_ApprovePlanExecutionStep_RequestParameters"></a>

 ** approval **
The status of approval for a plan execution step.
Type: String
Valid Values: `approve | decline`
Required: Yes

 ** comment **
A comment that you can enter about a plan execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** executionId **
The execution identifier of a plan execution.
Type: String
Required: Yes

 ** planArn **
The Amazon Resource Name (ARN) of the plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

 ** stepName **
The name of a step in a plan execution.
Type: String
Required: Yes

## Errors
<a name="API_ApprovePlanExecutionStep_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404
HTTP Status Code: 404

## See Also
<a name="API_ApprovePlanExecutionStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/ApprovePlanExecutionStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/ApprovePlanExecutionStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ApprovePlanExecutionStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/ApprovePlanExecutionStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ApprovePlanExecutionStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/ApprovePlanExecutionStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/ApprovePlanExecutionStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/ApprovePlanExecutionStep)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/ApprovePlanExecutionStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ApprovePlanExecutionStep)
