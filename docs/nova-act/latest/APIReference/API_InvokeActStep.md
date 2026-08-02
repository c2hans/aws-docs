---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_InvokeActStep.html
---

# InvokeActStep
<a name="API_InvokeActStep"></a>

Executes the next step of an act, processing tool call results and returning new tool calls if needed.

## Request Syntax
<a name="API_InvokeActStep_RequestSyntax"></a>

```
PUT /workflow-definitions/{{workflowDefinitionName}}/workflow-runs/{{workflowRunId}}/sessions/{{sessionId}}/acts/{{actId}}/invoke-step/ HTTP/1.1
Content-type: application/json

{
   "callResults": [
      {
         "callId": "{{string}}",
         "content": [
            { ... }
         ]
      }
   ],
   "previousStepId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_InvokeActStep_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actId](#API_InvokeActStep_RequestSyntax) **   <a name="novaact-InvokeActStep-request-uri-actId"></a>
The unique identifier of the act to invoke the next step for.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [sessionId](#API_InvokeActStep_RequestSyntax) **   <a name="novaact-InvokeActStep-request-uri-sessionId"></a>
The unique identifier of the session containing the act.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [workflowDefinitionName](#API_InvokeActStep_RequestSyntax) **   <a name="novaact-InvokeActStep-request-uri-workflowDefinitionName"></a>
The name of the workflow definition containing the act.
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9_-]{1,40}`
Required: Yes

 ** [workflowRunId](#API_InvokeActStep_RequestSyntax) **   <a name="novaact-InvokeActStep-request-uri-workflowRunId"></a>
The unique identifier of the workflow run containing the act.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_InvokeActStep_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [callResults](#API_InvokeActStep_RequestSyntax) **   <a name="novaact-InvokeActStep-request-callResults"></a>
The results from previous tool calls that the act requested.
Type: Array of [CallResult](API_CallResult.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [previousStepId](#API_InvokeActStep_RequestSyntax) **   <a name="novaact-InvokeActStep-request-previousStepId"></a>
The identifier of the previous step, used for tracking execution flow.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## Response Syntax
<a name="API_InvokeActStep_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "calls": [
      {
         "callId": "string",
         "input": JSON value,
         "name": "string"
      }
   ],
   "stepId": "string"
}
```

## Response Elements
<a name="API_InvokeActStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [calls](#API_InvokeActStep_ResponseSyntax) **   <a name="novaact-InvokeActStep-response-calls"></a>
A list of tool calls that the act wants to execute in this step.
Type: Array of [Call](API_Call.md) objects

 ** [stepId](#API_InvokeActStep_ResponseSyntax) **   <a name="novaact-InvokeActStep-response-stepId"></a>
The unique identifier for this execution step.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_InvokeActStep_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient permissions to perform this action.
 ** message **
You don't have sufficient permissions to perform this action. Verify your IAM permissions and try again.
HTTP Status Code: 403

 [ConflictException](API_ConflictException.md)
The request could not be completed due to a conflict with the current state of the resource.
 ** message **
The requested operation conflicts with the current state of the resource.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 409

 [InternalServerException](API_InternalServerException.md)
An internal server error occurred. Please try again later.
 ** message **
The service encountered an internal error. Try again later.
 ** reason **
The reason for the internal server error.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The requested resource was not found.
 ** message **
The specified resource was not found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 404

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The request would exceed a service quota limit.
 ** message **
The request would exceed one or more service quotas for your account.
 ** quotaCode **
The code for the specific quota that was exceeded.
 ** resourceId **
The identifier of the resource that exceeded the quota.
 ** resourceType **
The type of resource that exceeded the quota.
 ** serviceCode **
The service code for the quota that was exceeded.
HTTP Status Code: 402

 [ThrottlingException](API_ThrottlingException.md)
The request was throttled due to too many requests. Please try again later.
 ** message **
The request was denied due to request throttling.
 ** quotaCode **
The quota code related to the throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the throttled request.
 ** serviceCode **
The service code where throttling occurred.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input parameters for the request are invalid.
 ** fieldList **
The list of fields that failed validation.
 ** message **
The input fails to satisfy the constraints specified by the service.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_InvokeActStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/nova-act-2025-08-22/InvokeActStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/nova-act-2025-08-22/InvokeActStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/InvokeActStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/nova-act-2025-08-22/InvokeActStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/InvokeActStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/nova-act-2025-08-22/InvokeActStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/nova-act-2025-08-22/InvokeActStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/nova-act-2025-08-22/InvokeActStep)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/nova-act-2025-08-22/InvokeActStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/InvokeActStep)
