---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_webrtc_JoinStorageSessionAsViewer.html
---

# JoinStorageSessionAsViewer
<a name="API_webrtc_JoinStorageSessionAsViewer"></a>

**Note**
Before using this API, you must call the `GetSignalingChannelEndpoint` API to request the WEBRTC endpoint. You then specify the endpoint and region in your `JoinStorageSessionAsViewer` API request.

 `JoinStorageSessionAsViewer` enables a viewer to join an ongoing cloud-recorded WebRTC streaming session. This API initiates a WebRTC connection by sending an SDP offer and ICE candidates between the viewer and the recording agent, allowing the viewer to receive real-time video from the master through the recording agent and participate in two-way audio communication through the recording agent. Once connected, the viewer's audio, if provided, is forwarded to all other connected peers, including the master participant, and is incorporated into the WebRTC stream being saved to the Kinesis Video stream.

**Important**
Viewers currently can't send any video tracks. Viewers can send an optional audio track or no tracks at all.
Current viewer participant sending requirements:
Video track: Not supported
Audio track (optional): Opus

If the master participant is currently connected to the video producing device, the resulting ingested video in the Kinesis video stream will have the following parameters: H.264 video and AAC audio.

**Note**
Viewer participants connect directly to the storage session and not directly to the master participant. The storage session takes care of mixing, duplicating, and routing the media to the appropriate destination.

**Note**
If the master participant isn't present, viewers won't be able to hear each other.

Once the viewer participant has negotiated a connection through WebRTC, the ingested audio session will be stored in the Kinesis video stream as long as the master participant is also connected to the storage session.

You can also use existing Kinesis Video Streams features like `HLS` or `DASH` playback, image generation via [GetImages](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-getImages.html), and more with ingested WebRTC media.

**Note**
S3 image delivery and notifications are not currently supported.

**Note**
Assume that only one video producing device client can be associated with a session for the channel. If more than one client joins the session of a specific channel as a video producing device, the most recent client request takes precedence.

 **Limits**

The current limits are in place:
+  **Maximum number of viewers:** 3
+  **Maximum time viewer participants remain connected to the storage session without a master participant present:** 3 minutes

**Important**
If a viewer disconnects from the storage session (closes the peer connection), their quota (viewer limit) remains consumed for 1 minute. During this 1-minute period, the viewer can invoke this API with the same Client ID to rejoin the session without consuming an additional viewer quota. After 1 minute, the viewer quota is released and available for other viewers to join.

 **Additional information**
+  **Idempotent** - This API is not idempotent.
+  **Retry behavior** - This is counted as a new API call.
+  **Concurrent calls** - Concurrent calls are allowed. An offer is sent once per each call.

## Request Syntax
<a name="API_webrtc_JoinStorageSessionAsViewer_RequestSyntax"></a>

```
POST /joinStorageSessionAsViewer HTTP/1.1
Content-type: application/json

{
   "channelArn": "{{string}}",
   "clientId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_webrtc_JoinStorageSessionAsViewer_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_webrtc_JoinStorageSessionAsViewer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelArn](#API_webrtc_JoinStorageSessionAsViewer_RequestSyntax) **   <a name="KinesisVideo-webrtc_JoinStorageSessionAsViewer-request-channelArn"></a>
The Amazon Resource Name (ARN) of the signaling channel.
Note the capitalization of this input parameter.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: Yes

 ** [clientId](#API_webrtc_JoinStorageSessionAsViewer_RequestSyntax) **   <a name="KinesisVideo-webrtc_JoinStorageSessionAsViewer-request-clientId"></a>
 The unique identifier for the sender client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_webrtc_JoinStorageSessionAsViewer_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_webrtc_JoinStorageSessionAsViewer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_webrtc_JoinStorageSessionAsViewer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have required permissions to perform this operation.
HTTP Status Code: 403

 ** ClientLimitExceededException **
 Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.
HTTP Status Code: 400

 ** InvalidArgumentException **
The value for this input parameter is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource is not found.
HTTP Status Code: 404

## See Also
<a name="API_webrtc_JoinStorageSessionAsViewer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSessionAsViewer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSessionAsViewer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSessionAsViewer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSessionAsViewer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSessionAsViewer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSessionAsViewer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSessionAsViewer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSessionAsViewer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSessionAsViewer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSessionAsViewer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
