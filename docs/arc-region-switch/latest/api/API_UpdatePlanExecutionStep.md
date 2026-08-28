---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlanExecutionStep.html
---

# UpdatePlanExecutionStep
<a name="API_UpdatePlanExecutionStep"></a>

Updates a specific step in an in-progress plan execution. This operation allows you to modify the step's comment or action.

## Request Parameters
<a name="API_UpdatePlanExecutionStep_RequestParameters"></a>

 ** actionToTake **
The updated action to take for the step. This can be used to skip or retry a step.
Type: String
Valid Values: `switchToUngraceful | skip`
Required: Yes

 ** comment **
An optional comment about the plan execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** executionId **
The unique identifier of the plan execution containing the step to update.
Type: String
Required: Yes

 ** planArn **
The Amazon Resource Name (ARN) of the plan containing the execution step to update.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

 ** stepName **
The name of the execution step to update.
Type: String
Required: Yes

## Errors
<a name="API_UpdatePlanExecutionStep_Errors"></a>

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
<a name="API_UpdatePlanExecutionStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/UpdatePlanExecutionStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/UpdatePlanExecutionStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/UpdatePlanExecutionStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/UpdatePlanExecutionStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/UpdatePlanExecutionStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/UpdatePlanExecutionStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/UpdatePlanExecutionStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/UpdatePlanExecutionStep)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/UpdatePlanExecutionStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/UpdatePlanExecutionStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
