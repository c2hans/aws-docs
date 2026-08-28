---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html
---

# AuthorizeSecurityGroupEgress
<a name="API_AuthorizeSecurityGroupEgress"></a>

Adds the specified outbound (egress) rules to a security group.

An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address ranges, the IP address ranges specified by a prefix list, or the instances that are associated with a source security group. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html).

You must specify exactly one of the following destinations: an IPv4 or IPv6 address range, a prefix list, or a security group. You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP type and code.

Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur.

For examples of rules that you can add to security groups for specific access scenarios, see [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html) in the *Amazon EC2 User Guide*.

For information about security group quotas, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_AuthorizeSecurityGroupEgress_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CidrIp**
Not supported. Use IP permissions instead.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FromPort**
Not supported. Use IP permissions instead.
Type: Integer
Required: No

 **GroupId**
The ID of the security group.
Type: String
Required: Yes

 **IpPermissions.N**
The permissions for the security group rules.
Type: Array of [IpPermission](API_IpPermission.md) objects
Required: No

 **IpProtocol**
Not supported. Use IP permissions instead.
Type: String
Required: No

 **SourceSecurityGroupName**
Not supported. Use IP permissions instead.
Type: String
Required: No

 **SourceSecurityGroupOwnerId**
Not supported. Use IP permissions instead.
Type: String
Required: No

 **TagSpecification.N**
The tags applied to the security group rule.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **ToPort**
Not supported. Use IP permissions instead.
Type: Integer
Required: No

## Response Elements
<a name="API_AuthorizeSecurityGroupEgress_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, returns an error.
Type: Boolean

 **securityGroupRuleSet**
Information about the outbound (egress) security group rules that were added.
Type: Array of [SecurityGroupRule](API_SecurityGroupRule.md) objects

## Errors
<a name="API_AuthorizeSecurityGroupEgress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AuthorizeSecurityGroupEgress_Examples"></a>

### Example 1
<a name="API_AuthorizeSecurityGroupEgress_Example_1"></a>

This example request grants your security group with the ID `sg-1a2b3c4d` access to the `192.0.2.0/24` and `198.51.100.0/24` IPv4 address ranges on TCP port 80.

#### Sample Request
<a name="API_AuthorizeSecurityGroupEgress_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AuthorizeSecurityGroupEgress
&GroupId=sg-1a2b3c4d
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=80
&IpPermissions.1.ToPort=80
&IpPermissions.1.IpRanges.1.CidrIp=192.0.2.0/24
&IpPermissions.1.IpRanges.2.CidrIp=198.51.100.0/24
&AUTHPARAMS
```

#### Sample Response
<a name="API_AuthorizeSecurityGroupEgress_Example_1_Response"></a>

```
<AuthorizeSecurityGroupEgressResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</AuthorizeSecurityGroupEgressResponse>
```

### Example 2
<a name="API_AuthorizeSecurityGroupEgress_Example_2"></a>

This example request grants egress access from the security group with the ID `sg-1a2b3c4d` to the security group with the ID `sg-9a8d7f5c` on TCP port 1433.

#### Sample Request
<a name="API_AuthorizeSecurityGroupEgress_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=AuthorizeSecurityGroupEgress
&GroupId=sg-1a2b3c4d
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=1433
&IpPermissions.1.ToPort=1433
&IpPermissions.1.Groups.1.GroupId=sg-9a8d7f5c
&AUTHPARAMS
```

### Example 3
<a name="API_AuthorizeSecurityGroupEgress_Example_3"></a>

This example request grants your security group with the ID `sg-1a2b3c4d` access to the `2001:db8:1234:1a00::/64` IPv6 address range on TCP port 22.

#### Sample Request
<a name="API_AuthorizeSecurityGroupEgress_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=AuthorizeSecurityGroupEgress
&GroupId=sg-1a2b3c4d
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=22
&IpPermissions.1.ToPort=22
&IpPermissions.1.Ipv6Ranges.1.CidrIpv6=2001:db8:1234:1a00::/64
&AUTHPARAMS
```

### Example 4
<a name="API_AuthorizeSecurityGroupEgress_Example_4"></a>

This example grants access over port 3389 (RDP) to the `192.0.2.0/24` IPv4 address range, and includes a description for the rule to help you identify the rule later.

#### Sample Request
<a name="API_AuthorizeSecurityGroupEgress_Example_4_Request"></a>

```
https://ec2.amazonaws.com/?Action=AuthorizeSecurityGroupEgress
&GroupId=sg-112233
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=3389
&IpPermissions.1.ToPort=3389
&IpPermissions.1.IpRanges.1.CidrIp=192.0.2.0/24
&IpPermissions.1.IpRanges.1.Description=Access to London office
```

## See Also
<a name="API_AuthorizeSecurityGroupEgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AuthorizeSecurityGroupEgress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AuthorizeSecurityGroupEgress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AuthorizeSecurityGroupEgress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AuthorizeSecurityGroupEgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AuthorizeSecurityGroupEgress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AuthorizeSecurityGroupEgress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AuthorizeSecurityGroupEgress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AuthorizeSecurityGroupEgress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AuthorizeSecurityGroupEgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AuthorizeSecurityGroupEgress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
