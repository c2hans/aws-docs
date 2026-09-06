---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html
---

# CreateStreamSessionConnection
<a name="API_CreateStreamSessionConnection"></a>

Enables clients to reconnect to a stream session while preserving all session state and data in the disconnected session. This reconnection process can be initiated when a stream session is in either `PENDING_CLIENT_RECONNECTION` or `ACTIVE` status. The process works as follows:

1. Initial disconnect:
   + When a client disconnects or loses connection, the stream session transitions from `CONNECTED` to `PENDING_CLIENT_RECONNECTION`

1. Reconnection time window:
   + Clients have `ConnectionTimeoutSeconds` (defined in [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html)) to reconnect before session termination
   + Your backend server must call **CreateStreamSessionConnection** to initiate reconnection
   + Session transitions to `RECONNECTING` status

1. Reconnection completion:
   + On successful **CreateStreamSessionConnection**, session status changes to `ACTIVE`
   + Provide the new connection information to the requesting client
   + Client must establish connection within `ConnectionTimeoutSeconds`
   + Session terminates automatically if client fails to connect in time

For more information about the stream session lifecycle, see [Stream sessions](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-sessions.html) in the *Amazon GameLift Streams Developer Guide*.

To begin re-connecting to an existing stream session, specify the stream group ID and stream session ID that you want to reconnect to, and the signal request to use with the stream.

## Request Syntax
<a name="API_CreateStreamSessionConnection_RequestSyntax"></a>

```
POST /streamgroups/{{Identifier}}/streamsessions/{{StreamSessionIdentifier}}/connections HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "SignalRequest": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateStreamSessionConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_CreateStreamSessionConnection_RequestSyntax) **   <a name="gameliftstreams-CreateStreamSessionConnection-request-uri-Identifier"></a>
 [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
 The stream group that you want to run this stream session with. The stream group must be in `ACTIVE` status.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [StreamSessionIdentifier](#API_CreateStreamSessionConnection_RequestSyntax) **   <a name="gameliftstreams-CreateStreamSessionConnection-request-uri-StreamSessionIdentifier"></a>
 [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream session resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567`. Example ID: `ABC123def4567`.
 The stream session must be in `PENDING_CLIENT_RECONNECTION` or `ACTIVE` status.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_CreateStreamSessionConnection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SignalRequest](#API_CreateStreamSessionConnection_RequestSyntax) **   <a name="gameliftstreams-CreateStreamSessionConnection-request-SignalRequest"></a>
A WebRTC ICE offer string to use when initializing a WebRTC connection. The offer is a very long JSON string. Provide the string as a text value in quotes. The offer must be newly generated, not the same offer provided to `StartStreamSession`.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [ClientToken](#API_CreateStreamSessionConnection_RequestSyntax) **   <a name="gameliftstreams-CreateStreamSessionConnection-request-ClientToken"></a>
 A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

## Response Syntax
<a name="API_CreateStreamSessionConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SignalResponse": "string"
}
```

## Response Elements
<a name="API_CreateStreamSessionConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SignalResponse](#API_CreateStreamSessionConnection_ResponseSyntax) **   <a name="gameliftstreams-CreateStreamSessionConnection-response-SignalResponse"></a>
The WebRTC answer string that the stream server generates in response to the `SignalRequest`.
Type: String

## Errors
<a name="API_CreateStreamSessionConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [ConflictException](API_ConflictException.md)
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
 ** Message **
Description of the error.
HTTP Status Code: 409

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error and is unable to complete the request.
 ** Message **
Description of the error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The resource specified in the request was not found. Correct the request before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling. Retry the request after the suggested wait time.
 ** Message **
Description of the error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.
 ** Message **
Description of the error.
HTTP Status Code: 400

## See Also
<a name="API_CreateStreamSessionConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/CreateStreamSessionConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/CreateStreamSessionConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/CreateStreamSessionConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/CreateStreamSessionConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/CreateStreamSessionConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/CreateStreamSessionConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/CreateStreamSessionConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/CreateStreamSessionConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/CreateStreamSessionConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/CreateStreamSessionConnection)
