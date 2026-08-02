---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGatewayOptions.html
---

# ModifyTransitGatewayOptions
<a name="API_ModifyTransitGatewayOptions"></a>

The transit gateway options.

## Contents
<a name="API_ModifyTransitGatewayOptions_Contents"></a>

 ** AddTransitGatewayCidrBlocks.N **
Adds IPv4 or IPv6 CIDR blocks for the transit gateway. Must be a size /24 CIDR block or larger for IPv4, or a size /64 CIDR block or larger for IPv6.
Type: Array of strings
Required: No

 ** AmazonSideAsn **
A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs.
The modify ASN operation is not allowed on a transit gateway if it has the following attachments:
+ Dynamic VPN
+ Static VPN
+ Direct Connect Gateway
+ Connect
+ VPN Concentrator
+ Client VPN
You must first delete all transit gateway attachments configured prior to modifying the ASN on the transit gateway.
Type: Long
Required: No

 ** AssociationDefaultRouteTableId **
The ID of the default association route table.
Type: String
Required: No

 ** AutoAcceptSharedAttachments **
Enable or disable automatic acceptance of attachment requests.
Type: String
Valid Values: `enable | disable`
Required: No

 ** DefaultRouteTableAssociation **
Enable or disable automatic association with the default association route table.
Type: String
Valid Values: `enable | disable`
Required: No

 ** DefaultRouteTablePropagation **
Indicates whether resource attachments automatically propagate routes to the default propagation route table. Enabled by default. If `defaultRouteTablePropagation` is set to `enable`, AWS Transit Gateway will create the default transit gateway route table.
Type: String
Valid Values: `enable | disable`
Required: No

 ** DnsSupport **
Enable or disable DNS support.
Type: String
Valid Values: `enable | disable`
Required: No

 ** EncryptionSupport **
Enable or disable encryption support for VPC Encryption Control.
Type: String
Valid Values: `enable | disable`
Required: No

 ** PropagationDefaultRouteTableId **
The ID of the default propagation route table.
Type: String
Required: No

 ** RemoveTransitGatewayCidrBlocks.N **
Removes CIDR blocks for the transit gateway.
Type: Array of strings
Required: No

 ** SecurityGroupReferencingSupport **
Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management.
This option is disabled by default.
For more information about security group referencing, see [Security group referencing](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security) in the * AWS Transit Gateways Guide*.
Type: String
Valid Values: `enable | disable`
Required: No

 ** VpnEcmpSupport **
Enable or disable Equal Cost Multipath Protocol support.
Type: String
Valid Values: `enable | disable`
Required: No

## See Also
<a name="API_ModifyTransitGatewayOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyTransitGatewayOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyTransitGatewayOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyTransitGatewayOptions)
