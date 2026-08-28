---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-modeloverview.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard ModelOverview
<a name="aws-properties-sagemaker-modelcard-modeloverview"></a>

An overview about the model.

## Syntax
<a name="aws-properties-sagemaker-modelcard-modeloverview-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-modeloverview-syntax.json"></a>

```
{
  "[AlgorithmType](#cfn-sagemaker-modelcard-modeloverview-algorithmtype)" : {{String}},
  "[InferenceEnvironment](#cfn-sagemaker-modelcard-modeloverview-inferenceenvironment)" : {{InferenceEnvironment}},
  "[ModelArtifact](#cfn-sagemaker-modelcard-modeloverview-modelartifact)" : {{[ String, ... ]}},
  "[ModelCreator](#cfn-sagemaker-modelcard-modeloverview-modelcreator)" : {{String}},
  "[ModelDescription](#cfn-sagemaker-modelcard-modeloverview-modeldescription)" : {{String}},
  "[ModelId](#cfn-sagemaker-modelcard-modeloverview-modelid)" : {{String}},
  "[ModelName](#cfn-sagemaker-modelcard-modeloverview-modelname)" : {{String}},
  "[ModelOwner](#cfn-sagemaker-modelcard-modeloverview-modelowner)" : {{String}},
  "[ModelVersion](#cfn-sagemaker-modelcard-modeloverview-modelversion)" : {{Number}},
  "[ProblemType](#cfn-sagemaker-modelcard-modeloverview-problemtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-modeloverview-syntax.yaml"></a>

```
  [AlgorithmType](#cfn-sagemaker-modelcard-modeloverview-algorithmtype): {{String}}
  [InferenceEnvironment](#cfn-sagemaker-modelcard-modeloverview-inferenceenvironment): {{
    InferenceEnvironment}}
  [ModelArtifact](#cfn-sagemaker-modelcard-modeloverview-modelartifact): {{
    - String}}
  [ModelCreator](#cfn-sagemaker-modelcard-modeloverview-modelcreator): {{String}}
  [ModelDescription](#cfn-sagemaker-modelcard-modeloverview-modeldescription): {{String}}
  [ModelId](#cfn-sagemaker-modelcard-modeloverview-modelid): {{String}}
  [ModelName](#cfn-sagemaker-modelcard-modeloverview-modelname): {{String}}
  [ModelOwner](#cfn-sagemaker-modelcard-modeloverview-modelowner): {{String}}
  [ModelVersion](#cfn-sagemaker-modelcard-modeloverview-modelversion): {{Number}}
  [ProblemType](#cfn-sagemaker-modelcard-modeloverview-problemtype): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-modeloverview-properties"></a>

`AlgorithmType`  <a name="cfn-sagemaker-modelcard-modeloverview-algorithmtype"></a>
The algorithm used to solve the problem.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceEnvironment`  <a name="cfn-sagemaker-modelcard-modeloverview-inferenceenvironment"></a>
An overview about model inference.
*Required*: No
*Type*: [InferenceEnvironment](aws-properties-sagemaker-modelcard-inferenceenvironment.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelArtifact`  <a name="cfn-sagemaker-modelcard-modeloverview-modelartifact"></a>
The location of the model artifact.
*Required*: No
*Type*: Array of String
*Maximum*: `1024 | 15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelCreator`  <a name="cfn-sagemaker-modelcard-modeloverview-modelcreator"></a>
The creator of the model.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelDescription`  <a name="cfn-sagemaker-modelcard-modeloverview-modeldescription"></a>
A description of the model.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-sagemaker-modelcard-modeloverview-modelid"></a>
The SageMaker AI Model ARN or non-SageMaker AI Model ID.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelName`  <a name="cfn-sagemaker-modelcard-modeloverview-modelname"></a>
The name of the model.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelOwner`  <a name="cfn-sagemaker-modelcard-modeloverview-modelowner"></a>
The owner of the model.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelVersion`  <a name="cfn-sagemaker-modelcard-modeloverview-modelversion"></a>
The version of the model.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProblemType`  <a name="cfn-sagemaker-modelcard-modeloverview-problemtype"></a>
The problem being solved with the model.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
