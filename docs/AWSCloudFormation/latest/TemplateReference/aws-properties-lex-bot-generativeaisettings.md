---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-generativeaisettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot GenerativeAISettings
<a name="aws-properties-lex-bot-generativeaisettings"></a>

Contains specifications about the generative AI capabilities from Amazon Bedrock that you can turn on for your bot.

## Syntax
<a name="aws-properties-lex-bot-generativeaisettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-generativeaisettings-syntax.json"></a>

```
{
  "[BuildtimeSettings](#cfn-lex-bot-generativeaisettings-buildtimesettings)" : {{BuildtimeSettings}},
  "[RuntimeSettings](#cfn-lex-bot-generativeaisettings-runtimesettings)" : {{RuntimeSettings}}
}
```

### YAML
<a name="aws-properties-lex-bot-generativeaisettings-syntax.yaml"></a>

```
  [BuildtimeSettings](#cfn-lex-bot-generativeaisettings-buildtimesettings): {{
    BuildtimeSettings}}
  [RuntimeSettings](#cfn-lex-bot-generativeaisettings-runtimesettings): {{
    RuntimeSettings}}
```

## Properties
<a name="aws-properties-lex-bot-generativeaisettings-properties"></a>

`BuildtimeSettings`  <a name="cfn-lex-bot-generativeaisettings-buildtimesettings"></a>
Property description not available.
*Required*: No
*Type*: [BuildtimeSettings](aws-properties-lex-bot-buildtimesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeSettings`  <a name="cfn-lex-bot-generativeaisettings-runtimesettings"></a>
Property description not available.
*Required*: No
*Type*: [RuntimeSettings](aws-properties-lex-bot-runtimesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
