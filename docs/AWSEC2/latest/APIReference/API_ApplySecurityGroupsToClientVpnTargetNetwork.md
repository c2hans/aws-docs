---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ApplySecurityGroupsToClientVpnTargetNetwork.html
---

# ApplySecurityGroupsToClientVpnTargetNetwork
<a name="API_ApplySecurityGroupsToClientVpnTargetNetwork"></a>

Applies a security group to the association between the target network and the Client VPN endpoint. This action replaces the existing security groups with the specified security groups.

## Request Parameters
<a name="API_ApplySecurityGroupsToClientVpnTargetNetwork_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SecurityGroupId.N**
The IDs of the security groups to apply to the associated target network. Up to 5 security groups can be applied to an associated target network.
Type: Array of strings
Required: Yes

 **VpcId**
The ID of the VPC in which the associated target network is located.
Type: String
Required: Yes

## Response Elements
<a name="API_ApplySecurityGroupsToClientVpnTargetNetwork_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **securityGroupIds**
The IDs of the applied security groups.
Type: Array of strings

## Errors
<a name="API_ApplySecurityGroupsToClientVpnTargetNetwork_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ApplySecurityGroupsToClientVpnTargetNetwork_Examples"></a>

### Example
<a name="API_ApplySecurityGroupsToClientVpnTargetNetwork_Example_1"></a>

This example applies a security group to a Client VPN endpoint.

#### Sample Request
<a name="API_ApplySecurityGroupsToClientVpnTargetNetwork_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ApplySecurityGroupsToClientVpnTargetNetwork
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&SecurityGroupId=sg-0618575f05EXAMPLE
&VpcId=vpc-3db97056EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_ApplySecurityGroupsToClientVpnTargetNetwork_Example_1_Response"></a>

```
<ApplySecurityGroupsToClientVpnTargetNetworkResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>5ef84b7f-505e-4e39-80cd-a11dbEXAMPLE</requestId>
    <securityGroupIds>
        <item>sg-0618575f05EXAMPLE</item>
    </securityGroupIds>
</ApplySecurityGroupsToClientVpnTargetNetworkResponse>
```

## See Also
<a name="API_ApplySecurityGroupsToClientVpnTargetNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ApplySecurityGroupsToClientVpnTargetNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ApplySecurityGroupsToClientVpnTargetNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ApplySecurityGroupsToClientVpnTargetNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ApplySecurityGroupsToClientVpnTargetNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ApplySecurityGroupsToClientVpnTargetNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ApplySecurityGroupsToClientVpnTargetNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ApplySecurityGroupsToClientVpnTargetNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ApplySecurityGroupsToClientVpnTargetNetwork)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ApplySecurityGroupsToClientVpnTargetNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ApplySecurityGroupsToClientVpnTargetNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
