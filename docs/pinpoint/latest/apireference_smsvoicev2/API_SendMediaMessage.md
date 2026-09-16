---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.html
---

# SendMediaMessage
<a name="API_SendMediaMessage"></a>

Creates a new multimedia message (MMS) and sends it to a recipient's phone number.

## Request Syntax
<a name="API_SendMediaMessage_RequestSyntax"></a>

```
{
   "ConfigurationSetName": "{{string}}",
   "Context": {
      "{{string}}" : "{{string}}"
   },
   "DestinationPhoneNumber": "{{string}}",
   "DryRun": {{boolean}},
   "MaxPrice": "{{string}}",
   "MediaUrls": [ "{{string}}" ],
   "MessageBody": "{{string}}",
   "MessageFeedbackEnabled": {{boolean}},
   "OriginationIdentity": "{{string}}",
   "ProtectConfigurationId": "{{string}}",
   "TimeToLive": {{number}}
}
```

## Request Parameters
<a name="API_SendMediaMessage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-ConfigurationSetName"></a>
The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [Context](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-Context"></a>
You can specify custom data in this field. If you do, that data is logged to the event destination.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `\S+`
Value Length Constraints: Minimum length of 1. Maximum length of 800.
Value Pattern: `(?!\s)^[\s\S]+(?<!\s)`
Required: No

 ** [DestinationPhoneNumber](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-DestinationPhoneNumber"></a>
The destination phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** [DryRun](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-DryRun"></a>
When set to true, the message is checked and validated, but isn't sent to the end recipient.
Type: Boolean
Required: No

 ** [MaxPrice](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-MaxPrice"></a>
The maximum amount that you want to spend, in US dollars, per each MMS message.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 8.
Pattern: `[0-9]{0,2}\.[0-9]{1,5}`
Required: No

 ** [MediaUrls](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-MediaUrls"></a>
An array of URLs to each media file to send.
The media files have to be stored in an S3 bucket. Supported media file formats are listed in [MMS file types, size and character limits](https://docs.aws.amazon.com/sms-voice/latest/userguide/mms-limitations-character.html). For more information on creating an S3 bucket and managing objects, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html), [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the *Amazon S3 User Guide*, and [Setting up an Amazon S3 bucket for MMS files](https://docs.aws.amazon.com/sms-voice/latest/userguide/send-mms-message.html#send-mms-message-bucket) in the * AWS End User Messaging SMS User Guide*.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `s3://([a-z0-9\.-]{3,63})/(.+)`
Required: No

 ** [MessageBody](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-MessageBody"></a>
The text body of the message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

 ** [MessageFeedbackEnabled](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-MessageFeedbackEnabled"></a>
Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using [PutMessageFeedback](API_PutMessageFeedback.md).
Type: Boolean
Required: No

 ** [OriginationIdentity](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-OriginationIdentity"></a>
The origination identity of the message. This can be either the PhoneNumber, PhoneNumberId, PhoneNumberArn, SenderId, SenderIdArn, PoolId, or PoolArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/\+-]+`
Required: Yes

 ** [ProtectConfigurationId](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-ProtectConfigurationId"></a>
The unique identifier of the protect configuration to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [TimeToLive](#API_SendMediaMessage_RequestSyntax) **   <a name="pinpoint-SendMediaMessage-request-TimeToLive"></a>
How long the media message is valid for. By default this is 72 hours.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 259200.
Required: No

## Response Syntax
<a name="API_SendMediaMessage_ResponseSyntax"></a>

```
{
   "MessageId": "string"
}
```

## Response Elements
<a name="API_SendMediaMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MessageId](#API_SendMediaMessage_ResponseSyntax) **   <a name="pinpoint-SendMediaMessage-response-MessageId"></a>
The unique identifier for the message.
Type: String

## Errors
<a name="API_SendMediaMessage_Errors"></a>

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
<a name="API_SendMediaMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/SendMediaMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/SendMediaMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SendMediaMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/SendMediaMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SendMediaMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/SendMediaMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/SendMediaMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/SendMediaMessage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/SendMediaMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SendMediaMessage)
