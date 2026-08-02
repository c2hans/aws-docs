---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkAclEntry.html
---

# NetworkAclEntry
<a name="API_NetworkAclEntry"></a>

Describes an entry in a network ACL.

## Contents
<a name="API_NetworkAclEntry_Contents"></a>

 ** cidrBlock **
The IPv4 network range to allow or deny, in CIDR notation.
Type: String
Required: No

 ** egress **
Indicates whether the rule is an egress rule (applied to traffic leaving the subnet).
Type: Boolean
Required: No

 ** icmpTypeCode **
ICMP protocol: The ICMP type and code.
Type: [IcmpTypeCode](API_IcmpTypeCode.md) object
Required: No

 ** ipv6CidrBlock **
The IPv6 network range to allow or deny, in CIDR notation.
Type: String
Required: No

 ** portRange **
TCP or UDP protocols: The range of ports the rule applies to.
Type: [PortRange](API_PortRange.md) object
Required: No

 ** protocol **
The protocol number. A value of "-1" means all protocols.
Type: String
Required: No

 ** ruleAction **
Indicates whether to allow or deny the traffic that matches the rule.
Type: String
Valid Values: `allow | deny`
Required: No

 ** ruleNumber **
The rule number for the entry. ACL entries are processed in ascending order by rule number.
Type: Integer
Required: No

## See Also
<a name="API_NetworkAclEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkAclEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkAclEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkAclEntry)
