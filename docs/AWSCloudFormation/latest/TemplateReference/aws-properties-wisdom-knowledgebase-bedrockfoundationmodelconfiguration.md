---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase BedrockFoundationModelConfiguration
<a name="aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration"></a>

The configuration of the Bedrock foundation model.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-syntax.json"></a>

```
{
  "[ModelArn](#cfn-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-modelarn)" : {{String}},
  "[ParsingPrompt](#cfn-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-parsingprompt)" : {{ParsingPrompt}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-syntax.yaml"></a>

```
  [ModelArn](#cfn-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-modelarn): {{String}}
  [ParsingPrompt](#cfn-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-parsingprompt): {{
    ParsingPrompt}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-properties"></a>

`ModelArn`  <a name="cfn-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-modelarn"></a>
The model ARN of the Bedrock foundation model.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model\/anthropic.claude-3-haiku-20240307-v1:0$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParsingPrompt`  <a name="cfn-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-parsingprompt"></a>
The parsing prompt of the Bedrock foundation model configuration.
*Required*: No
*Type*: [ParsingPrompt](aws-properties-wisdom-knowledgebase-parsingprompt.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
