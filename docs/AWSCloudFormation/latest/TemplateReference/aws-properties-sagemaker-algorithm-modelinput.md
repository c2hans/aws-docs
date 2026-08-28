---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-algorithm-modelinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Algorithm ModelInput
<a name="aws-properties-sagemaker-algorithm-modelinput"></a>

Input object for the model.

## Syntax
<a name="aws-properties-sagemaker-algorithm-modelinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-algorithm-modelinput-syntax.json"></a>

```
{
  "[DataInputConfig](#cfn-sagemaker-algorithm-modelinput-datainputconfig)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-algorithm-modelinput-syntax.yaml"></a>

```
  [DataInputConfig](#cfn-sagemaker-algorithm-modelinput-datainputconfig): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-algorithm-modelinput-properties"></a>

`DataInputConfig`  <a name="cfn-sagemaker-algorithm-modelinput-datainputconfig"></a>
The input configuration object for the model.
*Required*: Yes
*Type*: String
*Pattern*: `[\S\s]+`
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
