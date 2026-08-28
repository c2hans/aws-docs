---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-speechmodelconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SpeechModelConfig
<a name="aws-properties-lex-bot-speechmodelconfig"></a>

Configuration settings that define which speech-to-text model to use for processing speech input.

## Syntax
<a name="aws-properties-lex-bot-speechmodelconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-speechmodelconfig-syntax.json"></a>

```
{
  "[DeepgramConfig](#cfn-lex-bot-speechmodelconfig-deepgramconfig)" : {{DeepgramSpeechModelConfig}}
}
```

### YAML
<a name="aws-properties-lex-bot-speechmodelconfig-syntax.yaml"></a>

```
  [DeepgramConfig](#cfn-lex-bot-speechmodelconfig-deepgramconfig): {{
    DeepgramSpeechModelConfig}}
```

## Properties
<a name="aws-properties-lex-bot-speechmodelconfig-properties"></a>

`DeepgramConfig`  <a name="cfn-lex-bot-speechmodelconfig-deepgramconfig"></a>
Configuration settings for using Deepgram as the speech-to-text provider.
*Required*: No
*Type*: [DeepgramSpeechModelConfig](aws-properties-lex-bot-deepgramspeechmodelconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
