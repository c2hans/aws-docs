---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Vpc.html
---

# Vpc
<a name="API_Vpc"></a>

Describes a VPC.

## Contents
<a name="API_Vpc_Contents"></a>

 ** blockPublicAccessStates **
The state of VPC Block Public Access (BPA).
Type: [BlockPublicAccessStates](API_BlockPublicAccessStates.md) object
Required: No

 ** cidrBlock **
The primary IPv4 CIDR block for the VPC.
Type: String
Required: No

 ** CidrBlockAssociationSet.N **
Information about the IPv4 CIDR blocks associated with the VPC.
Type: Array of [VpcCidrBlockAssociation](API_VpcCidrBlockAssociation.md) objects
Required: No

 ** dhcpOptionsId **
The ID of the set of DHCP options you've associated with the VPC.
Type: String
Required: No

 ** instanceTenancy **
The allowed tenancy of instances launched into the VPC.
Type: String
Valid Values: `default | dedicated | host`
Required: No

 ** Ipv6CidrBlockAssociationSet.N **
Information about the IPv6 CIDR blocks associated with the VPC.
Type: Array of [VpcIpv6CidrBlockAssociation](API_VpcIpv6CidrBlockAssociation.md) objects
Required: No

 ** isDefault **
Indicates whether the VPC is the default VPC.
Type: Boolean
Required: No

 ** ownerId **
The ID of the AWS account that owns the VPC.
Type: String
Required: No

 ** state **
The current state of the VPC.
Type: String
Valid Values: `pending | available`
Required: No

 ** TagSet.N **
Any tags assigned to the VPC.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcId **
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_Vpc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Vpc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Vpc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Vpc)
