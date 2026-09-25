---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber Tag
<a name="aws-properties-eventsv2-subscriber-tag"></a>

The metadata that you apply to the subscriber to help you categorize and organize it. Each tag consists of a key and a value, both of which you define.

## Syntax
<a name="aws-properties-eventsv2-subscriber-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-tag-syntax.json"></a>

```
{
  "[Key](#cfn-eventsv2-subscriber-tag-key)" : {{String}},
  "[Value](#cfn-eventsv2-subscriber-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-tag-syntax.yaml"></a>

```
  [Key](#cfn-eventsv2-subscriber-tag-key): {{String}}
  [Value](#cfn-eventsv2-subscriber-tag-value): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-tag-properties"></a>

`Key`  <a name="cfn-eventsv2-subscriber-tag-key"></a>
The key name of the tag. The key can be 1 to 128 characters and must not begin or end with a space.
*Required*: Yes
*Type*: String
*Pattern*: `^\S([\s\S]*\S)?(?![\s\S])`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-eventsv2-subscriber-tag-value"></a>
The value for the tag. The value can be 0 to 256 characters and can be empty.
*Required*: Yes
*Type*: String
*Pattern*: `^(\S([\s\S]*\S)?)?(?![\s\S])`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
