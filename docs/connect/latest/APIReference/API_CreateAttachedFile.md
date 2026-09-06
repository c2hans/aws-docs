---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateAttachedFile.html
---

# CreateAttachedFile
<a name="API_CreateAttachedFile"></a>

Creates an attached file for a completed voice contact by copying a recording from a source S3 URI into Connect Customer managed storage. Use this API to attach voice recordings to contacts for downstream processing such as conversational analytics.

**Important**
The `AssociatedResourceArn` must be the ARN of a completed voice contact, `FileUseCaseType` must be set to `VOICE_RECORDING`, and `FileSourceUri` must be a valid S3 URI.

**Note**
For example, you can call `CreateContact`, then `CreateAttachedFile`, then `StartContactConversationalAnalyticsJob` to create a contact, attach a recording, and run post-call analytics.

## Request Syntax
<a name="API_CreateAttachedFile_RequestSyntax"></a>

```
PUT /attached-files/{{InstanceId}}/files?associatedResourceArn={{AssociatedResourceArn}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "FileSourceUri": "{{string}}",
   "FileUseCaseType": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAttachedFile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociatedResourceArn](#API_CreateAttachedFile_RequestSyntax) **   <a name="connect-CreateAttachedFile-request-uri-AssociatedResourceArn"></a>
The ARN of the completed voice contact to attach the file to. Only voice contacts with Telephony subtype are supported.
This value must be a valid ARN.
Required: Yes

 ** [InstanceId](#API_CreateAttachedFile_RequestSyntax) **   <a name="connect-CreateAttachedFile-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateAttachedFile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateAttachedFile_RequestSyntax) **   <a name="connect-CreateAttachedFile-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [FileSourceUri](#API_CreateAttachedFile_RequestSyntax) **   <a name="connect-CreateAttachedFile-request-FileSourceUri"></a>
The S3 URI of the file to be attached. Only S3 source URIs are supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

 ** [FileUseCaseType](#API_CreateAttachedFile_RequestSyntax) **   <a name="connect-CreateAttachedFile-request-FileUseCaseType"></a>
The use case for the file.
Only `VOICE_RECORDING` is supported.
Type: String
Valid Values: `CONTACT_ANALYSIS | EMAIL_MESSAGE | EMAIL_MESSAGE_PLAIN_TEXT | EMAIL_MESSAGE_REDACTED | EMAIL_MESSAGE_PLAIN_TEXT_REDACTED | ATTACHMENT | VOICE_RECORDING`
Required: Yes

 ** [Tags](#API_CreateAttachedFile_RequestSyntax) **   <a name="connect-CreateAttachedFile-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "Tags": {"key1":"value1", "key2":"value2"} }`.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAttachedFile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": "string",
   "FileArn": "string",
   "FileId": "string",
   "FileStatus": "string"
}
```

## Response Elements
<a name="API_CreateAttachedFile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_CreateAttachedFile_ResponseSyntax) **   <a name="connect-CreateAttachedFile-response-CreationTime"></a>
The time of Creation of the file resource as an ISO timestamp. It's specified in ISO 8601 format: `yyyy-MM-ddThh:mm:ss.SSSZ`. For example, `2024-05-03T02:41:28.172Z`.
Type: String

 ** [FileArn](#API_CreateAttachedFile_ResponseSyntax) **   <a name="connect-CreateAttachedFile-response-FileArn"></a>
The unique identifier of the attached file resource (ARN).
Type: String

 ** [FileId](#API_CreateAttachedFile_ResponseSyntax) **   <a name="connect-CreateAttachedFile-response-FileId"></a>
The unique identifier of the attached file resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [FileStatus](#API_CreateAttachedFile_ResponseSyntax) **   <a name="connect-CreateAttachedFile-response-FileStatus"></a>
The current status of the attached file. Valid values: `PROCESSING` \| `APPROVED` \| `REJECTED` \| `FAILED`.
Type: String
Valid Values: `APPROVED | REJECTED | PROCESSING | FAILED`

## Errors
<a name="API_CreateAttachedFile_Errors"></a>

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
<a name="API_CreateAttachedFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateAttachedFile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateAttachedFile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateAttachedFile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateAttachedFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateAttachedFile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateAttachedFile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateAttachedFile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateAttachedFile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateAttachedFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateAttachedFile)
