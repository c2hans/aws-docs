---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LocalGatewayRouteTableVirtualInterfaceGroupAssociation.html
---

# LocalGatewayRouteTableVirtualInterfaceGroupAssociation
<a name="API_LocalGatewayRouteTableVirtualInterfaceGroupAssociation"></a>

Describes an association between a local gateway route table and a virtual interface group.

## Contents
<a name="API_LocalGatewayRouteTableVirtualInterfaceGroupAssociation_Contents"></a>

 ** localGatewayId **
The ID of the local gateway.
Type: String
Required: No

 ** localGatewayRouteTableArn **
The Amazon Resource Name (ARN) of the local gateway route table for the virtual interface group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** localGatewayRouteTableId **
The ID of the local gateway route table.
Type: String
Required: No

 ** localGatewayRouteTableVirtualInterfaceGroupAssociationId **
The ID of the association.
Type: String
Required: No

 ** localGatewayVirtualInterfaceGroupId **
The ID of the virtual interface group.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the local gateway virtual interface group association.
Type: String
Required: No

 ** state **
The state of the association.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the association.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_LocalGatewayRouteTableVirtualInterfaceGroupAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LocalGatewayRouteTableVirtualInterfaceGroupAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LocalGatewayRouteTableVirtualInterfaceGroupAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LocalGatewayRouteTableVirtualInterfaceGroupAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
