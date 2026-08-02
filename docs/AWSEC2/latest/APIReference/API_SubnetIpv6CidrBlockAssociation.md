---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SubnetIpv6CidrBlockAssociation.html
---

# SubnetIpv6CidrBlockAssociation
<a name="API_SubnetIpv6CidrBlockAssociation"></a>

Describes an association between a subnet and an IPv6 CIDR block.

## Contents
<a name="API_SubnetIpv6CidrBlockAssociation_Contents"></a>

 ** associationId **
The ID of the association.
Type: String
Required: No

 ** ipSource **
The source that allocated the IP address space. `byoip` or `amazon` indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). `none` indicates private space.
Type: String
Valid Values: `amazon | byoip | none`
Required: No

 ** ipv6AddressAttribute **
Public IPv6 addresses are those advertised on the internet from AWS. Private IP addresses are not and cannot be advertised on the internet from AWS.
Type: String
Valid Values: `public | private`
Required: No

 ** ipv6CidrBlock **
The IPv6 CIDR block.
Type: String
Required: No

 ** ipv6CidrBlockState **
The state of the CIDR block.
Type: [SubnetCidrBlockState](API_SubnetCidrBlockState.md) object
Required: No

## See Also
<a name="API_SubnetIpv6CidrBlockAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SubnetIpv6CidrBlockAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SubnetIpv6CidrBlockAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SubnetIpv6CidrBlockAssociation)
