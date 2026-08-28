---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StaleIpPermission.html
---

# StaleIpPermission
<a name="API_StaleIpPermission"></a>

Describes a stale rule in a security group.

## Contents
<a name="API_StaleIpPermission_Contents"></a>

 ** fromPort **
If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).
Type: Integer
Required: No

 ** Groups.N **
The security group pairs. Returns the ID of the referenced security group and VPC, and the ID and status of the VPC peering connection.
Type: Array of [UserIdGroupPair](API_UserIdGroupPair.md) objects
Required: No

 ** ipProtocol **
The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number (see [Protocol Numbers)](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
Type: String
Required: No

 ** IpRanges.N **
The IP ranges. Not applicable for stale security group rules.
Type: Array of strings
Required: No

 ** PrefixListIds.N **
The prefix list IDs. Not applicable for stale security group rules.
Type: Array of strings
Required: No

 ** toPort **
If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes).
Type: Integer
Required: No

## See Also
<a name="API_StaleIpPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/StaleIpPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/StaleIpPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/StaleIpPermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
