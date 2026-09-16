---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetNotebookExport.html
---

# GetNotebookExport
<a name="API_GetNotebookExport"></a>

Gets the details of a notebook export in Amazon SageMaker Unified Studio.

## Request Syntax
<a name="API_GetNotebookExport_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/notebook-exports/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNotebookExport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetNotebookExport_RequestSyntax) **   <a name="datazone-GetNotebookExport-request-uri-domainIdentifier"></a>
The identifier of the Amazon SageMaker Unified Studio domain in which the notebook export exists.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetNotebookExport_RequestSyntax) **   <a name="datazone-GetNotebookExport-request-uri-identifier"></a>
The identifier of the notebook export.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_GetNotebookExport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNotebookExport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "completedAt": number,
   "createdAt": number,
   "createdBy": "string",
   "domainId": "string",
   "error": {
      "message": "string"
   },
   "fileFormat": "string",
   "id": "string",
   "notebookId": "string",
   "outputLocation": { ... },
   "owningProjectId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetNotebookExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [completedAt](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-completedAt"></a>
The timestamp of when the notebook export completed.
Type: Timestamp

 ** [createdAt](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-createdAt"></a>
The timestamp of when the notebook export was started.
Type: Timestamp

 ** [createdBy](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-createdBy"></a>
The identifier of the user who started the notebook export.
Type: String

 ** [domainId](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-domainId"></a>
The identifier of the Amazon SageMaker Unified Studio domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [error](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-error"></a>
The error details if the notebook export failed.
Type: [NotebookExportError](API_NotebookExportError.md) object

 ** [fileFormat](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-fileFormat"></a>
The file format of the notebook export.
Type: String
Valid Values: `PDF | IPYNB`

 ** [id](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-id"></a>
The identifier of the notebook export.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [notebookId](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-notebookId"></a>
The identifier of the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [outputLocation](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-outputLocation"></a>
The output location of the exported notebook in Amazon Simple Storage Service.
Type: [OutputLocation](API_OutputLocation.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [owningProjectId](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-owningProjectId"></a>
The identifier of the project that owns the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [status](#API_GetNotebookExport_ResponseSyntax) **   <a name="datazone-GetNotebookExport-response-status"></a>
The status of the notebook export.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`

## Errors
<a name="API_GetNotebookExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetNotebookExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetNotebookExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetNotebookExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetNotebookExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetNotebookExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetNotebookExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetNotebookExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetNotebookExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetNotebookExport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetNotebookExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetNotebookExport)
