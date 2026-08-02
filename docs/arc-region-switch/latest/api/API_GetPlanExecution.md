---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanExecution.html
---

# GetPlanExecution
<a name="API_GetPlanExecution"></a>

Retrieves detailed information about a specific plan execution. You must specify the plan ARN and execution ID.

## Request Parameters
<a name="API_GetPlanExecution_RequestParameters"></a>

 ** executionId **
The execution identifier of a plan execution.
Type: String
Required: Yes

 ** maxResults **
The number of objects that you want to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String
Required: No

 ** planArn **
The Amazon Resource Name (ARN) of the plan with the execution to retrieve.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

## Response Elements
<a name="API_GetPlanExecution_ResponseElements"></a>

The following elements are returned by the service.

 ** actualRecoveryTime **
The actual recovery time that Region switch calculates for a plan execution. Actual recovery time includes the time for the plan to run added to the time elapsed until the application health alarms that you've specified are healthy again.
Type: String
Pattern: `P(?!$)(\d+Y)?(\d+M)?(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+S)?)?`

 ** comment **
A comment included on the plan execution.
Type: String

 ** endTime **
The time (UTC) when the plan execution ended.
Type: Timestamp

 ** executionAction **
The plan execution action. Valid values are `activate`, to activate an AWS Region, or `deactivate`, to deactivate a Region.
Type: String
Valid Values: `activate | deactivate | postRecovery`

 ** executionId **
The execution identifier of a plan execution.
Type: String

 ** executionRegion **
The AWS Region for a plan execution.
Type: String

 ** executionState **
The plan execution state. Provides the state of a plan execution, for example, In Progress or Paused by Operator.
Type: String
Valid Values: `inProgress | pausedByFailedStep | pausedByOperator | completed | completedWithExceptions | canceled | planExecutionTimedOut | pendingManualApproval | failed | pending | completedMonitoringApplicationHealth`

 ** generatedReportDetails **
Information about the location of a generated report, or the cause of its failure.
Type: Array of [GeneratedReport](API_GeneratedReport.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** mode **
The plan execution mode. Valid values are `graceful`, for graceful executions, or `ungraceful`, for ungraceful executions.
Type: String
Valid Values: `graceful | ungraceful`

 ** nextToken **
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String

 ** plan **
The details of the Region switch plan.
Type: [Plan](API_Plan.md) object

 ** planArn **
The Amazon Resource Name (ARN) of the plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`

 ** recoveryExecutionId **
The unique identifier of the most recent recovery execution. Required when starting a post-recovery execution.
Type: String

 ** startTime **
The time (UTC) when the plan execution started.
Type: Timestamp

 ** stepStates **
The states of the steps in the plan execution.
Type: Array of [StepState](API_StepState.md) objects

 ** updatedAt **
The timestamp when the plan execution was last updated.
Type: Timestamp

 ** version **
The version for the plan.
Type: String

## Errors
<a name="API_GetPlanExecution_Errors"></a>

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
<a name="API_GetPlanExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/GetPlanExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/GetPlanExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/GetPlanExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/GetPlanExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/GetPlanExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/GetPlanExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/GetPlanExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/GetPlanExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/GetPlanExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/GetPlanExecution)
