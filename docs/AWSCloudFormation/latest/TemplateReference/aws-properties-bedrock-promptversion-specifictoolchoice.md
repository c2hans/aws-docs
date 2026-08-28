---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-specifictoolchoice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion SpecificToolChoice
<a name="aws-properties-bedrock-promptversion-specifictoolchoice"></a>

The model must request a specific tool. For example, `{"tool" : {"name" : "Your tool name"}}`. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide

**Note**
This field is only supported by Anthropic Claude 3 models.

## Syntax
<a name="aws-properties-bedrock-promptversion-specifictoolchoice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-specifictoolchoice-syntax.json"></a>

```
{
  "[Name](#cfn-bedrock-promptversion-specifictoolchoice-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-specifictoolchoice-syntax.yaml"></a>

```
  [Name](#cfn-bedrock-promptversion-specifictoolchoice-name): {{String}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-specifictoolchoice-properties"></a>

`Name`  <a name="cfn-bedrock-promptversion-specifictoolchoice-name"></a>
The name of the tool that the model must request.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
