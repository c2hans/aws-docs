---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-pool-mandatorykeyword.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::Pool MandatoryKeyword
<a name="aws-properties-smsvoice-pool-mandatorykeyword"></a>

The keywords `HELP` and `STOP` are mandatory keywords that each phone number must have. For more information, see [Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html) in the AWS End User Messaging SMS User Guide.

## Syntax
<a name="aws-properties-smsvoice-pool-mandatorykeyword-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-pool-mandatorykeyword-syntax.json"></a>

```
{
  "[Message](#cfn-smsvoice-pool-mandatorykeyword-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-smsvoice-pool-mandatorykeyword-syntax.yaml"></a>

```
  [Message](#cfn-smsvoice-pool-mandatorykeyword-message): {{String}}
```

## Properties
<a name="aws-properties-smsvoice-pool-mandatorykeyword-properties"></a>

`Message`  <a name="cfn-smsvoice-pool-mandatorykeyword-message"></a>
The message associated with the keyword.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\s\S]+$`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
