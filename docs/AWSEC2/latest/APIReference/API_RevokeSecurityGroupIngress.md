---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html
---

# RevokeSecurityGroupIngress
<a name="API_RevokeSecurityGroupIngress"></a>

Removes the specified inbound (ingress) rules from a security group.

You can specify rules using either rule IDs or security group rule properties. If you use rule properties, the values that you specify (for example, ports) must match the existing rule's values exactly. Each rule has a protocol, from and to ports, and source (CIDR range, security group, or prefix list). For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not need to specify the description to revoke the rule.

For a default VPC, if the values you specify do not match the existing rule's values, no error is returned, and the output describes the security group rules that were not revoked.

For a non-default VPC, if the values you specify do not match the existing rule's values, an `InvalidPermission.NotFound` client error is returned, and no rules are revoked.

 AWS recommends that you describe the security group to verify that the rules were removed.

Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.

## Request Parameters
<a name="API_RevokeSecurityGroupIngress_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CidrIp**
The CIDR IP address range. You can't specify this parameter when specifying a source security group.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FromPort**
If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP, this is the ICMP type or -1 (all ICMP types).
Type: Integer
Required: No

 **GroupId**
The ID of the security group.
Type: String
Required: No

 **GroupName**
[Default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.
Type: String
Required: No

 **IpPermissions.N**
The sets of IP permissions. You can't specify a source security group and a CIDR IP address range in the same set of permissions.
Type: Array of [IpPermission](API_IpPermission.md) objects
Required: No

 **IpProtocol**
The IP protocol name (`tcp`, `udp`, `icmp`) or number (see [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)). Use `-1` to specify all.
Type: String
Required: No

 **SecurityGroupRuleId.N**
The IDs of the security group rules.
Type: Array of strings
Required: No

 **SourceSecurityGroupName**
[Default VPC] The name of the source security group. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. The source security group must be in the same VPC. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.
Type: String
Required: No

 **SourceSecurityGroupOwnerId**
Not supported.
Type: String
Required: No

 **ToPort**
If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP, this is the ICMP code or -1 (all ICMP codes).
Type: Integer
Required: No

## Response Elements
<a name="API_RevokeSecurityGroupIngress_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, returns an error.
Type: Boolean

 **revokedSecurityGroupRuleSet**
Details about the revoked security group rules.
Type: Array of [RevokedSecurityGroupRule](API_RevokedSecurityGroupRule.md) objects

 **unknownIpPermissionSet**
The inbound rules that were unknown to the service. In some cases, `unknownIpPermissionSet` might be in a different format from the request parameter.
Type: Array of [IpPermission](API_IpPermission.md) objects

## Errors
<a name="API_RevokeSecurityGroupIngress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RevokeSecurityGroupIngress_Examples"></a>

### Example 1
<a name="API_RevokeSecurityGroupIngress_Example_1"></a>

This example revokes TCP port 80 access from the `205.192.0.0/16` IPv4 address range for the security group named `websrv`. If the security group is for a VPC, specify the ID of the security group instead of the name.

#### Sample Request
<a name="API_RevokeSecurityGroupIngress_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=RevokeSecurityGroupIngress
&GroupName=websrv
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=80
&IpPermissions.1.ToPort=80
&IpPermissions.1.IpRanges.1.CidrIp=205.192.0.0/16
&AUTHPARAMS
```

#### Sample Response
<a name="API_RevokeSecurityGroupIngress_Example_1_Response"></a>

```
<RevokeSecurityGroupIngressResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</RevokeSecurityGroupIngressResponse>
```

### Example 2
<a name="API_RevokeSecurityGroupIngress_Example_2"></a>

This example revokes TCP port 22 (SSH) access from IPv6 range `2001:db8:1234:1a00::/64`.

#### Sample Request
<a name="API_RevokeSecurityGroupIngress_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=RevokeSecurityGroupIngress
&GroupName=websrv
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=80
&IpPermissions.1.ToPort=80
&IpPermissions.1.Ipv6Ranges.1.CidrIpv6=2001:db8:1234:1a00::/64
&AUTHPARAMS
```

### Example 3
<a name="API_RevokeSecurityGroupIngress_Example_3"></a>

This example revokes TCP port 22 access from the `203.0.113.4/32` address range for the security group `sg-112233`. The security group rule includes the description 'Access from workstation 1a2b'. Specifying the description to revoke the rule is optional, but if you do specify the description, it must match the existing rule's value exactly.

#### Sample Request
<a name="API_RevokeSecurityGroupIngress_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=RevokeSecurityGroupIngress
&GroupId=sg-112233
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=22
&IpPermissions.1.ToPort=22
&IpPermissions.1.IpRanges.1.CidrIp=203.0.113.4/32
&IpPermissions.1.IpRanges.1.Description=Access from workstation 1a2b
&AUTHPARAMS
```

## See Also
<a name="API_RevokeSecurityGroupIngress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RevokeSecurityGroupIngress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RevokeSecurityGroupIngress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RevokeSecurityGroupIngress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RevokeSecurityGroupIngress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RevokeSecurityGroupIngress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RevokeSecurityGroupIngress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RevokeSecurityGroupIngress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RevokeSecurityGroupIngress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RevokeSecurityGroupIngress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RevokeSecurityGroupIngress)
