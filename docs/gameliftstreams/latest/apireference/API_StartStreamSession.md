---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html
---

# StartStreamSession
<a name="API_StartStreamSession"></a>

 This action initiates a new stream session and outputs connection information that clients can use to access the stream. A stream session refers to an instance of a stream that Amazon GameLift Streams transmits from the server to the end-user. A stream session runs on a compute resource that a stream group has allocated. The start stream session process works as follows:

1. Prerequisites:
   + You must have a stream group in `ACTIVE` status
   + You must have idle or on-demand capacity in a stream group in the location you want to stream from
   + You must have at least one application associated to the stream group (use [AssociateApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html) if needed)

1. Start stream request:
   + Your backend server calls **StartStreamSession** to initiate connection
   + Amazon GameLift Streams creates the stream session resource, assigns an Amazon Resource Name (ARN) value, and begins searching for available stream capacity to run the stream
   + Session transitions to `ACTIVATING` status

1. Placement completion:
   + If Amazon GameLift Streams is successful in finding capacity for the stream, the stream session status changes to `ACTIVE` status and **StartStreamSession** returns stream connection information
   + If Amazon GameLift Streams was not successful in finding capacity within the placement timeout period (defined according to the capacity type and platform type), the stream session status changes to `ERROR` status and **StartStreamSession** returns a `StatusReason` of `placementTimeout`

1. Connection completion:
   + Provide the new connection information to the requesting client
   + Client must establish connection within `ConnectionTimeoutSeconds` (specified in **StartStreamSession** parameters)
   + Session terminates automatically if client fails to connect in time

For more information about the stream session lifecycle, see [Stream sessions](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-sessions.html) in the *Amazon GameLift Streams Developer Guide*.

Timeouts to be aware of that affect a stream session:
+  **Placement timeout**: The amount of time that Amazon GameLift Streams has to find capacity for a stream request. Placement timeout varies based on the capacity type used to fulfill your stream request:
  +  **Always-on capacity**: 75 seconds
  +  **On-demand capacity**:
    + Linux/Proton runtimes: 90 seconds
    + Windows runtime: 10 minutes
+  **Connection timeout**: The amount of time that Amazon GameLift Streams waits for a client to connect to a stream session in `ACTIVE` status, or reconnect to a stream session in `PENDING_CLIENT_RECONNECTION` status, the latter of which occurs when a client disconnects or loses connection from a stream session. If no client connects before the timeout, Amazon GameLift Streams terminates the stream session. This value is specified by `ConnectionTimeoutSeconds` in the `StartStreamSession` parameters.
+  **Maximum session length**: A stream session will be terminated after this amount of time has elapsed since it started, regardless of any existing client connections. This value is specified by `SessionLengthSeconds` in the `StartStreamSession` parameters.

To start a new stream session, specify a stream group ID and application ID, along with the transport protocol and signal request to use with the stream session.

For stream groups that have multiple locations, provide a set of locations ordered by priority using a `Locations` parameter. Amazon GameLift Streams will start a single stream session in the next available location. An application must be finished replicating to a remote location before the remote location can host a stream.

To reconnect to a stream session after a client disconnects or loses connection, use [CreateStreamSessionConnection](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html).

## Request Syntax
<a name="API_StartStreamSession_RequestSyntax"></a>

```
POST /streamgroups/{{Identifier}}/streamsessions HTTP/1.1
Content-type: application/json

{
   "AdditionalEnvironmentVariables": {
      "{{string}}" : "{{string}}"
   },
   "AdditionalLaunchArgs": [ "{{string}}" ],
   "ApplicationIdentifier": "{{string}}",
   "ClientToken": "{{string}}",
   "ConnectionTimeoutSeconds": {{number}},
   "Description": "{{string}}",
   "DisplayConfiguration": {
      "Resolution": {
         "Height": {{number}},
         "Width": {{number}}
      }
   },
   "Locations": [ "{{string}}" ],
   "PerformanceStatsConfiguration": {
      "SharedWithClient": {{boolean}}
   },
   "Protocol": "{{string}}",
   "RoleArn": "{{string}}",
   "SessionLengthSeconds": {{number}},
   "SignalRequest": "{{string}}",
   "UserId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartStreamSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-uri-Identifier"></a>
The stream group to run this stream session with.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_StartStreamSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationIdentifier](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-ApplicationIdentifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`. Example ID: `a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [Protocol](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-Protocol"></a>
The data transport protocol to use for the stream session.
Type: String
Valid Values: `WebRTC`
Required: Yes

 ** [SignalRequest](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-SignalRequest"></a>
A WebRTC ICE offer string to use when initializing a WebRTC connection. Typically, the offer is a very long JSON string. Provide the string as a text value in quotes.
Amazon GameLift Streams also supports setting the field to "NO\_CLIENT\_CONNECTION". This will create a session without needing any browser request or Web SDK integration. The session starts up as usual and waits for a reconnection from a browser, which is accomplished using [CreateStreamSessionConnection](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html).
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [AdditionalEnvironmentVariables](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-AdditionalEnvironmentVariables"></a>
A set of options that you can use to control the stream session runtime environment, expressed as a set of key-value pairs. You can use this to configure the application or stream session details. You can also provide custom environment variables that Amazon GameLift Streams passes to your game client.
If you want to debug your application with environment variables, we recommend that you do so in a local environment outside of Amazon GameLift Streams. For more information, refer to the Compatibility Guidance in the troubleshooting section of the Developer Guide.
 `AdditionalEnvironmentVariables` and `AdditionalLaunchArgs` have similar purposes. `AdditionalEnvironmentVariables` passes data using environment variables; while `AdditionalLaunchArgs` passes data using command-line arguments.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[_a-zA-Z][_a-zA-Z0-9]*`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [AdditionalLaunchArgs](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-AdditionalLaunchArgs"></a>
A list of CLI arguments that are sent to the streaming server when a stream session launches. You can use this to configure the application or stream session details. You can also provide custom arguments that Amazon GameLift Streams passes to your game client.
 `AdditionalEnvironmentVariables` and `AdditionalLaunchArgs` have similar purposes. `AdditionalEnvironmentVariables` passes data using environment variables; while `AdditionalLaunchArgs` passes data using command-line arguments.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [ClientToken](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-ClientToken"></a>
 A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [ConnectionTimeoutSeconds](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-ConnectionTimeoutSeconds"></a>
Length of time (in seconds) that Amazon GameLift Streams should wait for a client to connect or reconnect to the stream session. Applies to both connection and reconnection scenarios. This time span starts when the stream session reaches `ACTIVE` state. If no client connects before the timeout, Amazon GameLift Streams terminates the stream session. Default value is 120.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3600.
Required: No

 ** [Description](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-Description"></a>
A human-readable label for the stream session. You can update this value later.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`
Required: No

 ** [DisplayConfiguration](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-DisplayConfiguration"></a>
The configuration for the stream session's virtual monitor, including the resolution settings.
If not specified, Amazon GameLift Streams uses the default resolution of 1920 × 1080.
Type: [DisplayConfiguration](API_DisplayConfiguration.md) object
Required: No

 ** [Locations](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-Locations"></a>
 A list of locations, in order of priority, where you want Amazon GameLift Streams to start a stream from. For example, `us-east-1`. Amazon GameLift Streams selects the location with the next available capacity to start a single stream session in. If this value is empty, Amazon GameLift Streams attempts to start a stream session in the primary location.
 For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [PerformanceStatsConfiguration](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-PerformanceStatsConfiguration"></a>
Configuration settings for sharing the stream session's performance stats with the client
Type: [PerformanceStatsConfiguration](API_PerformanceStatsConfiguration.md) object
Required: No

 ** [RoleArn](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-RoleArn"></a>
The ARN of an AWS Identity and Access Management (IAM) role that Amazon GameLift Streams assumes on your behalf during the stream session. The role grants Amazon GameLift Streams permission to obtain temporary credentials for your application. The role's trust policy must allow the `gameliftstreams.amazonaws.com` service principal to assume it. The role name must start with `GameLiftStreams-`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:iam::\d{12}:role/.+`
Required: No

 ** [SessionLengthSeconds](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-SessionLengthSeconds"></a>
The maximum duration of a session. Amazon GameLift Streams will automatically terminate a session after this amount of time has elapsed, regardless of any existing client connections. Default value is 43200 (12 hours).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: No

 ** [UserId](#API_StartStreamSession_RequestSyntax) **   <a name="gameliftstreams-StartStreamSession-request-UserId"></a>
 An opaque, unique identifier for an end-user, defined by the developer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[-_a-zA-Z0-9/=+]*`
Required: No

## Response Syntax
<a name="API_StartStreamSession_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "AdditionalEnvironmentVariables": {
      "string" : "string"
   },
   "AdditionalLaunchArgs": [ "string" ],
   "ApplicationArn": "string",
   "Arn": "string",
   "ConnectionTimeoutSeconds": number,
   "CreatedAt": number,
   "Description": "string",
   "DisplayConfiguration": {
      "Resolution": {
         "Height": number,
         "Width": number
      }
   },
   "ExportFilesMetadata": {
      "OutputUri": "string",
      "Status": "string",
      "StatusReason": "string"
   },
   "LastUpdatedAt": number,
   "Location": "string",
   "LogFileLocationUri": "string",
   "PerformanceStatsConfiguration": {
      "SharedWithClient": boolean
   },
   "Protocol": "string",
   "RoleArn": "string",
   "SessionLengthSeconds": number,
   "SignalRequest": "string",
   "SignalResponse": "string",
   "Status": "string",
   "StatusReason": "string",
   "StreamGroupId": "string",
   "UserId": "string",
   "WebSdkProtocolUrl": "string"
}
```

## Response Elements
<a name="API_StartStreamSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [AdditionalEnvironmentVariables](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-AdditionalEnvironmentVariables"></a>
A set of options that you can use to control the stream session runtime environment, expressed as a set of key-value pairs. You can use this to configure the application or stream session details. You can also provide custom environment variables that Amazon GameLift Streams passes to your game client.
If you want to debug your application with environment variables, we recommend that you do so in a local environment outside of Amazon GameLift Streams. For more information, refer to the Compatibility Guidance in the troubleshooting section of the Developer Guide.
 `AdditionalEnvironmentVariables` and `AdditionalLaunchArgs` have similar purposes. `AdditionalEnvironmentVariables` passes data using environment variables; while `AdditionalLaunchArgs` passes data using command-line arguments.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[_a-zA-Z][_a-zA-Z0-9]*`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [AdditionalLaunchArgs](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-AdditionalLaunchArgs"></a>
A list of CLI arguments that are sent to the streaming server when a stream session launches. You can use this to configure the application or stream session details. You can also provide custom arguments that Amazon GameLift Streams passes to your game client.
 `AdditionalEnvironmentVariables` and `AdditionalLaunchArgs` have similar purposes. `AdditionalEnvironmentVariables` passes data using environment variables; while `AdditionalLaunchArgs` passes data using command-line arguments.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [ApplicationArn](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-ApplicationArn"></a>
The application streaming in this session.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [Arn](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-Arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that's assigned to a stream session resource. When combined with the stream group resource ID, this value uniquely identifies the stream session across all AWS Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamsession/[stream group resource ID]/[stream session resource ID]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [ConnectionTimeoutSeconds](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-ConnectionTimeoutSeconds"></a>
The length of time that Amazon GameLift Streams should wait for a client to connect or reconnect to the stream session. This time span starts when the stream session reaches `ACTIVE` or `PENDING_CLIENT_RECONNECTION` state. If no client connects (or reconnects) before the timeout, Amazon GameLift Streams terminates the stream session.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3600.

 ** [CreatedAt](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [Description](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-Description"></a>
A human-readable label for the stream session. You can update this value at any time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`

 ** [DisplayConfiguration](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-DisplayConfiguration"></a>
The configuration for the stream session's virtual monitor.
Type: [DisplayConfiguration](API_DisplayConfiguration.md) object

 ** [ExportFilesMetadata](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-ExportFilesMetadata"></a>
Provides details about the stream session's exported files.
Type: [ExportFilesMetadata](API_ExportFilesMetadata.md) object

 ** [LastUpdatedAt](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-LastUpdatedAt"></a>
A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [Location](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-Location"></a>
The location where Amazon GameLift Streams hosts and streams your application. For example, `us-east-1`. For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9-]+`

 ** [LogFileLocationUri](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-LogFileLocationUri"></a>
Access location for log files that your content generates during a stream session. These log files are uploaded to cloud storage location at the end of a stream session. The Amazon GameLift Streams application resource defines which log files to upload.
Type: String

 ** [PerformanceStatsConfiguration](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-PerformanceStatsConfiguration"></a>
The performance stats configuration for the stream session
Type: [PerformanceStatsConfiguration](API_PerformanceStatsConfiguration.md) object

 ** [Protocol](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-Protocol"></a>
The data transfer protocol in use with the stream session.
Type: String
Valid Values: `WebRTC`

 ** [RoleArn](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-RoleArn"></a>
The ARN of the AWS Identity and Access Management (IAM) role that Amazon GameLift Streams assumes on behalf of your application during the stream session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:iam::\d{12}:role/.+`

 ** [SessionLengthSeconds](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-SessionLengthSeconds"></a>
The maximum duration of a session. Amazon GameLift Streams will automatically terminate a session after this amount of time has elapsed, regardless of any existing client connections.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.

 ** [SignalRequest](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-SignalRequest"></a>
The WebRTC ICE offer string that a client generates to initiate a connection to the stream session.
Type: String
Length Constraints: Minimum length of 1.

 ** [SignalResponse](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-SignalResponse"></a>
The WebRTC answer string that the stream server generates in response to the `SignalRequest`.
Type: String

 ** [Status](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-Status"></a>
The current status of the stream session. A stream session is ready for a client to connect when in `ACTIVE` status.
+  `ACTIVATING`: The stream session is starting and preparing to stream.
+  `ACTIVE`: The stream session is ready and waiting for a client connection. A client has `ConnectionTimeoutSeconds` (specified in `StartStreamSession`) from when the session reaches `ACTIVE` state to establish a connection. If no client connects within this timeframe, the session automatically terminates.
+  `CONNECTED`: The stream session has a connected client. A session will automatically terminate if there is no user input for 60 minutes, or if the maximum length of a session specified by `SessionLengthSeconds` in `StartStreamSession` is exceeded.
+  `ERROR`: The stream session failed to activate. See `StatusReason` (returned by `GetStreamSession` and `StartStreamSession`) for more information.
+  `PENDING_CLIENT_RECONNECTION`: A client has recently disconnected and the stream session is waiting for the client to reconnect. A client has `ConnectionTimeoutSeconds` (specified in `StartStreamSession`) from when the session reaches `PENDING_CLIENT_RECONNECTION` state to re-establish a connection. If no client connects within this timeframe, the session automatically terminates.
+  `RECONNECTING`: A client has initiated a reconnect to a session that was in `PENDING_CLIENT_RECONNECTION` state.
+  `TERMINATING`: The stream session is ending.
+  `TERMINATED`: The stream session has ended.
Type: String
Valid Values: `ACTIVATING | ACTIVE | CONNECTED | PENDING_CLIENT_RECONNECTION | RECONNECTING | TERMINATING | TERMINATED | ERROR`

 ** [StatusReason](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-StatusReason"></a>
A short description of the reason the stream session is in `ERROR` status or `TERMINATED` status.
 `ERROR` status reasons:
+  `applicationLogS3DestinationError`: Could not write the application log to the Amazon S3 bucket that is configured for the streaming application. Make sure the bucket still exists.
+  `internalError`: An internal service error occurred. Start a new stream session to continue streaming.
+  `invalidSignalRequest`: The WebRTC signal request that was sent is not valid. When starting or reconnecting to a stream session, use `generateSignalRequest` in the Amazon GameLift Streams Web SDK to generate a new signal request.
+  `placementTimeout`: Amazon GameLift Streams could not find available stream capacity to start a stream session. Increase the stream capacity in the stream group or wait until capacity becomes available.
 `TERMINATED` status reasons:
+  `apiTerminated`: The stream session was terminated by an API call to [TerminateStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html).
+  `applicationExit`: The streaming application exited or crashed. The stream session was terminated because the application is no longer running.
+  `connectionTimeout`: The stream session was terminated because the client failed to connect within the connection timeout period specified by `ConnectionTimeoutSeconds`.
+  `maxSessionLengthTimeout`: The stream session was terminated because it exceeded the maximum session length timeout period specified by `SessionLengthSeconds`.
+  `reconnectionTimeout`: The stream session was terminated because the client failed to reconnect within the reconnection timeout period specified by `ConnectionTimeoutSeconds` after losing connection.
Type: String
Valid Values: `internalError | invalidSignalRequest | placementTimeout | applicationLogS3DestinationError | assumeRoleFailed | applicationExit | connectionTimeout | reconnectionTimeout | maxSessionLengthTimeout | idleTimeout | apiTerminated`

 ** [StreamGroupId](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-StreamGroupId"></a>
The unique identifier for the Amazon GameLift Streams stream group that is hosting the stream session. Format example: `sg-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`

 ** [UserId](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-UserId"></a>
 An opaque, unique identifier for an end-user, defined by the developer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[-_a-zA-Z0-9/=+]*`

 ** [WebSdkProtocolUrl](#API_StartStreamSession_ResponseSyntax) **   <a name="gameliftstreams-StartStreamSession-response-WebSdkProtocolUrl"></a>
The URL of an S3 bucket that stores Amazon GameLift Streams WebSDK files. The URL is used to establish connection with the client.
Type: String

## Errors
<a name="API_StartStreamSession_Errors"></a>

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

## Examples
<a name="API_StartStreamSession_Examples"></a>

### CLI Example
<a name="API_StartStreamSession_Example_1"></a>

The following example shows how to use the CLI to start a Amazon GameLift Streams stream session. The request uses an ARN value to identify a stream group for the new session.

#### Sample Request
<a name="API_StartStreamSession_Example_1_Request"></a>

```
aws gameliftstreams start-stream-session \
  --description MyGame-stream \
  --identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4 \
  --application-identifier arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6 \
  --protocol WebRTC \
  --signal-request "[webrtc-ice-offer json string]" \
  --connection-timeout-seconds 300 \
  --session-length-seconds 7200 \
  --additional-launch-args '["-dx11","-fullscreen"]' \
  --additional-environment-variables '{"USERNAME": "BestPlayerEver",
      "LANG": "ja_JP.UTF-8",
      "AUTHTOKEN": "abcdef01234567899876543210fedcba"
    }'
```

## See Also
<a name="API_StartStreamSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/StartStreamSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/StartStreamSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/StartStreamSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/StartStreamSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/StartStreamSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/StartStreamSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/StartStreamSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/StartStreamSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/StartStreamSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/StartStreamSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
