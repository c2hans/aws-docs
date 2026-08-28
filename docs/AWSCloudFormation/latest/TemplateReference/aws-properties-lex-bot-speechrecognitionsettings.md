---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-speechrecognitionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SpeechRecognitionSettings
<a name="aws-properties-lex-bot-speechrecognitionsettings"></a>

Settings that control how Amazon Lex processes and recognizes speech input from users.

## Syntax
<a name="aws-properties-lex-bot-speechrecognitionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-speechrecognitionsettings-syntax.json"></a>

```
{
  "[SpeechModelConfig](#cfn-lex-bot-speechrecognitionsettings-speechmodelconfig)" : {{SpeechModelConfig}},
  "[SpeechModelPreference](#cfn-lex-bot-speechrecognitionsettings-speechmodelpreference)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-speechrecognitionsettings-syntax.yaml"></a>

```
  [SpeechModelConfig](#cfn-lex-bot-speechrecognitionsettings-speechmodelconfig): {{
    SpeechModelConfig}}
  [SpeechModelPreference](#cfn-lex-bot-speechrecognitionsettings-speechmodelpreference): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-speechrecognitionsettings-properties"></a>

`SpeechModelConfig`  <a name="cfn-lex-bot-speechrecognitionsettings-speechmodelconfig"></a>
Configuration settings for the selected speech-to-text model.
*Required*: No
*Type*: [SpeechModelConfig](aws-properties-lex-bot-speechmodelconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpeechModelPreference`  <a name="cfn-lex-bot-speechrecognitionsettings-speechmodelpreference"></a>
The speech-to-text model to use.
*Required*: No
*Type*: String
*Allowed values*: `Standard | Neural | Deepgram | Advanced`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
