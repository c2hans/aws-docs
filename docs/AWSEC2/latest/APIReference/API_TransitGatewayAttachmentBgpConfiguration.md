---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayAttachmentBgpConfiguration.html
---

# TransitGatewayAttachmentBgpConfiguration
<a name="API_TransitGatewayAttachmentBgpConfiguration"></a>

The BGP configuration information.

## Contents
<a name="API_TransitGatewayAttachmentBgpConfiguration_Contents"></a>

 ** bgpStatus **
The BGP status.
Type: String
Valid Values: `up | down`
Required: No

 ** peerAddress **
The interior BGP peer IP address for the appliance.
Type: String
Required: No

 ** peerAsn **
The peer Autonomous System Number (ASN).
Type: Long
Required: No

 ** transitGatewayAddress **
The interior BGP peer IP address for the transit gateway.
Type: String
Required: No

 ** transitGatewayAsn **
The transit gateway Autonomous System Number (ASN).
Type: Long
Required: No

## See Also
<a name="API_TransitGatewayAttachmentBgpConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayAttachmentBgpConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayAttachmentBgpConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayAttachmentBgpConfiguration)
