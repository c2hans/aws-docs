---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-flowconditionalconnectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow FlowConditionalConnectionConfiguration
<a name="aws-properties-bedrock-flow-flowconditionalconnectionconfiguration"></a>

The configuration of a connection between a condition node and another node.

## Syntax
<a name="aws-properties-bedrock-flow-flowconditionalconnectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-flowconditionalconnectionconfiguration-syntax.json"></a>

```
{
  "[Condition](#cfn-bedrock-flow-flowconditionalconnectionconfiguration-condition)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-flowconditionalconnectionconfiguration-syntax.yaml"></a>

```
  [Condition](#cfn-bedrock-flow-flowconditionalconnectionconfiguration-condition): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-flowconditionalconnectionconfiguration-properties"></a>

`Condition`  <a name="cfn-bedrock-flow-flowconditionalconnectionconfiguration-condition"></a>
The condition that triggers this connection. For more information about how to write conditions, see the **Condition** node type in the [Node types](https://docs.aws.amazon.com/bedrock/latest/userguide/node-types.html) topic in the Amazon Bedrock User Guide.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]([_]?[0-9a-zA-Z]){1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
