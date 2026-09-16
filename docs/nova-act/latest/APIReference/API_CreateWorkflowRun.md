---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateWorkflowRun.html
---

# CreateWorkflowRun
<a name="API_CreateWorkflowRun"></a>

Creates a new execution instance of a workflow definition with specified parameters.

## Request Syntax
<a name="API_CreateWorkflowRun_RequestSyntax"></a>

```
PUT /workflow-definitions/{{workflowDefinitionName}}/workflow-runs HTTP/1.1
Content-type: application/json

{
   "clientInfo": {
      "compatibilityVersion": {{number}},
      "sdkVersion": "{{string}}"
   },
   "clientToken": "{{string}}",
   "logGroupName": "{{string}}",
   "modelId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkflowRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowDefinitionName](#API_CreateWorkflowRun_RequestSyntax) **   <a name="novaact-CreateWorkflowRun-request-uri-workflowDefinitionName"></a>
The name of the workflow definition to execute.
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9_-]{1,40}`
Required: Yes

## Request Body
<a name="API_CreateWorkflowRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientInfo](#API_CreateWorkflowRun_RequestSyntax) **   <a name="novaact-CreateWorkflowRun-request-clientInfo"></a>
Information about the client making the request, including compatibility version and SDK version.
Type: [ClientInfo](API_ClientInfo.md) object
Required: Yes

 ** [clientToken](#API_CreateWorkflowRun_RequestSyntax) **   <a name="novaact-CreateWorkflowRun-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`
Required: No

 ** [logGroupName](#API_CreateWorkflowRun_RequestSyntax) **   <a name="novaact-CreateWorkflowRun-request-logGroupName"></a>
The CloudWatch log group name for storing workflow execution logs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9_/.-]+`
Required: No

 ** [modelId](#API_CreateWorkflowRun_RequestSyntax) **   <a name="novaact-CreateWorkflowRun-request-modelId"></a>
The ID of the AI model to use for workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_CreateWorkflowRun_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "status": "string",
   "workflowRunId": "string"
}
```

## Response Elements
<a name="API_CreateWorkflowRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [status](#API_CreateWorkflowRun_ResponseSyntax) **   <a name="novaact-CreateWorkflowRun-response-status"></a>
The initial status of the workflow run after creation.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT | DELETING`

 ** [workflowRunId](#API_CreateWorkflowRun_ResponseSyntax) **   <a name="novaact-CreateWorkflowRun-response-workflowRunId"></a>
The unique identifier for the created workflow run.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_CreateWorkflowRun_Errors"></a>

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
<a name="API_CreateWorkflowRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/nova-act-2025-08-22/CreateWorkflowRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/nova-act-2025-08-22/CreateWorkflowRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/CreateWorkflowRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/nova-act-2025-08-22/CreateWorkflowRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/CreateWorkflowRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/nova-act-2025-08-22/CreateWorkflowRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/nova-act-2025-08-22/CreateWorkflowRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/nova-act-2025-08-22/CreateWorkflowRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/nova-act-2025-08-22/CreateWorkflowRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/CreateWorkflowRun)
