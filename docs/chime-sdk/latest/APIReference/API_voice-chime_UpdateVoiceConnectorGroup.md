---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnectorGroup.html
---

# UpdateVoiceConnectorGroup
<a name="API_voice-chime_UpdateVoiceConnectorGroup"></a>

Updates the settings for the specified Amazon Chime SDK Voice Connector group.

## Request Syntax
<a name="API_voice-chime_UpdateVoiceConnectorGroup_RequestSyntax"></a>

```
PUT /voice-connector-groups/{{voiceConnectorGroupId}} HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "VoiceConnectorItems": [
      {
         "Priority": {{number}},
         "VoiceConnectorId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_voice-chime_UpdateVoiceConnectorGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [voiceConnectorGroupId](#API_voice-chime_UpdateVoiceConnectorGroup_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceConnectorGroup-request-uri-VoiceConnectorGroupId"></a>
The Voice Connector ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_UpdateVoiceConnectorGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_voice-chime_UpdateVoiceConnectorGroup_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceConnectorGroup-request-Name"></a>
The name of the Voice Connector group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: Yes

 ** [VoiceConnectorItems](#API_voice-chime_UpdateVoiceConnectorGroup_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceConnectorGroup-request-VoiceConnectorItems"></a>
The `VoiceConnectorItems` to associate with the Voice Connector group.
Type: Array of [VoiceConnectorItem](API_voice-chime_VoiceConnectorItem.md) objects
Required: Yes

## Response Syntax
<a name="API_voice-chime_UpdateVoiceConnectorGroup_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "VoiceConnectorGroup": {
      "CreatedTimestamp": "string",
      "Name": "string",
      "UpdatedTimestamp": "string",
      "VoiceConnectorGroupArn": "string",
      "VoiceConnectorGroupId": "string",
      "VoiceConnectorItems": [
         {
            "Priority": number,
            "VoiceConnectorId": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_voice-chime_UpdateVoiceConnectorGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [VoiceConnectorGroup](#API_voice-chime_UpdateVoiceConnectorGroup_ResponseSyntax) **   <a name="chimesdk-voice-chime_UpdateVoiceConnectorGroup-response-VoiceConnectorGroup"></a>
The updated Voice Connector group.
Type: [VoiceConnectorGroup](API_voice-chime_VoiceConnectorGroup.md) object

## Errors
<a name="API_voice-chime_UpdateVoiceConnectorGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
Multiple instances of the same request were made simultaneously.
HTTP Status Code: 409

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
<a name="API_voice-chime_UpdateVoiceConnectorGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/UpdateVoiceConnectorGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/UpdateVoiceConnectorGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/UpdateVoiceConnectorGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/UpdateVoiceConnectorGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/UpdateVoiceConnectorGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/UpdateVoiceConnectorGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/UpdateVoiceConnectorGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/UpdateVoiceConnectorGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/UpdateVoiceConnectorGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/UpdateVoiceConnectorGroup)
