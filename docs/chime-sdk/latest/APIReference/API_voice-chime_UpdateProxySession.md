---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateProxySession.html
---

# UpdateProxySession
<a name="API_voice-chime_UpdateProxySession"></a>

Updates the specified proxy session details, such as voice or SMS capabilities.

**Important**
End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.

## Request Syntax
<a name="API_voice-chime_UpdateProxySession_RequestSyntax"></a>

```
POST /voice-connectors/{{voiceConnectorId}}/proxy-sessions/{{proxySessionId}} HTTP/1.1
Content-type: application/json

{
   "Capabilities": [ "{{string}}" ],
   "ExpiryMinutes": {{number}}
}
```

## URI Request Parameters
<a name="API_voice-chime_UpdateProxySession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [proxySessionId](#API_voice-chime_UpdateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateProxySession-request-uri-ProxySessionId"></a>
The proxy session ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** [voiceConnectorId](#API_voice-chime_UpdateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateProxySession-request-uri-VoiceConnectorId"></a>
The Voice Connector ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_UpdateProxySession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Capabilities](#API_voice-chime_UpdateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateProxySession-request-Capabilities"></a>
The proxy session capabilities.
Type: Array of strings
Valid Values: `Voice | SMS`
Required: Yes

 ** [ExpiryMinutes](#API_voice-chime_UpdateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_UpdateProxySession-request-ExpiryMinutes"></a>
The number of minutes allowed for the proxy session.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_voice-chime_UpdateProxySession_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "ProxySession": {
      "Capabilities": [ "string" ],
      "CreatedTimestamp": "string",
      "EndedTimestamp": "string",
      "ExpiryMinutes": number,
      "GeoMatchLevel": "string",
      "GeoMatchParams": {
         "AreaCode": "string",
         "Country": "string"
      },
      "Name": "string",
      "NumberSelectionBehavior": "string",
      "Participants": [
         {
            "PhoneNumber": "string",
            "ProxyPhoneNumber": "string"
         }
      ],
      "ProxySessionId": "string",
      "Status": "string",
      "UpdatedTimestamp": "string",
      "VoiceConnectorId": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_UpdateProxySession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ProxySession](#API_voice-chime_UpdateProxySession_ResponseSyntax) **   <a name="chimesdk-voice-chime_UpdateProxySession-response-ProxySession"></a>
The updated proxy session details.
Type: [ProxySession](API_voice-chime_ProxySession.md) object

## Errors
<a name="API_voice-chime_UpdateProxySession_Errors"></a>

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
<a name="API_voice-chime_UpdateProxySession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/UpdateProxySession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/UpdateProxySession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/UpdateProxySession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/UpdateProxySession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/UpdateProxySession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/UpdateProxySession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/UpdateProxySession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/UpdateProxySession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/UpdateProxySession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/UpdateProxySession)
