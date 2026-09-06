---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-configuration-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Configuration VpcConfig
<a name="aws-properties-omics-configuration-vpcconfig"></a>

VPC configuration for workflow runs.

## Syntax
<a name="aws-properties-omics-configuration-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-configuration-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-omics-configuration-vpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-omics-configuration-vpcconfig-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-omics-configuration-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-omics-configuration-vpcconfig-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-omics-configuration-vpcconfig-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-omics-configuration-vpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-omics-configuration-vpcconfig-securitygroupids"></a>
List of security group IDs. Maximum of 5 security groups allowed.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-omics-configuration-vpcconfig-subnetids"></a>
List of subnet IDs. Maximum of 16 subnets allowed.
*Required*: No
*Type*: Array of String
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
