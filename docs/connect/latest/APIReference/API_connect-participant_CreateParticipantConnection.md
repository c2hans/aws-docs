---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_CreateParticipantConnection.html
---

# CreateParticipantConnection
<a name="API_connect-participant_CreateParticipantConnection"></a>

Creates the participant's connection.

For security recommendations, see [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat).

For WebRTC security recommendations, see [Connect Customer WebRTC security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-webrtc-security).

**Note**
 `ParticipantToken` is used for invoking this API instead of `ConnectionToken`.

The participant token is valid for the lifetime of the participant – until they are part of a contact. For WebRTC participants, if they leave or are disconnected for 60 seconds, a new participant needs to be created using the [CreateParticipant](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateParticipant.html) API.

 **For `WEBSOCKET` Type**:

The response URL for has a connect expiry timeout of 100s. Clients must manually connect to the returned websocket URL and subscribe to the desired topic.

For chat, you need to publish the following on the established websocket connection:

 `{"topic":"aws/subscribe","content":{"topics":["aws/chat"]}}`

Upon websocket URL expiry, as specified in the response ConnectionExpiry parameter, clients need to call this API again to obtain a new websocket URL and perform the same steps as before.

The expiry time for the connection token is different than the `ChatDurationInMinutes`. Expiry time for the connection token is 1 day.

 **For `WEBRTC_CONNECTION` Type**:

The response includes connection data required for the client application to join the call using the Amazon Chime SDK client libraries. The WebRTCConnection response contains Meeting and Attendee information needed to establish the media connection.

The attendee join token in WebRTCConnection response is valid for the lifetime of the participant in the call. If a participant leaves or is disconnected for 60 seconds, their participant credentials will no longer be valid, and a new participant will need to be created to rejoin the call.

 **Message streaming support**: This API can also be used together with the [StartContactStreaming](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactStreaming.html) API to create a participant connection for chat contacts that are not using a websocket. For more information about message streaming, [Enable real-time chat message streaming](https://docs.aws.amazon.com/connect/latest/adminguide/chat-message-streaming.html) in the *Amazon Connect Administrator Guide*.

 **Multi-user web, in-app, video calling support**:

For WebRTC calls, this API is used in conjunction with the CreateParticipant API to enable multi-party calling. The StartWebRTCContact API creates the initial contact and routes it to an agent, while CreateParticipant adds additional participants to the ongoing call. For more information about multi-party WebRTC calls, see [Enable multi-user web, in-app, and video calling](https://docs.aws.amazon.com/connect/latest/adminguide/enable-multiuser-inapp.html) in the *Amazon Connect Administrator Guide*.

 **Feature specifications**: For information about feature specifications, such as the allowed number of open websocket connections per participant or maximum number of WebRTC participants, see [Feature specifications](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#feature-limits) in the *Amazon Connect Administrator Guide*.

**Note**
The Amazon Connect Participant Service APIs do not use [Signature Version 4 authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Request Syntax
<a name="API_connect-participant_CreateParticipantConnection_RequestSyntax"></a>

```
POST /participant/connection HTTP/1.1
X-Amz-Bearer: {{ParticipantToken}}
Content-type: application/json

{
   "ConnectParticipant": {{boolean}},
   "Type": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_connect-participant_CreateParticipantConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ParticipantToken](#API_connect-participant_CreateParticipantConnection_RequestSyntax) **   <a name="connect-connect-participant_CreateParticipantConnection-request-ParticipantToken"></a>
This is a header parameter.
The ParticipantToken as obtained from [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) API response.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_connect-participant_CreateParticipantConnection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConnectParticipant](#API_connect-participant_CreateParticipantConnection_RequestSyntax) **   <a name="connect-connect-participant_CreateParticipantConnection-request-ConnectParticipant"></a>
Amazon Connect Participant is used to mark the participant as connected for customer participant in message streaming, as well as for agent or manager participant in non-streaming chats.
Type: Boolean
Required: No

 ** [Type](#API_connect-participant_CreateParticipantConnection_RequestSyntax) **   <a name="connect-connect-participant_CreateParticipantConnection-request-Type"></a>
Type of connection information required. If you need `CONNECTION_CREDENTIALS` along with marking participant as connected, pass `CONNECTION_CREDENTIALS` in `Type`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `WEBSOCKET | CONNECTION_CREDENTIALS | WEBRTC_CONNECTION`
Required: No

## Response Syntax
<a name="API_connect-participant_CreateParticipantConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectionCredentials": {
      "ConnectionToken": "string",
      "Expiry": "string"
   },
   "WebRTCConnection": {
      "Attendee": {
         "AttendeeId": "string",
         "JoinToken": "string"
      },
      "Meeting": {
         "MediaPlacement": {
            "AudioFallbackUrl": "string",
            "AudioHostUrl": "string",
            "EventIngestionUrl": "string",
            "SignalingUrl": "string"
         },
         "MeetingFeatures": {
            "Audio": {
               "EchoReduction": "string"
            }
         },
         "MeetingId": "string"
      }
   },
   "Websocket": {
      "ConnectionExpiry": "string",
      "Url": "string"
   }
}
```

## Response Elements
<a name="API_connect-participant_CreateParticipantConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionCredentials](#API_connect-participant_CreateParticipantConnection_ResponseSyntax) **   <a name="connect-connect-participant_CreateParticipantConnection-response-ConnectionCredentials"></a>
Creates the participant's connection credentials. The authentication token associated with the participant's connection.
Type: [ConnectionCredentials](API_connect-participant_ConnectionCredentials.md) object

 ** [WebRTCConnection](#API_connect-participant_CreateParticipantConnection_ResponseSyntax) **   <a name="connect-connect-participant_CreateParticipantConnection-response-WebRTCConnection"></a>
Creates the participant's WebRTC connection data required for the client application (mobile application or website) to connect to the call.
Type: [WebRTCConnection](API_connect-participant_WebRTCConnection.md) object

 ** [Websocket](#API_connect-participant_CreateParticipantConnection_ResponseSyntax) **   <a name="connect-connect-participant_CreateParticipantConnection-response-Websocket"></a>
Creates the participant's websocket connection.
Type: [Websocket](API_connect-participant_Websocket.md) object

## Errors
<a name="API_connect-participant_CreateParticipantConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the Amazon Connect service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by Amazon Connect.
HTTP Status Code: 400

## See Also
<a name="API_connect-participant_CreateParticipantConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectparticipant-2018-09-07/CreateParticipantConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectparticipant-2018-09-07/CreateParticipantConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/CreateParticipantConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectparticipant-2018-09-07/CreateParticipantConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/CreateParticipantConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectparticipant-2018-09-07/CreateParticipantConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectparticipant-2018-09-07/CreateParticipantConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectparticipant-2018-09-07/CreateParticipantConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectparticipant-2018-09-07/CreateParticipantConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/CreateParticipantConnection)
