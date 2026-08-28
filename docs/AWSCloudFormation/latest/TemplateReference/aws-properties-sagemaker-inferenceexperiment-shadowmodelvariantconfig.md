---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferenceexperiment-shadowmodelvariantconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceExperiment ShadowModelVariantConfig
<a name="aws-properties-sagemaker-inferenceexperiment-shadowmodelvariantconfig"></a>

The name and sampling percentage of a shadow variant.

## Syntax
<a name="aws-properties-sagemaker-inferenceexperiment-shadowmodelvariantconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferenceexperiment-shadowmodelvariantconfig-syntax.json"></a>

```
{
  "[SamplingPercentage](#cfn-sagemaker-inferenceexperiment-shadowmodelvariantconfig-samplingpercentage)" : {{Integer}},
  "[ShadowModelVariantName](#cfn-sagemaker-inferenceexperiment-shadowmodelvariantconfig-shadowmodelvariantname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferenceexperiment-shadowmodelvariantconfig-syntax.yaml"></a>

```
  [SamplingPercentage](#cfn-sagemaker-inferenceexperiment-shadowmodelvariantconfig-samplingpercentage): {{Integer}}
  [ShadowModelVariantName](#cfn-sagemaker-inferenceexperiment-shadowmodelvariantconfig-shadowmodelvariantname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferenceexperiment-shadowmodelvariantconfig-properties"></a>

`SamplingPercentage`  <a name="cfn-sagemaker-inferenceexperiment-shadowmodelvariantconfig-samplingpercentage"></a>
 The percentage of inference requests that Amazon SageMaker replicates from the production variant to the shadow variant.
*Required*: Yes
*Type*: Integer
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShadowModelVariantName`  <a name="cfn-sagemaker-inferenceexperiment-shadowmodelvariantconfig-shadowmodelvariantname"></a>
The name of the shadow variant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
