---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UpdateNotebook.html
---

# UpdateNotebook
<a name="API_UpdateNotebook"></a>

Updates a [notebook](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html) in Amazon SageMaker Unified Studio.

## Request Syntax
<a name="API_UpdateNotebook_RequestSyntax"></a>

```
PATCH /v2/domains/{{domainIdentifier}}/notebooks/{{identifier}} HTTP/1.1
Content-type: application/json

{
   "cellOrder": [
      {
      }
   ],
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "environmentConfiguration": {
      "imageVersion": "{{string}}",
      "packageConfig": {
         "packageManager": "{{string}}",
         "packageSpecification": "{{string}}"
      }
   },
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "name": "{{string}}",
   "parameters": {
      "{{string}}" : "{{string}}"
   },
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateNotebook_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_UpdateNotebook_RequestSyntax) **   <a name="datazone-UpdateNotebook-request-uri-domainIdentifier"></a>
The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_UpdateNotebook_RequestSyntax) **   <a name="datazone-UpdateNotebook-request-uri-identifier"></a>
The identifier of the notebook to update.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_UpdateNotebook_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [cellOrder](#API_UpdateNotebook_RequestSyntax) **   <a name="datazone-UpdateNotebook-request-cellOrder"></a>
The updated ordered list of cells in the notebook.
Type: Array of [CellInformation](API_CellInformation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [clientToken](#API_UpdateNotebook_RequestSyntax) **   <a name="datazone-UpdateNotebook-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_UpdateNotebook_RequestSyntax) **   <a name="datazone-UpdateNotebook-request-description"></a>
The updated description of the notebook.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [environmentConfiguration](#API_UpdateNotebook_RequestSyntax) **   <a name="datazone-UpdateNotebook-request-environmentConfiguration"></a>
The updated environment configuration for the notebook.
Type: [EnvironmentConfig](API_EnvironmentConfig.md) object
Required: No

 ** [metadata](#API_UpdateNotebook_RequestSyntax) **   <a name="datazone-UpdateNotebook-request-metadata"></a>
The updated metadata for the notebook, specified as key-value pairs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [name](#API_UpdateNotebook_RequestSyntax) **   <a name="datazone-UpdateNotebook-request-name"></a>
The updated name of the notebook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [parameters](#API_UpdateNotebook_RequestSyntax) **   <a name="datazone-UpdateNotebook-request-parameters"></a>
The updated sensitive parameters for the notebook, specified as key-value pairs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [status](#API_UpdateNotebook_RequestSyntax) **   <a name="datazone-UpdateNotebook-request-status"></a>
The updated status of the notebook.
Type: String
Valid Values: `ACTIVE | ARCHIVED`
Required: No

## Response Syntax
<a name="API_UpdateNotebook_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cellOrder": [
      {
      }
   ],
   "computeId": "string",
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "environmentConfiguration": {
      "imageVersion": "string",
      "packageConfig": {
         "packageManager": "string",
         "packageSpecification": "string"
      }
   },
   "error": {
      "message": "string"
   },
   "id": "string",
   "lockedAt": number,
   "lockedBy": "string",
   "lockExpiresAt": number,
   "metadata": {
      "string" : "string"
   },
   "name": "string",
   "owningProjectId": "string",
   "parameters": {
      "string" : "string"
   },
   "status": "string",
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_UpdateNotebook_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cellOrder](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-cellOrder"></a>
The ordered list of cells in the notebook.
Type: Array of [CellInformation](API_CellInformation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [computeId](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-computeId"></a>
The identifier of the compute associated with the notebook.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.

 ** [createdAt](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-createdAt"></a>
The timestamp of when the notebook was created.
Type: Timestamp

 ** [createdBy](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-createdBy"></a>
The identifier of the user who created the notebook.
Type: String

 ** [description](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-description"></a>
The description of the notebook.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-domainId"></a>
The identifier of the Amazon SageMaker Unified Studio domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentConfiguration](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-environmentConfiguration"></a>
The environment configuration of the notebook.
Type: [EnvironmentConfig](API_EnvironmentConfig.md) object

 ** [error](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-error"></a>
The error details if the notebook is in a failed state.
Type: [NotebookError](API_NotebookError.md) object

 ** [id](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-id"></a>
The identifier of the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lockedAt](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-lockedAt"></a>
The timestamp of when the notebook was locked.
Type: Timestamp

 ** [lockedBy](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-lockedBy"></a>
The identifier of the user who locked the notebook.
Type: String

 ** [lockExpiresAt](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-lockExpiresAt"></a>
The timestamp of when the notebook lock expires.
Type: Timestamp

 ** [metadata](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-metadata"></a>
The metadata of the notebook.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [name](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-name"></a>
The name of the notebook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [owningProjectId](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-owningProjectId"></a>
The identifier of the project that owns the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [parameters](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-parameters"></a>
The sensitive parameters of the notebook.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [status](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-status"></a>
The status of the notebook.
Type: String
Valid Values: `ACTIVE | ARCHIVED`

 ** [updatedAt](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-updatedAt"></a>
The timestamp of when the notebook was last updated.
Type: Timestamp

 ** [updatedBy](#API_UpdateNotebook_ResponseSyntax) **   <a name="datazone-UpdateNotebook-response-updatedBy"></a>
The identifier of the user who last updated the notebook.
Type: String

## Errors
<a name="API_UpdateNotebook_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateNotebook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/UpdateNotebook)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/UpdateNotebook)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UpdateNotebook)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/UpdateNotebook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UpdateNotebook)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/UpdateNotebook)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/UpdateNotebook)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/UpdateNotebook)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/UpdateNotebook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UpdateNotebook)
