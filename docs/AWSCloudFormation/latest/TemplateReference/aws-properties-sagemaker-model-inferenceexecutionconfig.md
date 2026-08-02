---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-model-inferenceexecutionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Model InferenceExecutionConfig
<a name="aws-properties-sagemaker-model-inferenceexecutionconfig"></a>

Specifies details about how containers in a multi-container endpoint are run.

## Syntax
<a name="aws-properties-sagemaker-model-inferenceexecutionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-model-inferenceexecutionconfig-syntax.json"></a>

```
{
  "[Mode](#cfn-sagemaker-model-inferenceexecutionconfig-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-model-inferenceexecutionconfig-syntax.yaml"></a>

```
  [Mode](#cfn-sagemaker-model-inferenceexecutionconfig-mode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-model-inferenceexecutionconfig-properties"></a>

`Mode`  <a name="cfn-sagemaker-model-inferenceexecutionconfig-mode"></a>
How containers in a multi-container are run. The following values are valid.
+ `Serial` - Containers run as a serial pipeline.
+ `Direct` - Only the individual container that you specify is run.
*Required*: Yes
*Type*: String
*Allowed values*: `Serial | Direct`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
