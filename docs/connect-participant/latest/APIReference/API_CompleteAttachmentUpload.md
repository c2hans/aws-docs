---
source_url: https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CompleteAttachmentUpload.html
---

# CompleteAttachmentUpload
<a name="API_connect-participant_CompleteAttachmentUpload"></a>

Allows you to confirm that the attachment has been uploaded using the pre-signed URL provided in StartAttachmentUpload API. A conflict exception is thrown when an attachment with that identifier is already being uploaded.

For security recommendations, see [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat).

**Note**
 `ConnectionToken` is used for invoking this API instead of `ParticipantToken`.

The Amazon Connect Participant Service APIs do not use [Signature Version 4 authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Request Syntax
<a name="API_connect-participant_CompleteAttachmentUpload_RequestSyntax"></a>

```
POST /participant/complete-attachment-upload HTTP/1.1
X-Amz-Bearer: {{ConnectionToken}}
Content-type: application/json

{
   "AttachmentIds": [ "{{string}}" ],
   "ClientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-participant_CompleteAttachmentUpload_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionToken](#API_connect-participant_CompleteAttachmentUpload_RequestSyntax) **   <a name="connect-connect-participant_CompleteAttachmentUpload-request-ConnectionToken"></a>
The authentication token associated with the participant's connection.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_connect-participant_CompleteAttachmentUpload_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AttachmentIds](#API_connect-participant_CompleteAttachmentUpload_RequestSyntax) **   <a name="connect-connect-participant_CompleteAttachmentUpload-request-AttachmentIds"></a>
A list of unique identifiers for the attachments.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [ClientToken](#API_connect-participant_CompleteAttachmentUpload_RequestSyntax) **   <a name="connect-connect-participant_CompleteAttachmentUpload-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Response Syntax
<a name="API_connect-participant_CompleteAttachmentUpload_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-participant_CompleteAttachmentUpload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-participant_CompleteAttachmentUpload_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation conflicts with the current state of a service resource associated with the request.
HTTP Status Code: 409

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
<a name="API_connect-participant_CompleteAttachmentUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectparticipant-2018-09-07/CompleteAttachmentUpload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectparticipant-2018-09-07/CompleteAttachmentUpload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/CompleteAttachmentUpload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectparticipant-2018-09-07/CompleteAttachmentUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/CompleteAttachmentUpload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectparticipant-2018-09-07/CompleteAttachmentUpload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectparticipant-2018-09-07/CompleteAttachmentUpload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectparticipant-2018-09-07/CompleteAttachmentUpload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectparticipant-2018-09-07/CompleteAttachmentUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/CompleteAttachmentUpload)
