---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_GetAttachment.html
---

# GetAttachment
<a name="API_connect-participant_GetAttachment"></a>

Provides a pre-signed URL for download of a completed attachment. This is an asynchronous API for use with active contacts.

For security recommendations, see [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat).

**Note**
The participant role `CUSTOM_BOT` is not permitted to access attachments customers may upload. An `AccessDeniedException` can indicate that the participant may be a CUSTOM\_BOT, and it doesn't have access to attachments.
 `ConnectionToken` is used for invoking this API instead of `ParticipantToken`.

The Amazon Connect Participant Service APIs do not use [Signature Version 4 authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Request Syntax
<a name="API_connect-participant_GetAttachment_RequestSyntax"></a>

```
POST /participant/attachment HTTP/1.1
X-Amz-Bearer: {{ConnectionToken}}
Content-type: application/json

{
   "AttachmentId": "{{string}}",
   "UrlExpiryInSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_connect-participant_GetAttachment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionToken](#API_connect-participant_GetAttachment_RequestSyntax) **   <a name="connect-connect-participant_GetAttachment-request-ConnectionToken"></a>
The authentication token associated with the participant's connection.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_connect-participant_GetAttachment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AttachmentId](#API_connect-participant_GetAttachment_RequestSyntax) **   <a name="connect-connect-participant_GetAttachment-request-AttachmentId"></a>
A unique identifier for the attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [UrlExpiryInSeconds](#API_connect-participant_GetAttachment_RequestSyntax) **   <a name="connect-connect-participant_GetAttachment-request-UrlExpiryInSeconds"></a>
The expiration time of the URL in ISO timestamp. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 300.
Required: No

## Response Syntax
<a name="API_connect-participant_GetAttachment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttachmentSizeInBytes": number,
   "Url": "string",
   "UrlExpiry": "string"
}
```

## Response Elements
<a name="API_connect-participant_GetAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentSizeInBytes](#API_connect-participant_GetAttachment_ResponseSyntax) **   <a name="connect-connect-participant_GetAttachment-response-AttachmentSizeInBytes"></a>
The size of the attachment in bytes.
Type: Long
Valid Range: Minimum value of 1.

 ** [Url](#API_connect-participant_GetAttachment_ResponseSyntax) **   <a name="connect-connect-participant_GetAttachment-response-Url"></a>
This is the pre-signed URL that can be used for uploading the file to Amazon S3 when used in response to [StartAttachmentUpload](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_StartAttachmentUpload.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [UrlExpiry](#API_connect-participant_GetAttachment_ResponseSyntax) **   <a name="connect-connect-participant_GetAttachment-response-UrlExpiry"></a>
The expiration time of the URL in ISO timestamp. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.
Type: String

## Errors
<a name="API_connect-participant_GetAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the Amazon Connect service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by Amazon Connect.
HTTP Status Code: 400

## See Also
<a name="API_connect-participant_GetAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectparticipant-2018-09-07/GetAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectparticipant-2018-09-07/GetAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/GetAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectparticipant-2018-09-07/GetAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/GetAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectparticipant-2018-09-07/GetAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectparticipant-2018-09-07/GetAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectparticipant-2018-09-07/GetAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectparticipant-2018-09-07/GetAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/GetAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
