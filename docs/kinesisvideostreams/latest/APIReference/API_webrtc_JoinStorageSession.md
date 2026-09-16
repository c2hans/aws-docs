---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_webrtc_JoinStorageSession.html
---

# JoinStorageSession
<a name="API_webrtc_JoinStorageSession"></a>

**Note**
Before using this API, you must call the `GetSignalingChannelEndpoint` API to request the WEBRTC endpoint. You then specify the endpoint and region in your `JoinStorageSession` API request.

Join the ongoing one way-video and/or multi-way audio WebRTC session as a video producing device for an input channel. If there's not an existing session for the channel, create a new streaming session and provide the Amazon Resource Name (ARN) of the signaling channel.

Currently for the `SINGLE_MASTER` type, a video producing device is able to ingest both audio and video media into a stream. Only video producing devices can join the session and record media.

**Important**
Both audio and video tracks are currently required for WebRTC ingestion.
Current requirements:
Video track: H.264
Audio track: Opus
Video:
Max resolution is SQFHD (1920x1920)
KVS WebRTC ingestion currently supports a specific set of H264 profiles:
constrained-baseline
baseline
main
high
constrained-high
progressive-high

The resulting ingested video in the Kinesis video stream will have the following parameters: H.264 video and AAC audio.

Once a master participant has negotiated a connection through WebRTC, the ingested media session will be stored in the Kinesis video stream. Multiple viewers are then able to play back real-time media through our Playback APIs.

You can also use existing Kinesis Video Streams features like `HLS` or `DASH` playback, image generation via [GetImages](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-getImages.html), and more with ingested WebRTC media.

**Note**
S3 image delivery and notifications are not currently supported.

**Note**
Assume that only one video producing device client can be associated with a session for the channel. If more than one client joins the session of a specific channel as a video producing device, the most recent client request takes precedence.

 **Additional information**
+  **Idempotent** - This API is not idempotent.
+  **Retry behavior** - This is counted as a new API call.
+  **Concurrent calls** - Concurrent calls are allowed. An offer is sent once per each call.

## Request Syntax
<a name="API_webrtc_JoinStorageSession_RequestSyntax"></a>

```
POST /joinStorageSession HTTP/1.1
Content-type: application/json

{
   "channelArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_webrtc_JoinStorageSession_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_webrtc_JoinStorageSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelArn](#API_webrtc_JoinStorageSession_RequestSyntax) **   <a name="KinesisVideo-webrtc_JoinStorageSession-request-channelArn"></a>
 The Amazon Resource Name (ARN) of the signaling channel.
Note the capitalization of this input parameter.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: Yes

## Response Syntax
<a name="API_webrtc_JoinStorageSession_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_webrtc_JoinStorageSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_webrtc_JoinStorageSession_Errors"></a>

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
<a name="API_webrtc_JoinStorageSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-video-webrtc-storage-2018-05-10/JoinStorageSession)
