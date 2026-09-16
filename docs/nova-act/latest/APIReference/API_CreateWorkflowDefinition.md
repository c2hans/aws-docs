---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateWorkflowDefinition.html
---

# CreateWorkflowDefinition
<a name="API_CreateWorkflowDefinition"></a>

Creates a new workflow definition template that can be used to execute multiple workflow runs.

## Request Syntax
<a name="API_CreateWorkflowDefinition_RequestSyntax"></a>

```
PUT /workflow-definitions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "exportConfig": {
      "s3BucketName": "{{string}}",
      "s3KeyPrefix": "{{string}}"
   },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkflowDefinition_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWorkflowDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateWorkflowDefinition_RequestSyntax) **   <a name="novaact-CreateWorkflowDefinition-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`
Required: No

 ** [description](#API_CreateWorkflowDefinition_RequestSyntax) **   <a name="novaact-CreateWorkflowDefinition-request-description"></a>
An optional description of the workflow definition's purpose and functionality.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Required: No

 ** [exportConfig](#API_CreateWorkflowDefinition_RequestSyntax) **   <a name="novaact-CreateWorkflowDefinition-request-exportConfig"></a>
Configuration for exporting workflow execution data to Amazon Simple Storage Service.
Type: [WorkflowExportConfig](API_WorkflowExportConfig.md) object
Required: No

 ** [name](#API_CreateWorkflowDefinition_RequestSyntax) **   <a name="novaact-CreateWorkflowDefinition-request-name"></a>
The name of the workflow definition. Must be unique within your account and region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9_-]{1,40}`
Required: Yes

## Response Syntax
<a name="API_CreateWorkflowDefinition_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_CreateWorkflowDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [status](#API_CreateWorkflowDefinition_ResponseSyntax) **   <a name="novaact-CreateWorkflowDefinition-response-status"></a>
The current status of the workflow definition after creation.
Type: String
Valid Values: `ACTIVE | DELETING`

## Errors
<a name="API_CreateWorkflowDefinition_Errors"></a>

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
<a name="API_CreateWorkflowDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/nova-act-2025-08-22/CreateWorkflowDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/nova-act-2025-08-22/CreateWorkflowDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/CreateWorkflowDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/nova-act-2025-08-22/CreateWorkflowDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/CreateWorkflowDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/nova-act-2025-08-22/CreateWorkflowDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/nova-act-2025-08-22/CreateWorkflowDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/nova-act-2025-08-22/CreateWorkflowDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/nova-act-2025-08-22/CreateWorkflowDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/CreateWorkflowDefinition)
