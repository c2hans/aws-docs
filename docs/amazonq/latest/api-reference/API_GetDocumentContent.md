---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetDocumentContent.html
---

# GetDocumentContent
<a name="API_GetDocumentContent"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Retrieves the content of a document that was ingested into Amazon Q Business. This API validates user authorization against document ACLs before returning a pre-signed URL for secure document access. You can download or view source documents referenced in chat responses through the URL.

## Request Syntax
<a name="API_GetDocumentContent_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/index/{{indexId}}/documents/{{documentId}}/content?dataSourceId={{dataSourceId}}&outputFormat={{outputFormat}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDocumentContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetDocumentContent_RequestSyntax) **   <a name="qbusiness-GetDocumentContent-request-uri-applicationId"></a>
The unique identifier of the Amazon Q Business application containing the document. This ensures the request is scoped to the correct application environment and its associated security policies.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [dataSourceId](#API_GetDocumentContent_RequestSyntax) **   <a name="qbusiness-GetDocumentContent-request-uri-dataSourceId"></a>
The identifier of the data source from which the document was ingested. This field is not present if the document is ingested by directly calling the BatchPutDocument API. If the document is from a file-upload data source, the datasource will be "uploaded-docs-file-stat-datasourceid".
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [documentId](#API_GetDocumentContent_RequestSyntax) **   <a name="qbusiness-GetDocumentContent-request-uri-documentId"></a>
The unique identifier of the document that is indexed via BatchPutDocument API or file-upload or connector sync. It is also found in chat or chatSync response.
Length Constraints: Minimum length of 1. Maximum length of 1825.
Pattern: `\P{C}*`
Required: Yes

 ** [indexId](#API_GetDocumentContent_RequestSyntax) **   <a name="qbusiness-GetDocumentContent-request-uri-indexId"></a>
The identifier of the index where documents are indexed.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [outputFormat](#API_GetDocumentContent_RequestSyntax) **   <a name="qbusiness-GetDocumentContent-request-uri-outputFormat"></a>
Document outputFormat. Defaults to RAW if not selected.
Valid Values: `RAW | EXTRACTED`

## Request Body
<a name="API_GetDocumentContent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDocumentContent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "mimeType": "string",
   "presignedUrl": "string"
}
```

## Response Elements
<a name="API_GetDocumentContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [mimeType](#API_GetDocumentContent_ResponseSyntax) **   <a name="qbusiness-GetDocumentContent-response-mimeType"></a>
The MIME type of the document content. When outputFormat is RAW, this corresponds to the original document's MIME type (e.g., application/pdf, text/plain, application/vnd.openxmlformats-officedocument.wordprocessingml.document). When outputFormat is EXTRACTED, the MIME type is always application/json.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [presignedUrl](#API_GetDocumentContent_ResponseSyntax) **   <a name="qbusiness-GetDocumentContent-response-presignedUrl"></a>
A pre-signed URL that provides temporary access to download the document content directly from Amazon Q Business. The URL expires after 5 minutes for security purposes. This URL is generated only after successful ACL validation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_GetDocumentContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_GetDocumentContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/GetDocumentContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/GetDocumentContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GetDocumentContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/GetDocumentContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GetDocumentContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/GetDocumentContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/GetDocumentContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/GetDocumentContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/GetDocumentContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GetDocumentContent)
