---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-registrationattachment-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::RegistrationAttachment Tag
<a name="aws-properties-smsvoice-registrationattachment-tag"></a>

The list of tags to be added to the specified topic.

## Syntax
<a name="aws-properties-smsvoice-registrationattachment-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-registrationattachment-tag-syntax.json"></a>

```
{
  "[Key](#cfn-smsvoice-registrationattachment-tag-key)" : {{String}},
  "[Value](#cfn-smsvoice-registrationattachment-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-smsvoice-registrationattachment-tag-syntax.yaml"></a>

```
  [Key](#cfn-smsvoice-registrationattachment-tag-key): {{String}}
  [Value](#cfn-smsvoice-registrationattachment-tag-value): {{String}}
```

## Properties
<a name="aws-properties-smsvoice-registrationattachment-tag-properties"></a>

`Key`  <a name="cfn-smsvoice-registrationattachment-tag-key"></a>
The key identifier, or name, of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-smsvoice-registrationattachment-tag-value"></a>
The string value associated with the key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
