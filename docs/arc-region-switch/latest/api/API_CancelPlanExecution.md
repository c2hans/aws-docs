---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CancelPlanExecution.html
---

# CancelPlanExecution
<a name="API_CancelPlanExecution"></a>

Cancels an in-progress plan execution. This operation stops the execution of the plan and prevents any further steps from being processed.

You must specify the plan ARN and execution ID. You can also provide an optional comment explaining why the execution was canceled.

## Request Syntax
<a name="API_CancelPlanExecution_RequestSyntax"></a>

```
{
   "comment": "{{string}}",
   "executionId": "{{string}}",
   "planArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelPlanExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [comment](#API_CancelPlanExecution_RequestSyntax) **   <a name="regionswitch-CancelPlanExecution-request-comment"></a>
A comment that you can enter about canceling a plan execution step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [executionId](#API_CancelPlanExecution_RequestSyntax) **   <a name="regionswitch-CancelPlanExecution-request-executionId"></a>
The execution identifier of a plan execution.
Type: String
Required: Yes

 ** [planArn](#API_CancelPlanExecution_RequestSyntax) **   <a name="regionswitch-CancelPlanExecution-request-planArn"></a>
The Amazon Resource Name (ARN) of the plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

## Response Elements
<a name="API_CancelPlanExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelPlanExecution_Errors"></a>

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
<a name="API_CancelPlanExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/CancelPlanExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/CancelPlanExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/CancelPlanExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/CancelPlanExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/CancelPlanExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/CancelPlanExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/CancelPlanExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/CancelPlanExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/CancelPlanExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/CancelPlanExecution)
