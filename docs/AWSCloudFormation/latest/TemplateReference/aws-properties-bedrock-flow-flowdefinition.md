---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-flowdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow FlowDefinition
<a name="aws-properties-bedrock-flow-flowdefinition"></a>

The definition of the nodes and connections between nodes in the flow.

## Syntax
<a name="aws-properties-bedrock-flow-flowdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-flowdefinition-syntax.json"></a>

```
{
  "[Connections](#cfn-bedrock-flow-flowdefinition-connections)" : {{[ FlowConnection, ... ]}},
  "[Nodes](#cfn-bedrock-flow-flowdefinition-nodes)" : {{[ FlowNode, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-flowdefinition-syntax.yaml"></a>

```
  [Connections](#cfn-bedrock-flow-flowdefinition-connections): {{
    - FlowConnection}}
  [Nodes](#cfn-bedrock-flow-flowdefinition-nodes): {{
    - FlowNode}}
```

## Properties
<a name="aws-properties-bedrock-flow-flowdefinition-properties"></a>

`Connections`  <a name="cfn-bedrock-flow-flowdefinition-connections"></a>
An array of connection definitions in the flow.
*Required*: No
*Type*: Array of [FlowConnection](aws-properties-bedrock-flow-flowconnection.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Nodes`  <a name="cfn-bedrock-flow-flowdefinition-nodes"></a>
An array of node definitions in the flow.
*Required*: No
*Type*: Array of [FlowNode](aws-properties-bedrock-flow-flownode.md)
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
