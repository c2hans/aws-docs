---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccessendpoint-cidroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessEndpoint CidrOptions
<a name="aws-properties-ec2-verifiedaccessendpoint-cidroptions"></a>

Describes the CIDR options for a Verified Access endpoint.

## Syntax
<a name="aws-properties-ec2-verifiedaccessendpoint-cidroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccessendpoint-cidroptions-syntax.json"></a>

```
{
  "[Cidr](#cfn-ec2-verifiedaccessendpoint-cidroptions-cidr)" : {{String}},
  "[PortRanges](#cfn-ec2-verifiedaccessendpoint-cidroptions-portranges)" : {{[ PortRange, ... ]}},
  "[Protocol](#cfn-ec2-verifiedaccessendpoint-cidroptions-protocol)" : {{String}},
  "[SubnetIds](#cfn-ec2-verifiedaccessendpoint-cidroptions-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccessendpoint-cidroptions-syntax.yaml"></a>

```
  [Cidr](#cfn-ec2-verifiedaccessendpoint-cidroptions-cidr): {{String}}
  [PortRanges](#cfn-ec2-verifiedaccessendpoint-cidroptions-portranges): {{
    - PortRange}}
  [Protocol](#cfn-ec2-verifiedaccessendpoint-cidroptions-protocol): {{String}}
  [SubnetIds](#cfn-ec2-verifiedaccessendpoint-cidroptions-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccessendpoint-cidroptions-properties"></a>

`Cidr`  <a name="cfn-ec2-verifiedaccessendpoint-cidroptions-cidr"></a>
The CIDR.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PortRanges`  <a name="cfn-ec2-verifiedaccessendpoint-cidroptions-portranges"></a>
The port ranges.
*Required*: No
*Type*: Array of [PortRange](aws-properties-ec2-verifiedaccessendpoint-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-ec2-verifiedaccessendpoint-cidroptions-protocol"></a>
The protocol.
*Required*: No
*Type*: String
*Allowed values*: `http | https | tcp`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-ec2-verifiedaccessendpoint-cidroptions-subnetids"></a>
The IDs of the subnets.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
