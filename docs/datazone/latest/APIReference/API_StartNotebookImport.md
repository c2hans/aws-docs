---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_StartNotebookImport.html
---

# StartNotebookImport
<a name="API_StartNotebookImport"></a>

Starts a notebook import in Amazon SageMaker Unified Studio. This operation imports a notebook from an Amazon Simple Storage Service location into a project.

## Request Syntax
<a name="API_StartNotebookImport_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/notebook-imports HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "owningProjectIdentifier": "{{string}}",
   "sourceLocation": { ... }
}
```

## URI Request Parameters
<a name="API_StartNotebookImport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_StartNotebookImport_RequestSyntax) **   <a name="datazone-StartNotebookImport-request-uri-domainIdentifier"></a>
The identifier of the Amazon SageMaker Unified Studio domain in which to import the notebook.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_StartNotebookImport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartNotebookImport_RequestSyntax) **   <a name="datazone-StartNotebookImport-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [description](#API_StartNotebookImport_RequestSyntax) **   <a name="datazone-StartNotebookImport-request-description"></a>
The description of the imported notebook.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [name](#API_StartNotebookImport_RequestSyntax) **   <a name="datazone-StartNotebookImport-request-name"></a>
The name of the imported notebook. The name must be between 1 and 256 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [owningProjectIdentifier](#API_StartNotebookImport_RequestSyntax) **   <a name="datazone-StartNotebookImport-request-owningProjectIdentifier"></a>
The identifier of the project that will own the imported notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [sourceLocation](#API_StartNotebookImport_RequestSyntax) **   <a name="datazone-StartNotebookImport-request-sourceLocation"></a>
The source location of the notebook to import. This specifies the Amazon Simple Storage Service URI of the notebook file.
Type: [SourceLocation](API_SourceLocation.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_StartNotebookImport_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "description": "string",
   "domainId": "string",
   "name": "string",
   "notebookId": "string",
   "owningProjectId": "string",
   "sourceLocation": { ... },
   "status": "string"
}
```

## Response Elements
<a name="API_StartNotebookImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_StartNotebookImport_ResponseSyntax) **   <a name="datazone-StartNotebookImport-response-createdAt"></a>
The timestamp of when the notebook import was started.
Type: Timestamp

 ** [createdBy](#API_StartNotebookImport_ResponseSyntax) **   <a name="datazone-StartNotebookImport-response-createdBy"></a>
The identifier of the user who started the notebook import.
Type: String

 ** [description](#API_StartNotebookImport_ResponseSyntax) **   <a name="datazone-StartNotebookImport-response-description"></a>
The description of the imported notebook.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [domainId](#API_StartNotebookImport_ResponseSyntax) **   <a name="datazone-StartNotebookImport-response-domainId"></a>
The identifier of the Amazon SageMaker Unified Studio domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [name](#API_StartNotebookImport_ResponseSyntax) **   <a name="datazone-StartNotebookImport-response-name"></a>
The name of the imported notebook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [notebookId](#API_StartNotebookImport_ResponseSyntax) **   <a name="datazone-StartNotebookImport-response-notebookId"></a>
The identifier of the imported notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_StartNotebookImport_ResponseSyntax) **   <a name="datazone-StartNotebookImport-response-owningProjectId"></a>
The identifier of the project that owns the imported notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [sourceLocation](#API_StartNotebookImport_ResponseSyntax) **   <a name="datazone-StartNotebookImport-response-sourceLocation"></a>
The source location from which the notebook was imported.
Type: [SourceLocation](API_SourceLocation.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_StartNotebookImport_ResponseSyntax) **   <a name="datazone-StartNotebookImport-response-status"></a>
The status of the notebook import.
Type: String
Valid Values: `ACTIVE | ARCHIVED | SYNC_IN_PROGRESS | SYNC_FAILED`

## Errors
<a name="API_StartNotebookImport_Errors"></a>

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
<a name="API_StartNotebookImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/StartNotebookImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/StartNotebookImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/StartNotebookImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/StartNotebookImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/StartNotebookImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/StartNotebookImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/StartNotebookImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/StartNotebookImport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/StartNotebookImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/StartNotebookImport)
