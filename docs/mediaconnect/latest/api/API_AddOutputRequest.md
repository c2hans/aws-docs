---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddOutputRequest.html
---

# AddOutputRequest
<a name="API_AddOutputRequest"></a>

 A request to add an output to a flow.

## Contents
<a name="API_AddOutputRequest_Contents"></a>

 ** cidrAllowList **   <a name="mediaconnect-Type-AddOutputRequest-cidrAllowList"></a>
 The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
Type: Array of strings
Required: No

 ** description **   <a name="mediaconnect-Type-AddOutputRequest-description"></a>
 A description of the output. This description appears only on the Audit Manager console and will not be seen by the end user.
Type: String
Required: No

 ** destination **   <a name="mediaconnect-Type-AddOutputRequest-destination"></a>
 The IP address from which video will be sent to output destinations.
Type: String
Required: No

 ** encryption **   <a name="mediaconnect-Type-AddOutputRequest-encryption"></a>
 The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.
Type: [Encryption](API_Encryption.md) object
Required: No

 ** maxLatency **   <a name="mediaconnect-Type-AddOutputRequest-maxLatency"></a>
 The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Type: Integer
Required: No

 ** mediaStreamOutputConfigurations **   <a name="mediaconnect-Type-AddOutputRequest-mediaStreamOutputConfigurations"></a>
 The media streams that are associated with the output, and the parameters for those associations.
Type: Array of [MediaStreamOutputConfigurationRequest](API_MediaStreamOutputConfigurationRequest.md) objects
Required: No

 ** minLatency **   <a name="mediaconnect-Type-AddOutputRequest-minLatency"></a>
 The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
Type: Integer
Required: No

 ** name **   <a name="mediaconnect-Type-AddOutputRequest-name"></a>
 The name of the output. This value must be unique within the current flow.
Type: String
Required: No

 ** ndiOutputTimecodeSource **   <a name="mediaconnect-Type-AddOutputRequest-ndiOutputTimecodeSource"></a>
Controls how MediaConnect generates timecodes for NDI output frames. If you don't specify this field, MediaConnect uses `EMBEDDED_TIMECODE`.
+  `EMBEDDED_TIMECODE` (default) - Preserves timecodes from the input transport stream. The timecodes must be embedded in the video stream as SEI timing messages. If no embedded timecode is detected, MediaConnect uses the UTC system time instead.
+  `UTC_SYSTEM_TIME` - Generates timecodes based on the system clock time when each frame is sent.
Type: String
Valid Values: `EMBEDDED_TIMECODE | UTC_SYSTEM_TIME`
Required: No

 ** ndiProgramName **   <a name="mediaconnect-Type-AddOutputRequest-ndiProgramName"></a>
 A suffix for the name of the NDI® sender that the flow creates. If a custom name isn't specified, MediaConnect uses the output name.
Type: String
Required: No

 ** ndiSpeedHqQuality **   <a name="mediaconnect-Type-AddOutputRequest-ndiSpeedHqQuality"></a>
A quality setting for the NDI Speed HQ encoder.
Type: Integer
Required: No

 ** outputStatus **   <a name="mediaconnect-Type-AddOutputRequest-outputStatus"></a>
 An indication of whether the new output should be enabled or disabled as soon as it is created. If you don't specify the outputStatus field in your request, MediaConnect sets it to ENABLED.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** outputTags **   <a name="mediaconnect-Type-AddOutputRequest-outputTags"></a>
 The key-value pairs that can be used to tag and organize the output.
Type: String to string map
Required: No

 ** port **   <a name="mediaconnect-Type-AddOutputRequest-port"></a>
 The port to use when content is distributed to this output.
Type: Integer
Required: No

 ** protocol **   <a name="mediaconnect-Type-AddOutputRequest-protocol"></a>
 The protocol to use for the output.
 AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
Type: String
Valid Values: `zixi-push | rtp-fec | rtp | zixi-pull | rist | st2110-jpegxs | cdi | srt-listener | srt-caller | fujitsu-qos | udp | ndi-speed-hq`
Required: No

 ** remoteId **   <a name="mediaconnect-Type-AddOutputRequest-remoteId"></a>
 The remote ID for the Zixi-pull output stream.
Type: String
Required: No

 ** routerIntegrationState **   <a name="mediaconnect-Type-AddOutputRequest-routerIntegrationState"></a>
Indicates whether to enable or disable router integration when creating a new flow output.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** routerIntegrationTransitEncryption **   <a name="mediaconnect-Type-AddOutputRequest-routerIntegrationTransitEncryption"></a>
The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.
Type: [FlowTransitEncryption](API_FlowTransitEncryption.md) object
Required: No

 ** senderControlPort **   <a name="mediaconnect-Type-AddOutputRequest-senderControlPort"></a>
 The port that the flow uses to send outbound requests to initiate connection with the sender.
Type: Integer
Required: No

 ** smoothingLatency **   <a name="mediaconnect-Type-AddOutputRequest-smoothingLatency"></a>
 The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
Type: Integer
Required: No

 ** streamId **   <a name="mediaconnect-Type-AddOutputRequest-streamId"></a>
 The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
Type: String
Required: No

 ** vpcInterfaceAttachment **   <a name="mediaconnect-Type-AddOutputRequest-vpcInterfaceAttachment"></a>
 The name of the VPC interface attachment to use for this output.
Type: [VpcInterfaceAttachment](API_VpcInterfaceAttachment.md) object
Required: No

## See Also
<a name="API_AddOutputRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/AddOutputRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/AddOutputRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/AddOutputRequest)
