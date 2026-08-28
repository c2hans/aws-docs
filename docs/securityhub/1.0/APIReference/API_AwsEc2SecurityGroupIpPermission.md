---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2SecurityGroupIpPermission.html
---

# AwsEc2SecurityGroupIpPermission
<a name="API_AwsEc2SecurityGroupIpPermission"></a>

An IP permission for an EC2 security group.

## Contents
<a name="API_AwsEc2SecurityGroupIpPermission_Contents"></a>

 ** FromPort **   <a name="securityhub-Type-AwsEc2SecurityGroupIpPermission-FromPort"></a>
The start of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number.
A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.
Type: Integer
Required: No

 ** IpProtocol **   <a name="securityhub-Type-AwsEc2SecurityGroupIpPermission-IpProtocol"></a>
The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number.
[VPC only] Use `-1` to specify all protocols.
When authorizing security group rules, specifying `-1` or a protocol number other than `tcp`, `udp`, `icmp`, or `icmpv6` allows traffic on all ports, regardless of any port range you specify.
For `tcp`, `udp`, and `icmp`, you must specify a port range.
For `icmpv6`, the port range is optional. If you omit the port range, traffic for all types and codes is allowed.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IpRanges **   <a name="securityhub-Type-AwsEc2SecurityGroupIpPermission-IpRanges"></a>
The IPv4 ranges.
Type: Array of [AwsEc2SecurityGroupIpRange](API_AwsEc2SecurityGroupIpRange.md) objects
Required: No

 ** Ipv6Ranges **   <a name="securityhub-Type-AwsEc2SecurityGroupIpPermission-Ipv6Ranges"></a>
The IPv6 ranges.
Type: Array of [AwsEc2SecurityGroupIpv6Range](API_AwsEc2SecurityGroupIpv6Range.md) objects
Required: No

 ** PrefixListIds **   <a name="securityhub-Type-AwsEc2SecurityGroupIpPermission-PrefixListIds"></a>
[VPC only] The prefix list IDs for an AWS service. With outbound rules, this is the AWS service to access through a VPC endpoint from instances associated with the security group.
Type: Array of [AwsEc2SecurityGroupPrefixListId](API_AwsEc2SecurityGroupPrefixListId.md) objects
Required: No

 ** ToPort **   <a name="securityhub-Type-AwsEc2SecurityGroupIpPermission-ToPort"></a>
The end of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code.
A value of `-1` indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.
Type: Integer
Required: No

 ** UserIdGroupPairs **   <a name="securityhub-Type-AwsEc2SecurityGroupIpPermission-UserIdGroupPairs"></a>
The security group and AWS account ID pairs.
Type: Array of [AwsEc2SecurityGroupUserIdGroupPair](API_AwsEc2SecurityGroupUserIdGroupPair.md) objects
Required: No

## See Also
<a name="API_AwsEc2SecurityGroupIpPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2SecurityGroupIpPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2SecurityGroupIpPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2SecurityGroupIpPermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
