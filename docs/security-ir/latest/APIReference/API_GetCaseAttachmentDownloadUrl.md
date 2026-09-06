---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetCaseAttachmentDownloadUrl.html
---

# GetCaseAttachmentDownloadUrl
<a name="API_GetCaseAttachmentDownloadUrl"></a>

Returns a Pre-Signed URL for uploading attachments into a case.

## Request Syntax
<a name="API_GetCaseAttachmentDownloadUrl_RequestSyntax"></a>

```
GET /v1/cases/{{caseId}}/get-presigned-url/{{attachmentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCaseAttachmentDownloadUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [attachmentId](#API_GetCaseAttachmentDownloadUrl_RequestSyntax) **   <a name="securityir-GetCaseAttachmentDownloadUrl-request-uri-attachmentId"></a>
Required element for GetCaseAttachmentDownloadUrl to identify the attachment ID for downloading an attachment.
Pattern: `[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}`
Required: Yes

 ** [caseId](#API_GetCaseAttachmentDownloadUrl_RequestSyntax) **   <a name="securityir-GetCaseAttachmentDownloadUrl-request-uri-caseId"></a>
Required element for GetCaseAttachmentDownloadUrl to identify the case ID for downloading an attachment from.
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

## Request Body
<a name="API_GetCaseAttachmentDownloadUrl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCaseAttachmentDownloadUrl_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "attachmentPresignedUrl": "string"
}
```

## Response Elements
<a name="API_GetCaseAttachmentDownloadUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [attachmentPresignedUrl](#API_GetCaseAttachmentDownloadUrl_ResponseSyntax) **   <a name="securityir-GetCaseAttachmentDownloadUrl-response-attachmentPresignedUrl"></a>
Response element providing the Amazon S3 presigned URL to download an attachment.
Type: String
Pattern: `https?://(?:www.)?[a-zA-Z0-9@:._+~#=-]{2,256}\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_+.~#?&/=]{0,2048})`

## Errors
<a name="API_GetCaseAttachmentDownloadUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** message **
The ID of the resource which lead to the access denial.
HTTP Status Code: 403

 ** ConflictException **
Returned when there is a conflict with the current state of the resource.
For UpdateResolverType, this error may occur when attempting to change an AWS-supported case to Self-managed, which is not supported.
 ** message **
The exception message.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **

 ** message **
The exception message.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
HTTP Status Code: 500

 ** InvalidTokenException **

 ** message **
The exception message.
HTTP Status Code: 423

 ** ResourceNotFoundException **

 ** message **
The exception message.
HTTP Status Code: 404

 ** SecurityIncidentResponseNotActiveException **

 ** message **
The exception message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

 ** message **
The exception message.
 ** quotaCode **
The code of the quota.
 ** resourceId **
The ID of the requested resource which lead to the service quota exception.
 ** resourceType **
The type of the requested resource which lead to the service quota exception.
 ** serviceCode **
The service code of the quota.
HTTP Status Code: 402

 ** ThrottlingException **

 ** message **
The exception message.
 ** quotaCode **
The quota code of the exception.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
 ** serviceCode **
The service code of the exception.
HTTP Status Code: 429

 ** ValidationException **
Returned when the request contains invalid parameters.
For UpdateResolverType, this error may occur when attempting an unsupported resolver type transition.
 ** fieldList **
The fields which lead to the exception.
 ** message **
The exception message.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetCaseAttachmentDownloadUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/GetCaseAttachmentDownloadUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/GetCaseAttachmentDownloadUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/GetCaseAttachmentDownloadUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/GetCaseAttachmentDownloadUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/GetCaseAttachmentDownloadUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/GetCaseAttachmentDownloadUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/GetCaseAttachmentDownloadUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/GetCaseAttachmentDownloadUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/GetCaseAttachmentDownloadUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/GetCaseAttachmentDownloadUrl)
