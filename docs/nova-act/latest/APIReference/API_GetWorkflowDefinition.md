---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_GetWorkflowDefinition.html
---

# GetWorkflowDefinition
<a name="API_GetWorkflowDefinition"></a>

Retrieves the details and configuration of a specific workflow definition.

## Request Syntax
<a name="API_GetWorkflowDefinition_RequestSyntax"></a>

```
GET /workflow-definitions/{{workflowDefinitionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflowDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowDefinitionName](#API_GetWorkflowDefinition_RequestSyntax) **   <a name="novaact-GetWorkflowDefinition-request-uri-workflowDefinitionName"></a>
The name of the workflow definition to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9_-]{1,40}`
Required: Yes

## Request Body
<a name="API_GetWorkflowDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflowDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "description": "string",
   "exportConfig": {
      "s3BucketName": "string",
      "s3KeyPrefix": "string"
   },
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetWorkflowDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetWorkflowDefinition_ResponseSyntax) **   <a name="novaact-GetWorkflowDefinition-response-arn"></a>
The Amazon Resource Name (ARN) of the workflow definition.
Type: String
Pattern: `arn:(aws|aws-cn|aws-us-gov):nova-act:[a-z0-9-]+:[0-9]{12}:workflow-definition/[a-zA-Z0-9_-]{1,40}`

 ** [createdAt](#API_GetWorkflowDefinition_ResponseSyntax) **   <a name="novaact-GetWorkflowDefinition-response-createdAt"></a>
The timestamp when the workflow definition was created.
Type: Timestamp

 ** [description](#API_GetWorkflowDefinition_ResponseSyntax) **   <a name="novaact-GetWorkflowDefinition-response-description"></a>
The description of the workflow definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.

 ** [exportConfig](#API_GetWorkflowDefinition_ResponseSyntax) **   <a name="novaact-GetWorkflowDefinition-response-exportConfig"></a>
The export configuration for the workflow definition.
Type: [WorkflowExportConfig](API_WorkflowExportConfig.md) object

 ** [name](#API_GetWorkflowDefinition_ResponseSyntax) **   <a name="novaact-GetWorkflowDefinition-response-name"></a>
The name of the workflow definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9_-]{1,40}`

 ** [status](#API_GetWorkflowDefinition_ResponseSyntax) **   <a name="novaact-GetWorkflowDefinition-response-status"></a>
The current status of the workflow definition.
Type: String
Valid Values: `ACTIVE | DELETING`

## Errors
<a name="API_GetWorkflowDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient permissions to perform this action.
 ** message **
You don't have sufficient permissions to perform this action. Verify your IAM permissions and try again.
HTTP Status Code: 403

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
<a name="API_GetWorkflowDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/nova-act-2025-08-22/GetWorkflowDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/nova-act-2025-08-22/GetWorkflowDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/GetWorkflowDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/nova-act-2025-08-22/GetWorkflowDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/GetWorkflowDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/nova-act-2025-08-22/GetWorkflowDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/nova-act-2025-08-22/GetWorkflowDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/nova-act-2025-08-22/GetWorkflowDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/nova-act-2025-08-22/GetWorkflowDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/GetWorkflowDefinition)
