---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_CreateNotifyCodeConfiguration.html
---

# CreateNotifyCodeConfiguration
<a name="API_CreateNotifyCodeConfiguration"></a>

Creates a notify code configuration. A notify code configuration is a reusable policy that defines how one-time passcodes are generated and rendered, including the code type, length, validity period, maximum number of attempts, and channel templates.

## Request Syntax
<a name="API_CreateNotifyCodeConfiguration_RequestSyntax"></a>

```
POST /v1/notify-code-configurations HTTP/1.1
Content-type: application/json

{
   "channelParameters": {
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
   "clientToken": "{{string}}",
   "codeConfigurationParameters": {
      "codeLength": {{number}},
      "codeType": "{{string}}",
      "maxAttempts": {{number}},
      "validityPeriodMinutes": {{number}}
   },
   "deletionProtectionEnabled": {{boolean}},
   "notifyCodeConfigurationName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateNotifyCodeConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateNotifyCodeConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelParameters](#API_CreateNotifyCodeConfiguration_RequestSyntax) **   <a name="endusermessaging-CreateNotifyCodeConfiguration-request-channelParameters"></a>
The channel-specific parameters used to render and deliver the one-time passcode. Provide parameters for any subset of channels. Each member configures one delivery route, and the route that is selected at send time uses the matching channel.
Type: [ChannelParameters](API_ChannelParameters.md) object
Required: No

 ** [clientToken](#API_CreateNotifyCodeConfiguration_RequestSyntax) **   <a name="endusermessaging-CreateNotifyCodeConfiguration-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [codeConfigurationParameters](#API_CreateNotifyCodeConfiguration_RequestSyntax) **   <a name="endusermessaging-CreateNotifyCodeConfiguration-request-codeConfigurationParameters"></a>
The passcode policy parameters, including the code type, length, validity period, and maximum number of attempts. Each member is optional. When you omit a member, no value is applied at create time and the default is applied when a passcode is sent.
Type: [CodeConfigurationParameters](API_CodeConfigurationParameters.md) object
Required: No

 ** [deletionProtectionEnabled](#API_CreateNotifyCodeConfiguration_RequestSyntax) **   <a name="endusermessaging-CreateNotifyCodeConfiguration-request-deletionProtectionEnabled"></a>
Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.
Type: Boolean
Required: No

 ** [notifyCodeConfigurationName](#API_CreateNotifyCodeConfiguration_RequestSyntax) **   <a name="endusermessaging-CreateNotifyCodeConfiguration-request-notifyCodeConfigurationName"></a>
The name of the notify code configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: Yes

 ** [tags](#API_CreateNotifyCodeConfiguration_RequestSyntax) **   <a name="endusermessaging-CreateNotifyCodeConfiguration-request-tags"></a>
An array of key and value pair tags that are associated with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateNotifyCodeConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "notifyCodeConfiguration": {
      "channelParameters": {
         "notify": {
            "notifyTemplateId": "string",
            "voiceId": "string"
         },
         "text": {
            "destinationCountryParameters": {
               "string" : "string"
            },
            "inlineTemplateBody": "string"
         },
         "voice": {
            "inlineTemplateBody": "string",
            "languageCode": "string",
            "voiceId": "string",
            "voiceMessageBodyTextType": "string"
         },
         "whatsApp": {
            "languageCode": "string",
            "whatsAppTemplateName": "string"
         }
      },
      "codeConfigurationParameters": {
         "codeLength": number,
         "codeType": "string",
         "maxAttempts": number,
         "validityPeriodMinutes": number
      },
      "createdAt": number,
      "deletionProtectionEnabled": boolean,
      "notifyCodeConfigurationArn": "string",
      "notifyCodeConfigurationId": "string",
      "notifyCodeConfigurationName": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_CreateNotifyCodeConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notifyCodeConfiguration](#API_CreateNotifyCodeConfiguration_ResponseSyntax) **   <a name="endusermessaging-CreateNotifyCodeConfiguration-response-notifyCodeConfiguration"></a>
The notify code configuration resource.
Type: [NotifyCodeConfiguration](API_NotifyCodeConfiguration.md) object

## Errors
<a name="API_CreateNotifyCodeConfiguration_Errors"></a>

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
<a name="API_CreateNotifyCodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/CreateNotifyCodeConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/CreateNotifyCodeConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/CreateNotifyCodeConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/CreateNotifyCodeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/CreateNotifyCodeConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/CreateNotifyCodeConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/CreateNotifyCodeConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/CreateNotifyCodeConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/CreateNotifyCodeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/CreateNotifyCodeConfiguration)
