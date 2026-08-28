---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-promptflownodesourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow PromptFlowNodeSourceConfiguration
<a name="aws-properties-bedrock-flow-promptflownodesourceconfiguration"></a>

Contains configurations for a prompt and whether it is from Prompt management or defined inline.

## Syntax
<a name="aws-properties-bedrock-flow-promptflownodesourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-promptflownodesourceconfiguration-syntax.json"></a>

```
{
  "[Inline](#cfn-bedrock-flow-promptflownodesourceconfiguration-inline)" : {{PromptFlowNodeInlineConfiguration}},
  "[Resource](#cfn-bedrock-flow-promptflownodesourceconfiguration-resource)" : {{PromptFlowNodeResourceConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-promptflownodesourceconfiguration-syntax.yaml"></a>

```
  [Inline](#cfn-bedrock-flow-promptflownodesourceconfiguration-inline): {{
    PromptFlowNodeInlineConfiguration}}
  [Resource](#cfn-bedrock-flow-promptflownodesourceconfiguration-resource): {{
    PromptFlowNodeResourceConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-flow-promptflownodesourceconfiguration-properties"></a>

`Inline`  <a name="cfn-bedrock-flow-promptflownodesourceconfiguration-inline"></a>
Contains configurations for a prompt that is defined inline
*Required*: No
*Type*: [PromptFlowNodeInlineConfiguration](aws-properties-bedrock-flow-promptflownodeinlineconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resource`  <a name="cfn-bedrock-flow-promptflownodesourceconfiguration-resource"></a>
Contains configurations for a prompt from Prompt management.
*Required*: No
*Type*: [PromptFlowNodeResourceConfiguration](aws-properties-bedrock-flow-promptflownoderesourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
