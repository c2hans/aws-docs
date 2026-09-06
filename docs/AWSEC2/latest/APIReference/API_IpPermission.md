---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpPermission.html
---

# IpPermission
<a name="API_IpPermission"></a>

Describes the permissions for a security group rule.

## Contents
<a name="API_IpPermission_Contents"></a>

 ** FromPort ** (request), ** fromPort ** (response)
If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).
Type: Integer
Required: No

 ** Groups.N **
The security group and AWS account ID pairs.
Type: Array of [UserIdGroupPair](API_UserIdGroupPair.md) objects
Required: No

 ** IpProtocol ** (request), ** ipProtocol ** (response)
The IP protocol name (`tcp`, `udp`, `icmp`, `icmpv6`) or number (see [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)).
Use `-1` to specify all protocols. When authorizing security group rules, specifying `-1` or a protocol number other than `tcp`, `udp`, `icmp`, or `icmpv6` allows traffic on all ports, regardless of any port range you specify. For `tcp`, `udp`, and `icmp`, you must specify a port range. For `icmpv6`, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.
Type: String
Required: No

 ** IpRanges.N **
The IPv4 address ranges.
Type: Array of [IpRange](API_IpRange.md) objects
Required: No

 ** Ipv6Ranges.N **
The IPv6 address ranges.
Type: Array of [Ipv6Range](API_Ipv6Range.md) objects
Required: No

 ** PrefixListIds.N **
The prefix list IDs.
Type: Array of [PrefixListId](API_PrefixListId.md) objects
Required: No

 ** ToPort ** (request), ** toPort ** (response)
If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).
Type: Integer
Required: No

## See Also
<a name="API_IpPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpPermission)
