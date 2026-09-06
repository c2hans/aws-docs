---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorStreamingConfiguration.html
---

# PutVoiceConnectorStreamingConfiguration
<a name="API_voice-chime_PutVoiceConnectorStreamingConfiguration"></a>

Updates a Voice Connector's streaming configuration settings.

## Request Syntax
<a name="API_voice-chime_PutVoiceConnectorStreamingConfiguration_RequestSyntax"></a>

```
PUT /voice-connectors/{{voiceConnectorId}}/streaming-configuration HTTP/1.1
Content-type: application/json

{
   "StreamingConfiguration": {
      "DataRetentionInHours": {{number}},
      "Disabled": {{boolean}},
      "MediaInsightsConfiguration": {
         "ConfigurationArn": "{{string}}",
         "Disabled": {{boolean}}
      },
      "StreamingNotificationTargets": [
         {
            "NotificationTarget": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_voice-chime_PutVoiceConnectorStreamingConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [voiceConnectorId](#API_voice-chime_PutVoiceConnectorStreamingConfiguration_RequestSyntax) **   <a name="chimesdk-voice-chime_PutVoiceConnectorStreamingConfiguration-request-uri-VoiceConnectorId"></a>
The Voice Connector ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_PutVoiceConnectorStreamingConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [StreamingConfiguration](#API_voice-chime_PutVoiceConnectorStreamingConfiguration_RequestSyntax) **   <a name="chimesdk-voice-chime_PutVoiceConnectorStreamingConfiguration-request-StreamingConfiguration"></a>
The streaming settings being updated.
Type: [StreamingConfiguration](API_voice-chime_StreamingConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_voice-chime_PutVoiceConnectorStreamingConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "StreamingConfiguration": {
      "DataRetentionInHours": number,
      "Disabled": boolean,
      "MediaInsightsConfiguration": {
         "ConfigurationArn": "string",
         "Disabled": boolean
      },
      "StreamingNotificationTargets": [
         {
            "NotificationTarget": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_voice-chime_PutVoiceConnectorStreamingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StreamingConfiguration](#API_voice-chime_PutVoiceConnectorStreamingConfiguration_ResponseSyntax) **   <a name="chimesdk-voice-chime_PutVoiceConnectorStreamingConfiguration-response-StreamingConfiguration"></a>
The updated streaming settings.
Type: [StreamingConfiguration](API_voice-chime_StreamingConfiguration.md) object

## Errors
<a name="API_voice-chime_PutVoiceConnectorStreamingConfiguration_Errors"></a>

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
<a name="API_voice-chime_PutVoiceConnectorStreamingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/PutVoiceConnectorStreamingConfiguration)
