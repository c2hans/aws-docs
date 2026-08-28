---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LocalGatewayRouteTableVpcAssociation.html
---

# LocalGatewayRouteTableVpcAssociation
<a name="API_LocalGatewayRouteTableVpcAssociation"></a>

Describes an association between a local gateway route table and a VPC.

## Contents
<a name="API_LocalGatewayRouteTableVpcAssociation_Contents"></a>

 ** localGatewayId **
The ID of the local gateway.
Type: String
Required: No

 ** localGatewayRouteTableArn **
The Amazon Resource Name (ARN) of the local gateway route table for the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** localGatewayRouteTableId **
The ID of the local gateway route table.
Type: String
Required: No

 ** localGatewayRouteTableVpcAssociationId **
The ID of the association.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the local gateway route table for the association.
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

 ** vpcId **
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_LocalGatewayRouteTableVpcAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LocalGatewayRouteTableVpcAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LocalGatewayRouteTableVpcAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LocalGatewayRouteTableVpcAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
