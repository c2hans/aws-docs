---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-botalias-botaliaslocalesettingsitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::BotAlias BotAliasLocaleSettingsItem
<a name="aws-properties-lex-botalias-botaliaslocalesettingsitem"></a>

Specifies settings that are unique to a locale. For example, you can use different Lambda function depending on the bot's locale.

## Syntax
<a name="aws-properties-lex-botalias-botaliaslocalesettingsitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-botalias-botaliaslocalesettingsitem-syntax.json"></a>

```
{
  "[BotAliasLocaleSetting](#cfn-lex-botalias-botaliaslocalesettingsitem-botaliaslocalesetting)" : {{BotAliasLocaleSettings}},
  "[LocaleId](#cfn-lex-botalias-botaliaslocalesettingsitem-localeid)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-botalias-botaliaslocalesettingsitem-syntax.yaml"></a>

```
  [BotAliasLocaleSetting](#cfn-lex-botalias-botaliaslocalesettingsitem-botaliaslocalesetting): {{
    BotAliasLocaleSettings}}
  [LocaleId](#cfn-lex-botalias-botaliaslocalesettingsitem-localeid): {{String}}
```

## Properties
<a name="aws-properties-lex-botalias-botaliaslocalesettingsitem-properties"></a>

`BotAliasLocaleSetting`  <a name="cfn-lex-botalias-botaliaslocalesettingsitem-botaliaslocalesetting"></a>
Specifies settings that are unique to a locale.
*Required*: Yes
*Type*: [BotAliasLocaleSettings](aws-properties-lex-botalias-botaliaslocalesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocaleId`  <a name="cfn-lex-botalias-botaliaslocalesettingsitem-localeid"></a>
The unique identifier of the locale.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
