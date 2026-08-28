---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroupRule.html
---

# SecurityGroupRule
<a name="API_SecurityGroupRule"></a>

Describes a security group rule.

## Contents
<a name="API_SecurityGroupRule_Contents"></a>

 ** cidrIpv4 **
The IPv4 CIDR range.
Type: String
Required: No

 ** cidrIpv6 **
The IPv6 CIDR range.
Type: String
Required: No

 ** description **
The security group rule description.
Type: String
Required: No

 ** fromPort **
If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).
Type: Integer
Required: No

 ** groupId **
The ID of the security group.
Type: String
Required: No

 ** groupOwnerId **
The ID of the AWS account that owns the security group.
Type: String
Required: No

 ** ipProtocol **
The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number (see [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)).
Use `-1` to specify all protocols.
Type: String
Required: No

 ** isEgress **
Indicates whether the security group rule is an outbound rule.
Type: Boolean
Required: No

 ** prefixListId **
The ID of the prefix list.
Type: String
Required: No

 ** referencedGroupInfo **
Describes the security group that is referenced in the rule.
Type: [ReferencedSecurityGroup](API_ReferencedSecurityGroup.md) object
Required: No

 ** securityGroupRuleArn **
The ARN of the security group rule.
Type: String
Required: No

 ** securityGroupRuleId **
The ID of the security group rule.
Type: String
Required: No

 ** TagSet.N **
The tags applied to the security group rule.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** toPort **
If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).
Type: Integer
Required: No

## See Also
<a name="API_SecurityGroupRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SecurityGroupRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SecurityGroupRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SecurityGroupRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
