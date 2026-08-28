---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRegistrationAttachment.html
---

# CreateRegistrationAttachment
<a name="API_CreateRegistrationAttachment"></a>

Create a new registration attachment to use for uploading a file or a URL to a file. The maximum file size is 500KB and valid file extensions are PDF, JPEG and PNG. For example, many sender ID registrations require a signed “letter of authorization” (LOA) to be submitted.

Use either `AttachmentUrl` or `AttachmentBody` to upload your attachment. If both are specified then an exception is returned.

## Request Syntax
<a name="API_CreateRegistrationAttachment_RequestSyntax"></a>

```
{
   "AttachmentBody": {{blob}},
   "AttachmentUrl": "{{string}}",
   "ClientToken": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateRegistrationAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttachmentBody](#API_CreateRegistrationAttachment_RequestSyntax) **   <a name="pinpoint-CreateRegistrationAttachment-request-AttachmentBody"></a>
The registration file to upload. The maximum file size is 500KB and valid file extensions are PDF, JPEG and PNG.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 6990508.
Required: No

 ** [AttachmentUrl](#API_CreateRegistrationAttachment_RequestSyntax) **   <a name="pinpoint-CreateRegistrationAttachment-request-AttachmentUrl"></a>
Registration files have to be stored in an Amazon S3 bucket. The URI to use when sending is in the format `s3://BucketName/FileName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S+`
Required: No

 ** [ClientToken](#API_CreateRegistrationAttachment_RequestSyntax) **   <a name="pinpoint-CreateRegistrationAttachment-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [Tags](#API_CreateRegistrationAttachment_RequestSyntax) **   <a name="pinpoint-CreateRegistrationAttachment-request-Tags"></a>
An array of tags (key and value pairs) to associate with the registration attachment.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateRegistrationAttachment_ResponseSyntax"></a>

```
{
   "AttachmentStatus": "string",
   "CreatedTimestamp": number,
   "RegistrationAttachmentArn": "string",
   "RegistrationAttachmentId": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateRegistrationAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentStatus](#API_CreateRegistrationAttachment_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAttachment-response-AttachmentStatus"></a>
The status of the registration attachment.
+  `UPLOAD_IN_PROGRESS` The attachment is being uploaded.
+  `UPLOAD_COMPLETE` The attachment has been uploaded.
+  `UPLOAD_FAILED` The attachment failed to uploaded.
+  `DELETED` The attachment has been deleted..
Type: String
Valid Values: `UPLOAD_IN_PROGRESS | UPLOAD_COMPLETE | UPLOAD_FAILED | DELETED`

 ** [CreatedTimestamp](#API_CreateRegistrationAttachment_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAttachment-response-CreatedTimestamp"></a>
The time when the registration attachment was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [RegistrationAttachmentArn](#API_CreateRegistrationAttachment_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAttachment-response-RegistrationAttachmentArn"></a>
The Amazon Resource Name (ARN) for the registration attachment.
Type: String

 ** [RegistrationAttachmentId](#API_CreateRegistrationAttachment_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAttachment-response-RegistrationAttachmentId"></a>
The unique identifier for the registration attachment.
Type: String

 ** [Tags](#API_CreateRegistrationAttachment_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationAttachment-response-Tags"></a>
An array of tags (key and value pairs) to associate with the registration attachment.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_CreateRegistrationAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.
 ** Reason **
The reason for the exception.
 ** ResourceId **
The unique identifier of the request.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateRegistrationAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
