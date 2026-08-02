---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartAttachedFileUpload.html
---

# StartAttachedFileUpload
<a name="API_StartAttachedFileUpload"></a>

Provides a pre-signed Amazon S3 URL in response for uploading your content.

**Important**
You may only use this API to upload attachments to an [Connect Customer Case](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateCase.html) or [Connect Customer Email](https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html).

## Request Syntax
<a name="API_StartAttachedFileUpload_RequestSyntax"></a>

```
PUT /attached-files/{{InstanceId}}?associatedResourceArn={{AssociatedResourceArn}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "CreatedBy": { ... },
   "FileName": "{{string}}",
   "FileSizeInBytes": {{number}},
   "FileUseCaseType": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "UrlExpiryInSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_StartAttachedFileUpload_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociatedResourceArn](#API_StartAttachedFileUpload_RequestSyntax) **   <a name="connect-StartAttachedFileUpload-request-uri-AssociatedResourceArn"></a>
The resource to which the attached file is (being) uploaded to. The supported resources are [Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html) and [Email](https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html).
This value must be a valid ARN.
Required: Yes

 ** [InstanceId](#API_StartAttachedFileUpload_RequestSyntax) **   <a name="connect-StartAttachedFileUpload-request-uri-InstanceId"></a>
The unique identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_StartAttachedFileUpload_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_StartAttachedFileUpload_RequestSyntax) **   <a name="connect-StartAttachedFileUpload-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [CreatedBy](#API_StartAttachedFileUpload_RequestSyntax) **   <a name="connect-StartAttachedFileUpload-request-CreatedBy"></a>
Represents the identity that created the file.
Type: [CreatedByInfo](API_CreatedByInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [FileName](#API_StartAttachedFileUpload_RequestSyntax) **   <a name="connect-StartAttachedFileUpload-request-FileName"></a>
A case-sensitive name of the attached file being uploaded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^\P{C}*$`
Required: Yes

 ** [FileSizeInBytes](#API_StartAttachedFileUpload_RequestSyntax) **   <a name="connect-StartAttachedFileUpload-request-FileSizeInBytes"></a>
The size of the attached file in bytes.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** [FileUseCaseType](#API_StartAttachedFileUpload_RequestSyntax) **   <a name="connect-StartAttachedFileUpload-request-FileUseCaseType"></a>
The use case for the file.
 Only `ATTACHMENTS` are supported.
Type: String
Valid Values: `CONTACT_ANALYSIS | EMAIL_MESSAGE | EMAIL_MESSAGE_PLAIN_TEXT | EMAIL_MESSAGE_REDACTED | EMAIL_MESSAGE_PLAIN_TEXT_REDACTED | ATTACHMENT | VOICE_RECORDING`
Required: Yes

 ** [Tags](#API_StartAttachedFileUpload_RequestSyntax) **   <a name="connect-StartAttachedFileUpload-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "Tags": {"key1":"value1", "key2":"value2"} }`.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [UrlExpiryInSeconds](#API_StartAttachedFileUpload_RequestSyntax) **   <a name="connect-StartAttachedFileUpload-request-UrlExpiryInSeconds"></a>
Optional override for the expiry of the pre-signed S3 URL in seconds. The default value is 300.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 300.
Required: No

## Response Syntax
<a name="API_StartAttachedFileUpload_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedBy": { ... },
   "CreationTime": "string",
   "FileArn": "string",
   "FileId": "string",
   "FileStatus": "string",
   "UploadUrlMetadata": {
      "HeadersToInclude": {
         "string" : "string"
      },
      "Url": "string",
      "UrlExpiry": "string"
   }
}
```

## Response Elements
<a name="API_StartAttachedFileUpload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedBy](#API_StartAttachedFileUpload_ResponseSyntax) **   <a name="connect-StartAttachedFileUpload-response-CreatedBy"></a>
Represents the identity that created the file.
Type: [CreatedByInfo](API_CreatedByInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [CreationTime](#API_StartAttachedFileUpload_ResponseSyntax) **   <a name="connect-StartAttachedFileUpload-response-CreationTime"></a>
The time of Creation of the file resource as an ISO timestamp. It's specified in ISO 8601 format: `yyyy-MM-ddThh:mm:ss.SSSZ`. For example, `2024-05-03T02:41:28.172Z`.
Type: String

 ** [FileArn](#API_StartAttachedFileUpload_ResponseSyntax) **   <a name="connect-StartAttachedFileUpload-response-FileArn"></a>
The unique identifier of the attached file resource (ARN).
Type: String

 ** [FileId](#API_StartAttachedFileUpload_ResponseSyntax) **   <a name="connect-StartAttachedFileUpload-response-FileId"></a>
The unique identifier of the attached file resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [FileStatus](#API_StartAttachedFileUpload_ResponseSyntax) **   <a name="connect-StartAttachedFileUpload-response-FileStatus"></a>
The current status of the attached file.
Type: String
Valid Values: `APPROVED | REJECTED | PROCESSING | FAILED`

 ** [UploadUrlMetadata](#API_StartAttachedFileUpload_ResponseSyntax) **   <a name="connect-StartAttachedFileUpload-response-UploadUrlMetadata"></a>
The headers to be provided while uploading the file to the URL.
Type: [UploadUrlMetadata](API_UploadUrlMetadata.md) object

## Errors
<a name="API_StartAttachedFileUpload_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_StartAttachedFileUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartAttachedFileUpload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartAttachedFileUpload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartAttachedFileUpload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartAttachedFileUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartAttachedFileUpload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartAttachedFileUpload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartAttachedFileUpload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartAttachedFileUpload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartAttachedFileUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartAttachedFileUpload)
