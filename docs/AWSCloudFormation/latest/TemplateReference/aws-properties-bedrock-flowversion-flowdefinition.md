---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-flowdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion FlowDefinition
<a name="aws-properties-bedrock-flowversion-flowdefinition"></a>

The definition of the nodes and connections between nodes in the flow.

## Syntax
<a name="aws-properties-bedrock-flowversion-flowdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-flowdefinition-syntax.json"></a>

```
{
  "[Connections](#cfn-bedrock-flowversion-flowdefinition-connections)" : {{[ FlowConnection, ... ]}},
  "[Nodes](#cfn-bedrock-flowversion-flowdefinition-nodes)" : {{[ FlowNode, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-flowdefinition-syntax.yaml"></a>

```
  [Connections](#cfn-bedrock-flowversion-flowdefinition-connections): {{
    - FlowConnection}}
  [Nodes](#cfn-bedrock-flowversion-flowdefinition-nodes): {{
    - FlowNode}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-flowdefinition-properties"></a>

`Connections`  <a name="cfn-bedrock-flowversion-flowdefinition-connections"></a>
An array of connection definitions in the flow.
*Required*: No
*Type*: Array of [FlowConnection](aws-properties-bedrock-flowversion-flowconnection.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Nodes`  <a name="cfn-bedrock-flowversion-flowdefinition-nodes"></a>
An array of node definitions in the flow.
*Required*: No
*Type*: Array of [FlowNode](aws-properties-bedrock-flowversion-flownode.md)
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
