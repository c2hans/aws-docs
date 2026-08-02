---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-intentdisambiguationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot IntentDisambiguationSettings
<a name="aws-properties-lex-bot-intentdisambiguationsettings"></a>

Configures the Intent Disambiguation feature that helps resolve ambiguous user inputs when multiple intents could match. When enabled, the system presents clarifying questions to users, helping them specify their exact intent for improved conversation accuracy.

## Syntax
<a name="aws-properties-lex-bot-intentdisambiguationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-intentdisambiguationsettings-syntax.json"></a>

```
{
  "[CustomDisambiguationMessage](#cfn-lex-bot-intentdisambiguationsettings-customdisambiguationmessage)" : {{String}},
  "[Enabled](#cfn-lex-bot-intentdisambiguationsettings-enabled)" : {{Boolean}},
  "[MaxDisambiguationIntents](#cfn-lex-bot-intentdisambiguationsettings-maxdisambiguationintents)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lex-bot-intentdisambiguationsettings-syntax.yaml"></a>

```
  [CustomDisambiguationMessage](#cfn-lex-bot-intentdisambiguationsettings-customdisambiguationmessage): {{String}}
  [Enabled](#cfn-lex-bot-intentdisambiguationsettings-enabled): {{Boolean}}
  [MaxDisambiguationIntents](#cfn-lex-bot-intentdisambiguationsettings-maxdisambiguationintents): {{Integer}}
```

## Properties
<a name="aws-properties-lex-bot-intentdisambiguationsettings-properties"></a>

`CustomDisambiguationMessage`  <a name="cfn-lex-bot-intentdisambiguationsettings-customdisambiguationmessage"></a>
Provides a custom message that will be displayed before presenting the disambiguation options to users. This message helps set the context for users and can be customized to match your bot's tone and brand. If not specified, a default message will be used.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-lex-bot-intentdisambiguationsettings-enabled"></a>
Determines whether the Intent Disambiguation feature is enabled. When set to `true`, Amazon Lex will present disambiguation options to users when multiple intents could match their input, with the default being `false`.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxDisambiguationIntents`  <a name="cfn-lex-bot-intentdisambiguationsettings-maxdisambiguationintents"></a>
Specifies the maximum number of intent options (2-5) to present to users when disambiguation is needed. This setting determines how many intent options will be shown to users when the system detects ambiguous input. The default value is 3.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
