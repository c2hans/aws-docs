---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityGroupRuleDescription.html
---

# SecurityGroupRuleDescription
<a name="API_SecurityGroupRuleDescription"></a>

Describes a set of permissions for a security group rule.

## Contents
<a name="API_SecurityGroupRuleDescription_Contents"></a>

 ** FromPort **   <a name="fms-Type-SecurityGroupRuleDescription-FromPort"></a>
The start of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of `-1` indicates all ICMP/ICMPv6 types.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** IPV4Range **   <a name="fms-Type-SecurityGroupRuleDescription-IPV4Range"></a>
The IPv4 ranges for the security group rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** IPV6Range **   <a name="fms-Type-SecurityGroupRuleDescription-IPV6Range"></a>
The IPv6 ranges for the security group rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-f0-9:./]+`
Required: No

 ** PrefixListId **   <a name="fms-Type-SecurityGroupRuleDescription-PrefixListId"></a>
The ID of the prefix list for the security group rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** Protocol **   <a name="fms-Type-SecurityGroupRuleDescription-Protocol"></a>
The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ToPort **   <a name="fms-Type-SecurityGroupRuleDescription-ToPort"></a>
The end of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of `-1` indicates all ICMP/ICMPv6 codes.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_SecurityGroupRuleDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/SecurityGroupRuleDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/SecurityGroupRuleDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/SecurityGroupRuleDescription)
