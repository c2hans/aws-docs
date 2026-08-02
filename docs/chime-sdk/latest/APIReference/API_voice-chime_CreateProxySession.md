---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateProxySession.html
---

# CreateProxySession
<a name="API_voice-chime_CreateProxySession"></a>

Creates a proxy session for the specified Amazon Chime SDK Voice Connector for the specified participant phone numbers.

**Important**
End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.

## Request Syntax
<a name="API_voice-chime_CreateProxySession_RequestSyntax"></a>

```
POST /voice-connectors/{{voiceConnectorId}}/proxy-sessions HTTP/1.1
Content-type: application/json

{
   "Capabilities": [ "{{string}}" ],
   "ExpiryMinutes": {{number}},
   "GeoMatchLevel": "{{string}}",
   "GeoMatchParams": {
      "AreaCode": "{{string}}",
      "Country": "{{string}}"
   },
   "Name": "{{string}}",
   "NumberSelectionBehavior": "{{string}}",
   "ParticipantPhoneNumbers": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_voice-chime_CreateProxySession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [voiceConnectorId](#API_voice-chime_CreateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateProxySession-request-uri-VoiceConnectorId"></a>
The Voice Connector ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_voice-chime_CreateProxySession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Capabilities](#API_voice-chime_CreateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateProxySession-request-Capabilities"></a>
The proxy session's capabilities.
Type: Array of strings
Valid Values: `Voice | SMS`
Required: Yes

 ** [ExpiryMinutes](#API_voice-chime_CreateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateProxySession-request-ExpiryMinutes"></a>
The number of minutes allowed for the proxy session.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [GeoMatchLevel](#API_voice-chime_CreateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateProxySession-request-GeoMatchLevel"></a>
The preference for matching the country or area code of the proxy phone number with that of the first participant.
Type: String
Valid Values: `Country | AreaCode`
Required: No

 ** [GeoMatchParams](#API_voice-chime_CreateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateProxySession-request-GeoMatchParams"></a>
The country and area code for the proxy phone number.
Type: [GeoMatchParams](API_voice-chime_GeoMatchParams.md) object
Required: No

 ** [Name](#API_voice-chime_CreateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateProxySession-request-Name"></a>
The name of the proxy session.
Type: String
Pattern: `^$|^[a-zA-Z0-9 ]{0,30}$`
Required: No

 ** [NumberSelectionBehavior](#API_voice-chime_CreateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateProxySession-request-NumberSelectionBehavior"></a>
The preference for proxy phone number reuse, or stickiness, between the same participants across sessions.
Type: String
Valid Values: `PreferSticky | AvoidSticky`
Required: No

 ** [ParticipantPhoneNumbers](#API_voice-chime_CreateProxySession_RequestSyntax) **   <a name="chimesdk-voice-chime_CreateProxySession-request-ParticipantPhoneNumbers"></a>
The participant phone numbers.
Type: Array of strings
Array Members: Fixed number of 2 items.
Pattern: `^\+?[1-9]\d{1,14}$`
Required: Yes

## Response Syntax
<a name="API_voice-chime_CreateProxySession_ResponseSyntax"></a>

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
<a name="API_voice-chime_CreateProxySession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ProxySession](#API_voice-chime_CreateProxySession_ResponseSyntax) **   <a name="chimesdk-voice-chime_CreateProxySession-response-ProxySession"></a>
The proxy session details.
Type: [ProxySession](API_voice-chime_ProxySession.md) object

## Errors
<a name="API_voice-chime_CreateProxySession_Errors"></a>

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
<a name="API_voice-chime_CreateProxySession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/CreateProxySession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/CreateProxySession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/CreateProxySession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/CreateProxySession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/CreateProxySession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/CreateProxySession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/CreateProxySession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/CreateProxySession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/CreateProxySession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/CreateProxySession)
