---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-unifiedspeechsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot UnifiedSpeechSettings
<a name="aws-properties-lex-bot-unifiedspeechsettings"></a>

Unified configuration settings that combine speech recognition and synthesis capabilities.

## Syntax
<a name="aws-properties-lex-bot-unifiedspeechsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-unifiedspeechsettings-syntax.json"></a>

```
{
  "[SpeechFoundationModel](#cfn-lex-bot-unifiedspeechsettings-speechfoundationmodel)" : {{SpeechFoundationModel}}
}
```

### YAML
<a name="aws-properties-lex-bot-unifiedspeechsettings-syntax.yaml"></a>

```
  [SpeechFoundationModel](#cfn-lex-bot-unifiedspeechsettings-speechfoundationmodel): {{
    SpeechFoundationModel}}
```

## Properties
<a name="aws-properties-lex-bot-unifiedspeechsettings-properties"></a>

`SpeechFoundationModel`  <a name="cfn-lex-bot-unifiedspeechsettings-speechfoundationmodel"></a>
The foundation model configuration to use for unified speech processing capabilities.
*Required*: Yes
*Type*: [SpeechFoundationModel](aws-properties-lex-bot-speechfoundationmodel.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
