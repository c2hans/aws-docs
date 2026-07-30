---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-fleet-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Fleet VpcConfig
<a name="aws-properties-codebuild-fleet-vpcconfig"></a>

Information about the VPC configuration that AWS CodeBuild accesses.

## Syntax
<a name="aws-properties-codebuild-fleet-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-fleet-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-codebuild-fleet-vpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[Subnets](#cfn-codebuild-fleet-vpcconfig-subnets)" : {{[ String, ... ]}},
  "[VpcId](#cfn-codebuild-fleet-vpcconfig-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-codebuild-fleet-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-codebuild-fleet-vpcconfig-securitygroupids): {{
    - String}}
  [Subnets](#cfn-codebuild-fleet-vpcconfig-subnets): {{
    - String}}
  [VpcId](#cfn-codebuild-fleet-vpcconfig-vpcid): {{String}}
```

## Properties
<a name="aws-properties-codebuild-fleet-vpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-codebuild-fleet-vpcconfig-securitygroupids"></a>
A list of one or more security groups IDs in your Amazon VPC.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-codebuild-fleet-vpcconfig-subnets"></a>
A list of one or more subnet IDs in your Amazon VPC.
*Required*: No
*Type*: Array of String
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-codebuild-fleet-vpcconfig-vpcid"></a>
The ID of the Amazon VPC.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
