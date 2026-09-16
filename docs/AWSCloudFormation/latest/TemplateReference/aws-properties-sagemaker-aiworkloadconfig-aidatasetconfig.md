---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-aiworkloadconfig-aidatasetconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AIWorkloadConfig AIDatasetConfig
<a name="aws-properties-sagemaker-aiworkloadconfig-aidatasetconfig"></a>

The dataset configuration for an AI workload. This is a union type — specify one of the members.

## Syntax
<a name="aws-properties-sagemaker-aiworkloadconfig-aidatasetconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-aiworkloadconfig-aidatasetconfig-syntax.json"></a>

```
{
  "[InputDataConfig](#cfn-sagemaker-aiworkloadconfig-aidatasetconfig-inputdataconfig)" : {{[ AIWorkloadInputDataConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-aiworkloadconfig-aidatasetconfig-syntax.yaml"></a>

```
  [InputDataConfig](#cfn-sagemaker-aiworkloadconfig-aidatasetconfig-inputdataconfig): {{
    - AIWorkloadInputDataConfig}}
```

## Properties
<a name="aws-properties-sagemaker-aiworkloadconfig-aidatasetconfig-properties"></a>

`InputDataConfig`  <a name="cfn-sagemaker-aiworkloadconfig-aidatasetconfig-inputdataconfig"></a>
An array of input data channel configurations for the workload.
*Required*: Yes
*Type*: Array of [AIWorkloadInputDataConfig](aws-properties-sagemaker-aiworkloadconfig-aiworkloadinputdataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
