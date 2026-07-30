---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-promptflownodesourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion PromptFlowNodeSourceConfiguration
<a name="aws-properties-bedrock-flowversion-promptflownodesourceconfiguration"></a>

Contains configurations for a prompt and whether it is from Prompt management or defined inline.

## Syntax
<a name="aws-properties-bedrock-flowversion-promptflownodesourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-promptflownodesourceconfiguration-syntax.json"></a>

```
{
  "[Inline](#cfn-bedrock-flowversion-promptflownodesourceconfiguration-inline)" : {{PromptFlowNodeInlineConfiguration}},
  "[Resource](#cfn-bedrock-flowversion-promptflownodesourceconfiguration-resource)" : {{PromptFlowNodeResourceConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-promptflownodesourceconfiguration-syntax.yaml"></a>

```
  [Inline](#cfn-bedrock-flowversion-promptflownodesourceconfiguration-inline): {{
    PromptFlowNodeInlineConfiguration}}
  [Resource](#cfn-bedrock-flowversion-promptflownodesourceconfiguration-resource): {{
    PromptFlowNodeResourceConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-promptflownodesourceconfiguration-properties"></a>

`Inline`  <a name="cfn-bedrock-flowversion-promptflownodesourceconfiguration-inline"></a>
Contains configurations for a prompt that is defined inline
*Required*: No
*Type*: [PromptFlowNodeInlineConfiguration](aws-properties-bedrock-flowversion-promptflownodeinlineconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resource`  <a name="cfn-bedrock-flowversion-promptflownodesourceconfiguration-resource"></a>
Contains configurations for a prompt from Prompt management.
*Required*: No
*Type*: [PromptFlowNodeResourceConfiguration](aws-properties-bedrock-flowversion-promptflownoderesourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
