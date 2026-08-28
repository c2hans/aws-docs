---
source_url: https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_StartAttachmentUpload.html
---

# StartAttachmentUpload
<a name="API_connect-participant_StartAttachmentUpload"></a>

Provides a pre-signed Amazon S3 URL in response for uploading the file directly to S3.

For security recommendations, see [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat).

**Note**
 `ConnectionToken` is used for invoking this API instead of `ParticipantToken`.

The Amazon Connect Participant Service APIs do not use [Signature Version 4 authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Request Syntax
<a name="API_connect-participant_StartAttachmentUpload_RequestSyntax"></a>

```
POST /participant/start-attachment-upload HTTP/1.1
X-Amz-Bearer: {{ConnectionToken}}
Content-type: application/json

{
   "AttachmentName": "{{string}}",
   "AttachmentSizeInBytes": {{number}},
   "ClientToken": "{{string}}",
   "ContentType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-participant_StartAttachmentUpload_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionToken](#API_connect-participant_StartAttachmentUpload_RequestSyntax) **   <a name="connect-connect-participant_StartAttachmentUpload-request-ConnectionToken"></a>
The authentication token associated with the participant's connection.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_connect-participant_StartAttachmentUpload_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AttachmentName](#API_connect-participant_StartAttachmentUpload_RequestSyntax) **   <a name="connect-connect-participant_StartAttachmentUpload-request-AttachmentName"></a>
A case-sensitive name of the attachment being uploaded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [AttachmentSizeInBytes](#API_connect-participant_StartAttachmentUpload_RequestSyntax) **   <a name="connect-connect-participant_StartAttachmentUpload-request-AttachmentSizeInBytes"></a>
The size of the attachment in bytes.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** [ClientToken](#API_connect-participant_StartAttachmentUpload_RequestSyntax) **   <a name="connect-connect-participant_StartAttachmentUpload-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [ContentType](#API_connect-participant_StartAttachmentUpload_RequestSyntax) **   <a name="connect-connect-participant_StartAttachmentUpload-request-ContentType"></a>
Describes the MIME file type of the attachment. For a list of supported file types, see [Feature specifications](https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html) in the *Amazon Connect Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_connect-participant_StartAttachmentUpload_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttachmentId": "string",
   "UploadMetadata": {
      "HeadersToInclude": {
         "string" : "string"
      },
      "Url": "string",
      "UrlExpiry": "string"
   }
}
```

## Response Elements
<a name="API_connect-participant_StartAttachmentUpload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentId](#API_connect-participant_StartAttachmentUpload_ResponseSyntax) **   <a name="connect-connect-participant_StartAttachmentUpload-response-AttachmentId"></a>
A unique identifier for the attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [UploadMetadata](#API_connect-participant_StartAttachmentUpload_ResponseSyntax) **   <a name="connect-connect-participant_StartAttachmentUpload-response-UploadMetadata"></a>
The headers to be provided while uploading the file to the URL.
Type: [UploadMetadata](API_connect-participant_UploadMetadata.md) object

## Errors
<a name="API_connect-participant_StartAttachmentUpload_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the Amazon Connect service.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The number of attachments per contact exceeds the quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by Amazon Connect.
HTTP Status Code: 400

## See Also
<a name="API_connect-participant_StartAttachmentUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectparticipant-2018-09-07/StartAttachmentUpload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectparticipant-2018-09-07/StartAttachmentUpload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/StartAttachmentUpload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectparticipant-2018-09-07/StartAttachmentUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/StartAttachmentUpload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectparticipant-2018-09-07/StartAttachmentUpload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectparticipant-2018-09-07/StartAttachmentUpload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectparticipant-2018-09-07/StartAttachmentUpload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectparticipant-2018-09-07/StartAttachmentUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/StartAttachmentUpload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
