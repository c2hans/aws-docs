---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-chatbot-customaction-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Chatbot::CustomAction Tag
<a name="aws-properties-chatbot-customaction-tag"></a>

**Note**
AWS Chatbot is now Amazon Q Developer. [Learn more](https://docs.aws.amazon.com/chatbot/latest/adminguide/service-rename.html)
`Type` attribute values remain unchanged.

A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.

## Syntax
<a name="aws-properties-chatbot-customaction-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-chatbot-customaction-tag-syntax.json"></a>

```
{
  "[Key](#cfn-chatbot-customaction-tag-key)" : {{String}},
  "[Value](#cfn-chatbot-customaction-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-chatbot-customaction-tag-syntax.yaml"></a>

```
  [Key](#cfn-chatbot-customaction-tag-key): {{String}}
  [Value](#cfn-chatbot-customaction-tag-value): {{String}}
```

## Properties
<a name="aws-properties-chatbot-customaction-tag-properties"></a>

`Key`  <a name="cfn-chatbot-customaction-tag-key"></a>
 A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: `aws:`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-chatbot-customaction-tag-value"></a>
A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
