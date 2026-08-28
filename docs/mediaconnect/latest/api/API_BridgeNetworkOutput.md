---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BridgeNetworkOutput.html
---

# BridgeNetworkOutput
<a name="API_BridgeNetworkOutput"></a>

 The output of the bridge. A network output is delivered to your premises.

## Contents
<a name="API_BridgeNetworkOutput_Contents"></a>

 ** ipAddress **   <a name="mediaconnect-Type-BridgeNetworkOutput-ipAddress"></a>
 The network output IP address.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-BridgeNetworkOutput-name"></a>
 The network output name.
Type: String
Required: Yes

 ** networkName **   <a name="mediaconnect-Type-BridgeNetworkOutput-networkName"></a>
 The network output's gateway network name.
Type: String
Required: Yes

 ** port **   <a name="mediaconnect-Type-BridgeNetworkOutput-port"></a>
 The network output's port.
Type: Integer
Required: Yes

 ** protocol **   <a name="mediaconnect-Type-BridgeNetworkOutput-protocol"></a>
 The network output protocol.
 AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
Type: String
Valid Values: `zixi-push | rtp-fec | rtp | zixi-pull | rist | st2110-jpegxs | cdi | srt-listener | srt-caller | fujitsu-qos | udp | ndi-speed-hq`
Required: Yes

 ** ttl **   <a name="mediaconnect-Type-BridgeNetworkOutput-ttl"></a>
 The network output TTL.
Type: Integer
Required: Yes

## See Also
<a name="API_BridgeNetworkOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BridgeNetworkOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BridgeNetworkOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BridgeNetworkOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
