---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-promptgenairesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt PromptGenAiResource
<a name="aws-properties-bedrock-prompt-promptgenairesource"></a>

Contains specifications for a generative AI resource with which to use the prompt. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html).

## Syntax
<a name="aws-properties-bedrock-prompt-promptgenairesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-promptgenairesource-syntax.json"></a>

```
{
  "[Agent](#cfn-bedrock-prompt-promptgenairesource-agent)" : {{PromptAgentResource}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-promptgenairesource-syntax.yaml"></a>

```
  [Agent](#cfn-bedrock-prompt-promptgenairesource-agent): {{
    PromptAgentResource}}
```

## Properties
<a name="aws-properties-bedrock-prompt-promptgenairesource-properties"></a>

`Agent`  <a name="cfn-bedrock-prompt-promptgenairesource-agent"></a>
Specifies an Amazon Bedrock agent with which to use the prompt.
*Required*: Yes
*Type*: [PromptAgentResource](aws-properties-bedrock-prompt-promptagentresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
