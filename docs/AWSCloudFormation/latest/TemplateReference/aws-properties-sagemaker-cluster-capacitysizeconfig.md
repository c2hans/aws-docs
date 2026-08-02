---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-capacitysizeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster CapacitySizeConfig
<a name="aws-properties-sagemaker-cluster-capacitysizeconfig"></a>

The configuration of the size measurements of the AMI update. Using this configuration, you can specify whether SageMaker should update your instance group by an amount or percentage of instances.

## Syntax
<a name="aws-properties-sagemaker-cluster-capacitysizeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-capacitysizeconfig-syntax.json"></a>

```
{
  "[Type](#cfn-sagemaker-cluster-capacitysizeconfig-type)" : {{String}},
  "[Value](#cfn-sagemaker-cluster-capacitysizeconfig-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-capacitysizeconfig-syntax.yaml"></a>

```
  [Type](#cfn-sagemaker-cluster-capacitysizeconfig-type): {{String}}
  [Value](#cfn-sagemaker-cluster-capacitysizeconfig-value): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-capacitysizeconfig-properties"></a>

`Type`  <a name="cfn-sagemaker-cluster-capacitysizeconfig-type"></a>
Specifies whether SageMaker should process the update by amount or percentage of instances.
*Required*: Yes
*Type*: String
*Pattern*: `INSTANCE_COUNT|CAPACITY_PERCENTAGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-cluster-capacitysizeconfig-value"></a>
Specifies the amount or percentage of instances SageMaker updates at a time.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
