---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-collectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob CollectionConfiguration
<a name="aws-properties-sagemaker-trainingjob-collectionconfiguration"></a>

Configuration information for the Amazon SageMaker Debugger output tensor collections.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-collectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-collectionconfiguration-syntax.json"></a>

```
{
  "[CollectionName](#cfn-sagemaker-trainingjob-collectionconfiguration-collectionname)" : {{String}},
  "[CollectionParameters](#cfn-sagemaker-trainingjob-collectionconfiguration-collectionparameters)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-collectionconfiguration-syntax.yaml"></a>

```
  [CollectionName](#cfn-sagemaker-trainingjob-collectionconfiguration-collectionname): {{String}}
  [CollectionParameters](#cfn-sagemaker-trainingjob-collectionconfiguration-collectionparameters): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-collectionconfiguration-properties"></a>

`CollectionName`  <a name="cfn-sagemaker-trainingjob-collectionconfiguration-collectionname"></a>
The name of the tensor collection. The name must be unique relative to other rule configuration names.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CollectionParameters`  <a name="cfn-sagemaker-trainingjob-collectionconfiguration-collectionparameters"></a>
Parameter values for the tensor collection. The allowed parameters are `"name"`, `"include_regex"`, `"reduction_config"`, `"save_config"`, `"tensor_names"`, and `"save_histogram"`.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
