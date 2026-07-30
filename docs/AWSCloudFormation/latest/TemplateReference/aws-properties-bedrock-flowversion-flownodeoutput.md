---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-flownodeoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion FlowNodeOutput
<a name="aws-properties-bedrock-flowversion-flownodeoutput"></a>

Contains configurations for an output from a node.

## Syntax
<a name="aws-properties-bedrock-flowversion-flownodeoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-flownodeoutput-syntax.json"></a>

```
{
  "[Name](#cfn-bedrock-flowversion-flownodeoutput-name)" : {{String}},
  "[Type](#cfn-bedrock-flowversion-flownodeoutput-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-flownodeoutput-syntax.yaml"></a>

```
  [Name](#cfn-bedrock-flowversion-flownodeoutput-name): {{String}}
  [Type](#cfn-bedrock-flowversion-flownodeoutput-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-flownodeoutput-properties"></a>

`Name`  <a name="cfn-bedrock-flowversion-flownodeoutput-name"></a>
A name for the output that you can reference.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-flowversion-flownodeoutput-type"></a>
The data type of the output. If the output doesn't match this type at runtime, a validation error will be thrown.
*Required*: Yes
*Type*: String
*Allowed values*: `String | Number | Boolean | Object | Array`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
