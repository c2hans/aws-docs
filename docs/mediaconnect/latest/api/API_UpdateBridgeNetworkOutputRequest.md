---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateBridgeNetworkOutputRequest.html
---

# UpdateBridgeNetworkOutputRequest
<a name="API_UpdateBridgeNetworkOutputRequest"></a>

Update an existing network output.

## Contents
<a name="API_UpdateBridgeNetworkOutputRequest_Contents"></a>

 ** ipAddress **   <a name="mediaconnect-Type-UpdateBridgeNetworkOutputRequest-ipAddress"></a>
The network output IP Address.
Type: String
Required: No

 ** networkName **   <a name="mediaconnect-Type-UpdateBridgeNetworkOutputRequest-networkName"></a>
The network output's gateway network name.
Type: String
Required: No

 ** port **   <a name="mediaconnect-Type-UpdateBridgeNetworkOutputRequest-port"></a>
The network output port.
Type: Integer
Required: No

 ** protocol **   <a name="mediaconnect-Type-UpdateBridgeNetworkOutputRequest-protocol"></a>
The network output protocol.
 AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
Type: String
Valid Values: `zixi-push | rtp-fec | rtp | zixi-pull | rist | st2110-jpegxs | cdi | srt-listener | srt-caller | fujitsu-qos | udp | ndi-speed-hq`
Required: No

 ** ttl **   <a name="mediaconnect-Type-UpdateBridgeNetworkOutputRequest-ttl"></a>
The network output TTL.
Type: Integer
Required: No

## See Also
<a name="API_UpdateBridgeNetworkOutputRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateBridgeNetworkOutputRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateBridgeNetworkOutputRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateBridgeNetworkOutputRequest)
