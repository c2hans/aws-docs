---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-phonenumber-optionalkeyword.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::PhoneNumber OptionalKeyword
<a name="aws-properties-smsvoice-phonenumber-optionalkeyword"></a>

The `OptionalKeyword `configuration. For more information, see [Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html) in the AWS End User Messaging SMS User Guide.

## Syntax
<a name="aws-properties-smsvoice-phonenumber-optionalkeyword-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-phonenumber-optionalkeyword-syntax.json"></a>

```
{
  "[Action](#cfn-smsvoice-phonenumber-optionalkeyword-action)" : {{String}},
  "[Keyword](#cfn-smsvoice-phonenumber-optionalkeyword-keyword)" : {{String}},
  "[Message](#cfn-smsvoice-phonenumber-optionalkeyword-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-smsvoice-phonenumber-optionalkeyword-syntax.yaml"></a>

```
  [Action](#cfn-smsvoice-phonenumber-optionalkeyword-action): {{String}}
  [Keyword](#cfn-smsvoice-phonenumber-optionalkeyword-keyword): {{String}}
  [Message](#cfn-smsvoice-phonenumber-optionalkeyword-message): {{String}}
```

## Properties
<a name="aws-properties-smsvoice-phonenumber-optionalkeyword-properties"></a>

`Action`  <a name="cfn-smsvoice-phonenumber-optionalkeyword-action"></a>
The action to perform when the keyword is used.
*Required*: Yes
*Type*: String
*Allowed values*: `AUTOMATIC_RESPONSE | OPT_OUT | OPT_IN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Keyword`  <a name="cfn-smsvoice-phonenumber-optionalkeyword-keyword"></a>
The new keyword to add.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!(?i)(stop|help)$)[ \S]+`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Message`  <a name="cfn-smsvoice-phonenumber-optionalkeyword-message"></a>
The message associated with the keyword.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\s\S]+$`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
