---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-webapp-vpc.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::WebApp Vpc
<a name="aws-properties-transfer-webapp-vpc"></a>

Contains the VPC configuration settings for hosting a web app endpoint, including the VPC ID, subnet IDs, and security group IDs for access control.

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
The IP address type for the web app's VPC endpoint. This determines whether the endpoint is accessible over IPv4 only, or over both IPv4 and IPv6.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUALSTACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-transfer-webapp-vpc-securitygroupids"></a>
The list of security group IDs that control access to the web app endpoint. These security groups determine which sources can access the endpoint based on IP addresses and port configurations.
*Required*: No
*Type*: Array of String
*Minimum*: `11`
*Maximum*: `20 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-transfer-webapp-vpc-subnetids"></a>
The list of subnet IDs within the VPC where the web app endpoint will be deployed. These subnets must be in the same VPC specified in the VpcId parameter.
*Required*: No
*Type*: Array of String
*Minimum*: `15`
*Maximum*: `24 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-transfer-webapp-vpc-vpcid"></a>
The identifier of the VPC where the web app endpoint will be hosted.
*Required*: No
*Type*: String
*Pattern*: `^vpc-[0-9a-f]{8,17}$`
*Minimum*: `12`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
