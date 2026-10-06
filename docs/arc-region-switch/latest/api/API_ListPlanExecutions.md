---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlanExecutions.html
---

# ListPlanExecutions
<a name="API_ListPlanExecutions"></a>

Lists the executions of a Region switch plan. This operation returns information about both current and historical executions.

## Request Syntax
<a name="API_ListPlanExecutions_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "planArn": "{{string}}",
   "state": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPlanExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPlanExecutions_RequestSyntax) **   <a name="regionswitch-ListPlanExecutions-request-maxResults"></a>
The number of objects that you want to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListPlanExecutions_RequestSyntax) **   <a name="regionswitch-ListPlanExecutions-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String
Required: No

 ** [planArn](#API_ListPlanExecutions_RequestSyntax) **   <a name="regionswitch-ListPlanExecutions-request-planArn"></a>
The ARN for the plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

 ** [state](#API_ListPlanExecutions_RequestSyntax) **   <a name="regionswitch-ListPlanExecutions-request-state"></a>
The state of the plan execution. For example, the plan execution might be In Progress.
Type: String
Valid Values: `inProgress | pausedByFailedStep | pausedByOperator | completed | completedWithExceptions | canceled | planExecutionTimedOut | pendingManualApproval | failed | pending | completedMonitoringApplicationHealth`
Required: No

## Response Syntax
<a name="API_ListPlanExecutions_ResponseSyntax"></a>

```
{
   "items": [
      {
         "actualRecoveryTime": "string",
         "comment": "string",
         "endTime": number,
         "executionAction": "string",
         "executionId": "string",
         "executionRegion": "string",
         "executionState": "string",
         "mode": "string",
         "planArn": "string",
         "recoveryExecutionId": "string",
         "startTime": number,
         "updatedAt": number,
         "version": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListPlanExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListPlanExecutions_ResponseSyntax) **   <a name="regionswitch-ListPlanExecutions-response-items"></a>
The items in the plan execution to return.
Type: Array of [AbbreviatedExecution](API_AbbreviatedExecution.md) objects

 ** [nextToken](#API_ListPlanExecutions_ResponseSyntax) **   <a name="regionswitch-ListPlanExecutions-response-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String

## Errors
<a name="API_ListPlanExecutions_Errors"></a>

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
<a name="API_ListPlanExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-region-switch-2022-07-26/ListPlanExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-region-switch-2022-07-26/ListPlanExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ListPlanExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-region-switch-2022-07-26/ListPlanExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ListPlanExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-region-switch-2022-07-26/ListPlanExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-region-switch-2022-07-26/ListPlanExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-region-switch-2022-07-26/ListPlanExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/arc-region-switch-2022-07-26/ListPlanExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ListPlanExecutions)
