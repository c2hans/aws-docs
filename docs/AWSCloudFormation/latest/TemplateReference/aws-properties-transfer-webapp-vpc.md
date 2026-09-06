---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-webapp-vpc.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::WebApp Vpc
<a name="aws-properties-transfer-webapp-vpc"></a>

<a name="aws-properties-transfer-webapp-vpc-description"></a>The `Vpc` property type specifies Property description not available. for an [AWS::Transfer::WebApp](aws-resource-transfer-webapp.md).

## Syntax
<a name="aws-properties-transfer-webapp-vpc-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-webapp-vpc-syntax.json"></a>

```
{
  "[IpAddressType](#cfn-transfer-webapp-vpc-ipaddresstype)" : {{String}},
  "[SecurityGroupIds](#cfn-transfer-webapp-vpc-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-transfer-webapp-vpc-subnetids)" : {{[ String, ... ]}},
  "[VpcId](#cfn-transfer-webapp-vpc-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-webapp-vpc-syntax.yaml"></a>

```
  [IpAddressType](#cfn-transfer-webapp-vpc-ipaddresstype): {{String}}
  [SecurityGroupIds](#cfn-transfer-webapp-vpc-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-transfer-webapp-vpc-subnetids): {{
    - String}}
  [VpcId](#cfn-transfer-webapp-vpc-vpcid): {{String}}
```

## Properties
<a name="aws-properties-transfer-webapp-vpc-properties"></a>

`IpAddressType`  <a name="cfn-transfer-webapp-vpc-ipaddresstype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUALSTACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-transfer-webapp-vpc-securitygroupids"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `11`
*Maximum*: `20 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-transfer-webapp-vpc-subnetids"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `15`
*Maximum*: `24 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-transfer-webapp-vpc-vpcid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^vpc-[0-9a-f]{8,17}$`
*Minimum*: `12`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
