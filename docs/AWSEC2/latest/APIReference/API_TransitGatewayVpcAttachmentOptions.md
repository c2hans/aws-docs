---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayVpcAttachmentOptions.html
---

# TransitGatewayVpcAttachmentOptions
<a name="API_TransitGatewayVpcAttachmentOptions"></a>

Describes the VPC attachment options.

## Contents
<a name="API_TransitGatewayVpcAttachmentOptions_Contents"></a>

 ** applianceModeSupport **
Indicates whether appliance mode support is enabled.
Type: String
Valid Values: `enable | disable`
Required: No

 ** dnsSupport **
Indicates whether DNS support is enabled.
Type: String
Valid Values: `enable | disable`
Required: No

 ** ipv6Support **
Indicates whether IPv6 support is disabled.
Type: String
Valid Values: `enable | disable`
Required: No

 ** securityGroupReferencingSupport **
Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management.
This option is enabled by default.
For more information about security group referencing, see [Security group referencing](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security) in the * AWS Transit Gateways Guide*.
Type: String
Valid Values: `enable | disable`
Required: No

## See Also
<a name="API_TransitGatewayVpcAttachmentOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayVpcAttachmentOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayVpcAttachmentOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayVpcAttachmentOptions)
