---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-trainingenvironment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard TrainingEnvironment
<a name="aws-properties-sagemaker-modelcard-trainingenvironment"></a>

SageMaker AI training image.

## Syntax
<a name="aws-properties-sagemaker-modelcard-trainingenvironment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-trainingenvironment-syntax.json"></a>

```
{
  "[ContainerImage](#cfn-sagemaker-modelcard-trainingenvironment-containerimage)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-trainingenvironment-syntax.yaml"></a>

```
  [ContainerImage](#cfn-sagemaker-modelcard-trainingenvironment-containerimage): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-trainingenvironment-properties"></a>

`ContainerImage`  <a name="cfn-sagemaker-modelcard-trainingenvironment-containerimage"></a>
SageMaker AI inference image URI.
*Required*: No
*Type*: Array of String
*Maximum*: `1024 | 15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
