---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcIpv6CidrBlockAssociation.html
---

# VpcIpv6CidrBlockAssociation
<a name="API_VpcIpv6CidrBlockAssociation"></a>

Describes an IPv6 CIDR block associated with a VPC.

## Contents
<a name="API_VpcIpv6CidrBlockAssociation_Contents"></a>

 ** associationId **
The association ID for the IPv6 CIDR block.
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
Information about the state of the CIDR block.
Type: [VpcCidrBlockState](API_VpcCidrBlockState.md) object
Required: No

 ** ipv6Pool **
The ID of the IPv6 address pool from which the IPv6 CIDR block is allocated.
Type: String
Required: No

 ** networkBorderGroup **
The name of the unique set of Availability Zones, Local Zones, or Wavelength Zones from which AWS advertises IP addresses, for example, `us-east-1-wl1-bos-wlz-1`.
Type: String
Required: No

## See Also
<a name="API_VpcIpv6CidrBlockAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcIpv6CidrBlockAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcIpv6CidrBlockAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcIpv6CidrBlockAssociation)
