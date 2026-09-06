---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListGoals.html
---

# ListGoals
<a name="API_ListGoals"></a>

Lists goals in the specified agent space with optional filtering

## Request Syntax
<a name="API_ListGoals_RequestSyntax"></a>

```
POST /backlog/agent-space/{{agentSpaceId}}/goals/list HTTP/1.1
Content-type: application/json

{
   "goalType": "{{string}}",
   "limit": {{number}},
   "nextToken": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListGoals_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_ListGoals_RequestSyntax) **   <a name="devopsagent-ListGoals-request-uri-agentSpaceId"></a>
The unique identifier for the agent space
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_ListGoals_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [goalType](#API_ListGoals_RequestSyntax) **   <a name="devopsagent-ListGoals-request-goalType"></a>
Filter goals by goal type
Type: String
Valid Values: `CUSTOMER_DEFINED | ONCALL_REPORT`
Required: No

 ** [limit](#API_ListGoals_RequestSyntax) **   <a name="devopsagent-ListGoals-request-limit"></a>
Maximum number of goals to return
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListGoals_RequestSyntax) **   <a name="devopsagent-ListGoals-request-nextToken"></a>
Pagination token for the next set of results
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [status](#API_ListGoals_RequestSyntax) **   <a name="devopsagent-ListGoals-request-status"></a>
Filter goals by goal status
Type: String
Valid Values: `ACTIVE | PAUSED | COMPLETE`
Required: No

## Response Syntax
<a name="API_ListGoals_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "goals": [
      {
         "agentSpaceArn": "string",
         "content": {
            "description": "string",
            "objectives": "string"
         },
         "createdAt": "string",
         "evaluationSchedule": {
            "expression": "string",
            "state": "string"
         },
         "goalId": "string",
         "goalType": "string",
         "lastEvaluatedAt": "string",
         "lastSuccessfulTaskId": "string",
         "lastTaskId": "string",
         "status": "string",
         "title": "string",
         "updatedAt": "string",
         "version": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListGoals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [goals](#API_ListGoals_ResponseSyntax) **   <a name="devopsagent-ListGoals-response-goals"></a>
List of goals matching the criteria
Type: Array of [Goal](API_Goal.md) objects

 ** [nextToken](#API_ListGoals_ResponseSyntax) **   <a name="devopsagent-ListGoals-response-nextToken"></a>
Pagination token for the next set of results
Type: String

## Errors
<a name="API_ListGoals_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the requested resource is denied due to insufficient permissions.
 ** message **
Detailed error message describing why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
Detailed error message describing the conflict.
HTTP Status Code: 409

 ** ContentSizeExceededException **
This exception is thrown when the content size exceeds the allowed limit.
HTTP Status Code: 413

 ** InternalServerException **
This exception is thrown when an unexpected error occurs in the processing of a request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters provided in the request are invalid.
 ** message **
Detailed error message describing which parameter is invalid and why.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** message **
Detailed error message describing which resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed the service quota limit.
 ** message **
Detailed error message describing which quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Please slow down and try again.
 ** message **
Detailed error message describing the throttling condition.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListGoals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/ListGoals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/ListGoals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ListGoals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/ListGoals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ListGoals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/ListGoals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/ListGoals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/ListGoals)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/ListGoals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ListGoals)
