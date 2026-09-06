---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-speechfoundationmodel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SpeechFoundationModel
<a name="aws-properties-lex-bot-speechfoundationmodel"></a>

Configuration for a foundation model used for speech synthesis and recognition capabilities.

## Syntax
<a name="aws-properties-lex-bot-speechfoundationmodel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-speechfoundationmodel-syntax.json"></a>

```
{
  "[ModelArn](#cfn-lex-bot-speechfoundationmodel-modelarn)" : {{String}},
  "[VoiceId](#cfn-lex-bot-speechfoundationmodel-voiceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-speechfoundationmodel-syntax.yaml"></a>

```
  [ModelArn](#cfn-lex-bot-speechfoundationmodel-modelarn): {{String}}
  [VoiceId](#cfn-lex-bot-speechfoundationmodel-voiceid): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-speechfoundationmodel-properties"></a>

`ModelArn`  <a name="cfn-lex-bot-speechfoundationmodel-modelarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VoiceId`  <a name="cfn-lex-bot-speechfoundationmodel-voiceid"></a>
The identifier of the voice to use for speech synthesis with the foundation model.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
