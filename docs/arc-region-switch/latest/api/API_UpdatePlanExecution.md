---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlanExecution.html
---

# UpdatePlanExecution
<a name="API_UpdatePlanExecution"></a>

Updates an in-progress plan execution. This operation allows you to modify certain aspects of the execution, such as adding a comment or changing the action.

## Request Parameters
<a name="API_UpdatePlanExecution_RequestParameters"></a>

 ** action **
The action specified for a plan execution, for example, Switch to Graceful or Pause.
Type: String
Valid Values: `switchToGraceful | switchToUngraceful | pause | resume`
Required: Yes

 ** comment **
An optional comment about the plan execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** executionId **
The execution identifier of a plan execution.
Type: String
Required: Yes

 ** planArn **
The Amazon Resource Name (ARN) of the plan with the execution to update.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

## Errors
<a name="API_UpdatePlanExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403
HTTP Status Code: 403

 ** IllegalStateException **
The operation failed because the current state of the resource doesn't allow the operation to proceed.
HTTP Status Code: 400
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404
HTTP Status Code: 404

## See Also
<a name="API_UpdatePlanExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/UpdatePlanExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/UpdatePlanExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/UpdatePlanExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/UpdatePlanExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/UpdatePlanExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/UpdatePlanExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/UpdatePlanExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/UpdatePlanExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/UpdatePlanExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/UpdatePlanExecution)
