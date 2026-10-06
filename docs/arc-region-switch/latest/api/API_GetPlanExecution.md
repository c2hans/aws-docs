---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanExecution.html
---

# GetPlanExecution
<a name="API_GetPlanExecution"></a>

Retrieves detailed information about a specific plan execution. You must specify the plan ARN and execution ID.

## Request Syntax
<a name="API_GetPlanExecution_RequestSyntax"></a>

```
{
   "executionId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "planArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPlanExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [executionId](#API_GetPlanExecution_RequestSyntax) **   <a name="regionswitch-GetPlanExecution-request-executionId"></a>
The execution identifier of a plan execution.
Type: String
Required: Yes

 ** [maxResults](#API_GetPlanExecution_RequestSyntax) **   <a name="regionswitch-GetPlanExecution-request-maxResults"></a>
The number of objects that you want to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_GetPlanExecution_RequestSyntax) **   <a name="regionswitch-GetPlanExecution-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String
Required: No

 ** [planArn](#API_GetPlanExecution_RequestSyntax) **   <a name="regionswitch-GetPlanExecution-request-planArn"></a>
The Amazon Resource Name (ARN) of the plan with the execution to retrieve.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

## Response Syntax
<a name="API_GetPlanExecution_ResponseSyntax"></a>

```
{
   "actualRecoveryTime": "string",
   "comment": "string",
   "endTime": number,
   "executionAction": "string",
   "executionId": "string",
   "executionRegion": "string",
   "executionState": "string",
   "generatedReportDetails": [
      {
         "reportGenerationTime": number,
         "reportOutput": { ... }
      }
   ],
   "mode": "string",
   "nextToken": "string",
   "plan": {
      "arn": "string",
      "associatedAlarms": {
         "string" : {
            "alarmType": "string",
            "crossAccountRole": "string",
            "externalId": "string",
            "resourceIdentifier": "string"
         }
      },
      "description": "string",
      "executionRole": "string",
      "name": "string",
      "owner": "string",
      "primaryRegion": "string",
      "recoveryApproach": "string",
      "recoveryTimeObjectiveMinutes": number,
      "regions": [ "string" ],
      "reportConfiguration": {
         "reportOutput": [
            { ... }
         ]
      },
      "triggers": [
         {
            "action": "string",
            "conditions": [
               {
                  "associatedAlarmName": "string",
                  "condition": "string"
               }
            ],
            "description": "string",
            "minDelayMinutesBetweenExecutions": number,
            "targetRegion": "string"
         }
      ],
      "updatedAt": number,
      "version": "string",
      "workflows": [
         {
            "steps": [
               {
                  "description": "string",
                  "executionBlockConfiguration": { ... },
                  "executionBlockType": "string",
                  "name": "string"
               }
            ],
            "workflowDescription": "string",
            "workflowTargetAction": "string",
            "workflowTargetRegion": "string"
         }
      ]
   },
   "planArn": "string",
   "recoveryExecutionId": "string",
   "startTime": number,
   "stepStates": [
      {
         "endTime": number,
         "name": "string",
         "startTime": number,
         "status": "string",
         "stepMode": "string"
      }
   ],
   "updatedAt": number,
   "version": "string"
}
```

## Response Elements
<a name="API_GetPlanExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actualRecoveryTime](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-actualRecoveryTime"></a>
The actual recovery time that Region switch calculates for a plan execution. Actual recovery time includes the time for the plan to run added to the time elapsed until the application health alarms that you've specified are healthy again.
Type: String
Pattern: `P(?!$)(\d+Y)?(\d+M)?(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+S)?)?`

 ** [comment](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-comment"></a>
A comment included on the plan execution.
Type: String

 ** [endTime](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-endTime"></a>
The time (UTC) when the plan execution ended.
Type: Timestamp

 ** [executionAction](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-executionAction"></a>
The plan execution action. Valid values are `activate`, to activate an AWS Region, or `deactivate`, to deactivate a Region.
Type: String
Valid Values: `activate | deactivate | postRecovery`

 ** [executionId](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-executionId"></a>
The execution identifier of a plan execution.
Type: String

 ** [executionRegion](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-executionRegion"></a>
The AWS Region for a plan execution.
Type: String

 ** [executionState](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-executionState"></a>
The plan execution state. Provides the state of a plan execution, for example, In Progress or Paused by Operator.
Type: String
Valid Values: `inProgress | pausedByFailedStep | pausedByOperator | completed | completedWithExceptions | canceled | planExecutionTimedOut | pendingManualApproval | failed | pending | completedMonitoringApplicationHealth`

 ** [generatedReportDetails](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-generatedReportDetails"></a>
Information about the location of a generated report, or the cause of its failure.
Type: Array of [GeneratedReport](API_GeneratedReport.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [mode](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-mode"></a>
The plan execution mode. Valid values are `graceful`, for graceful executions, or `ungraceful`, for ungraceful executions.
Type: String
Valid Values: `graceful | ungraceful`

 ** [nextToken](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String

 ** [plan](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-plan"></a>
The details of the Region switch plan.
Type: [Plan](API_Plan.md) object

 ** [planArn](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-planArn"></a>
The Amazon Resource Name (ARN) of the plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`

 ** [recoveryExecutionId](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-recoveryExecutionId"></a>
The unique identifier of the most recent recovery execution. Required when starting a post-recovery execution.
Type: String

 ** [startTime](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-startTime"></a>
The time (UTC) when the plan execution started.
Type: Timestamp

 ** [stepStates](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-stepStates"></a>
The states of the steps in the plan execution.
Type: Array of [StepState](API_StepState.md) objects

 ** [updatedAt](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-updatedAt"></a>
The timestamp when the plan execution was last updated.
Type: Timestamp

 ** [version](#API_GetPlanExecution_ResponseSyntax) **   <a name="regionswitch-GetPlanExecution-response-version"></a>
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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/GetPlanExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/GetPlanExecution)
