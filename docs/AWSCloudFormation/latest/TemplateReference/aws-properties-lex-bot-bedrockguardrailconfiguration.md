---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-bedrockguardrailconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot BedrockGuardrailConfiguration
<a name="aws-properties-lex-bot-bedrockguardrailconfiguration"></a>

The details on the Bedrock guardrail configuration.

## Syntax
<a name="aws-properties-lex-bot-bedrockguardrailconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-bedrockguardrailconfiguration-syntax.json"></a>

```
{
  "[BedrockGuardrailIdentifier](#cfn-lex-bot-bedrockguardrailconfiguration-bedrockguardrailidentifier)" : {{String}},
  "[BedrockGuardrailVersion](#cfn-lex-bot-bedrockguardrailconfiguration-bedrockguardrailversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-bedrockguardrailconfiguration-syntax.yaml"></a>

```
  [BedrockGuardrailIdentifier](#cfn-lex-bot-bedrockguardrailconfiguration-bedrockguardrailidentifier): {{String}}
  [BedrockGuardrailVersion](#cfn-lex-bot-bedrockguardrailconfiguration-bedrockguardrailversion): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-bedrockguardrailconfiguration-properties"></a>

`BedrockGuardrailIdentifier`  <a name="cfn-lex-bot-bedrockguardrailconfiguration-bedrockguardrailidentifier"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BedrockGuardrailVersion`  <a name="cfn-lex-bot-bedrockguardrailconfiguration-bedrockguardrailversion"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
