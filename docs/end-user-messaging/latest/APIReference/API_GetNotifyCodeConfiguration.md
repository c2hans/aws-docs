---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_GetNotifyCodeConfiguration.html
---

# GetNotifyCodeConfiguration
<a name="API_GetNotifyCodeConfiguration"></a>

Retrieves a notify code configuration.

## Request Syntax
<a name="API_GetNotifyCodeConfiguration_RequestSyntax"></a>

```
GET /v1/notify-code-configurations/{{notifyCodeConfigurationId+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNotifyCodeConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [notifyCodeConfigurationId](#API_GetNotifyCodeConfiguration_RequestSyntax) **   <a name="endusermessaging-GetNotifyCodeConfiguration-request-uri-notifyCodeConfigurationId"></a>
The unique identifier of the notify code configuration. You can specify either the bare ID or the full Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Request Body
<a name="API_GetNotifyCodeConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNotifyCodeConfiguration_ResponseSyntax"></a>

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
<a name="API_GetNotifyCodeConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notifyCodeConfiguration](#API_GetNotifyCodeConfiguration_ResponseSyntax) **   <a name="endusermessaging-GetNotifyCodeConfiguration-response-notifyCodeConfiguration"></a>
The notify code configuration resource.
Type: [NotifyCodeConfiguration](API_NotifyCodeConfiguration.md) object

## Errors
<a name="API_GetNotifyCodeConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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

 ** ThrottlingException **
The request was denied because it exceeded the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_GetNotifyCodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/GetNotifyCodeConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/GetNotifyCodeConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/GetNotifyCodeConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/GetNotifyCodeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/GetNotifyCodeConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/GetNotifyCodeConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/GetNotifyCodeConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/GetNotifyCodeConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/GetNotifyCodeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/GetNotifyCodeConfiguration)
