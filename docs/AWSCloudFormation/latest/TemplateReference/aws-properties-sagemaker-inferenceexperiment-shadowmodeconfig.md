---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferenceexperiment-shadowmodeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceExperiment ShadowModeConfig
<a name="aws-properties-sagemaker-inferenceexperiment-shadowmodeconfig"></a>

 The configuration of `ShadowMode` inference experiment type, which specifies a production variant to take all the inference requests, and a shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant it also specifies the percentage of requests that Amazon SageMaker replicates.

## Syntax
<a name="aws-properties-sagemaker-inferenceexperiment-shadowmodeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferenceexperiment-shadowmodeconfig-syntax.json"></a>

```
{
  "[ShadowModelVariants](#cfn-sagemaker-inferenceexperiment-shadowmodeconfig-shadowmodelvariants)" : {{[ ShadowModelVariantConfig, ... ]}},
  "[SourceModelVariantName](#cfn-sagemaker-inferenceexperiment-shadowmodeconfig-sourcemodelvariantname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferenceexperiment-shadowmodeconfig-syntax.yaml"></a>

```
  [ShadowModelVariants](#cfn-sagemaker-inferenceexperiment-shadowmodeconfig-shadowmodelvariants): {{
    - ShadowModelVariantConfig}}
  [SourceModelVariantName](#cfn-sagemaker-inferenceexperiment-shadowmodeconfig-sourcemodelvariantname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferenceexperiment-shadowmodeconfig-properties"></a>

`ShadowModelVariants`  <a name="cfn-sagemaker-inferenceexperiment-shadowmodeconfig-shadowmodelvariants"></a>
List of shadow variant configurations.
*Required*: Yes
*Type*: Array of [ShadowModelVariantConfig](aws-properties-sagemaker-inferenceexperiment-shadowmodelvariantconfig.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceModelVariantName`  <a name="cfn-sagemaker-inferenceexperiment-shadowmodeconfig-sourcemodelvariantname"></a>
 The name of the production variant, which takes all the inference requests.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
