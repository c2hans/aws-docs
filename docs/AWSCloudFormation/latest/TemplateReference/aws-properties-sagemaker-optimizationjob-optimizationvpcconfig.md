---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-optimizationjob-optimizationvpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::OptimizationJob OptimizationVpcConfig
<a name="aws-properties-sagemaker-optimizationjob-optimizationvpcconfig"></a>

A VPC in Amazon VPC that's accessible to an optimized that you create with an optimization job. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).

## Syntax
<a name="aws-properties-sagemaker-optimizationjob-optimizationvpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-optimizationjob-optimizationvpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-sagemaker-optimizationjob-optimizationvpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[Subnets](#cfn-sagemaker-optimizationjob-optimizationvpcconfig-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-optimizationjob-optimizationvpcconfig-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-sagemaker-optimizationjob-optimizationvpcconfig-securitygroupids): {{
    - String}}
  [Subnets](#cfn-sagemaker-optimizationjob-optimizationvpcconfig-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-optimizationjob-optimizationvpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-sagemaker-optimizationjob-optimizationvpcconfig-securitygroupids"></a>
The VPC security group IDs, in the form `sg-xxxxxxxx`. Specify the security groups for the VPC that is specified in the `Subnets` field.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `32 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subnets`  <a name="cfn-sagemaker-optimizationjob-optimizationvpcconfig-subnets"></a>
The ID of the subnets in the VPC to which you want to connect your optimized model.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `32 | 16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
