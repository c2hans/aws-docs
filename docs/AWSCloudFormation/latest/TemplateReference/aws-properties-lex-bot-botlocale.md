---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-botlocale.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot BotLocale
<a name="aws-properties-lex-bot-botlocale"></a>

Provides configuration information for a locale.

## Syntax
<a name="aws-properties-lex-bot-botlocale-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-botlocale-syntax.json"></a>

```
{
  "[AudioFillerSettings](#cfn-lex-bot-botlocale-audiofillersettings)" : {{AudioFillerSettings}},
  "[CustomVocabulary](#cfn-lex-bot-botlocale-customvocabulary)" : {{CustomVocabulary}},
  "[Description](#cfn-lex-bot-botlocale-description)" : {{String}},
  "[GenerativeAISettings](#cfn-lex-bot-botlocale-generativeaisettings)" : {{GenerativeAISettings}},
  "[Intents](#cfn-lex-bot-botlocale-intents)" : {{[ Intent, ... ]}},
  "[LocaleId](#cfn-lex-bot-botlocale-localeid)" : {{String}},
  "[NluConfidenceThreshold](#cfn-lex-bot-botlocale-nluconfidencethreshold)" : {{Number}},
  "[SlotTypes](#cfn-lex-bot-botlocale-slottypes)" : {{[ SlotType, ... ]}},
  "[SpeechDetectionSensitivity](#cfn-lex-bot-botlocale-speechdetectionsensitivity)" : {{String}},
  "[SpeechRecognitionSettings](#cfn-lex-bot-botlocale-speechrecognitionsettings)" : {{SpeechRecognitionSettings}},
  "[UnifiedSpeechSettings](#cfn-lex-bot-botlocale-unifiedspeechsettings)" : {{UnifiedSpeechSettings}},
  "[VoiceSettings](#cfn-lex-bot-botlocale-voicesettings)" : {{VoiceSettings}}
}
```

### YAML
<a name="aws-properties-lex-bot-botlocale-syntax.yaml"></a>

```
  [AudioFillerSettings](#cfn-lex-bot-botlocale-audiofillersettings): {{
    AudioFillerSettings}}
  [CustomVocabulary](#cfn-lex-bot-botlocale-customvocabulary): {{
    CustomVocabulary}}
  [Description](#cfn-lex-bot-botlocale-description): {{String}}
  [GenerativeAISettings](#cfn-lex-bot-botlocale-generativeaisettings): {{
    GenerativeAISettings}}
  [Intents](#cfn-lex-bot-botlocale-intents): {{
    - Intent}}
  [LocaleId](#cfn-lex-bot-botlocale-localeid): {{String}}
  [NluConfidenceThreshold](#cfn-lex-bot-botlocale-nluconfidencethreshold): {{Number}}
  [SlotTypes](#cfn-lex-bot-botlocale-slottypes): {{
    - SlotType}}
  [SpeechDetectionSensitivity](#cfn-lex-bot-botlocale-speechdetectionsensitivity): {{String}}
  [SpeechRecognitionSettings](#cfn-lex-bot-botlocale-speechrecognitionsettings): {{
    SpeechRecognitionSettings}}
  [UnifiedSpeechSettings](#cfn-lex-bot-botlocale-unifiedspeechsettings): {{
    UnifiedSpeechSettings}}
  [VoiceSettings](#cfn-lex-bot-botlocale-voicesettings): {{
    VoiceSettings}}
```

## Properties
<a name="aws-properties-lex-bot-botlocale-properties"></a>

`AudioFillerSettings`  <a name="cfn-lex-bot-botlocale-audiofillersettings"></a>
Property description not available.
*Required*: No
*Type*: [AudioFillerSettings](aws-properties-lex-bot-audiofillersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomVocabulary`  <a name="cfn-lex-bot-botlocale-customvocabulary"></a>
Specifies a custom vocabulary to use with a specific locale.
*Required*: No
*Type*: [CustomVocabulary](aws-properties-lex-bot-customvocabulary.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-lex-bot-botlocale-description"></a>
A description of the bot locale. Use this to help identify the bot locale in lists.
*Required*: No
*Type*: String
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GenerativeAISettings`  <a name="cfn-lex-bot-botlocale-generativeaisettings"></a>
Property description not available.
*Required*: No
*Type*: [GenerativeAISettings](aws-properties-lex-bot-generativeaisettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Intents`  <a name="cfn-lex-bot-botlocale-intents"></a>
One or more intents defined for the locale.
*Required*: No
*Type*: Array of [Intent](aws-properties-lex-bot-intent.md)
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocaleId`  <a name="cfn-lex-bot-botlocale-localeid"></a>
The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NluConfidenceThreshold`  <a name="cfn-lex-bot-botlocale-nluconfidencethreshold"></a>
Determines the threshold where Amazon Lex will insert the `AMAZON.FallbackIntent`, `AMAZON.KendraSearchIntent`, or both when returning alternative intents. You must configure an `AMAZON.FallbackIntent`. `AMAZON.KendraSearchIntent` is only inserted if it is configured for the bot.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlotTypes`  <a name="cfn-lex-bot-botlocale-slottypes"></a>
One or more slot types defined for the locale.
*Required*: No
*Type*: Array of [SlotType](aws-properties-lex-bot-slottype.md)
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpeechDetectionSensitivity`  <a name="cfn-lex-bot-botlocale-speechdetectionsensitivity"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `Default | HighNoiseTolerance | MaximumNoiseTolerance`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpeechRecognitionSettings`  <a name="cfn-lex-bot-botlocale-speechrecognitionsettings"></a>
Property description not available.
*Required*: No
*Type*: [SpeechRecognitionSettings](aws-properties-lex-bot-speechrecognitionsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnifiedSpeechSettings`  <a name="cfn-lex-bot-botlocale-unifiedspeechsettings"></a>
Property description not available.
*Required*: No
*Type*: [UnifiedSpeechSettings](aws-properties-lex-bot-unifiedspeechsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VoiceSettings`  <a name="cfn-lex-bot-botlocale-voicesettings"></a>
Defines settings for using an Amazon Polly voice to communicate with a user.
Valid values include:
+  `standard`
+  `neural`
+  `long-form`
+  `generative`
*Required*: No
*Type*: [VoiceSettings](aws-properties-lex-bot-voicesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
