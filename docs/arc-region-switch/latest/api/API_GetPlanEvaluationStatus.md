---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanEvaluationStatus.html
---

# GetPlanEvaluationStatus
<a name="API_GetPlanEvaluationStatus"></a>

Retrieves the evaluation status of a Region switch plan. The evaluation status provides information about the last time the plan was evaluated and any warnings or issues detected.

## Request Parameters
<a name="API_GetPlanEvaluationStatus_RequestParameters"></a>

 ** maxResults **
The number of objects that you want to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** planArn **
The Amazon Resource Name (ARN) of the Region switch plan to retrieve evaluation status for.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

## Response Elements
<a name="API_GetPlanEvaluationStatus_ResponseElements"></a>

The following elements are returned by the service.

 ** evaluationState **
The evaluation state for the plan.
Type: String
Valid Values: `passed | actionRequired | pendingEvaluation | unknown`

 ** lastEvaluatedVersion **
The version of the last evaluation of the plan.
Type: String

 ** lastEvaluationTime **
The time of the last time that Region switch ran an evaluation of the plan.
Type: Timestamp

 ** nextToken **
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** planArn **
The Amazon Resource Name (ARN) of the plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`

 ** region **
The AWS Region for the plan.
Type: String
Pattern: `[a-z]{2}-[a-z-]+-\d+`

 ** warnings **
The current evaluation warnings for the plan.
Type: Array of [ResourceWarning](API_ResourceWarning.md) objects

## Errors
<a name="API_GetPlanEvaluationStatus_Errors"></a>

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
<a name="API_GetPlanEvaluationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/GetPlanEvaluationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/GetPlanEvaluationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/GetPlanEvaluationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/GetPlanEvaluationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/GetPlanEvaluationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/GetPlanEvaluationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/GetPlanEvaluationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/GetPlanEvaluationStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/GetPlanEvaluationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/GetPlanEvaluationStatus)
