---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Ipv6CidrBlockAssociation.html
---

# Ipv6CidrBlockAssociation
<a name="API_Ipv6CidrBlockAssociation"></a>

An IPV6 CIDR block association.

## Contents
<a name="API_Ipv6CidrBlockAssociation_Contents"></a>

 ** AssociationId **   <a name="securityhub-Type-Ipv6CidrBlockAssociation-AssociationId"></a>
The association ID for the IPv6 CIDR block.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CidrBlockState **   <a name="securityhub-Type-Ipv6CidrBlockAssociation-CidrBlockState"></a>
Information about the state of the CIDR block. Valid values are as follows:
+  `associating`
+  `associated`
+  `disassociating`
+  `disassociated`
+  `failed`
+  `failing`
Type: String
Pattern: `.*\S.*`
Required: No

 ** Ipv6CidrBlock **   <a name="securityhub-Type-Ipv6CidrBlockAssociation-Ipv6CidrBlock"></a>
The IPv6 CIDR block.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Ipv6CidrBlockAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Ipv6CidrBlockAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Ipv6CidrBlockAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Ipv6CidrBlockAssociation)
