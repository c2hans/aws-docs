---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendRcsMessage.html
---

# SendRcsMessage
<a name="API_SendRcsMessage"></a>

Creates a new RCS message and sends it to a recipient's phone number. RCS messages support rich content including text, files, rich cards, and carousels with interactive suggested actions.

## Request Syntax
<a name="API_SendRcsMessage_RequestSyntax"></a>

```
{
   "ConfigurationSetName": "{{string}}",
   "Context": {
      "{{string}}" : "{{string}}"
   },
   "DestinationPhoneNumber": "{{string}}",
   "DryRun": {{boolean}},
   "FallbackConfiguration": {
      "Channel": "{{string}}",
      "MediaUrls": [ "{{string}}" ],
      "MessageBody": "{{string}}",
      "OriginationIdentity": "{{string}}"
   },
   "MaxPrice": "{{string}}",
   "MessageFeedbackEnabled": {{boolean}},
   "MessageTrafficType": "{{string}}",
   "OriginationIdentity": "{{string}}",
   "ProtectConfigurationId": "{{string}}",
   "RcsMessageContent": {
      "Content": { ... },
      "Suggestions": [
         { ... }
      ]
   },
   "TimeToLive": {{number}}
}
```

## Request Parameters
<a name="API_SendRcsMessage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-ConfigurationSetName"></a>
The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [Context](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-Context"></a>
You can specify custom data in this field. If you do, that data is logged to the event destination.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `\S+`
Value Length Constraints: Minimum length of 1. Maximum length of 800.
Value Pattern: `(?!\s)^[\s\S]+(?<!\s)`
Required: No

 ** [DestinationPhoneNumber](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-DestinationPhoneNumber"></a>
The destination phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** [DryRun](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-DryRun"></a>
When set to true, the message is checked and validated, but isn't sent to the end recipient.
Type: Boolean
Required: No

 ** [FallbackConfiguration](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-FallbackConfiguration"></a>
Configuration for SMS or MMS fallback when RCS delivery fails. If provided, the service sends a fallback message via the specified channel when the RCS message fails or the TimeToLive expires.
Type: [RcsFallbackConfiguration](API_RcsFallbackConfiguration.md) object
Required: No

 ** [MaxPrice](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-MaxPrice"></a>
The maximum amount that you want to spend, in US dollars, per each RCS message.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 8.
Pattern: `[0-9]{0,2}\.[0-9]{1,5}`
Required: No

 ** [MessageFeedbackEnabled](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-MessageFeedbackEnabled"></a>
Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using [PutMessageFeedback](API_PutMessageFeedback.md).
Type: Boolean
Required: No

 ** [MessageTrafficType](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-MessageTrafficType"></a>
The traffic type of the RCS message. Valid values are AUTHENTICATION, TRANSACTION, PROMOTION, SERVICE\_REQUEST, and ACKNOWLEDGEMENT. This field is reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** [OriginationIdentity](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-OriginationIdentity"></a>
The origination identity of the message. This can be either the RcsAgentId, RcsAgentArn, PoolId, or PoolArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/\+-]+`
Required: Yes

 ** [ProtectConfigurationId](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-ProtectConfigurationId"></a>
The unique identifier of the protect configuration to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [RcsMessageContent](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-RcsMessageContent"></a>
The content of the RCS message. Contains the message content (text, file, rich card, or carousel) and optional message-level suggested actions.
Type: [RcsMessageContent](API_RcsMessageContent.md) object
Required: No

 ** [TimeToLive](#API_SendRcsMessage_RequestSyntax) **   <a name="pinpoint-SendRcsMessage-request-TimeToLive"></a>
The duration in seconds that the RCS message is valid for delivery. If the message cannot be delivered within this duration, it is considered expired. Valid values are 1 to 172800 (48 hours). If a FallbackConfiguration is provided, the fallback is triggered when the duration expires without delivery confirmation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 172800.
Required: No

## Response Syntax
<a name="API_SendRcsMessage_ResponseSyntax"></a>

```
{
   "MessageId": "string"
}
```

## Response Elements
<a name="API_SendRcsMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MessageId](#API_SendRcsMessage_ResponseSyntax) **   <a name="pinpoint-SendRcsMessage-response-MessageId"></a>
The unique identifier for the message.
Type: String

## Errors
<a name="API_SendRcsMessage_Errors"></a>

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
<a name="API_SendRcsMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/SendRcsMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/SendRcsMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SendRcsMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/SendRcsMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SendRcsMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/SendRcsMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/SendRcsMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/SendRcsMessage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/SendRcsMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SendRcsMessage)
