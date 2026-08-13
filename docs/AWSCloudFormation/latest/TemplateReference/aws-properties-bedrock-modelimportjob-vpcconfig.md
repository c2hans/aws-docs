---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-modelimportjob-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ModelImportJob VpcConfig
<a name="aws-properties-bedrock-modelimportjob-vpcconfig"></a>

The configuration of a virtual private cloud (VPC). For more information, see [Protect your data using Amazon Virtual Private Cloud and AWS PrivateLink](https://docs.aws.amazon.com/bedrock/latest/userguide/usingVPC.html).

## Syntax
<a name="aws-properties-bedrock-modelimportjob-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-modelimportjob-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-bedrock-modelimportjob-vpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-bedrock-modelimportjob-vpcconfig-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-modelimportjob-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-bedrock-modelimportjob-vpcconfig-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-bedrock-modelimportjob-vpcconfig-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-modelimportjob-vpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-bedrock-modelimportjob-vpcconfig-securitygroupids"></a>
An array of IDs for each security group in the VPC to use.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `32 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-bedrock-modelimportjob-vpcconfig-subnetids"></a>
An array of IDs for each subnet in the VPC to use.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `32 | 16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
