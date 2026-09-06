---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendVoiceMessage.html
---

# SendVoiceMessage
<a name="API_SendVoiceMessage"></a>

Allows you to send a request that sends a voice message. This operation uses [Amazon Polly](http://aws.amazon.com/polly/) to convert a text script into a voice message.

## Request Syntax
<a name="API_SendVoiceMessage_RequestSyntax"></a>

```
{
   "ConfigurationSetName": "{{string}}",
   "Context": {
      "{{string}}" : "{{string}}"
   },
   "DestinationPhoneNumber": "{{string}}",
   "DryRun": {{boolean}},
   "MaxPricePerMinute": "{{string}}",
   "MessageBody": "{{string}}",
   "MessageBodyTextType": "{{string}}",
   "MessageFeedbackEnabled": {{boolean}},
   "OriginationIdentity": "{{string}}",
   "ProtectConfigurationId": "{{string}}",
   "TimeToLive": {{number}},
   "VoiceId": "{{string}}"
}
```

## Request Parameters
<a name="API_SendVoiceMessage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-ConfigurationSetName"></a>
The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [Context](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-Context"></a>
You can specify custom data in this field. If you do, that data is logged to the event destination.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `\S+`
Value Length Constraints: Minimum length of 1. Maximum length of 800.
Value Pattern: `(?!\s)^[\s\S]+(?<!\s)`
Required: No

 ** [DestinationPhoneNumber](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-DestinationPhoneNumber"></a>
The destination phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** [DryRun](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-DryRun"></a>
When set to true, the message is checked and validated, but isn't sent to the end recipient.
Type: Boolean
Required: No

 ** [MaxPricePerMinute](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-MaxPricePerMinute"></a>
The maximum amount to spend per voice message, in US dollars.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 8.
Pattern: `[0-9]{0,2}\.[0-9]{1,5}`
Required: No

 ** [MessageBody](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-MessageBody"></a>
The text to convert to a voice message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6000.
Pattern: `(?!\s*$)[\s\S]+`
Required: No

 ** [MessageBodyTextType](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-MessageBodyTextType"></a>
Specifies if the MessageBody field contains text or [speech synthesis markup language (SSML)](https://docs.aws.amazon.com/polly/latest/dg/what-is.html).
+ TEXT: This is the default value. When used the maximum character limit is 3000.
+ SSML: When used the maximum character limit is 6000 including SSML tagging.
Type: String
Valid Values: `TEXT | SSML`
Required: No

 ** [MessageFeedbackEnabled](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-MessageFeedbackEnabled"></a>
Set to true to enable message feedback for the message. When a user receives the message you need to update the message status using [PutMessageFeedback](API_PutMessageFeedback.md).
Type: Boolean
Required: No

 ** [OriginationIdentity](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-OriginationIdentity"></a>
The origination identity to use for the voice call. This can be the PhoneNumber, PhoneNumberId, PhoneNumberArn, PoolId, or PoolArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/\+-]+`
Required: Yes

 ** [ProtectConfigurationId](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-ProtectConfigurationId"></a>
The unique identifier for the protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [TimeToLive](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-TimeToLive"></a>
How long the voice message is valid for. By default this is 72 hours.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 259200.
Required: No

 ** [VoiceId](#API_SendVoiceMessage_RequestSyntax) **   <a name="pinpoint-SendVoiceMessage-request-VoiceId"></a>
The voice for the [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/what-is.html) service to use. By default this is set to "MATTHEW".
Type: String
Valid Values: `AMY | ASTRID | BIANCA | BRIAN | CAMILA | CARLA | CARMEN | CELINE | CHANTAL | CONCHITA | CRISTIANO | DORA | EMMA | ENRIQUE | EWA | FILIZ | GERAINT | GIORGIO | GWYNETH | HANS | INES | IVY | JACEK | JAN | JOANNA | JOEY | JUSTIN | KARL | KENDRA | KIMBERLY | LEA | LIV | LOTTE | LUCIA | LUPE | MADS | MAJA | MARLENE | MATHIEU | MATTHEW | MAXIM | MIA | MIGUEL | MIZUKI | NAJA | NICOLE | PENELOPE | RAVEENA | RICARDO | RUBEN | RUSSELL | SALLI | SEOYEON | TAKUMI | TATYANA | VICKI | VITORIA | ZEINA | ZHIYU`
Required: No

## Response Syntax
<a name="API_SendVoiceMessage_ResponseSyntax"></a>

```
{
   "MessageId": "string"
}
```

## Response Elements
<a name="API_SendVoiceMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MessageId](#API_SendVoiceMessage_ResponseSyntax) **   <a name="pinpoint-SendVoiceMessage-response-MessageId"></a>
The unique identifier for the message.
Type: String

## Errors
<a name="API_SendVoiceMessage_Errors"></a>

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
<a name="API_SendVoiceMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/SendVoiceMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/SendVoiceMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SendVoiceMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/SendVoiceMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SendVoiceMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/SendVoiceMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/SendVoiceMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/SendVoiceMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/SendVoiceMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SendVoiceMessage)
