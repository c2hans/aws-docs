---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInstanceConnectEndpoint.html
---

# CreateInstanceConnectEndpoint
<a name="API_CreateInstanceConnectEndpoint"></a>

Creates an EC2 Instance Connect Endpoint.

An EC2 Instance Connect Endpoint allows you to connect to an instance, without requiring the instance to have a public IPv4 or public IPv6 address. For more information, see [Connect to your instances using EC2 Instance Connect Endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect-Endpoint.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateInstanceConnectEndpoint_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpAddressType**
The IP address type of the endpoint.
If no value is specified, the default value is determined by the IP address type of the subnet:
+  `dualstack` - If the subnet has both IPv4 and IPv6 CIDRs
+  `ipv4` - If the subnet has only IPv4 CIDRs
+  `ipv6` - If the subnet has only IPv6 CIDRs
 `PreserveClientIp` is only supported on IPv4 EC2 Instance Connect Endpoints. To use `PreserveClientIp`, the value for `IpAddressType` must be `ipv4`.
Type: String
Valid Values: `ipv4 | dualstack | ipv6`
Required: No

 **PreserveClientIp**
Indicates whether the client IP address is preserved as the source. The following are the possible values.
+  `true` - Use the client IP address as the source.
+  `false` - Use the network interface IP address as the source.
 `PreserveClientIp` is only supported on IPv4 EC2 Instance Connect Endpoints. To use `PreserveClientIp`, the value for `IpAddressType` must be `ipv4`.
Default: `false`
Type: Boolean
Required: No

 **SecurityGroupId.N**
One or more security groups to associate with the endpoint. If you don't specify a security group, the default security group for your VPC will be associated with the endpoint.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Required: No

 **SubnetId**
The ID of the subnet in which to create the EC2 Instance Connect Endpoint.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the EC2 Instance Connect Endpoint during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateInstanceConnectEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive idempotency token provided by the client in the the request.
Type: String

 **instanceConnectEndpoint**
Information about the EC2 Instance Connect Endpoint.
Type: [Ec2InstanceConnectEndpoint](API_Ec2InstanceConnectEndpoint.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateInstanceConnectEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateInstanceConnectEndpoint_Examples"></a>

### Example: Create an EC2 Instance Connect Endpoint
<a name="API_CreateInstanceConnectEndpoint_Example_1"></a>

This example creates an EC2 Instance Connect Endpoint in the specified subnet.

#### Sample Request
<a name="API_CreateInstanceConnectEndpoint_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateInstanceConnectEndpoint
&SubnetId=subnet-0123456789example
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateInstanceConnectEndpoint_Example_1_Response"></a>

```
<CreateInstanceConnectEndpointResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>a9effc88-e86c-4730-b1e8-30ba091babd1</requestId>
  <instanceConnectEndpoint>
    <createdAt>2023-06-06T20:01:31.000Z</createdAt>
    <instanceConnectEndpointArn>arn:aws:ec2:region:account-id:instance-connect-endpoint/eice-0123456789example</instanceConnectEndpointArn>
    <instanceConnectEndpointId>eice-0123456789example</instanceConnectEndpointId>
    <networkInterfaceIdSet />
    <ownerId>account-id</ownerId>
    <preserveClientIp>false</preserveClientIp>
    <securityGroupIdSet>
      <item>sg-0123456789example</item>
    </securityGroupIdSet>
    <state>create-in-progress</state>
    <stateMessage />
    <subnetId>subnet-0123456789example</subnetId>
    <tagSet />
    <vpcId>vpc-0123456789example</vpcId>
  </instanceConnectEndpoint>
</CreateInstanceConnectEndpointResponse>
```

## See Also
<a name="API_CreateInstanceConnectEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateInstanceConnectEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateInstanceConnectEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateInstanceConnectEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateInstanceConnectEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateInstanceConnectEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateInstanceConnectEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateInstanceConnectEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateInstanceConnectEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateInstanceConnectEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateInstanceConnectEndpoint)
