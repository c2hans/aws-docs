---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Transport.html
---

# Transport
<a name="API_Transport"></a>

 Attributes related to the transport stream that are used in a source or output.

## Contents
<a name="API_Transport_Contents"></a>

 ** protocol **   <a name="mediaconnect-Type-Transport-protocol"></a>
 The protocol that is used by the source or output.
 AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
Type: String
Valid Values: `zixi-push | rtp-fec | rtp | zixi-pull | rist | st2110-jpegxs | cdi | srt-listener | srt-caller | fujitsu-qos | udp | ndi-speed-hq`
Required: Yes

 ** cidrAllowList **   <a name="mediaconnect-Type-Transport-cidrAllowList"></a>
 The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16
Type: Array of strings
Required: No

 ** maxBitrate **   <a name="mediaconnect-Type-Transport-maxBitrate"></a>
 The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams.
Type: Integer
Required: No

 ** maxLatency **   <a name="mediaconnect-Type-Transport-maxLatency"></a>
 The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Type: Integer
Required: No

 ** maxSyncBuffer **   <a name="mediaconnect-Type-Transport-maxSyncBuffer"></a>
 The size of the buffer (in milliseconds) to use to sync incoming source data.
Type: Integer
Required: No

 ** minLatency **   <a name="mediaconnect-Type-Transport-minLatency"></a>
 The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
Type: Integer
Required: No

 ** ndiOutputTimecodeSource **   <a name="mediaconnect-Type-Transport-ndiOutputTimecodeSource"></a>
The timecode source for NDI output frames. For NDI outputs, this field is always present and defaults to `EMBEDDED_TIMECODE`.
+  `EMBEDDED_TIMECODE` - Preserves timecodes from the input transport stream. The timecodes must be embedded in the video stream as SEI timing messages. If no embedded timecode is detected, MediaConnect uses the UTC system time instead.
+  `UTC_SYSTEM_TIME` - Generates timecodes based on the system clock time when each frame is sent.
Type: String
Valid Values: `EMBEDDED_TIMECODE | UTC_SYSTEM_TIME`
Required: No

 ** ndiProgramName **   <a name="mediaconnect-Type-Transport-ndiProgramName"></a>
A suffix for the name of the NDI® sender that the flow creates. If a custom name isn't specified, MediaConnect uses the output name.
Type: String
Required: No

 ** ndiSourceSettings **   <a name="mediaconnect-Type-Transport-ndiSourceSettings"></a>
 The settings for the NDI source. This includes the exact name of the upstream NDI sender that you want to connect to your source.
Type: [NdiSourceSettings](API_NdiSourceSettings.md) object
Required: No

 ** ndiSpeedHqQuality **   <a name="mediaconnect-Type-Transport-ndiSpeedHqQuality"></a>
A quality setting for the NDI Speed HQ encoder.
Type: Integer
Required: No

 ** remoteId **   <a name="mediaconnect-Type-Transport-remoteId"></a>
 The remote ID for the Zixi-pull stream.
Type: String
Required: No

 ** senderControlPort **   <a name="mediaconnect-Type-Transport-senderControlPort"></a>
 The port that the flow uses to send outbound requests to initiate connection with the sender.
Type: Integer
Required: No

 ** senderIpAddress **   <a name="mediaconnect-Type-Transport-senderIpAddress"></a>
 The IP address that the flow communicates with to initiate connection with the sender.
Type: String
Required: No

 ** smoothingLatency **   <a name="mediaconnect-Type-Transport-smoothingLatency"></a>
 The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
Type: Integer
Required: No

 ** sourceListenerAddress **   <a name="mediaconnect-Type-Transport-sourceListenerAddress"></a>
 Source IP or domain name for SRT-caller protocol.
Type: String
Required: No

 ** sourceListenerPort **   <a name="mediaconnect-Type-Transport-sourceListenerPort"></a>
 Source port for SRT-caller protocol.
Type: Integer
Required: No

 ** streamId **   <a name="mediaconnect-Type-Transport-streamId"></a>
 The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
Type: String
Required: No

## See Also
<a name="API_Transport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Transport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Transport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Transport)
