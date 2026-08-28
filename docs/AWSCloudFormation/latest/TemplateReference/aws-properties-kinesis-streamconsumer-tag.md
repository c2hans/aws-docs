---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-streamconsumer-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::StreamConsumer Tag
<a name="aws-properties-kinesis-streamconsumer-tag"></a>

Metadata assigned to the stream or consumer, consisting of a key-value pair.

## Syntax
<a name="aws-properties-kinesis-streamconsumer-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-streamconsumer-tag-syntax.json"></a>

```
{
  "[Key](#cfn-kinesis-streamconsumer-tag-key)" : {{String}},
  "[Value](#cfn-kinesis-streamconsumer-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesis-streamconsumer-tag-syntax.yaml"></a>

```
  [Key](#cfn-kinesis-streamconsumer-tag-key): {{String}}
  [Value](#cfn-kinesis-streamconsumer-tag-value): {{String}}
```

## Properties
<a name="aws-properties-kinesis-streamconsumer-tag-properties"></a>

`Key`  <a name="cfn-kinesis-streamconsumer-tag-key"></a>
A unique identifier for the tag. The maximum length for a tag key is 128 characters.
A tag key can only contain the following:
+ Unicode letters
+ Digits
+ White space
+ One or more of these symbols: `_`, `.`, `/`, `=`, `+`, `-`, `%`, `@`
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-kinesis-streamconsumer-tag-value"></a>
An optional string, typically used to describe or define the tag. The maximum length for a tag value is 256 characters.
A tag value can only contain the following:
+ Unicode letters
+ Digits
+ White space
+ One or more of these symbols: `_`, `.`, `/`, `=`, `+`, `-`, `%`, `@`
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
