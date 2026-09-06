---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Ipv6Range.html
---

# Ipv6Range
<a name="API_Ipv6Range"></a>

Describes an IPv6 address range.

## Contents
<a name="API_Ipv6Range_Contents"></a>

 ** CidrIpv6 ** (request), ** cidrIpv6 ** (response)
The IPv6 address range. You can either specify a CIDR block or a source security group, not both. To specify a single IPv6 address, use the /128 prefix length.
 AWS [canonicalizes](https://en.wikipedia.org/wiki/Canonicalization) IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, AWS canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.
Type: String
Required: No

 ** Description ** (request), ** description ** (response)
A description for the security group rule that references this IPv6 address range.
Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and .\_-:/()\#,@[]\+=&;{}\!$\*
Type: String
Required: No

## See Also
<a name="API_Ipv6Range_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Ipv6Range)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Ipv6Range)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Ipv6Range)
