---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-server-endpointdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Server EndpointDetails
<a name="aws-properties-transfer-server-endpointdetails"></a>

The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.

## Syntax
<a name="aws-properties-transfer-server-endpointdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-server-endpointdetails-syntax.json"></a>

```
{
  "[AddressAllocationIds](#cfn-transfer-server-endpointdetails-addressallocationids)" : {{[ String, ... ]}},
  "[SecurityGroupIds](#cfn-transfer-server-endpointdetails-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-transfer-server-endpointdetails-subnetids)" : {{[ String, ... ]}},
  "[VpcEndpointId](#cfn-transfer-server-endpointdetails-vpcendpointid)" : {{String}},
  "[VpcId](#cfn-transfer-server-endpointdetails-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-server-endpointdetails-syntax.yaml"></a>

```
  [AddressAllocationIds](#cfn-transfer-server-endpointdetails-addressallocationids): {{
    - String}}
  [SecurityGroupIds](#cfn-transfer-server-endpointdetails-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-transfer-server-endpointdetails-subnetids): {{
    - String}}
  [VpcEndpointId](#cfn-transfer-server-endpointdetails-vpcendpointid): {{String}}
  [VpcId](#cfn-transfer-server-endpointdetails-vpcid): {{String}}
```

## Properties
<a name="aws-properties-transfer-server-endpointdetails-properties"></a>

`AddressAllocationIds`  <a name="cfn-transfer-server-endpointdetails-addressallocationids"></a>
A list of address allocation IDs that are required to attach an Elastic IP address to your server's endpoint.
An address allocation ID corresponds to the allocation ID of an Elastic IP address. This value can be retrieved from the `allocationId` field from the Amazon EC2 [Address](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Address.html) data type. One way to retrieve this value is by calling the EC2 [DescribeAddresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html) API.
This parameter is optional. Set this parameter if you want to make your VPC endpoint public-facing. For details, see [Create an internet-facing endpoint for your server](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#create-internet-facing-endpoint).
This property can only be set as follows:
+ `EndpointType` must be set to `VPC`
+ The Transfer Family server must be offline.
+ You cannot set this parameter for Transfer Family servers that use the FTP protocol.
+ The server must already have `SubnetIds` populated (`SubnetIds` and `AddressAllocationIds` cannot be updated simultaneously).
+ `AddressAllocationIds` can't contain duplicates, and must be equal in length to `SubnetIds`. For example, if you have three subnet IDs, you must also specify three address allocation IDs.
+ Call the `UpdateServer` API to set or change this parameter.
+ You can't set address allocation IDs for servers that have an `IpAddressType` set to `DUALSTACK` You can only set this property if `IpAddressType` is set to `IPV4`.
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SecurityGroupIds`  <a name="cfn-transfer-server-endpointdetails-securitygroupids"></a>
A list of security groups IDs that are available to attach to your server's endpoint.
While `SecurityGroupIds` appears in the response syntax for consistency with `CreateServer` and `UpdateServer` operations, this field is not populated in `DescribeServer` responses. Security groups are managed at the VPC endpoint level and can be modified outside of the Transfer Family service. To retrieve current security group information, use the EC2 `DescribeVpcEndpoints` API with the `VpcEndpointId` returned in the response.
This property can only be set when `EndpointType` is set to `VPC`.
You can edit the `SecurityGroupIds` property in the [UpdateServer](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateServer.html) API only if you are changing the `EndpointType` from `PUBLIC` or `VPC_ENDPOINT` to `VPC`. To change security groups associated with your server's VPC endpoint after creation, use the Amazon EC2 [ModifyVpcEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html) API.
*Required*: No
*Type*: Array of String
*Minimum*: `11`
*Maximum*: `20`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SubnetIds`  <a name="cfn-transfer-server-endpointdetails-subnetids"></a>
A list of subnet IDs that are required to host your server endpoint in your VPC.
This property can only be set when `EndpointType` is set to `VPC`.
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`VpcEndpointId`  <a name="cfn-transfer-server-endpointdetails-vpcendpointid"></a>
The ID of the VPC endpoint.
 This property can only be set when `EndpointType` is set to `VPC_ENDPOINT` .
*Required*: No
*Type*: String
*Pattern*: `^vpce-[0-9a-f]{17}$`
*Minimum*: `22`
*Maximum*: `22`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`VpcId`  <a name="cfn-transfer-server-endpointdetails-vpcid"></a>
The VPC ID of the virtual private cloud in which the server's endpoint will be hosted.
 This property can only be set when `EndpointType` is set to `VPC` .
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
