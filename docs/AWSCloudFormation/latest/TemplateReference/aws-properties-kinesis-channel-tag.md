---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel Tag
<a name="aws-properties-kinesis-channel-tag"></a>

Metadata assigned to the stream or consumer, consisting of a key-value pair.

## Syntax
<a name="aws-properties-kinesis-channel-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-tag-syntax.json"></a>

```
{
  "[Key](#cfn-kinesis-channel-tag-key)" : {{String}},
  "[Value](#cfn-kinesis-channel-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-tag-syntax.yaml"></a>

```
  [Key](#cfn-kinesis-channel-tag-key): {{String}}
  [Value](#cfn-kinesis-channel-tag-value): {{String}}
```

## Properties
<a name="aws-properties-kinesis-channel-tag-properties"></a>

`Key`  <a name="cfn-kinesis-channel-tag-key"></a>
A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, \_ . / = \+ - % @
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-kinesis-channel-tag-value"></a>
An optional string, typically used to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, \_ . / = \+ - % @
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
