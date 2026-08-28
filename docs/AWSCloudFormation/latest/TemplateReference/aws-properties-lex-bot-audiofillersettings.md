---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-audiofillersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot AudioFillerSettings
<a name="aws-properties-lex-bot-audiofillersettings"></a>

Configuration that plays background filler audio during speech-to-speech interactions to mask processing delays and improve the perceived responsiveness of the bot.

Audio filler requires `unifiedSpeechSettings` (speech-to-speech) to be enabled on the bot locale when `enabled` is `true`.

## Syntax
<a name="aws-properties-lex-bot-audiofillersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-audiofillersettings-syntax.json"></a>

```
{
  "[AudioType](#cfn-lex-bot-audiofillersettings-audiotype)" : {{String}},
  "[Enabled](#cfn-lex-bot-audiofillersettings-enabled)" : {{Boolean}},
  "[MinimumPlayDurationInMilliseconds](#cfn-lex-bot-audiofillersettings-minimumplaydurationinmilliseconds)" : {{Integer}},
  "[ResponseDeliveryDelayInMilliseconds](#cfn-lex-bot-audiofillersettings-responsedeliverydelayinmilliseconds)" : {{Integer}},
  "[StartDelayInMilliseconds](#cfn-lex-bot-audiofillersettings-startdelayinmilliseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lex-bot-audiofillersettings-syntax.yaml"></a>

```
  [AudioType](#cfn-lex-bot-audiofillersettings-audiotype): {{String}}
  [Enabled](#cfn-lex-bot-audiofillersettings-enabled): {{Boolean}}
  [MinimumPlayDurationInMilliseconds](#cfn-lex-bot-audiofillersettings-minimumplaydurationinmilliseconds): {{Integer}}
  [ResponseDeliveryDelayInMilliseconds](#cfn-lex-bot-audiofillersettings-responsedeliverydelayinmilliseconds): {{Integer}}
  [StartDelayInMilliseconds](#cfn-lex-bot-audiofillersettings-startdelayinmilliseconds): {{Integer}}
```

## Properties
<a name="aws-properties-lex-bot-audiofillersettings-properties"></a>

`AudioType`  <a name="cfn-lex-bot-audiofillersettings-audiotype"></a>
The identifier of the audio filler to play while Amazon Lex processes the user's input. This field is required when `enabled` is `true`.
*Required*: No
*Type*: String
*Allowed values*: `MELODY_CHIPPER_CHIME | MELODY_CURIOUS_CRAWL | MELODY_RISING_RIPPLE | MELODY_PATIENT_PING | MELODY_PONDERING_PONG | TYPING_KINETIC_KEYS | TYPING_QUIET_QWERTY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-lex-bot-audiofillersettings-enabled"></a>
Specifies whether audio filler playback is enabled for the bot locale. Set to `true` to play filler audio while Amazon Lex processes a user utterance. Set to `false` to disable filler audio.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumPlayDurationInMilliseconds`  <a name="cfn-lex-bot-audiofillersettings-minimumplaydurationinmilliseconds"></a>
The minimum time, in milliseconds, that audio filler plays once it has started, even if the bot response becomes ready sooner. Valid range is `1000` to `5000` milliseconds. If not specified, Amazon Lex uses a default of `3000` milliseconds.
*Required*: No
*Type*: Integer
*Minimum*: `1000`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResponseDeliveryDelayInMilliseconds`  <a name="cfn-lex-bot-audiofillersettings-responsedeliverydelayinmilliseconds"></a>
The silent delay, in milliseconds, inserted between the end of audio filler playback and the start of the bot's response. Valid range is `200` to `1000` milliseconds. If not specified, Amazon Lex uses a default of `500` milliseconds.
*Required*: No
*Type*: Integer
*Minimum*: `200`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartDelayInMilliseconds`  <a name="cfn-lex-bot-audiofillersettings-startdelayinmilliseconds"></a>
The time, in milliseconds, to wait after the end of the user's utterance before starting audio filler playback. Valid range is `500` to `5000` milliseconds. If not specified, Amazon Lex uses a default of `2500` milliseconds.
*Required*: No
*Type*: Integer
*Minimum*: `500`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
