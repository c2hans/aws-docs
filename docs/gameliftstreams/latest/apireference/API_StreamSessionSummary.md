---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StreamSessionSummary.html
---

# StreamSessionSummary
<a name="API_StreamSessionSummary"></a>

Describes an Amazon GameLift Streams stream session. To retrieve additional details for the stream session, call [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html).

## Contents
<a name="API_StreamSessionSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApplicationArn **   <a name="gameliftstreams-Type-StreamSessionSummary-ApplicationArn"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`
Required: No

 ** Arn **   <a name="gameliftstreams-Type-StreamSessionSummary-Arn"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream session resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`
Required: No

 ** CreatedAt **   <a name="gameliftstreams-Type-StreamSessionSummary-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp
Required: No

 ** ExportFilesMetadata **   <a name="gameliftstreams-Type-StreamSessionSummary-ExportFilesMetadata"></a>
Provides details about the stream session's exported files.
Type: [ExportFilesMetadata](API_ExportFilesMetadata.md) object
Required: No

 ** LastUpdatedAt **   <a name="gameliftstreams-Type-StreamSessionSummary-LastUpdatedAt"></a>
A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp
Required: No

 ** Location **   <a name="gameliftstreams-Type-StreamSessionSummary-Location"></a>
The location where Amazon GameLift Streams hosts and streams your application. For example, `us-east-1`. For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** Protocol **   <a name="gameliftstreams-Type-StreamSessionSummary-Protocol"></a>
The data transfer protocol in use with the stream session.
Type: String
Valid Values: `WebRTC`
Required: No

 ** RoleArn **   <a name="gameliftstreams-Type-StreamSessionSummary-RoleArn"></a>
The ARN of the AWS Identity and Access Management (IAM) role that Amazon GameLift Streams assumes on behalf of your application during the stream session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:iam::\d{12}:role/.+`
Required: No

 ** Status **   <a name="gameliftstreams-Type-StreamSessionSummary-Status"></a>
The current status of the stream session resource.
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
Required: No

 ** StatusReason **   <a name="gameliftstreams-Type-StreamSessionSummary-StatusReason"></a>
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
Required: No

 ** UserId **   <a name="gameliftstreams-Type-StreamSessionSummary-UserId"></a>
 An opaque, unique identifier for an end-user, defined by the developer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[-_a-zA-Z0-9/=+]*`
Required: No

## See Also
<a name="API_StreamSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/StreamSessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/StreamSessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/StreamSessionSummary)
