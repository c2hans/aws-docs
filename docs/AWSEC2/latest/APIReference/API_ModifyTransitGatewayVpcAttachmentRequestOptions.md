---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGatewayVpcAttachmentRequestOptions.html
---

# ModifyTransitGatewayVpcAttachmentRequestOptions
<a name="API_ModifyTransitGatewayVpcAttachmentRequestOptions"></a>

Describes the options for a VPC attachment.

## Contents
<a name="API_ModifyTransitGatewayVpcAttachmentRequestOptions_Contents"></a>

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
Specifies whether IPv6 support is enabled for the attachment. When enabled, the transit gateway network interface receives an IPv6 address. When you enable route propagation, IPv6 VPC CIDRs propagate to the transit gateway route tables. When disabled, the network interface does not receive an IPv6 address, and IPv6 routes do not propagate. The setting does not filter IPv6 traffic.
Type: String
Valid Values: `enable | disable`
Required: No

 ** SecurityGroupReferencingSupport **
Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management.
This option is disabled by default.
For more information about security group referencing, see [Security group referencing](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security) in the * AWS Transit Gateways Guide*.
Type: String
Valid Values: `enable | disable`
Required: No

## See Also
<a name="API_ModifyTransitGatewayVpcAttachmentRequestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyTransitGatewayVpcAttachmentRequestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyTransitGatewayVpcAttachmentRequestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyTransitGatewayVpcAttachmentRequestOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
