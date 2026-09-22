---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateNotebook.html
---

# CreateNotebook
<a name="API_CreateNotebook"></a>

Creates a [notebook](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html) in Amazon SageMaker Unified Studio. A notebook is a collaborative document within a project that contains code cells for interactive computing.

## Request Syntax
<a name="API_CreateNotebook_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/notebooks HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "name": "{{string}}",
   "owningProjectIdentifier": "{{string}}",
   "parameters": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateNotebook_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateNotebook_RequestSyntax) **   <a name="datazone-CreateNotebook-request-uri-domainIdentifier"></a>
The identifier of the Amazon SageMaker Unified Studio domain in which to create the notebook.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateNotebook_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateNotebook_RequestSyntax) **   <a name="datazone-CreateNotebook-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_CreateNotebook_RequestSyntax) **   <a name="datazone-CreateNotebook-request-description"></a>
The description of the notebook.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [metadata](#API_CreateNotebook_RequestSyntax) **   <a name="datazone-CreateNotebook-request-metadata"></a>
The metadata for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [name](#API_CreateNotebook_RequestSyntax) **   <a name="datazone-CreateNotebook-request-name"></a>
The name of the notebook. The name must be between 1 and 256 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [owningProjectIdentifier](#API_CreateNotebook_RequestSyntax) **   <a name="datazone-CreateNotebook-request-owningProjectIdentifier"></a>
The identifier of the project that owns the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [parameters](#API_CreateNotebook_RequestSyntax) **   <a name="datazone-CreateNotebook-request-parameters"></a>
The sensitive parameters for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [type](#API_CreateNotebook_RequestSyntax) **   <a name="datazone-CreateNotebook-request-type"></a>
The type of the notebook.
Type: String
Valid Values: `DATA | SQL | QUERYBOOK`
Required: No

## Response Syntax
<a name="API_CreateNotebook_ResponseSyntax"></a>

```
HTTP/1.1 201
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
   "gitMetadata": {
      "branch": "string",
      "commitHash": "string",
      "commitMessage": "string",
      "committedAt": number,
      "connectionId": "string",
      "fileName": "string",
      "repository": "string"
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
   "type": "string",
   "updatedAt": number,
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_CreateNotebook_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [cellOrder](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-cellOrder"></a>
The ordered list of cells in the notebook.
Type: Array of [CellInformation](API_CellInformation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [computeId](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-computeId"></a>
The identifier of the compute associated with the notebook.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.

 ** [createdAt](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-createdAt"></a>
The timestamp of when the notebook was created.
Type: Timestamp

 ** [createdBy](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-createdBy"></a>
The identifier of the user who created the notebook.
Type: String

 ** [description](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-description"></a>
The description of the notebook.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-domainId"></a>
The identifier of the Amazon SageMaker Unified Studio domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [environmentConfiguration](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-environmentConfiguration"></a>
The environment configuration of the notebook.
Type: [EnvironmentConfig](API_EnvironmentConfig.md) object

 ** [error](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-error"></a>
The error details if the notebook creation failed.
Type: [NotebookError](API_NotebookError.md) object

 ** [gitMetadata](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-gitMetadata"></a>
The Git metadata associated with the notebook.
Type: [GitMetadata](API_GitMetadata.md) object

 ** [id](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-id"></a>
The identifier of the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [lockedAt](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-lockedAt"></a>
The timestamp of when the notebook was locked.
Type: Timestamp

 ** [lockedBy](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-lockedBy"></a>
The identifier of the user who locked the notebook.
Type: String

 ** [lockExpiresAt](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-lockExpiresAt"></a>
The timestamp of when the notebook lock expires.
Type: Timestamp

 ** [metadata](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-metadata"></a>
The metadata of the notebook.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [name](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-name"></a>
The name of the notebook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [owningProjectId](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-owningProjectId"></a>
The identifier of the project that owns the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [parameters](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-parameters"></a>
The sensitive parameters of the notebook.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [status](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-status"></a>
The status of the notebook.
Type: String
Valid Values: `ACTIVE | ARCHIVED | SYNC_IN_PROGRESS | SYNC_FAILED`

 ** [type](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-type"></a>
The type of the notebook.
Type: String
Valid Values: `DATA | SQL | QUERYBOOK`

 ** [updatedAt](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-updatedAt"></a>
The timestamp of when the notebook was last updated.
Type: Timestamp

 ** [updatedBy](#API_CreateNotebook_ResponseSyntax) **   <a name="datazone-CreateNotebook-response-updatedBy"></a>
The identifier of the user who last updated the notebook.
Type: String

## Errors
<a name="API_CreateNotebook_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_CreateNotebook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateNotebook)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateNotebook)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateNotebook)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateNotebook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateNotebook)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateNotebook)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateNotebook)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateNotebook)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateNotebook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateNotebook)
