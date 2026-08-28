---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html
---

# AuthorizeSecurityGroupIngress
<a name="API_AuthorizeSecurityGroupIngress"></a>

Adds the specified inbound (ingress) rules to a security group.

An inbound rule permits instances to receive traffic from the specified IPv4 or IPv6 address range, the IP address ranges that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html).

You must specify exactly one of the following sources: an IPv4 or IPv6 address range, a prefix list, or a security group. You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP/ICMPv6 type and code.

Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.

For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *Amazon EC2 User Guide*.

For more information about security group quotas, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_AuthorizeSecurityGroupIngress_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CidrIp**
The IPv4 address range, in CIDR format.
 AWS [canonicalizes](https://en.wikipedia.org/wiki/Canonicalization) IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, AWS canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.
To specify an IPv6 address range, use IP permissions instead.
To specify multiple rules and descriptions for the rules, use IP permissions instead.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FromPort**
If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP, this is the ICMP type or -1 (all ICMP types).
To specify multiple rules and descriptions for the rules, use IP permissions instead.
Type: Integer
Required: No

 **GroupId**
The ID of the security group.
Type: String
Required: No

 **GroupName**
[Default VPC] The name of the security group. For security groups for a default VPC you can specify either the ID or the name of the security group. For security groups for a nondefault VPC, you must specify the ID of the security group.
Type: String
Required: No

 **IpPermissions.N**
The permissions for the security group rules.
Type: Array of [IpPermission](API_IpPermission.md) objects
Required: No

 **IpProtocol**
The IP protocol name (`tcp`, `udp`, `icmp`) or number (see [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)). To specify all protocols, use `-1`.
To specify `icmpv6`, use IP permissions instead.
If you specify a protocol other than one of the supported values, traffic is allowed on all ports, regardless of any ports that you specify.
To specify multiple rules and descriptions for the rules, use IP permissions instead.
Type: String
Required: No

 **SourceSecurityGroupName**
[Default VPC] The name of the source security group.
The rule grants full ICMP, UDP, and TCP access. To create a rule with a specific protocol and port range, specify a set of IP permissions instead.
Type: String
Required: No

 **SourceSecurityGroupOwnerId**
The AWS account ID for the source security group, if the source security group is in a different account.
The rule grants full ICMP, UDP, and TCP access. To create a rule with a specific protocol and port range, use IP permissions instead.
Type: String
Required: No

 **TagSpecification.N**
The tags applied to the security group rule.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **ToPort**
If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).
To specify multiple rules and descriptions for the rules, use IP permissions instead.
Type: Integer
Required: No

## Response Elements
<a name="API_AuthorizeSecurityGroupIngress_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, returns an error.
Type: Boolean

 **securityGroupRuleSet**
Information about the inbound (ingress) security group rules that were added.
Type: Array of [SecurityGroupRule](API_SecurityGroupRule.md) objects

## Errors
<a name="API_AuthorizeSecurityGroupIngress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AuthorizeSecurityGroupIngress_Examples"></a>

### Example 1
<a name="API_AuthorizeSecurityGroupIngress_Example_1"></a>

This example request grants TCP port 80 access from the source group `sg-2a2b3c4d` to the security group `sg-1a2b3c4d`. The source security group must be in the same VPC or in a peer VPC (requires a VPC peering connection).

#### Sample Request
<a name="API_AuthorizeSecurityGroupIngress_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AuthorizeSecurityGroupIngress
&GroupId=sg-1a2b3c4d
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=80
&IpPermissions.1.ToPort=80
&IpPermissions.1.Groups.1.GroupId=sg-2a2b3c4d
&AUTHPARAMS
```

### Example 2
<a name="API_AuthorizeSecurityGroupIngress_Example_2"></a>

This example grants SSH access (port 22) from the IPv6 range `2001:db8:1234:1a00::/64`.

#### Sample Request
<a name="API_AuthorizeSecurityGroupIngress_Example_2_Request"></a>

```
https://ec2.amazonaws.com/
?Action=AuthorizeSecurityGroupIngress
&GroupId=sg-1a2b3c4d
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=22
&IpPermissions.1.ToPort=22
&IpPermissions.1.Ipv6Ranges.1.CidrIpv6=2001:db8:1234:1a00::/64
&AUTHPARAMS
```

### Example 3
<a name="API_AuthorizeSecurityGroupIngress_Example_3"></a>

This example grants access over port 3389 (RDP) from the `192.0.2.0/24` IPv4 address range, and includes a description for the rule to help you identify the rule later.

#### Sample Request
<a name="API_AuthorizeSecurityGroupIngress_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=AuthorizeSecurityGroupIngress
&GroupId=sg-112233
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=3389
&IpPermissions.1.ToPort=3389
&IpPermissions.1.IpRanges.1.CidrIp=192.0.2.0/24
&IpPermissions.1.IpRanges.1.Description=Access from New York office
```

## See Also
<a name="API_AuthorizeSecurityGroupIngress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AuthorizeSecurityGroupIngress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AuthorizeSecurityGroupIngress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AuthorizeSecurityGroupIngress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AuthorizeSecurityGroupIngress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AuthorizeSecurityGroupIngress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AuthorizeSecurityGroupIngress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AuthorizeSecurityGroupIngress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AuthorizeSecurityGroupIngress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AuthorizeSecurityGroupIngress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AuthorizeSecurityGroupIngress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
