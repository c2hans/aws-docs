---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-flownode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow FlowNode
<a name="aws-properties-bedrock-flow-flownode"></a>

Contains configurations about a node in the flow.

## Syntax
<a name="aws-properties-bedrock-flow-flownode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-flownode-syntax.json"></a>

```
{
  "[Configuration](#cfn-bedrock-flow-flownode-configuration)" : {{FlowNodeConfiguration}},
  "[Inputs](#cfn-bedrock-flow-flownode-inputs)" : {{[ FlowNodeInput, ... ]}},
  "[Name](#cfn-bedrock-flow-flownode-name)" : {{String}},
  "[Outputs](#cfn-bedrock-flow-flownode-outputs)" : {{[ FlowNodeOutput, ... ]}},
  "[Type](#cfn-bedrock-flow-flownode-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-flownode-syntax.yaml"></a>

```
  [Configuration](#cfn-bedrock-flow-flownode-configuration): {{
    FlowNodeConfiguration}}
  [Inputs](#cfn-bedrock-flow-flownode-inputs): {{
    - FlowNodeInput}}
  [Name](#cfn-bedrock-flow-flownode-name): {{String}}
  [Outputs](#cfn-bedrock-flow-flownode-outputs): {{
    - FlowNodeOutput}}
  [Type](#cfn-bedrock-flow-flownode-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-flownode-properties"></a>

`Configuration`  <a name="cfn-bedrock-flow-flownode-configuration"></a>
Contains configurations for the node.
*Required*: No
*Type*: [FlowNodeConfiguration](aws-properties-bedrock-flow-flownodeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Inputs`  <a name="cfn-bedrock-flow-flownode-inputs"></a>
An array of objects, each of which contains information about an input into the node.
*Required*: No
*Type*: Array of [FlowNodeInput](aws-properties-bedrock-flow-flownodeinput.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-flow-flownode-name"></a>
A name for the node.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Outputs`  <a name="cfn-bedrock-flow-flownode-outputs"></a>
A list of objects, each of which contains information about an output from the node.
*Required*: No
*Type*: Array of [FlowNodeOutput](aws-properties-bedrock-flow-flownodeoutput.md)
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-flow-flownode-type"></a>
The type of node. This value must match the name of the key that you provide in the configuration you provide in the `FlowNodeConfiguration` field.
*Required*: Yes
*Type*: String
*Allowed values*: `Input | Output | KnowledgeBase | Condition | Lex | Prompt | LambdaFunction | Agent | Storage | Retrieval | Iterator | Collector | InlineCode | Loop | LoopInput | LoopController`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
