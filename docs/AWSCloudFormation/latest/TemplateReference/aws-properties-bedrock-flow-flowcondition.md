---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-flowcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow FlowCondition
<a name="aws-properties-bedrock-flow-flowcondition"></a>

Defines a condition in the condition node.

## Syntax
<a name="aws-properties-bedrock-flow-flowcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-flowcondition-syntax.json"></a>

```
{
  "[Expression](#cfn-bedrock-flow-flowcondition-expression)" : {{String}},
  "[Name](#cfn-bedrock-flow-flowcondition-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-flowcondition-syntax.yaml"></a>

```
  [Expression](#cfn-bedrock-flow-flowcondition-expression): {{String}}
  [Name](#cfn-bedrock-flow-flowcondition-name): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-flowcondition-properties"></a>

`Expression`  <a name="cfn-bedrock-flow-flowcondition-expression"></a>
Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in [Node types in prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-flow-flowcondition-name"></a>
A name for the condition that you can reference.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
