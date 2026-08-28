---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-botaliaslocalesettingsitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot BotAliasLocaleSettingsItem
<a name="aws-properties-lex-bot-botaliaslocalesettingsitem"></a>

Specifies locale settings for a single locale.

## Syntax
<a name="aws-properties-lex-bot-botaliaslocalesettingsitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-botaliaslocalesettingsitem-syntax.json"></a>

```
{
  "[BotAliasLocaleSetting](#cfn-lex-bot-botaliaslocalesettingsitem-botaliaslocalesetting)" : {{BotAliasLocaleSettings}},
  "[LocaleId](#cfn-lex-bot-botaliaslocalesettingsitem-localeid)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-botaliaslocalesettingsitem-syntax.yaml"></a>

```
  [BotAliasLocaleSetting](#cfn-lex-bot-botaliaslocalesettingsitem-botaliaslocalesetting): {{
    BotAliasLocaleSettings}}
  [LocaleId](#cfn-lex-bot-botaliaslocalesettingsitem-localeid): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-botaliaslocalesettingsitem-properties"></a>

`BotAliasLocaleSetting`  <a name="cfn-lex-bot-botaliaslocalesettingsitem-botaliaslocalesetting"></a>
Specifies locale settings for a locale.
*Required*: Yes
*Type*: [BotAliasLocaleSettings](aws-properties-lex-bot-botaliaslocalesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocaleId`  <a name="cfn-lex-bot-botaliaslocalesettingsitem-localeid"></a>
Specifies the locale that the settings apply to.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
