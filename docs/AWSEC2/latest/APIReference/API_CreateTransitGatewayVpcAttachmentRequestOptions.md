---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayVpcAttachmentRequestOptions.html
---

# CreateTransitGatewayVpcAttachmentRequestOptions
<a name="API_CreateTransitGatewayVpcAttachmentRequestOptions"></a>

Describes the options for a VPC attachment.

## Contents
<a name="API_CreateTransitGatewayVpcAttachmentRequestOptions_Contents"></a>

 ** ApplianceModeSupport **
Enable or disable support for appliance mode. If enabled, a traffic flow between a source and destination uses the same Availability Zone for the VPC attachment for the lifetime of that flow. The default is `disable`.
Type: String
Valid Values: `enable | disable`
Required: No

 ** DnsSupport **
Enable or disable DNS support. The default is `enable`.
Type: String
Valid Values: `enable | disable`
Required: No

 ** Ipv6Support **
Specifies whether IPv6 support is enabled for the attachment. When enabled, the transit gateway network interface receives an IPv6 address. When you enable route propagation, IPv6 VPC CIDRs propagate to the transit gateway route tables. When disabled, the network interface does not receive an IPv6 address, and IPv6 routes do not propagate. The setting does not filter IPv6 traffic. The default is `disable`.
Type: String
Valid Values: `enable | disable`
Required: No

 ** SecurityGroupReferencingSupport **
Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management.
This option is set to `enable` by default. However, at the transit gateway level the default is set to `disable`.
For more information about security group referencing, see [Security group referencing ](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security) in the * AWS Transit Gateways Guide*.
Type: String
Valid Values: `enable | disable`
Required: No

## See Also
<a name="API_CreateTransitGatewayVpcAttachmentRequestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGatewayVpcAttachmentRequestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGatewayVpcAttachmentRequestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGatewayVpcAttachmentRequestOptions)
