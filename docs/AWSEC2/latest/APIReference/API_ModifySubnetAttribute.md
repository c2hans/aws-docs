---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySubnetAttribute.html
---

# ModifySubnetAttribute
<a name="API_ModifySubnetAttribute"></a>

Modifies a subnet attribute. You can only modify one attribute at a time.

Use this action to modify subnets on AWS Outposts.
+ To modify a subnet on an Outpost rack, set both `MapCustomerOwnedIpOnLaunch` and `CustomerOwnedIpv4Pool`. These two parameters act as a single attribute.
+ To modify a subnet on an Outpost server, set either `EnableLniAtDeviceIndex` or `DisableLniAtDeviceIndex`.

For more information about AWS Outposts, see the following:
+  [Outpost servers](https://docs.aws.amazon.com/outposts/latest/userguide/how-servers-work.html)
+  [Outpost racks](https://docs.aws.amazon.com/outposts/latest/userguide/how-racks-work.html)

## Request Parameters
<a name="API_ModifySubnetAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssignIpv6AddressOnCreation**
Specify `true` to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. This includes a network interface that's created when launching an instance into the subnet (the instance therefore receives an IPv6 address).
If you enable the IPv6 addressing feature for your subnet, your network interface or instance only receives an IPv6 address if it's created using version `2016-11-15` or later of the Amazon EC2 API.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **CustomerOwnedIpv4Pool**
The customer-owned IPv4 address pool associated with the subnet.
You must set this value when you specify `true` for `MapCustomerOwnedIpOnLaunch`.
Type: String
Required: No

 **DisableLniAtDeviceIndex**
 Specify `true` to indicate that local network interfaces at the current position should be disabled.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **EnableDns64**
Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.
You must first configure a NAT gateway in a public subnet (separate from the subnet containing the IPv6-only workloads). For example, the subnet containing the NAT gateway should have a `0.0.0.0/0` route pointing to the internet gateway. For more information, see [Configure DNS64 and NAT64](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-nat64-dns64.html#nat-gateway-nat64-dns64-walkthrough) in the *Amazon VPC User Guide*.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **EnableLniAtDeviceIndex**
 Indicates the device position for local network interfaces in this subnet. For example, `1` indicates local network interfaces in this subnet are the secondary network interface (eth1). A local network interface cannot be the primary network interface (eth0).
Type: Integer
Required: No

 **EnableResourceNameDnsAAAARecordOnLaunch**
Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **EnableResourceNameDnsARecordOnLaunch**
Indicates whether to respond to DNS queries for instance hostnames with DNS A records.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **MapCustomerOwnedIpOnLaunch**
Specify `true` to indicate that network interfaces attached to instances created in the specified subnet should be assigned a customer-owned IPv4 address.
When this value is `true`, you must specify the customer-owned IP pool using `CustomerOwnedIpv4Pool`.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **MapPublicIpOnLaunch**
Specify `true` to indicate that network interfaces attached to instances created in the specified subnet should be assigned a public IPv4 address.
 AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [Amazon VPC pricing page](http://aws.amazon.com/vpc/pricing/).
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **PrivateDnsHostnameTypeOnLaunch**
The type of hostname to assign to instances in the subnet at launch. For IPv4-only and dual-stack (IPv4 and IPv6) subnets, an instance DNS name can be based on the instance IPv4 address (ip-name) or the instance ID (resource-name). For IPv6 only subnets, an instance DNS name must be based on the instance ID (resource-name).
Type: String
Valid Values: `ip-name | resource-name`
Required: No

 **SubnetId**
The ID of the subnet.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifySubnetAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ModifySubnetAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifySubnetAttribute_Examples"></a>

### Example 1
<a name="API_ModifySubnetAttribute_Example_1"></a>

This example modifies the attribute for `subnet-1a2b3c4d` to specify that all instances launched into this subnet are assigned a public IPv4 address.

#### Sample Request
<a name="API_ModifySubnetAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifySubnetAttribute
&SubnetId=subnet-1a2b3c4d
&MapPublicIpOnLaunch.Value=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifySubnetAttribute_Example_1_Response"></a>

```
<ModifySubnetAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>c500a0bc-ad14-46c2-b9c5-e24aexample</requestId>
    <return>true</return>
</ModifySubnetAttributeResponse>
```

### Example 2
<a name="API_ModifySubnetAttribute_Example_2"></a>

This example modifies the attribute for `subnet-1a2b3c4d` to specify that all network interfaces created in this subnet (and therefore all instances launched into this subnet with a new network interface) are assigned an IPv6 address.

#### Sample Request
<a name="API_ModifySubnetAttribute_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifySubnetAttribute
&SubnetId=subnet-1a2b3c4d
&AssignIpv6AddressOnCreation.Value=true
&AUTHPARAMS
```

## See Also
<a name="API_ModifySubnetAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifySubnetAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifySubnetAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifySubnetAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifySubnetAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifySubnetAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifySubnetAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifySubnetAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifySubnetAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifySubnetAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifySubnetAttribute)
