---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-promptinputvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow PromptInputVariable
<a name="aws-properties-bedrock-flow-promptinputvariable"></a>

Contains information about a variable in the prompt.

## Syntax
<a name="aws-properties-bedrock-flow-promptinputvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-promptinputvariable-syntax.json"></a>

```
{
  "[Name](#cfn-bedrock-flow-promptinputvariable-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-promptinputvariable-syntax.yaml"></a>

```
  [Name](#cfn-bedrock-flow-promptinputvariable-name): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-promptinputvariable-properties"></a>

`Name`  <a name="cfn-bedrock-flow-promptinputvariable-name"></a>
The name of the variable.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
