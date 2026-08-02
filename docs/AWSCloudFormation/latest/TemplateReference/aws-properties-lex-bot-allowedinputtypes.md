---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-allowedinputtypes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot AllowedInputTypes
<a name="aws-properties-lex-bot-allowedinputtypes"></a>

Specifies the allowed input types.

## Syntax
<a name="aws-properties-lex-bot-allowedinputtypes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-allowedinputtypes-syntax.json"></a>

```
{
  "[AllowAudioInput](#cfn-lex-bot-allowedinputtypes-allowaudioinput)" : {{Boolean}},
  "[AllowDTMFInput](#cfn-lex-bot-allowedinputtypes-allowdtmfinput)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-lex-bot-allowedinputtypes-syntax.yaml"></a>

```
  [AllowAudioInput](#cfn-lex-bot-allowedinputtypes-allowaudioinput): {{Boolean}}
  [AllowDTMFInput](#cfn-lex-bot-allowedinputtypes-allowdtmfinput): {{Boolean}}
```

## Properties
<a name="aws-properties-lex-bot-allowedinputtypes-properties"></a>

`AllowAudioInput`  <a name="cfn-lex-bot-allowedinputtypes-allowaudioinput"></a>
Indicates whether audio input is allowed.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowDTMFInput`  <a name="cfn-lex-bot-allowedinputtypes-allowdtmfinput"></a>
Indicates whether DTMF input is allowed.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
