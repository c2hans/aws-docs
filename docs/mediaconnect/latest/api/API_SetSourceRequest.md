---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SetSourceRequest.html
---

# SetSourceRequest
<a name="API_SetSourceRequest"></a>

 The settings for the source of the flow.

## Contents
<a name="API_SetSourceRequest_Contents"></a>

 ** decryption **   <a name="mediaconnect-Type-SetSourceRequest-decryption"></a>
 The type of encryption that is used on the content ingested from this source. Allowable encryption types: static-key.
Type: [Encryption](API_Encryption.md) object
Required: No

 ** description **   <a name="mediaconnect-Type-SetSourceRequest-description"></a>
 A description for the source. This value is not used or seen outside of the current MediaConnect account.
Type: String
Required: No

 ** entitlementArn **   <a name="mediaconnect-Type-SetSourceRequest-entitlementArn"></a>
 The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator's flow.
Type: String
Pattern: `arn:.+:mediaconnect.+:entitlement:.+`
Required: No

 ** gatewayBridgeSource **   <a name="mediaconnect-Type-SetSourceRequest-gatewayBridgeSource"></a>
 The source configuration for cloud flows receiving a stream from a bridge.
Type: [SetGatewayBridgeSourceRequest](API_SetGatewayBridgeSourceRequest.md) object
Required: No

 ** ingestPort **   <a name="mediaconnect-Type-SetSourceRequest-ingestPort"></a>
 The port that the flow will be listening on for incoming content.
Type: Integer
Required: No

 ** maxBitrate **   <a name="mediaconnect-Type-SetSourceRequest-maxBitrate"></a>
 The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams.
Type: Integer
Required: No

 ** maxLatency **   <a name="mediaconnect-Type-SetSourceRequest-maxLatency"></a>
 The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Type: Integer
Required: No

 ** maxSyncBuffer **   <a name="mediaconnect-Type-SetSourceRequest-maxSyncBuffer"></a>
 The size of the buffer (in milliseconds) to use to sync incoming source data.
Type: Integer
Required: No

 ** mediaStreamSourceConfigurations **   <a name="mediaconnect-Type-SetSourceRequest-mediaStreamSourceConfigurations"></a>
 The media streams that are associated with the source, and the parameters for those associations.
Type: Array of [MediaStreamSourceConfigurationRequest](API_MediaStreamSourceConfigurationRequest.md) objects
Required: No

 ** minLatency **   <a name="mediaconnect-Type-SetSourceRequest-minLatency"></a>
 The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
Type: Integer
Required: No

 ** name **   <a name="mediaconnect-Type-SetSourceRequest-name"></a>
 The name of the source.
Type: String
Required: No

 ** ndiSourceSettings **   <a name="mediaconnect-Type-SetSourceRequest-ndiSourceSettings"></a>
 The settings for the NDI® source. This includes the exact name of the upstream NDI sender that you want to connect to your source.
Type: [NdiSourceSettings](API_NdiSourceSettings.md) object
Required: No

 ** protocol **   <a name="mediaconnect-Type-SetSourceRequest-protocol"></a>
 The protocol that is used by the source.
 AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
Type: String
Valid Values: `zixi-push | rtp-fec | rtp | zixi-pull | rist | st2110-jpegxs | cdi | srt-listener | srt-caller | fujitsu-qos | udp | ndi-speed-hq`
Required: No

 ** routerIntegrationState **   <a name="mediaconnect-Type-SetSourceRequest-routerIntegrationState"></a>
Indicates whether to enable or disable router integration when setting a flow source.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** routerIntegrationTransitDecryption **   <a name="mediaconnect-Type-SetSourceRequest-routerIntegrationTransitDecryption"></a>
The decryption configuration for the flow source when router integration is enabled. Specifies how the source content should be decrypted when router integration is used.
Type: [FlowTransitEncryption](API_FlowTransitEncryption.md) object
Required: No

 ** senderControlPort **   <a name="mediaconnect-Type-SetSourceRequest-senderControlPort"></a>
 The port that the flow uses to send outbound requests to initiate connection with the sender.
Type: Integer
Required: No

 ** senderIpAddress **   <a name="mediaconnect-Type-SetSourceRequest-senderIpAddress"></a>
 The IP address that the flow communicates with to initiate connection with the sender.
Type: String
Required: No

 ** sourceListenerAddress **   <a name="mediaconnect-Type-SetSourceRequest-sourceListenerAddress"></a>
 Source IP or domain name for SRT-caller protocol.
Type: String
Required: No

 ** sourceListenerPort **   <a name="mediaconnect-Type-SetSourceRequest-sourceListenerPort"></a>
 Source port for SRT-caller protocol.
Type: Integer
Required: No

 ** sourceTags **   <a name="mediaconnect-Type-SetSourceRequest-sourceTags"></a>
 The key-value pairs that can be used to tag and organize the source.
Type: String to string map
Required: No

 ** streamId **   <a name="mediaconnect-Type-SetSourceRequest-streamId"></a>
 The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
Type: String
Required: No

 ** vpcInterfaceName **   <a name="mediaconnect-Type-SetSourceRequest-vpcInterfaceName"></a>
 The name of the VPC interface to use for this source.
Type: String
Required: No

 ** whitelistCidr **   <a name="mediaconnect-Type-SetSourceRequest-whitelistCidr"></a>
 The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
Type: String
Required: No

## See Also
<a name="API_SetSourceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SetSourceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SetSourceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SetSourceRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
