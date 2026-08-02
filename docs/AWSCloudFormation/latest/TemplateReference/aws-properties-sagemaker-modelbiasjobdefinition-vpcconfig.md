---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelBiasJobDefinition VpcConfig
<a name="aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig"></a>

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).

## Syntax
<a name="aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[Subnets](#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-securitygroupids): {{
    - String}}
  [Subnets](#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-sagemaker-modelbiasjobdefinition-vpcconfig-securitygroupids"></a>
The VPC security group IDs, in the form `sg-xxxxxxxx`. Specify the security groups for the VPC that is specified in the `Subnets` field.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `32 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subnets`  <a name="cfn-sagemaker-modelbiasjobdefinition-vpcconfig-subnets"></a>
The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html).
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `32 | 16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
