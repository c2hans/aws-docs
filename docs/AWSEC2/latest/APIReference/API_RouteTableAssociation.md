---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RouteTableAssociation.html
---

# RouteTableAssociation
<a name="API_RouteTableAssociation"></a>

Describes an association between a route table and a subnet or gateway.

## Contents
<a name="API_RouteTableAssociation_Contents"></a>

 ** associationState **
The state of the association.
Type: [RouteTableAssociationState](API_RouteTableAssociationState.md) object
Required: No

 ** gatewayId **
The ID of the internet gateway or virtual private gateway.
Type: String
Required: No

 ** main **
Indicates whether this is the main route table.
Type: Boolean
Required: No

 ** publicIpv4Pool **
The ID of a public IPv4 pool. A public IPv4 pool is a pool of IPv4 addresses that you've brought to AWS with BYOIP.
Type: String
Required: No

 ** routeTableAssociationId **
The ID of the association.
Type: String
Required: No

 ** routeTableId **
The ID of the route table.
Type: String
Required: No

 ** subnetId **
The ID of the subnet. A subnet ID is not returned for an implicit association.
Type: String
Required: No

## See Also
<a name="API_RouteTableAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RouteTableAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RouteTableAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RouteTableAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
