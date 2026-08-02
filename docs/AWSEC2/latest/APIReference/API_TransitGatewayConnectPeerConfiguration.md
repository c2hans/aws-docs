---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayConnectPeerConfiguration.html
---

# TransitGatewayConnectPeerConfiguration
<a name="API_TransitGatewayConnectPeerConfiguration"></a>

Describes the Connect peer details.

## Contents
<a name="API_TransitGatewayConnectPeerConfiguration_Contents"></a>

 ** BgpConfigurations.N **
The BGP configuration details.
Type: Array of [TransitGatewayAttachmentBgpConfiguration](API_TransitGatewayAttachmentBgpConfiguration.md) objects
Required: No

 ** InsideCidrBlocks.N **
The range of interior BGP peer IP addresses.
Type: Array of strings
Required: No

 ** peerAddress **
The Connect peer IP address on the appliance side of the tunnel.
Type: String
Required: No

 ** protocol **
The tunnel protocol.
Type: String
Valid Values: `gre`
Required: No

 ** transitGatewayAddress **
The Connect peer IP address on the transit gateway side of the tunnel.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayConnectPeerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayConnectPeerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayConnectPeerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayConnectPeerConfiguration)
