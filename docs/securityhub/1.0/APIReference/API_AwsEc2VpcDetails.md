---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2VpcDetails.html
---

# AwsEc2VpcDetails
<a name="API_AwsEc2VpcDetails"></a>

Details about an EC2 VPC.

## Contents
<a name="API_AwsEc2VpcDetails_Contents"></a>

 ** CidrBlockAssociationSet **   <a name="securityhub-Type-AwsEc2VpcDetails-CidrBlockAssociationSet"></a>
Information about the IPv4 CIDR blocks associated with the VPC.
Type: Array of [CidrBlockAssociation](API_CidrBlockAssociation.md) objects
Required: No

 ** DhcpOptionsId **   <a name="securityhub-Type-AwsEc2VpcDetails-DhcpOptionsId"></a>
The identifier of the set of Dynamic Host Configuration Protocol (DHCP) options that are associated with the VPC. If the default options are associated with the VPC, then this is default.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Ipv6CidrBlockAssociationSet **   <a name="securityhub-Type-AwsEc2VpcDetails-Ipv6CidrBlockAssociationSet"></a>
Information about the IPv6 CIDR blocks associated with the VPC.
Type: Array of [Ipv6CidrBlockAssociation](API_Ipv6CidrBlockAssociation.md) objects
Required: No

 ** State **   <a name="securityhub-Type-AwsEc2VpcDetails-State"></a>
The current state of the VPC. Valid values are `available` or `pending`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2VpcDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2VpcDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2VpcDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2VpcDetails)
