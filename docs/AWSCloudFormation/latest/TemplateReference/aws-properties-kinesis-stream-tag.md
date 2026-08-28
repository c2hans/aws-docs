---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-stream-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Stream Tag
<a name="aws-properties-kinesis-stream-tag"></a>

Metadata assigned to the stream or consumer, consisting of a key-value pair.

## Syntax
<a name="aws-properties-kinesis-stream-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-stream-tag-syntax.json"></a>

```
{
  "[Key](#cfn-kinesis-stream-tag-key)" : {{String}},
  "[Value](#cfn-kinesis-stream-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-stream-tag-syntax.yaml"></a>

```
  [Key](#cfn-kinesis-stream-tag-key): {{String}}
  [Value](#cfn-kinesis-stream-tag-value): {{String}}
```

## Properties
<a name="aws-properties-kinesis-stream-tag-properties"></a>

`Key`  <a name="cfn-kinesis-stream-tag-key"></a>
A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, \_ . / = \+ - % @
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-kinesis-stream-tag-value"></a>
An optional string, typically used to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, \_ . / = \+ - % @
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
