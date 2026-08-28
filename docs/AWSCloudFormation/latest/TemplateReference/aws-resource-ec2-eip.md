---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eip.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EIP
<a name="aws-resource-ec2-eip"></a>

Specifies an Elastic IP (EIP) address and can, optionally, associate it with an Amazon EC2 instance.

You can allocate an Elastic IP address from an address pool owned by AWS or from an address pool created from a public IPv4 address range that you have brought to AWS for use with your AWS resources using bring your own IP addresses (BYOIP). For more information, see [Bring Your Own IP Addresses (BYOIP)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html) in the *Amazon EC2 User Guide*.

For more information, see [Elastic IP Addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-resource-ec2-eip-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-eip-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::EIP",
  "Properties" : {
      "[Address](#cfn-ec2-eip-address)" : {{String}},
      "[Domain](#cfn-ec2-eip-domain)" : {{String}},
      "[InstanceId](#cfn-ec2-eip-instanceid)" : {{String}},
      "[IpamPoolId](#cfn-ec2-eip-ipampoolid)" : {{String}},
      "[NetworkBorderGroup](#cfn-ec2-eip-networkbordergroup)" : {{String}},
      "[PublicIpv4Pool](#cfn-ec2-eip-publicipv4pool)" : {{String}},
      "[Tags](#cfn-ec2-eip-tags)" : {{[ Tag, ... ]}},
      "[TransferAddress](#cfn-ec2-eip-transferaddress)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-eip-syntax.yaml"></a>

```
Type: AWS::EC2::EIP
Properties:
  [Address](#cfn-ec2-eip-address): {{String}}
  [Domain](#cfn-ec2-eip-domain): {{String}}
  [InstanceId](#cfn-ec2-eip-instanceid): {{String}}
  [IpamPoolId](#cfn-ec2-eip-ipampoolid): {{String}}
  [NetworkBorderGroup](#cfn-ec2-eip-networkbordergroup): {{String}}
  [PublicIpv4Pool](#cfn-ec2-eip-publicipv4pool): {{String}}
  [Tags](#cfn-ec2-eip-tags): {{
    - Tag}}
  [TransferAddress](#cfn-ec2-eip-transferaddress): {{String}}
```

## Properties
<a name="aws-resource-ec2-eip-properties"></a>

`Address`  <a name="cfn-ec2-eip-address"></a>
An Elastic IP address or a carrier IP address in a Wavelength Zone.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Domain`  <a name="cfn-ec2-eip-domain"></a>
The network (`vpc`).
If you define an Elastic IP address and associate it with a VPC that is defined in the same template, you must declare a dependency on the VPC-gateway attachment by using the [ DependsOn Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html) on this resource.
*Required*: No
*Type*: String
*Allowed values*: `vpc | standard`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceId`  <a name="cfn-ec2-eip-instanceid"></a>
The ID of the instance.
Updates to the `InstanceId` property may require *some interruptions*. Updates on an EIP reassociates the address on its associated resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpamPoolId`  <a name="cfn-ec2-eip-ipampoolid"></a>
 The ID of an IPAM pool which has an Amazon-provided or BYOIP public IPv4 CIDR provisioned to it. For more information, see [Allocate sequential Elastic IP addresses from an IPAM pool](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-eip-pool.html) in the *Amazon VPC IPAM User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkBorderGroup`  <a name="cfn-ec2-eip-networkbordergroup"></a>
 A unique set of Availability Zones, Local Zones, or Wavelength Zones from which AWS advertises IP addresses. Use this parameter to limit the IP address to this location. IP addresses cannot move between network border groups.
Use [DescribeAvailabilityZones](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html) to view the network border groups.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PublicIpv4Pool`  <a name="cfn-ec2-eip-publicipv4pool"></a>
The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool.
Updates to the `PublicIpv4Pool` property may require *some interruptions*. Updates on an EIP reassociates the address on its associated resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-eip-tags"></a>
Any tags assigned to the Elastic IP address.
Updates to the `Tags` property may require *some interruptions*. Updates on an EIP reassociates the address on its associated resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-eip-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransferAddress`  <a name="cfn-ec2-eip-transferaddress"></a>
The Elastic IP address you are accepting for transfer. You can only accept one transferred address. For more information on Elastic IP address transfers, see [Transfer Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#transfer-EIPs-intro) in the *Amazon Virtual Private Cloud User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-eip-return-values"></a>

### Ref
<a name="aws-resource-ec2-eip-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Elastic IP address.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-eip-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-eip-return-values-fn--getatt-fn--getatt"></a>

`AllocationId`  <a name="AllocationId-fn::getatt"></a>
The ID that AWS assigns to represent the allocation of the address for use with Amazon VPC. This is returned only for VPC elastic IP addresses. For example, `eipalloc-5723d13e`.

`PublicIp`  <a name="PublicIp-fn::getatt"></a>
The Elastic IP address.

## Examples
<a name="aws-resource-ec2-eip--examples"></a>

### Allocate an Elastic IP address
<a name="aws-resource-ec2-eip--examples--Allocate_an_Elastic_IP_address"></a>

This example shows how to allocate an Elastic IP address and assign it to an Amazon EC2 instance with the logical name `myInstance`.

#### JSON
<a name="aws-resource-ec2-eip--examples--Allocate_an_Elastic_IP_address--json"></a>

```
"Resources": {
  "myEIP" : {
      "Type" : "AWS::EC2::EIP",
      "Properties" : {
          "InstanceId" : { "Ref" : "myInstance" }
      }
  }
}
```

#### YAML
<a name="aws-resource-ec2-eip--examples--Allocate_an_Elastic_IP_address--yaml"></a>

```
Resources:
  myEIP:
    Type: AWS::EC2::EIP
    Properties:
      InstanceId: !Ref myInstance
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
