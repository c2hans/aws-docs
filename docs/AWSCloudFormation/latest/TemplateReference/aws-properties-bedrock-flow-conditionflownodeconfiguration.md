---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-conditionflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow ConditionFlowNodeConfiguration
<a name="aws-properties-bedrock-flow-conditionflownodeconfiguration"></a>

Defines a condition node in your flow. You can specify conditions that determine which node comes next in the flow. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-flow-conditionflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-conditionflownodeconfiguration-syntax.json"></a>

```
{
  "[Conditions](#cfn-bedrock-flow-conditionflownodeconfiguration-conditions)" : {{[ FlowCondition, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-conditionflownodeconfiguration-syntax.yaml"></a>

```
  [Conditions](#cfn-bedrock-flow-conditionflownodeconfiguration-conditions): {{
    - FlowCondition}}
```

## Properties
<a name="aws-properties-bedrock-flow-conditionflownodeconfiguration-properties"></a>

`Conditions`  <a name="cfn-bedrock-flow-conditionflownodeconfiguration-conditions"></a>
An array of conditions. Each member contains the name of a condition and an expression that defines the condition.
*Required*: Yes
*Type*: Array of [FlowCondition](aws-properties-bedrock-flow-flowcondition.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
