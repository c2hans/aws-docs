---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-flownodeinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion FlowNodeInput
<a name="aws-properties-bedrock-flowversion-flownodeinput"></a>

Contains configurations for an input in an Amazon Bedrock Flows node.

## Syntax
<a name="aws-properties-bedrock-flowversion-flownodeinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-flownodeinput-syntax.json"></a>

```
{
  "[Expression](#cfn-bedrock-flowversion-flownodeinput-expression)" : {{String}},
  "[Name](#cfn-bedrock-flowversion-flownodeinput-name)" : {{String}},
  "[Type](#cfn-bedrock-flowversion-flownodeinput-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-flownodeinput-syntax.yaml"></a>

```
  [Expression](#cfn-bedrock-flowversion-flownodeinput-expression): {{String}}
  [Name](#cfn-bedrock-flowversion-flownodeinput-name): {{String}}
  [Type](#cfn-bedrock-flowversion-flownodeinput-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-flownodeinput-properties"></a>

`Expression`  <a name="cfn-bedrock-flowversion-flownodeinput-expression"></a>
An expression that formats the input for the node. For an explanation of how to create expressions, see [Expressions in Prompt flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-expressions.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-flowversion-flownodeinput-name"></a>
Specifies a name for the input that you can reference.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-flowversion-flownodeinput-type"></a>
Specifies the data type of the input. If the input doesn't match this type at runtime, a validation error will be thrown.
*Required*: Yes
*Type*: String
*Allowed values*: `String | Number | Boolean | Object | Array`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
