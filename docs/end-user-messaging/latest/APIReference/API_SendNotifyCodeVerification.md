---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_SendNotifyCodeVerification.html
---

# SendNotifyCodeVerification
<a name="API_SendNotifyCodeVerification"></a>

Generates a one-time passcode and delivers it to a recipient over the requested channel. The passcode policy is captured from the referenced notify code configuration at the time of the request, so later updates to the configuration do not affect verifications that are already in progress.

## Request Syntax
<a name="API_SendNotifyCodeVerification_RequestSyntax"></a>

```
POST /v1/notify-code-verifications/send HTTP/1.1
Content-type: application/json

{
   "channel": "{{string}}",
   "configurationSetName": "{{string}}",
   "context": {
      "{{string}}" : "{{string}}"
   },
   "destinationIdentity": "{{string}}",
   "notifyCodeConfiguration": "{{string}}",
   "originationIdentity": "{{string}}",
   "overrideChannelParameters": {
      "notify": {
         "notifyTemplateId": "{{string}}",
         "voiceId": "{{string}}"
      },
      "text": {
         "destinationCountryParameters": {
            "{{string}}" : "{{string}}"
         },
         "inlineTemplateBody": "{{string}}"
      },
      "voice": {
         "inlineTemplateBody": "{{string}}",
         "languageCode": "{{string}}",
         "voiceId": "{{string}}",
         "voiceMessageBodyTextType": "{{string}}"
      },
      "whatsApp": {
         "languageCode": "{{string}}",
         "whatsAppTemplateName": "{{string}}"
      }
   },
   "overrideCodeConfigurationParameters": {
      "codeLength": {{number}},
      "codeType": "{{string}}",
      "maxAttempts": {{number}},
      "validityPeriodMinutes": {{number}}
   },
   "referenceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendNotifyCodeVerification_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SendNotifyCodeVerification_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channel](#API_SendNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-request-channel"></a>
The channel used to deliver the one-time passcode to the recipient.
Type: String
Valid Values: `TEXT | VOICE | WHATSAPP`
Required: Yes

 ** [configurationSetName](#API_SendNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-request-configurationSetName"></a>
The name of the configuration set used to control how delivery events for the message are handled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** [context](#API_SendNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-request-context"></a>
A map of custom key and value pairs that are propagated to the delivery events for this verification.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `\S+`
Value Length Constraints: Minimum length of 1. Maximum length of 800.
Value Pattern: `\S(?:[\s\S]*\S)?`
Required: No

 ** [destinationIdentity](#API_SendNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-request-destinationIdentity"></a>
The recipient identifier. For the TEXT and VOICE channels, specify an E.164 phone number. For the WhatsApp channel, specify a WhatsApp address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[\x21-\x22\x24-\x7E]+`
Required: Yes

 ** [notifyCodeConfiguration](#API_SendNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-request-notifyCodeConfiguration"></a>
The identifier or Amazon Resource Name (ARN) of the notify code configuration that supplies the passcode policy and template defaults. When you do not specify a configuration, you must supply the template in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [originationIdentity](#API_SendNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-request-originationIdentity"></a>
The identity used to send the message, such as a phone number, sender ID, or pool that is owned by your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/+-]+`
Required: Yes

 ** [overrideChannelParameters](#API_SendNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-request-overrideChannelParameters"></a>
The channel-specific parameters used to render and deliver the one-time passcode for this request. The route that is derived from the channel and the origination identity selects the matching channel. When you do not specify channel parameters, the service uses the parameters from the referenced notify code configuration.
Type: [ChannelParameters](API_ChannelParameters.md) object
Required: No

 ** [overrideCodeConfigurationParameters](#API_SendNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-request-overrideCodeConfigurationParameters"></a>
The per-send overrides for the passcode policy parameters, including the code type, length, validity period, and maximum number of attempts. These values override the values from the referenced notify code configuration. When you do not specify a value, the value from the configuration is used, and if neither is set, the service default applies.
Type: [CodeConfigurationParameters](API_CodeConfigurationParameters.md) object
Required: No

 ** [referenceId](#API_SendNotifyCodeVerification_RequestSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-request-referenceId"></a>
A caller-supplied reference identifier that binds a send request to a later validate request. Specify the same value in both requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_-]+`
Required: No

## Response Syntax
<a name="API_SendNotifyCodeVerification_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "messageId": "string",
   "verificationId": "string"
}
```

## Response Elements
<a name="API_SendNotifyCodeVerification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messageId](#API_SendNotifyCodeVerification_ResponseSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-response-messageId"></a>
The service-generated identifier for the message that delivers the one-time passcode.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`

 ** [verificationId](#API_SendNotifyCodeVerification_ResponseSyntax) **   <a name="endusermessaging-SendNotifyCodeVerification-response-verificationId"></a>
The service-generated identifier for the verification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_:/-]+`

## Errors
<a name="API_SendNotifyCodeVerification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
The identifier of the resource that the request conflicts with.
 ** resourceType **
The type of the resource that the request conflicts with.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.
 ** resourceId **
The identifier of the resource that could not be found.
 ** resourceType **
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed a service quota for your account.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because it exceeded the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_SendNotifyCodeVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/SendNotifyCodeVerification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/SendNotifyCodeVerification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/SendNotifyCodeVerification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/SendNotifyCodeVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/SendNotifyCodeVerification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/SendNotifyCodeVerification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/SendNotifyCodeVerification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/SendNotifyCodeVerification)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/SendNotifyCodeVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/SendNotifyCodeVerification)
