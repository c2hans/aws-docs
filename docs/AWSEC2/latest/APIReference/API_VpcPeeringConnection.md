---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcPeeringConnection.html
---

# VpcPeeringConnection
<a name="API_VpcPeeringConnection"></a>

Describes a VPC peering connection.

## Contents
<a name="API_VpcPeeringConnection_Contents"></a>

 ** accepterVpcInfo **
Information about the accepter VPC. CIDR block information is only returned when describing an active VPC peering connection.
Type: [VpcPeeringConnectionVpcInfo](API_VpcPeeringConnectionVpcInfo.md) object
Required: No

 ** expirationTime **
The time that an unaccepted VPC peering connection will expire.
Type: Timestamp
Required: No

 ** requesterVpcInfo **
Information about the requester VPC. CIDR block information is only returned when describing an active VPC peering connection.
Type: [VpcPeeringConnectionVpcInfo](API_VpcPeeringConnectionVpcInfo.md) object
Required: No

 ** status **
The status of the VPC peering connection.
Type: [VpcPeeringConnectionStateReason](API_VpcPeeringConnectionStateReason.md) object
Required: No

 ** TagSet.N **
Any tags assigned to the resource.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcPeeringConnectionId **
The ID of the VPC peering connection.
Type: String
Required: No

## See Also
<a name="API_VpcPeeringConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcPeeringConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcPeeringConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcPeeringConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
