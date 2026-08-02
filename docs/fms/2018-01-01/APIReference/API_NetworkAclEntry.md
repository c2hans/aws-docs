---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkAclEntry.html
---

# NetworkAclEntry
<a name="API_NetworkAclEntry"></a>

Describes a rule in a network ACL.

Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, AWS processes the entries in the network ACL according to the rule numbers, in ascending order.

When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.

## Contents
<a name="API_NetworkAclEntry_Contents"></a>

 ** Egress **   <a name="fms-Type-NetworkAclEntry-Egress"></a>
Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If it's not an egress rule, then it's an ingress, or inbound, rule.
Type: Boolean
Required: Yes

 ** Protocol **   <a name="fms-Type-NetworkAclEntry-Protocol"></a>
The protocol number. A value of "-1" means all protocols.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** RuleAction **   <a name="fms-Type-NetworkAclEntry-RuleAction"></a>
Indicates whether to allow or deny the traffic that matches the rule.
Type: String
Valid Values: `allow | deny`
Required: Yes

 ** CidrBlock **   <a name="fms-Type-NetworkAclEntry-CidrBlock"></a>
The IPv4 network range to allow or deny, in CIDR notation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** IcmpTypeCode **   <a name="fms-Type-NetworkAclEntry-IcmpTypeCode"></a>
ICMP protocol: The ICMP type and code.
Type: [NetworkAclIcmpTypeCode](API_NetworkAclIcmpTypeCode.md) object
Required: No

 ** Ipv6CidrBlock **   <a name="fms-Type-NetworkAclEntry-Ipv6CidrBlock"></a>
The IPv6 network range to allow or deny, in CIDR notation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PortRange **   <a name="fms-Type-NetworkAclEntry-PortRange"></a>
TCP or UDP protocols: The range of ports the rule applies to.
Type: [NetworkAclPortRange](API_NetworkAclPortRange.md) object
Required: No

## See Also
<a name="API_NetworkAclEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkAclEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkAclEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkAclEntry)
