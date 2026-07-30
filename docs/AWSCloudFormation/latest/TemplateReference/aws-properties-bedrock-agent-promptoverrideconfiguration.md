---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-promptoverrideconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent PromptOverrideConfiguration
<a name="aws-properties-bedrock-agent-promptoverrideconfiguration"></a>

Contains configurations to override prompts in different parts of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).

## Syntax
<a name="aws-properties-bedrock-agent-promptoverrideconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-promptoverrideconfiguration-syntax.json"></a>

```
{
  "[OverrideLambda](#cfn-bedrock-agent-promptoverrideconfiguration-overridelambda)" : {{String}},
  "[PromptConfigurations](#cfn-bedrock-agent-promptoverrideconfiguration-promptconfigurations)" : {{[ PromptConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-promptoverrideconfiguration-syntax.yaml"></a>

```
  [OverrideLambda](#cfn-bedrock-agent-promptoverrideconfiguration-overridelambda): {{String}}
  [PromptConfigurations](#cfn-bedrock-agent-promptoverrideconfiguration-promptconfigurations): {{
    - PromptConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-agent-promptoverrideconfiguration-properties"></a>

`OverrideLambda`  <a name="cfn-bedrock-agent-promptoverrideconfiguration-overridelambda"></a>
The ARN of the Lambda function to use when parsing the raw foundation model output in parts of the agent sequence. If you specify this field, at least one of the `promptConfigurations` must contain a `parserMode` value that is set to `OVERRIDDEN`. For more information, see [Parser Lambda function in Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/lambda-parser.html).
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:lambda:[a-z0-9-]{1,20}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PromptConfigurations`  <a name="cfn-bedrock-agent-promptoverrideconfiguration-promptconfigurations"></a>
Contains configurations to override a prompt template in one part of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).
*Required*: Yes
*Type*: Array of [PromptConfiguration](aws-properties-bedrock-agent-promptconfiguration.md)
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
