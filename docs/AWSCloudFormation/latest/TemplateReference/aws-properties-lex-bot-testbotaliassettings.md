---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-testbotaliassettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot TestBotAliasSettings
<a name="aws-properties-lex-bot-testbotaliassettings"></a>

Specifies configuration settings for the alias used to test the bot. If the `TestBotAliasSettings` property is not specified, the settings are configured with default values.

## Syntax
<a name="aws-properties-lex-bot-testbotaliassettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-testbotaliassettings-syntax.json"></a>

```
{
  "[BotAliasLocaleSettings](#cfn-lex-bot-testbotaliassettings-botaliaslocalesettings)" : {{[ BotAliasLocaleSettingsItem, ... ]}},
  "[ConversationLogSettings](#cfn-lex-bot-testbotaliassettings-conversationlogsettings)" : {{ConversationLogSettings}},
  "[Description](#cfn-lex-bot-testbotaliassettings-description)" : {{String}},
  "[SentimentAnalysisSettings](#cfn-lex-bot-testbotaliassettings-sentimentanalysissettings)" : {{SentimentAnalysisSettings}}
}
```

### YAML
<a name="aws-properties-lex-bot-testbotaliassettings-syntax.yaml"></a>

```
  [BotAliasLocaleSettings](#cfn-lex-bot-testbotaliassettings-botaliaslocalesettings): {{
    - BotAliasLocaleSettingsItem}}
  [ConversationLogSettings](#cfn-lex-bot-testbotaliassettings-conversationlogsettings): {{
    ConversationLogSettings}}
  [Description](#cfn-lex-bot-testbotaliassettings-description): {{String}}
  [SentimentAnalysisSettings](#cfn-lex-bot-testbotaliassettings-sentimentanalysissettings): {{
    SentimentAnalysisSettings}}
```

## Properties
<a name="aws-properties-lex-bot-testbotaliassettings-properties"></a>

`BotAliasLocaleSettings`  <a name="cfn-lex-bot-testbotaliassettings-botaliaslocalesettings"></a>
Specifies settings that are unique to a locale. For example, you can use a different Lambda function depending on the bot's locale.
*Required*: No
*Type*: [Array](aws-properties-lex-bot-botaliaslocalesettings.md) of [BotAliasLocaleSettingsItem](aws-properties-lex-bot-botaliaslocalesettingsitem.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConversationLogSettings`  <a name="cfn-lex-bot-testbotaliassettings-conversationlogsettings"></a>
Specifies settings for conversation logs that save audio, text, and metadata information for conversations with your users.
*Required*: No
*Type*: [ConversationLogSettings](aws-properties-lex-bot-conversationlogsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-lex-bot-testbotaliassettings-description"></a>
Specifies a description for the test bot alias.
*Required*: No
*Type*: String
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SentimentAnalysisSettings`  <a name="cfn-lex-bot-testbotaliassettings-sentimentanalysissettings"></a>
Specifies whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.
*Required*: No
*Type*: [SentimentAnalysisSettings](aws-properties-lex-bot-sentimentanalysissettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
