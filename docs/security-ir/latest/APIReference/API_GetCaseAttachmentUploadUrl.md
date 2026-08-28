---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetCaseAttachmentUploadUrl.html
---

# GetCaseAttachmentUploadUrl
<a name="API_GetCaseAttachmentUploadUrl"></a>

Uploads an attachment to a case.

## Request Syntax
<a name="API_GetCaseAttachmentUploadUrl_RequestSyntax"></a>

```
POST /v1/cases/{{caseId}}/get-presigned-url HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "contentLength": {{number}},
   "fileName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetCaseAttachmentUploadUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_GetCaseAttachmentUploadUrl_RequestSyntax) **   <a name="securityir-GetCaseAttachmentUploadUrl-request-uri-caseId"></a>
Required element for GetCaseAttachmentUploadUrl to identify the case ID for uploading an attachment.
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

## Request Body
<a name="API_GetCaseAttachmentUploadUrl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_GetCaseAttachmentUploadUrl_RequestSyntax) **   <a name="securityir-GetCaseAttachmentUploadUrl-request-clientToken"></a>
The `clientToken` field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [contentLength](#API_GetCaseAttachmentUploadUrl_RequestSyntax) **   <a name="securityir-GetCaseAttachmentUploadUrl-request-contentLength"></a>
Required element for GetCaseAttachmentUploadUrl to identify the size of the file attachment.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 104857600.
Required: Yes

 ** [fileName](#API_GetCaseAttachmentUploadUrl_RequestSyntax) **   <a name="securityir-GetCaseAttachmentUploadUrl-request-fileName"></a>
Required element for GetCaseAttachmentUploadUrl to identify the file name of the attachment to upload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9._-]+`
Required: Yes

## Response Syntax
<a name="API_GetCaseAttachmentUploadUrl_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "attachmentPresignedUrl": "string"
}
```

## Response Elements
<a name="API_GetCaseAttachmentUploadUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [attachmentPresignedUrl](#API_GetCaseAttachmentUploadUrl_ResponseSyntax) **   <a name="securityir-GetCaseAttachmentUploadUrl-response-attachmentPresignedUrl"></a>
Response element providing the Amazon S3 presigned URL to upload the attachment.
Type: String
Pattern: `https?://(?:www.)?[a-zA-Z0-9@:._+~#=-]{2,256}\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_+.~#?&/=]{0,2048})`

## Errors
<a name="API_GetCaseAttachmentUploadUrl_Errors"></a>

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
<a name="API_GetCaseAttachmentUploadUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/GetCaseAttachmentUploadUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/GetCaseAttachmentUploadUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/GetCaseAttachmentUploadUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/GetCaseAttachmentUploadUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/GetCaseAttachmentUploadUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/GetCaseAttachmentUploadUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/GetCaseAttachmentUploadUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/GetCaseAttachmentUploadUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/GetCaseAttachmentUploadUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/GetCaseAttachmentUploadUrl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
