---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetAttachedFile.html
---

# GetAttachedFile
<a name="API_GetAttachedFile"></a>

Provides a pre-signed URL for download of an approved attached file. This API also returns metadata about the attached file. It will only return a downloadURL if the status of the attached file is `APPROVED`.

## Request Syntax
<a name="API_GetAttachedFile_RequestSyntax"></a>

```
GET /attached-files/{{InstanceId}}/{{FileId}}?associatedResourceArn={{AssociatedResourceArn}}&urlExpiryInSeconds={{UrlExpiryInSeconds}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAttachedFile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociatedResourceArn](#API_GetAttachedFile_RequestSyntax) **   <a name="connect-GetAttachedFile-request-uri-AssociatedResourceArn"></a>
The resource to which the attached file is (being) uploaded to. The supported resources are [Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html), [Email](https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html), and [Task](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html).
This value must be a valid ARN.
Required: Yes

 ** [FileId](#API_GetAttachedFile_RequestSyntax) **   <a name="connect-GetAttachedFile-request-uri-FileId"></a>
The unique identifier of the attached file resource.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_GetAttachedFile_RequestSyntax) **   <a name="connect-GetAttachedFile-request-uri-InstanceId"></a>
The unique identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UrlExpiryInSeconds](#API_GetAttachedFile_RequestSyntax) **   <a name="connect-GetAttachedFile-request-uri-UrlExpiryInSeconds"></a>
Optional override for the expiry of the pre-signed S3 URL in seconds. The default value is 300.
Valid Range: Minimum value of 5. Maximum value of 300.

## Request Body
<a name="API_GetAttachedFile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAttachedFile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssociatedResourceArn": "string",
   "CreatedBy": { ... },
   "CreationTime": "string",
   "DownloadUrlMetadata": {
      "Url": "string",
      "UrlExpiry": "string"
   },
   "FileArn": "string",
   "FileId": "string",
   "FileName": "string",
   "FileSizeInBytes": number,
   "FileStatus": "string",
   "FileUseCaseType": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetAttachedFile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociatedResourceArn](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-AssociatedResourceArn"></a>
The resource to which the attached file is (being) uploaded to. The supported resources are [Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html), [Email](https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html), and [Task](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html).
Type: String

 ** [CreatedBy](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-CreatedBy"></a>
Represents the identity that created the file.
Type: [CreatedByInfo](API_CreatedByInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [CreationTime](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-CreationTime"></a>
The time of Creation of the file resource as an ISO timestamp. It's specified in ISO 8601 format: `yyyy-MM-ddThh:mm:ss.SSSZ`. For example, `2024-05-03T02:41:28.172Z`.
Type: String

 ** [DownloadUrlMetadata](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-DownloadUrlMetadata"></a>
URL and expiry to be used when downloading the attached file.
Type: [DownloadUrlMetadata](API_DownloadUrlMetadata.md) object

 ** [FileArn](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-FileArn"></a>
The unique identifier of the attached file resource (ARN).
Type: String

 ** [FileId](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-FileId"></a>
The unique identifier of the attached file resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [FileName](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-FileName"></a>
A case-sensitive name of the attached file being uploaded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^\P{C}*$`

 ** [FileSizeInBytes](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-FileSizeInBytes"></a>
The size of the attached file in bytes.
Type: Long
Valid Range: Minimum value of 1.

 ** [FileStatus](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-FileStatus"></a>
The current status of the attached file.
Type: String
Valid Values: `APPROVED | REJECTED | PROCESSING | FAILED`

 ** [FileUseCaseType](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-FileUseCaseType"></a>
The use case for the file.
Type: String
Valid Values: `CONTACT_ANALYSIS | EMAIL_MESSAGE | EMAIL_MESSAGE_PLAIN_TEXT | EMAIL_MESSAGE_REDACTED | EMAIL_MESSAGE_PLAIN_TEXT_REDACTED | ATTACHMENT | VOICE_RECORDING`

 ** [Tags](#API_GetAttachedFile_ResponseSyntax) **   <a name="connect-GetAttachedFile-response-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "Tags": {"key1":"value1", "key2":"value2"} }`.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_GetAttachedFile_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_GetAttachedFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetAttachedFile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetAttachedFile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetAttachedFile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetAttachedFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetAttachedFile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetAttachedFile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetAttachedFile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetAttachedFile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetAttachedFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetAttachedFile)
