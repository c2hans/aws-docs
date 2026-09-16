---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html
---

# GetStreamSession
<a name="API_GetStreamSession"></a>

Retrieves properties for a Amazon GameLift Streams stream session resource. Specify the Amazon Resource Name (ARN) of the stream session that you want to retrieve and its stream group ARN. If the operation is successful, it returns properties for the requested resource.

## Request Syntax
<a name="API_GetStreamSession_RequestSyntax"></a>

```
GET /streamgroups/{{Identifier}}/streamsessions/{{StreamSessionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetStreamSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetStreamSession_RequestSyntax) **   <a name="gameliftstreams-GetStreamSession-request-uri-Identifier"></a>
The stream group that runs this stream session.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [StreamSessionIdentifier](#API_GetStreamSession_RequestSyntax) **   <a name="gameliftstreams-GetStreamSession-request-uri-StreamSessionIdentifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream session resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567`. Example ID: `ABC123def4567`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_GetStreamSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetStreamSession_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetStreamSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdditionalEnvironmentVariables](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-AdditionalEnvironmentVariables"></a>
A set of options that you can use to control the stream session runtime environment, expressed as a set of key-value pairs. You can use this to configure the application or stream session details. You can also provide custom environment variables that Amazon GameLift Streams passes to your game client.
If you want to debug your application with environment variables, we recommend that you do so in a local environment outside of Amazon GameLift Streams. For more information, refer to the Compatibility Guidance in the troubleshooting section of the Developer Guide.
 `AdditionalEnvironmentVariables` and `AdditionalLaunchArgs` have similar purposes. `AdditionalEnvironmentVariables` passes data using environment variables; while `AdditionalLaunchArgs` passes data using command-line arguments.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[_a-zA-Z][_a-zA-Z0-9]*`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [AdditionalLaunchArgs](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-AdditionalLaunchArgs"></a>
A list of CLI arguments that are sent to the streaming server when a stream session launches. You can use this to configure the application or stream session details. You can also provide custom arguments that Amazon GameLift Streams passes to your game client.
 `AdditionalEnvironmentVariables` and `AdditionalLaunchArgs` have similar purposes. `AdditionalEnvironmentVariables` passes data using environment variables; while `AdditionalLaunchArgs` passes data using command-line arguments.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [ApplicationArn](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-ApplicationArn"></a>
The application streaming in this session.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [Arn](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-Arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that's assigned to a stream session resource. When combined with the stream group resource ID, this value uniquely identifies the stream session across all AWS Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamsession/[stream group resource ID]/[stream session resource ID]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [ConnectionTimeoutSeconds](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-ConnectionTimeoutSeconds"></a>
The length of time that Amazon GameLift Streams should wait for a client to connect or reconnect to the stream session. This time span starts when the stream session reaches `ACTIVE` or `PENDING_CLIENT_RECONNECTION` state. If no client connects (or reconnects) before the timeout, Amazon GameLift Streams terminates the stream session.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3600.

 ** [CreatedAt](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [Description](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-Description"></a>
A human-readable label for the stream session. You can update this value at any time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`

 ** [DisplayConfiguration](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-DisplayConfiguration"></a>
The configuration for the stream session's virtual monitor.
Type: [DisplayConfiguration](API_DisplayConfiguration.md) object

 ** [ExportFilesMetadata](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-ExportFilesMetadata"></a>
Provides details about the stream session's exported files.
Type: [ExportFilesMetadata](API_ExportFilesMetadata.md) object

 ** [LastUpdatedAt](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-LastUpdatedAt"></a>
A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [Location](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-Location"></a>
The location where Amazon GameLift Streams hosts and streams your application. For example, `us-east-1`. For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9-]+`

 ** [LogFileLocationUri](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-LogFileLocationUri"></a>
Access location for log files that your content generates during a stream session. These log files are uploaded to cloud storage location at the end of a stream session. The Amazon GameLift Streams application resource defines which log files to upload.
Type: String

 ** [PerformanceStatsConfiguration](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-PerformanceStatsConfiguration"></a>
The performance stats configuration for the stream session
Type: [PerformanceStatsConfiguration](API_PerformanceStatsConfiguration.md) object

 ** [Protocol](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-Protocol"></a>
The data transfer protocol in use with the stream session.
Type: String
Valid Values: `WebRTC`

 ** [RoleArn](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-RoleArn"></a>
The ARN of the AWS Identity and Access Management (IAM) role that Amazon GameLift Streams assumes on behalf of your application during the stream session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:iam::\d{12}:role/.+`

 ** [SessionLengthSeconds](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-SessionLengthSeconds"></a>
The maximum duration of a session. Amazon GameLift Streams will automatically terminate a session after this amount of time has elapsed, regardless of any existing client connections.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.

 ** [SignalRequest](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-SignalRequest"></a>
The WebRTC ICE offer string that a client generates to initiate a connection to the stream session.
Type: String
Length Constraints: Minimum length of 1.

 ** [SignalResponse](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-SignalResponse"></a>
The WebRTC answer string that the stream server generates in response to the `SignalRequest`.
Type: String

 ** [Status](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-Status"></a>
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

 ** [StatusReason](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-StatusReason"></a>
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

 ** [StreamGroupId](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-StreamGroupId"></a>
The unique identifier for the Amazon GameLift Streams stream group that is hosting the stream session. Format example: `sg-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`

 ** [UserId](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-UserId"></a>
 An opaque, unique identifier for an end-user, defined by the developer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[-_a-zA-Z0-9/=+]*`

 ** [WebSdkProtocolUrl](#API_GetStreamSession_ResponseSyntax) **   <a name="gameliftstreams-GetStreamSession-response-WebSdkProtocolUrl"></a>
The URL of an S3 bucket that stores Amazon GameLift Streams WebSDK files. The URL is used to establish connection with the client.
Type: String

## Errors
<a name="API_GetStreamSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

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
<a name="API_GetStreamSession_Examples"></a>

### CLI Example
<a name="API_GetStreamSession_Example_1"></a>

The following example shows how to use the CLI to retrieve metadata for a stream session.

#### Sample Request
<a name="API_GetStreamSession_Example_1_Request"></a>

```
aws gameliftstreams get-stream-session \
    --identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4 \
    --stream-session-identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567
```

## See Also
<a name="API_GetStreamSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/GetStreamSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/GetStreamSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/GetStreamSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/GetStreamSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/GetStreamSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/GetStreamSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/GetStreamSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/GetStreamSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/GetStreamSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/GetStreamSession)
