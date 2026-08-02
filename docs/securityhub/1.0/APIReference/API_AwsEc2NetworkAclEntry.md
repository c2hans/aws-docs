---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2NetworkAclEntry.html
---

# AwsEc2NetworkAclEntry
<a name="API_AwsEc2NetworkAclEntry"></a>

A rule for the network ACL. Each rule allows or denies access based on the IP address, traffic direction, port, and protocol.

## Contents
<a name="API_AwsEc2NetworkAclEntry_Contents"></a>

 ** CidrBlock **   <a name="securityhub-Type-AwsEc2NetworkAclEntry-CidrBlock"></a>
The IPV4 network range for which to deny or allow access.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Egress **   <a name="securityhub-Type-AwsEc2NetworkAclEntry-Egress"></a>
Whether the rule is an egress rule. An egress rule is a rule that applies to traffic that leaves the subnet.
Type: Boolean
Required: No

 ** IcmpTypeCode **   <a name="securityhub-Type-AwsEc2NetworkAclEntry-IcmpTypeCode"></a>
The Internet Control Message Protocol (ICMP) type and code for which to deny or allow access.
Type: [IcmpTypeCode](API_IcmpTypeCode.md) object
Required: No

 ** Ipv6CidrBlock **   <a name="securityhub-Type-AwsEc2NetworkAclEntry-Ipv6CidrBlock"></a>
The IPV6 network range for which to deny or allow access.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PortRange **   <a name="securityhub-Type-AwsEc2NetworkAclEntry-PortRange"></a>
For TCP or UDP protocols, the range of ports that the rule applies to.
Type: [PortRangeFromTo](API_PortRangeFromTo.md) object
Required: No

 ** Protocol **   <a name="securityhub-Type-AwsEc2NetworkAclEntry-Protocol"></a>
The protocol that the rule applies to. To deny or allow access to all protocols, use the value `-1`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleAction **   <a name="securityhub-Type-AwsEc2NetworkAclEntry-RuleAction"></a>
Whether the rule is used to allow access or deny access.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RuleNumber **   <a name="securityhub-Type-AwsEc2NetworkAclEntry-RuleNumber"></a>
The rule number. The rules are processed in order by their number.
Type: Integer
Required: No

## See Also
<a name="API_AwsEc2NetworkAclEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2NetworkAclEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2NetworkAclEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2NetworkAclEntry)
