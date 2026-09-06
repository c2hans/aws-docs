---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-phonenumber-mandatorykeywords.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::PhoneNumber MandatoryKeywords
<a name="aws-properties-smsvoice-phonenumber-mandatorykeywords"></a>

The keywords `HELP` and `STOP` are mandatory keywords that each phone number must have. For more information, see [Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html) in the AWS End User Messaging SMS User Guide.

## Syntax
<a name="aws-properties-smsvoice-phonenumber-mandatorykeywords-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-phonenumber-mandatorykeywords-syntax.json"></a>

```
{
  "[HELP](#cfn-smsvoice-phonenumber-mandatorykeywords-help)" : {{MandatoryKeyword}},
  "[STOP](#cfn-smsvoice-phonenumber-mandatorykeywords-stop)" : {{MandatoryKeyword}}
}
```

### YAML
<a name="aws-properties-smsvoice-phonenumber-mandatorykeywords-syntax.yaml"></a>

```
  [HELP](#cfn-smsvoice-phonenumber-mandatorykeywords-help): {{
    MandatoryKeyword}}
  [STOP](#cfn-smsvoice-phonenumber-mandatorykeywords-stop): {{
    MandatoryKeyword}}
```

## Properties
<a name="aws-properties-smsvoice-phonenumber-mandatorykeywords-properties"></a>

`HELP`  <a name="cfn-smsvoice-phonenumber-mandatorykeywords-help"></a>
Specifies the `HELP` keyword that customers use to obtain customer support for this phone number. For more information, see [Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html) in the AWS End User Messaging SMS User Guide.
*Required*: Yes
*Type*: [MandatoryKeyword](aws-properties-smsvoice-phonenumber-mandatorykeyword.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`STOP`  <a name="cfn-smsvoice-phonenumber-mandatorykeywords-stop"></a>
Specifies the `STOP` keyword that customers use to opt out of receiving messages from this phone number. For more information, see [Required opt-out keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-required.html) in the AWS End User Messaging SMS User Guide.
*Required*: Yes
*Type*: [MandatoryKeyword](aws-properties-smsvoice-phonenumber-mandatorykeyword.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
