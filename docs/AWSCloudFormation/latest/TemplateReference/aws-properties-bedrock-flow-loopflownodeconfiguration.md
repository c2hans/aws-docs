---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-loopflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow LoopFlowNodeConfiguration
<a name="aws-properties-bedrock-flow-loopflownodeconfiguration"></a>

Contains configurations for the nodes of a DoWhile loop in your flow.

A DoWhile loop is made up of the following nodes:
+ `Loop` - The container node that holds the loop's flow definition. This node encompasses the entire loop structure.
+ `LoopInput` - The entry point node for the loop. This node receives inputs from nodes outside the loop and from previous loop iterations.
+ Body nodes - The processing nodes that execute within each loop iteration. These can be nodes for handling data in your flow, such as a prompt or Lambda function nodes. Some node types aren't supported inside a DoWhile loop body. For more information, see [LoopIncompatibleNodeTypeFlowValidationDetails](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_LoopIncompatibleNodeTypeFlowValidationDetails.html).
+ `LoopController` - The node that evaluates whether the loop should continue or exit based on a condition.

These nodes work together to create a loop that runs at least once and continues until a specified condition is met or a maximum number of iterations is reached.

## Syntax
<a name="aws-properties-bedrock-flow-loopflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-loopflownodeconfiguration-syntax.json"></a>

```
{
  "[Definition](#cfn-bedrock-flow-loopflownodeconfiguration-definition)" : {{FlowDefinition}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-loopflownodeconfiguration-syntax.yaml"></a>

```
  [Definition](#cfn-bedrock-flow-loopflownodeconfiguration-definition): {{
    FlowDefinition}}
```

## Properties
<a name="aws-properties-bedrock-flow-loopflownodeconfiguration-properties"></a>

`Definition`  <a name="cfn-bedrock-flow-loopflownodeconfiguration-definition"></a>
The definition of the DoWhile loop nodes and connections between nodes in the flow.
*Required*: Yes
*Type*: [FlowDefinition](aws-properties-bedrock-flow-flowdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
