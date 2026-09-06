---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BridgeNetworkSource.html
---

# BridgeNetworkSource
<a name="API_BridgeNetworkSource"></a>

 The source of the bridge. A network source originates at your premises.

## Contents
<a name="API_BridgeNetworkSource_Contents"></a>

 ** multicastIp **   <a name="mediaconnect-Type-BridgeNetworkSource-multicastIp"></a>
 The network source multicast IP.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-BridgeNetworkSource-name"></a>
 The name of the network source.
Type: String
Required: Yes

 ** networkName **   <a name="mediaconnect-Type-BridgeNetworkSource-networkName"></a>
 The network source's gateway network name.
Type: String
Required: Yes

 ** port **   <a name="mediaconnect-Type-BridgeNetworkSource-port"></a>
 The network source port.
Type: Integer
Required: Yes

 ** protocol **   <a name="mediaconnect-Type-BridgeNetworkSource-protocol"></a>
 The network source protocol.
 AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
Type: String
Valid Values: `zixi-push | rtp-fec | rtp | zixi-pull | rist | st2110-jpegxs | cdi | srt-listener | srt-caller | fujitsu-qos | udp | ndi-speed-hq`
Required: Yes

 ** multicastSourceSettings **   <a name="mediaconnect-Type-BridgeNetworkSource-multicastSourceSettings"></a>
The settings related to the multicast source.
Type: [MulticastSourceSettings](API_MulticastSourceSettings.md) object
Required: No

## See Also
<a name="API_BridgeNetworkSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BridgeNetworkSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BridgeNetworkSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BridgeNetworkSource)
