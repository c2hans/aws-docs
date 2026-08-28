---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream Tag
<a name="aws-properties-kinesisfirehose-deliverystream-tag"></a>

Metadata that you can assign to a Firehose stream, consisting of a key-value pair.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-tag-syntax.json"></a>

```
{
  "[Key](#cfn-kinesisfirehose-deliverystream-tag-key)" : {{String}},
  "[Value](#cfn-kinesisfirehose-deliverystream-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-tag-syntax.yaml"></a>

```
  [Key](#cfn-kinesisfirehose-deliverystream-tag-key): {{String}}
  [Value](#cfn-kinesisfirehose-deliverystream-tag-value): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-tag-properties"></a>

`Key`  <a name="cfn-kinesisfirehose-deliverystream-tag-key"></a>
A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, \_ . / = \+ - % @
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:\/=+\-@%]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-kinesisfirehose-deliverystream-tag-value"></a>
An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, \_ . / = \+ - % @
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}_.:\/=+\-@%]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
