---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddBridgeNetworkOutputRequest.html
---

# AddBridgeNetworkOutputRequest
<a name="API_AddBridgeNetworkOutputRequest"></a>

Add a network output to an existing bridge.

## Contents
<a name="API_AddBridgeNetworkOutputRequest_Contents"></a>

 ** ipAddress **   <a name="mediaconnect-Type-AddBridgeNetworkOutputRequest-ipAddress"></a>
 The network output IP Address.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-AddBridgeNetworkOutputRequest-name"></a>
 The network output name. This name is used to reference the output and must be unique among outputs in this bridge.
Type: String
Required: Yes

 ** networkName **   <a name="mediaconnect-Type-AddBridgeNetworkOutputRequest-networkName"></a>
 The network output's gateway network name.
Type: String
Required: Yes

 ** port **   <a name="mediaconnect-Type-AddBridgeNetworkOutputRequest-port"></a>
 The network output port.
Type: Integer
Required: Yes

 ** protocol **   <a name="mediaconnect-Type-AddBridgeNetworkOutputRequest-protocol"></a>
 The network output protocol.
 AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
Type: String
Valid Values: `zixi-push | rtp-fec | rtp | zixi-pull | rist | st2110-jpegxs | cdi | srt-listener | srt-caller | fujitsu-qos | udp | ndi-speed-hq`
Required: Yes

 ** ttl **   <a name="mediaconnect-Type-AddBridgeNetworkOutputRequest-ttl"></a>
 The network output TTL.
Type: Integer
Required: Yes

## See Also
<a name="API_AddBridgeNetworkOutputRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/AddBridgeNetworkOutputRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/AddBridgeNetworkOutputRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/AddBridgeNetworkOutputRequest)
