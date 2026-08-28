---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-qinconnectassistantconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot QInConnectAssistantConfiguration
<a name="aws-properties-lex-bot-qinconnectassistantconfiguration"></a>

<a name="aws-properties-lex-bot-qinconnectassistantconfiguration-description"></a>The `QInConnectAssistantConfiguration` property type specifies Property description not available. for an [AWS::Lex::Bot](aws-resource-lex-bot.md).

## Syntax
<a name="aws-properties-lex-bot-qinconnectassistantconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-qinconnectassistantconfiguration-syntax.json"></a>

```
{
  "[AssistantArn](#cfn-lex-bot-qinconnectassistantconfiguration-assistantarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-qinconnectassistantconfiguration-syntax.yaml"></a>

```
  [AssistantArn](#cfn-lex-bot-qinconnectassistantconfiguration-assistantarn): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-qinconnectassistantconfiguration-properties"></a>

`AssistantArn`  <a name="cfn-lex-bot-qinconnectassistantconfiguration-assistantarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
