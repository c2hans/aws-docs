---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_StartNotebookExport.html
---

# StartNotebookExport
<a name="API_StartNotebookExport"></a>

Starts a notebook export in Amazon SageMaker Unified Studio. This operation exports a notebook to a specified file format and stores the output in Amazon Simple Storage Service.

## Request Syntax
<a name="API_StartNotebookExport_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/notebook-exports HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "fileFormat": "{{string}}",
   "notebookIdentifier": "{{string}}",
   "owningProjectIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartNotebookExport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_StartNotebookExport_RequestSyntax) **   <a name="datazone-StartNotebookExport-request-uri-domainIdentifier"></a>
The identifier of the Amazon SageMaker Unified Studio domain in which to export the notebook.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_StartNotebookExport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartNotebookExport_RequestSyntax) **   <a name="datazone-StartNotebookExport-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [fileFormat](#API_StartNotebookExport_RequestSyntax) **   <a name="datazone-StartNotebookExport-request-fileFormat"></a>
The file format for the notebook export. Valid values are `PDF` and `IPYNB`.
Type: String
Valid Values: `PDF | IPYNB`
Required: Yes

 ** [notebookIdentifier](#API_StartNotebookExport_RequestSyntax) **   <a name="datazone-StartNotebookExport-request-notebookIdentifier"></a>
The identifier of the notebook to export.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [owningProjectIdentifier](#API_StartNotebookExport_RequestSyntax) **   <a name="datazone-StartNotebookExport-request-owningProjectIdentifier"></a>
The identifier of the project that owns the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Response Syntax
<a name="API_StartNotebookExport_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": number,
   "createdBy": "string",
   "domainId": "string",
   "fileFormat": "string",
   "id": "string",
   "notebookId": "string",
   "owningProjectId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StartNotebookExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_StartNotebookExport_ResponseSyntax) **   <a name="datazone-StartNotebookExport-response-createdAt"></a>
The timestamp of when the notebook export was started.
Type: Timestamp

 ** [createdBy](#API_StartNotebookExport_ResponseSyntax) **   <a name="datazone-StartNotebookExport-response-createdBy"></a>
The identifier of the user who started the notebook export.
Type: String

 ** [domainId](#API_StartNotebookExport_ResponseSyntax) **   <a name="datazone-StartNotebookExport-response-domainId"></a>
The identifier of the Amazon SageMaker Unified Studio domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [fileFormat](#API_StartNotebookExport_ResponseSyntax) **   <a name="datazone-StartNotebookExport-response-fileFormat"></a>
The file format of the notebook export.
Type: String
Valid Values: `PDF | IPYNB`

 ** [id](#API_StartNotebookExport_ResponseSyntax) **   <a name="datazone-StartNotebookExport-response-id"></a>
The identifier of the notebook export.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [notebookId](#API_StartNotebookExport_ResponseSyntax) **   <a name="datazone-StartNotebookExport-response-notebookId"></a>
The identifier of the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [owningProjectId](#API_StartNotebookExport_ResponseSyntax) **   <a name="datazone-StartNotebookExport-response-owningProjectId"></a>
The identifier of the project that owns the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_StartNotebookExport_ResponseSyntax) **   <a name="datazone-StartNotebookExport-response-status"></a>
The status of the notebook export.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

## Errors
<a name="API_StartNotebookExport_Errors"></a>

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
<a name="API_StartNotebookExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/StartNotebookExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/StartNotebookExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/StartNotebookExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/StartNotebookExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/StartNotebookExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/StartNotebookExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/StartNotebookExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/StartNotebookExport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/StartNotebookExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/StartNotebookExport)
