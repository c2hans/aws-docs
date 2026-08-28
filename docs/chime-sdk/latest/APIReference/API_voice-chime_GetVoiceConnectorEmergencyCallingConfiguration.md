---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration.html
---

# GetVoiceConnectorEmergencyCallingConfiguration
<a name="API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration"></a>

Retrieves the emergency calling configuration details for the specified Voice Connector.

## Request Syntax
<a name="API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration_RequestSyntax"></a>

```
GET /voice-connectors/{{voiceConnectorId}}/emergency-calling-configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [voiceConnectorId](#API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration_RequestSyntax) **   <a name="chimesdk-voice-chime_GetVoiceConnectorEmergencyCallingConfiguration-request-uri-VoiceConnectorId"></a>
The Voice Connector ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EmergencyCallingConfiguration": {
      "DNIS": [
         {
            "CallingCountry": "string",
            "EmergencyPhoneNumber": "string",
            "TestPhoneNumber": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EmergencyCallingConfiguration](#API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration_ResponseSyntax) **   <a name="chimesdk-voice-chime_GetVoiceConnectorEmergencyCallingConfiguration-response-EmergencyCallingConfiguration"></a>
The details of the emergency calling configuration.
Type: [EmergencyCallingConfiguration](API_voice-chime_EmergencyCallingConfiguration.md) object

## Errors
<a name="API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
The requested resource couldn't be found.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The number of customer requests exceeds the request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client isn't authorized to request a resource.
HTTP Status Code: 401

## See Also
<a name="API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/GetVoiceConnectorEmergencyCallingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
