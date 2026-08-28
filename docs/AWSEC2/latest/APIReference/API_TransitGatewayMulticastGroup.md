---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayMulticastGroup.html
---

# TransitGatewayMulticastGroup
<a name="API_TransitGatewayMulticastGroup"></a>

Describes the transit gateway multicast group resources.

## Contents
<a name="API_TransitGatewayMulticastGroup_Contents"></a>

 ** groupIpAddress **
The IP address assigned to the transit gateway multicast group.
Type: String
Required: No

 ** groupMember **
Indicates that the resource is a transit gateway multicast group member.
Type: Boolean
Required: No

 ** groupSource **
Indicates that the resource is a transit gateway multicast group member.
Type: Boolean
Required: No

 ** memberType **
The member type (for example, `static`).
Type: String
Valid Values: `static | igmp`
Required: No

 ** networkInterfaceId **
The ID of the transit gateway attachment.
Type: String
Required: No

 ** resourceId **
The ID of the resource.
Type: String
Required: No

 ** resourceOwnerId **
 The ID of the AWS account that owns the transit gateway multicast domain group resource.
Type: String
Required: No

 ** resourceType **
The type of resource, for example a VPC attachment.
Type: String
Valid Values: `vpc | vpn | vpn-concentrator | direct-connect-gateway | connect | peering | tgw-peering | client-vpn`
Required: No

 ** sourceType **
The source type.
Type: String
Valid Values: `static | igmp`
Required: No

 ** subnetId **
The ID of the subnet.
Type: String
Required: No

 ** transitGatewayAttachmentId **
The ID of the transit gateway attachment.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayMulticastGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayMulticastGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayMulticastGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayMulticastGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
