---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferenceexperiment-modelvariantconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceExperiment ModelVariantConfig
<a name="aws-properties-sagemaker-inferenceexperiment-modelvariantconfig"></a>

Contains information about the deployment options of a model.

## Syntax
<a name="aws-properties-sagemaker-inferenceexperiment-modelvariantconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferenceexperiment-modelvariantconfig-syntax.json"></a>

```
{
  "[InfrastructureConfig](#cfn-sagemaker-inferenceexperiment-modelvariantconfig-infrastructureconfig)" : {{ModelInfrastructureConfig}},
  "[ModelName](#cfn-sagemaker-inferenceexperiment-modelvariantconfig-modelname)" : {{String}},
  "[VariantName](#cfn-sagemaker-inferenceexperiment-modelvariantconfig-variantname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferenceexperiment-modelvariantconfig-syntax.yaml"></a>

```
  [InfrastructureConfig](#cfn-sagemaker-inferenceexperiment-modelvariantconfig-infrastructureconfig): {{
    ModelInfrastructureConfig}}
  [ModelName](#cfn-sagemaker-inferenceexperiment-modelvariantconfig-modelname): {{String}}
  [VariantName](#cfn-sagemaker-inferenceexperiment-modelvariantconfig-variantname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferenceexperiment-modelvariantconfig-properties"></a>

`InfrastructureConfig`  <a name="cfn-sagemaker-inferenceexperiment-modelvariantconfig-infrastructureconfig"></a>
The configuration for the infrastructure that the model will be deployed to.
*Required*: Yes
*Type*: [ModelInfrastructureConfig](aws-properties-sagemaker-inferenceexperiment-modelinfrastructureconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelName`  <a name="cfn-sagemaker-inferenceexperiment-modelvariantconfig-modelname"></a>
The name of the Amazon SageMaker Model entity.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VariantName`  <a name="cfn-sagemaker-inferenceexperiment-modelvariantconfig-variantname"></a>
The name of the variant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
