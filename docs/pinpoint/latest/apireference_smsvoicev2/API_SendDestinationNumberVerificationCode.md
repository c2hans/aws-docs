---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendDestinationNumberVerificationCode.html
---

# SendDestinationNumberVerificationCode
<a name="API_SendDestinationNumberVerificationCode"></a>

Before you can send test messages to a verified destination phone number you need to opt-in the verified destination phone number. Creates a new text message with a verification code and send it to a verified destination phone number. Once you have the verification code use [VerifyDestinationNumber](API_VerifyDestinationNumber.md) to opt-in the verified destination phone number to receive messages.

## Request Syntax
<a name="API_SendDestinationNumberVerificationCode_RequestSyntax"></a>

```
{
   "ConfigurationSetName": "{{string}}",
   "Context": {
      "{{string}}" : "{{string}}"
   },
   "DestinationCountryParameters": {
      "{{string}}" : "{{string}}"
   },
   "LanguageCode": "{{string}}",
   "OriginationIdentity": "{{string}}",
   "VerificationChannel": "{{string}}",
   "VerifiedDestinationNumberId": "{{string}}"
}
```

## Request Parameters
<a name="API_SendDestinationNumberVerificationCode_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_SendDestinationNumberVerificationCode_RequestSyntax) **   <a name="pinpoint-SendDestinationNumberVerificationCode-request-ConfigurationSetName"></a>
The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [Context](#API_SendDestinationNumberVerificationCode_RequestSyntax) **   <a name="pinpoint-SendDestinationNumberVerificationCode-request-Context"></a>
You can specify custom data in this field. If you do, that data is logged to the event destination.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `\S+`
Value Length Constraints: Minimum length of 1. Maximum length of 800.
Value Pattern: `(?!\s)^[\s\S]+(?<!\s)`
Required: No

 ** [DestinationCountryParameters](#API_SendDestinationNumberVerificationCode_RequestSyntax) **   <a name="pinpoint-SendDestinationNumberVerificationCode-request-DestinationCountryParameters"></a>
This field is used for any country-specific registration requirements. Currently, this setting is only used when you send messages to recipients in India using a sender ID. For more information see [Special requirements for sending SMS messages to recipients in India](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-senderid-india.html).
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Valid Keys: `IN_TEMPLATE_ID | IN_ENTITY_ID`
Value Length Constraints: Minimum length of 1. Maximum length of 64.
Value Pattern: `\S+`
Required: No

 ** [LanguageCode](#API_SendDestinationNumberVerificationCode_RequestSyntax) **   <a name="pinpoint-SendDestinationNumberVerificationCode-request-LanguageCode"></a>
Choose the language to use for the message.
Type: String
Valid Values: `DE_DE | EN_GB | EN_US | ES_419 | ES_ES | FR_CA | FR_FR | IT_IT | JA_JP | KO_KR | PT_BR | ZH_CN | ZH_TW`
Required: No

 ** [OriginationIdentity](#API_SendDestinationNumberVerificationCode_RequestSyntax) **   <a name="pinpoint-SendDestinationNumberVerificationCode-request-OriginationIdentity"></a>
The origination identity of the message. This can be either the PhoneNumber, PhoneNumberId, PhoneNumberArn, SenderId, SenderIdArn, PoolId, or PoolArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/\+-]+`
Required: No

 ** [VerificationChannel](#API_SendDestinationNumberVerificationCode_RequestSyntax) **   <a name="pinpoint-SendDestinationNumberVerificationCode-request-VerificationChannel"></a>
Choose to send the verification code as an SMS or voice message.
Type: String
Valid Values: `TEXT | VOICE`
Required: Yes

 ** [VerifiedDestinationNumberId](#API_SendDestinationNumberVerificationCode_RequestSyntax) **   <a name="pinpoint-SendDestinationNumberVerificationCode-request-VerifiedDestinationNumberId"></a>
The unique identifier for the verified destination phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_SendDestinationNumberVerificationCode_ResponseSyntax"></a>

```
{
   "MessageId": "string"
}
```

## Response Elements
<a name="API_SendDestinationNumberVerificationCode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MessageId](#API_SendDestinationNumberVerificationCode_ResponseSyntax) **   <a name="pinpoint-SendDestinationNumberVerificationCode-response-MessageId"></a>
The unique identifier for the message.
Type: String

## Errors
<a name="API_SendDestinationNumberVerificationCode_Errors"></a>

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
<a name="API_SendDestinationNumberVerificationCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/SendDestinationNumberVerificationCode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/SendDestinationNumberVerificationCode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SendDestinationNumberVerificationCode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/SendDestinationNumberVerificationCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SendDestinationNumberVerificationCode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/SendDestinationNumberVerificationCode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/SendDestinationNumberVerificationCode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/SendDestinationNumberVerificationCode)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/SendDestinationNumberVerificationCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SendDestinationNumberVerificationCode)
