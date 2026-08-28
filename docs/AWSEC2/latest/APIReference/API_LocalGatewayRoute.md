---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LocalGatewayRoute.html
---

# LocalGatewayRoute
<a name="API_LocalGatewayRoute"></a>

Describes a route for a local gateway route table.

## Contents
<a name="API_LocalGatewayRoute_Contents"></a>

 ** coipPoolId **
The ID of the customer-owned address pool.
Type: String
Required: No

 ** destinationCidrBlock **
The CIDR block used for destination matches.
Type: String
Required: No

 ** destinationPrefixListId **
 The ID of the prefix list.
Type: String
Required: No

 ** localGatewayRouteTableArn **
The Amazon Resource Name (ARN) of the local gateway route table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** localGatewayRouteTableId **
The ID of the local gateway route table.
Type: String
Required: No

 ** localGatewayVirtualInterfaceGroupId **
The ID of the virtual interface group.
Type: String
Required: No

 ** networkInterfaceId **
The ID of the network interface.
Type: String
Required: No

 ** ownerId **
The ID of the AWS account that owns the local gateway route.
Type: String
Required: No

 ** state **
The state of the route.
Type: String
Valid Values: `pending | active | blackhole | deleting | deleted`
Required: No

 ** subnetId **
The ID of the subnet.
Type: String
Required: No

 ** type **
The route type.
Type: String
Valid Values: `static | propagated`
Required: No

## See Also
<a name="API_LocalGatewayRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LocalGatewayRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LocalGatewayRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LocalGatewayRoute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
