---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteRegistrationAttachment.html
---

# DeleteRegistrationAttachment
<a name="API_DeleteRegistrationAttachment"></a>

Permanently delete the specified registration attachment.

## Request Syntax
<a name="API_DeleteRegistrationAttachment_RequestSyntax"></a>

```
{
   "RegistrationAttachmentId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRegistrationAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RegistrationAttachmentId](#API_DeleteRegistrationAttachment_RequestSyntax) **   <a name="pinpoint-DeleteRegistrationAttachment-request-RegistrationAttachmentId"></a>
The unique identifier for the registration attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteRegistrationAttachment_ResponseSyntax"></a>

```
{
   "AttachmentStatus": "string",
   "AttachmentUploadErrorReason": "string",
   "CreatedTimestamp": number,
   "RegistrationAttachmentArn": "string",
   "RegistrationAttachmentId": "string"
}
```

## Response Elements
<a name="API_DeleteRegistrationAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentStatus](#API_DeleteRegistrationAttachment_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationAttachment-response-AttachmentStatus"></a>
The status of the registration attachment.
+  `UPLOAD_IN_PROGRESS` The attachment is being uploaded.
+  `UPLOAD_COMPLETE` The attachment has been uploaded.
+  `UPLOAD_FAILED` The attachment failed to uploaded.
+  `DELETED` The attachment has been deleted..
Type: String
Valid Values: `UPLOAD_IN_PROGRESS | UPLOAD_COMPLETE | UPLOAD_FAILED | DELETED`

 ** [AttachmentUploadErrorReason](#API_DeleteRegistrationAttachment_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationAttachment-response-AttachmentUploadErrorReason"></a>
The error message if the upload failed.
Type: String
Valid Values: `INTERNAL_ERROR`

 ** [CreatedTimestamp](#API_DeleteRegistrationAttachment_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationAttachment-response-CreatedTimestamp"></a>
The time when the registration attachment was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [RegistrationAttachmentArn](#API_DeleteRegistrationAttachment_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationAttachment-response-RegistrationAttachmentArn"></a>
The Amazon Resource Name (ARN) for the registration attachment.
Type: String

 ** [RegistrationAttachmentId](#API_DeleteRegistrationAttachment_ResponseSyntax) **   <a name="pinpoint-DeleteRegistrationAttachment-response-RegistrationAttachmentId"></a>
The unique identifier for the registration attachment.
Type: String

## Errors
<a name="API_DeleteRegistrationAttachment_Errors"></a>

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

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
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
<a name="API_DeleteRegistrationAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistrationAttachment)
