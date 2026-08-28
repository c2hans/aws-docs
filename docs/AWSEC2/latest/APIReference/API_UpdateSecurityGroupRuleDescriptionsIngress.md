---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsIngress.html
---

# UpdateSecurityGroupRuleDescriptionsIngress
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress"></a>

Updates the description of an ingress (inbound) security group rule. You can replace an existing description, or add a description to a rule that did not have one previously. You can remove a description for a security group rule by omitting the description parameter in the request.

## Request Parameters
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress_RequestParameters"></a>

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
[Default VPC] The name of the security group. You must specify either the security group ID or the security group name. For security groups in a nondefault VPC, you must specify the security group ID.
Type: String
Required: No

 **IpPermissions.N**
The IP permissions for the security group rule. You must specify either IP permissions or a description.
Type: Array of [IpPermission](API_IpPermission.md) objects
Required: No

 **SecurityGroupRuleDescription.N**
The description for the ingress security group rules. You must specify either a description or IP permissions.
Type: Array of [SecurityGroupRuleDescription](API_SecurityGroupRuleDescription.md) objects
Required: No

## Response Elements
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, returns an error.
Type: Boolean

## Errors
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress_Examples"></a>

### Example 1
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress_Example_1"></a>

This example updates the description for the security group rule that allows inbound access over port 22 from the `203.0.113.0/16` IPv4 address range. The description '`SSH access from ABC office`' replaces any existing description for the rule.

#### Sample Request
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=UpdateSecurityGroupRuleDescriptionsIngress
&GroupId=sg-112233
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=22
&IpPermissions.1.ToPort=22
&IpPermissions.1.IpRanges.1.CidrIp=203.0.113.0/16
&IpPermissions.1.IpRanges.1.Description=SSH access from ABC office
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress_Example_1_Response"></a>

```
<UpdateSecurityGroupRuleDescriptionsIngressResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>b4a57536-2e4a-4cbe-82f0-399example</requestId>
    <return>true</return>
</UpdateSecurityGroupRuleDescriptionsIngressResponse>
```

### Example 2
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress_Example_2"></a>

This example removes the description for the specified security group rule.

#### Sample Request
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=UpdateSecurityGroupRuleDescriptionsIngress
&GroupId=sg-112233
&IpPermissions.1.IpProtocol=tcp
&IpPermissions.1.FromPort=22
&IpPermissions.1.ToPort=22
&IpPermissions.1.IpRanges.1.CidrIp=203.0.113.4/32
&AUTHPARAMS
```

## See Also
<a name="API_UpdateSecurityGroupRuleDescriptionsIngress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsIngress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsIngress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsIngress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsIngress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsIngress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsIngress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsIngress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsIngress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsIngress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/UpdateSecurityGroupRuleDescriptionsIngress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
