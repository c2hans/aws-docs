---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster VpcConfig
<a name="aws-properties-sagemaker-cluster-vpcconfig"></a>

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).

## Syntax
<a name="aws-properties-sagemaker-cluster-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-sagemaker-cluster-vpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[Subnets](#cfn-sagemaker-cluster-vpcconfig-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-sagemaker-cluster-vpcconfig-securitygroupids): {{
    - String}}
  [Subnets](#cfn-sagemaker-cluster-vpcconfig-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-vpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-sagemaker-cluster-vpcconfig-securitygroupids"></a>
The VPC security group IDs, in the form `sg-xxxxxxxx`. Specify the security groups for the VPC that is specified in the `Subnets` field.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `32 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-sagemaker-cluster-vpcconfig-subnets"></a>
The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html).
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `32 | 16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
