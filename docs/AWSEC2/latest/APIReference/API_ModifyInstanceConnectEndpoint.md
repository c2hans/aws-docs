---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceConnectEndpoint.html
---

# ModifyInstanceConnectEndpoint
<a name="API_ModifyInstanceConnectEndpoint"></a>

Modifies the specified EC2 Instance Connect Endpoint.

For more information, see [Modify an EC2 Instance Connect Endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-ec2-instance-connect-endpoint.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_ModifyInstanceConnectEndpoint_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceConnectEndpointId**
The ID of the EC2 Instance Connect Endpoint to modify.
Type: String
Required: Yes

 **IpAddressType**
The new IP address type for the EC2 Instance Connect Endpoint.
 `PreserveClientIp` is only supported on IPv4 EC2 Instance Connect Endpoints. To use `PreserveClientIp`, the value for `IpAddressType` must be `ipv4`.
Type: String
Valid Values: `ipv4 | dualstack | ipv6`
Required: No

 **PreserveClientIp**
Indicates whether the client IP address is preserved as the source when you connect to a resource. The following are the possible values.
+  `true` - Use the IP address of the client. Your instance must have an IPv4 address.
+  `false` - Use the IP address of the network interface.
Type: Boolean
Required: No

 **SecurityGroupId.N**
Changes the security groups for the EC2 Instance Connect Endpoint. The new set of groups you specify replaces the current set. You must specify at least one group, even if it's just the default security group in the VPC. You must specify the ID of the security group, not the name.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Required: No

## Response Elements
<a name="API_ModifyInstanceConnectEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds and an error otherwise.
Type: Boolean

## Errors
<a name="API_ModifyInstanceConnectEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyInstanceConnectEndpoint_Examples"></a>

### Example: Modify an EC2 Instance Connect Endpoint
<a name="API_ModifyInstanceConnectEndpoint_Example_1"></a>

This example modifies all the parameters of an EC2 Instance Connect Endpoint in a single request.

#### Sample Request
<a name="API_ModifyInstanceConnectEndpoint_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyInstanceConnectEndpoint
&InstanceConnectEndpointId=eice-0123456789example
&SecurityGroupId.1=sg-0123456789example
&IpAddressType=dualstack
&PreserveClientIp=false
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyInstanceConnectEndpoint_Example_1_Response"></a>

```
<ModifyInstanceConnectEndpointResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <return>true</return>
</ModifyInstanceConnectEndpointResponse>
```

## See Also
<a name="API_ModifyInstanceConnectEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyInstanceConnectEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyInstanceConnectEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyInstanceConnectEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyInstanceConnectEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyInstanceConnectEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyInstanceConnectEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyInstanceConnectEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyInstanceConnectEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyInstanceConnectEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyInstanceConnectEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
