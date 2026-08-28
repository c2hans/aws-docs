---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayOptions.html
---

# TransitGatewayOptions
<a name="API_TransitGatewayOptions"></a>

Describes the options for a transit gateway.

## Contents
<a name="API_TransitGatewayOptions_Contents"></a>

 ** amazonSideAsn **
A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs.
Type: Long
Required: No

 ** associationDefaultRouteTableId **
The ID of the default association route table.
Type: String
Required: No

 ** autoAcceptSharedAttachments **
Indicates whether attachment requests are automatically accepted.
Type: String
Valid Values: `enable | disable`
Required: No

 ** defaultRouteTableAssociation **
Indicates whether resource attachments are automatically associated with the default association route table. Enabled by default. Either `defaultRouteTableAssociation` or `defaultRouteTablePropagation` must be set to `enable` for AWS Transit Gateway to create the default transit gateway route table.
Type: String
Valid Values: `enable | disable`
Required: No

 ** defaultRouteTablePropagation **
Indicates whether resource attachments automatically propagate routes to the default propagation route table. Enabled by default. If `defaultRouteTablePropagation` is set to `enable`, AWS Transit Gateway creates the default transit gateway route table.
Type: String
Valid Values: `enable | disable`
Required: No

 ** dnsSupport **
Indicates whether DNS support is enabled.
Type: String
Valid Values: `enable | disable`
Required: No

 ** encryptionSupport **
Defines if the Transit Gateway supports VPC Encryption Control.
Type: [EncryptionSupport](API_EncryptionSupport.md) object
Required: No

 ** multicastSupport **
Indicates whether multicast is enabled on the transit gateway
Type: String
Valid Values: `enable | disable`
Required: No

 ** propagationDefaultRouteTableId **
The ID of the default propagation route table.
Type: String
Required: No

 ** securityGroupReferencingSupport **
Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management.
This option is disabled by default.
Type: String
Valid Values: `enable | disable`
Required: No

 ** TransitGatewayCidrBlocks.N **
The transit gateway CIDR blocks.
Type: Array of strings
Required: No

 ** vpnEcmpSupport **
Indicates whether Equal Cost Multipath Protocol support is enabled.
Type: String
Valid Values: `enable | disable`
Required: No

## See Also
<a name="API_TransitGatewayOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
