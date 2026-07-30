---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-promptflownoderesourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow PromptFlowNodeResourceConfiguration
<a name="aws-properties-bedrock-flow-promptflownoderesourceconfiguration"></a>

Contains configurations for a prompt from Prompt management to use in a node.

## Syntax
<a name="aws-properties-bedrock-flow-promptflownoderesourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-promptflownoderesourceconfiguration-syntax.json"></a>

```
{
  "[PromptArn](#cfn-bedrock-flow-promptflownoderesourceconfiguration-promptarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-promptflownoderesourceconfiguration-syntax.yaml"></a>

```
  [PromptArn](#cfn-bedrock-flow-promptflownoderesourceconfiguration-promptarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-promptflownoderesourceconfiguration-properties"></a>

`PromptArn`  <a name="cfn-bedrock-flow-promptflownoderesourceconfiguration-promptarn"></a>
The Amazon Resource Name (ARN) of the prompt from Prompt management.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10}(?::[0-9]{1,5})?)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
