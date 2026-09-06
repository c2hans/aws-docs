---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html
---

# RevokeSecurityGroupEgress
<a name="API_RevokeSecurityGroupEgress"></a>

Removes the specified outbound (egress) rules from the specified security group.

You can specify rules using either rule IDs or security group rule properties. If you use rule properties, the values that you specify (for example, ports) must match the existing rule's values exactly. Each rule has a protocol, from and to ports, and destination (CIDR range, security group, or prefix list). For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not need to specify the description to revoke the rule.

For a default VPC, if the values you specify do not match the existing rule's values, no error is returned, and the output describes the security group rules that were not revoked.

 AWS recommends that you describe the security group to verify that the rules were removed.

Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.

## Request Parameters
<a name="API_RevokeSecurityGroupEgress_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CidrIp**
Not supported. Use a set of IP permissions to specify the CIDR.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FromPort**
Not supported. Use a set of IP permissions to specify the port.
Type: Integer
Required: No

 **GroupId**
The ID of the security group.
Type: String
Required: Yes

 **IpPermissions.N**
The sets of IP permissions. You can't specify a destination security group and a CIDR IP address range in the same set of permissions.
Type: Array of [IpPermission](API_IpPermission.md) objects
Required: No

 **IpProtocol**
Not supported. Use a set of IP permissions to specify the protocol name or number.
Type: String
Required: No

 **SecurityGroupRuleId.N**
The IDs of the security group rules.
Type: Array of strings
Required: No

 **SourceSecurityGroupName**
Not supported. Use a set of IP permissions to specify a destination security group.
Type: String
Required: No

 **SourceSecurityGroupOwnerId**
Not supported. Use a set of IP permissions to specify a destination security group.
Type: String
Required: No

 **ToPort**
Not supported. Use a set of IP permissions to specify the port.
Type: Integer
Required: No

## Response Elements
<a name="API_RevokeSecurityGroupEgress_ResponseElements"></a>

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
The outbound rules that were unknown to the service. In some cases, `unknownIpPermissionSet` might be in a different format from the request parameter.
Type: Array of [IpPermission](API_IpPermission.md) objects

## Errors
<a name="API_RevokeSecurityGroupEgress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RevokeSecurityGroupEgress_Examples"></a>

### Example 1
<a name="API_RevokeSecurityGroupEgress_Example_1"></a>

This example revokes the access that the specified security group has to the `205.192.0.0/16` and `205.159.0.0/16` IPv4 address ranges on TCP port 80.

#### Sample Request
<a name="API_RevokeSecurityGroupEgress_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=RevokeSecurityGroupEgress
&GroupId=sg-1a2b3c4d
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=80
&IpPermissions.1.ToPort=80
&IpPermissions.1.IpRanges.1.CidrIp=205.192.0.0/16
&IpPermissions.1.IpRanges.2.CidrIp=205.159.0.0/16
&AUTHPARAMS
```

### Example 2
<a name="API_RevokeSecurityGroupEgress_Example_2"></a>

This example revokes the access that the specified security group has to the security group with the ID `sg-9a8d7f5c` on TCP port 1433.

#### Sample Request
<a name="API_RevokeSecurityGroupEgress_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=RevokeSecurityGroupEgress
&GroupId=sg-1a2b3c4d
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=1433
&IpPermissions.1.ToPort=1433
&IpPermissions.1.Groups.1.GroupId=sg-9a8d7f5c
&AUTHPARAMS
```

### Example 3
<a name="API_RevokeSecurityGroupEgress_Example_3"></a>

This example revokes TCP port 22 access to the `203.0.113.4/32` address range for the security group `sg-112233`. The security group rule includes the description 'Access to office CT12'. Specifying the description to revoke the rule is optional, but if you do specify the description, it must match the existing rule's value exactly.

#### Sample Request
<a name="API_RevokeSecurityGroupEgress_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=RevokeSecurityGroupEgress
&GroupId=sg-112233
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=22
&IpPermissions.1.ToPort=22
&IpPermissions.1.IpRanges.1.CidrIp=203.0.113.4/32
&IpPermissions.1.IpRanges.1.Description=Access to office CT12
&AUTHPARAMS
```

## See Also
<a name="API_RevokeSecurityGroupEgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RevokeSecurityGroupEgress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RevokeSecurityGroupEgress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RevokeSecurityGroupEgress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RevokeSecurityGroupEgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RevokeSecurityGroupEgress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RevokeSecurityGroupEgress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RevokeSecurityGroupEgress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RevokeSecurityGroupEgress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RevokeSecurityGroupEgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RevokeSecurityGroupEgress)
