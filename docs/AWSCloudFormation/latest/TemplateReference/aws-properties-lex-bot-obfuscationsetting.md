---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-obfuscationsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot ObfuscationSetting
<a name="aws-properties-lex-bot-obfuscationsetting"></a>

Determines whether Amazon Lex obscures slot values in conversation logs.

## Syntax
<a name="aws-properties-lex-bot-obfuscationsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-obfuscationsetting-syntax.json"></a>

```
{
  "[ObfuscationSettingType](#cfn-lex-bot-obfuscationsetting-obfuscationsettingtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-obfuscationsetting-syntax.yaml"></a>

```
  [ObfuscationSettingType](#cfn-lex-bot-obfuscationsetting-obfuscationsettingtype): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-obfuscationsetting-properties"></a>

`ObfuscationSettingType`  <a name="cfn-lex-bot-obfuscationsetting-obfuscationsettingtype"></a>
Value that determines whether Amazon Lex obscures slot values in conversation logs. The default is to obscure the values.
*Required*: Yes
*Type*: String
*Allowed values*: `None | DefaultObfuscation`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
