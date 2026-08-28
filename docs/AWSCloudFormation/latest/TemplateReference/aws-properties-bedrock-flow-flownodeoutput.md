---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-flownodeoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow FlowNodeOutput
<a name="aws-properties-bedrock-flow-flownodeoutput"></a>

Contains configurations for an output from a node.

## Syntax
<a name="aws-properties-bedrock-flow-flownodeoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-flownodeoutput-syntax.json"></a>

```
{
  "[Name](#cfn-bedrock-flow-flownodeoutput-name)" : {{String}},
  "[Type](#cfn-bedrock-flow-flownodeoutput-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-flownodeoutput-syntax.yaml"></a>

```
  [Name](#cfn-bedrock-flow-flownodeoutput-name): {{String}}
  [Type](#cfn-bedrock-flow-flownodeoutput-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-flownodeoutput-properties"></a>

`Name`  <a name="cfn-bedrock-flow-flownodeoutput-name"></a>
A name for the output that you can reference.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-flow-flownodeoutput-type"></a>
The data type of the output. If the output doesn't match this type at runtime, a validation error will be thrown.
*Required*: Yes
*Type*: String
*Allowed values*: `String | Number | Boolean | Object | Array`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
