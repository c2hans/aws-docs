---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcPeeringConnectionVpcInfo.html
---

# VpcPeeringConnectionVpcInfo
<a name="API_VpcPeeringConnectionVpcInfo"></a>

Describes a VPC in a VPC peering connection.

## Contents
<a name="API_VpcPeeringConnectionVpcInfo_Contents"></a>

 ** cidrBlock **
The IPv4 CIDR block for the VPC.
Type: String
Required: No

 ** CidrBlockSet.N **
Information about the IPv4 CIDR blocks for the VPC.
Type: Array of [CidrBlock](API_CidrBlock.md) objects
Required: No

 ** Ipv6CidrBlockSet.N **
The IPv6 CIDR block for the VPC.
Type: Array of [Ipv6CidrBlock](API_Ipv6CidrBlock.md) objects
Required: No

 ** ownerId **
The ID of the AWS account that owns the VPC.
Type: String
Required: No

 ** peeringOptions **
Information about the VPC peering connection options for the accepter or requester VPC.
Type: [VpcPeeringConnectionOptionsDescription](API_VpcPeeringConnectionOptionsDescription.md) object
Required: No

 ** region **
The Region in which the VPC is located.
Type: String
Required: No

 ** vpcId **
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_VpcPeeringConnectionVpcInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcPeeringConnectionVpcInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcPeeringConnectionVpcInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcPeeringConnectionVpcInfo)
