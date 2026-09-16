---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsEgress.html
---

# UpdateSecurityGroupRuleDescriptionsEgress
<a name="API_UpdateSecurityGroupRuleDescriptionsEgress"></a>

Updates the description of an egress (outbound) security group rule. You can replace an existing description, or add a description to a rule that did not have one previously. You can remove a description for a security group rule by omitting the description parameter in the request.

## Request Parameters
<a name="API_UpdateSecurityGroupRuleDescriptionsEgress_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **GroupId**
The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.
Type: String
Required: No

 **GroupName**
[Default VPC] The name of the security group. You must specify either the security group ID or the security group name.
Type: String
Required: No

 **IpPermissions.N**
The IP permissions for the security group rule. You must specify either the IP permissions or the description.
Type: Array of [IpPermission](API_IpPermission.md) objects
Required: No

 **SecurityGroupRuleDescription.N**
The description for the egress security group rules. You must specify either the description or the IP permissions.
Type: Array of [SecurityGroupRuleDescription](API_SecurityGroupRuleDescription.md) objects
Required: No

## Response Elements
<a name="API_UpdateSecurityGroupRuleDescriptionsEgress_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, returns an error.
Type: Boolean

## Errors
<a name="API_UpdateSecurityGroupRuleDescriptionsEgress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_UpdateSecurityGroupRuleDescriptionsEgress_Examples"></a>

### Example
<a name="API_UpdateSecurityGroupRuleDescriptionsEgress_Example_1"></a>

This example updates the description for the security group rule that allows outbound access over port 80 to the `205.192.0.0/16` IPv4 address range. The description '`Outbound HTTP access to server 2`' replaces any existing description for the rule.

#### Sample Request
<a name="API_UpdateSecurityGroupRuleDescriptionsEgress_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=UpdateSecurityGroupRuleDescriptionsEgress
&GroupId=sg-112233
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=80
&IpPermissions.1.ToPort=80
&IpPermissions.1.IpRanges.1.CidrIp=205.192.0.0/16
&IpPermissions.1.IpRanges.1.Description=Outbound HTTP access to server 2
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateSecurityGroupRuleDescriptionsEgress_Example_1_Response"></a>

```
<UpdateSecurityGroupRuleDescriptionsEgressResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1480cf25-4fbe-4168-aa9c-365example</requestId>
    <return>true</return>
</UpdateSecurityGroupRuleDescriptionsEgressResponse>
```

## See Also
<a name="API_UpdateSecurityGroupRuleDescriptionsEgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsEgress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsEgress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsEgress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsEgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsEgress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsEgress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsEgress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsEgress)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsEgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsEgress)
