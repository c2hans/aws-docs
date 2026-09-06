---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-nluimprovementspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot NluImprovementSpecification
<a name="aws-properties-lex-bot-nluimprovementspecification"></a>

Configures the Assisted Natural Language Understanding (NLU) feature for your bot. This specification determines whether enhanced intent recognition and utterance understanding capabilities are active.

## Syntax
<a name="aws-properties-lex-bot-nluimprovementspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-nluimprovementspecification-syntax.json"></a>

```
{
  "[AssistedNluMode](#cfn-lex-bot-nluimprovementspecification-assistednlumode)" : {{String}},
  "[Enabled](#cfn-lex-bot-nluimprovementspecification-enabled)" : {{Boolean}},
  "[IntentDisambiguationSettings](#cfn-lex-bot-nluimprovementspecification-intentdisambiguationsettings)" : {{IntentDisambiguationSettings}}
}
```

### YAML
<a name="aws-properties-lex-bot-nluimprovementspecification-syntax.yaml"></a>

```
  [AssistedNluMode](#cfn-lex-bot-nluimprovementspecification-assistednlumode): {{String}}
  [Enabled](#cfn-lex-bot-nluimprovementspecification-enabled): {{Boolean}}
  [IntentDisambiguationSettings](#cfn-lex-bot-nluimprovementspecification-intentdisambiguationsettings): {{
    IntentDisambiguationSettings}}
```

## Properties
<a name="aws-properties-lex-bot-nluimprovementspecification-properties"></a>

`AssistedNluMode`  <a name="cfn-lex-bot-nluimprovementspecification-assistednlumode"></a>
Specifies the mode for Assisted NLU operation. Use `Primary` to make Assisted NLU the primary intent recognition method, or `Fallback` to use it only when standard NLU confidence is low.
*Required*: No
*Type*: String
*Allowed values*: `Primary | Fallback`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-lex-bot-nluimprovementspecification-enabled"></a>
Determines whether the Assisted NLU feature is enabled for the bot. When set to `true`, Amazon Lex uses advanced models to improve intent recognition and slot resolution, with the default being `false`.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntentDisambiguationSettings`  <a name="cfn-lex-bot-nluimprovementspecification-intentdisambiguationsettings"></a>
An object containing specifications for the Intent Disambiguation feature within the Assisted NLU settings. These settings determine how the bot handles ambiguous user inputs that could match multiple intents.
*Required*: No
*Type*: [IntentDisambiguationSettings](aws-properties-lex-bot-intentdisambiguationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
