---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-promptinferenceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion PromptInferenceConfiguration
<a name="aws-properties-bedrock-promptversion-promptinferenceconfiguration"></a>

Contains inference configurations for the prompt.

## Syntax
<a name="aws-properties-bedrock-promptversion-promptinferenceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-promptinferenceconfiguration-syntax.json"></a>

```
{
  "[Text](#cfn-bedrock-promptversion-promptinferenceconfiguration-text)" : {{PromptModelInferenceConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-promptinferenceconfiguration-syntax.yaml"></a>

```
  [Text](#cfn-bedrock-promptversion-promptinferenceconfiguration-text): {{
    PromptModelInferenceConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-promptinferenceconfiguration-properties"></a>

`Text`  <a name="cfn-bedrock-promptversion-promptinferenceconfiguration-text"></a>
Contains inference configurations for a text prompt.
*Required*: Yes
*Type*: [PromptModelInferenceConfiguration](aws-properties-bedrock-promptversion-promptmodelinferenceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
