---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sns-topic-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SNS::Topic Tag
<a name="aws-properties-sns-topic-tag"></a>

The list of tags to be added to the specified topic.

## Syntax
<a name="aws-properties-sns-topic-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sns-topic-tag-syntax.json"></a>

```
{
  "[Key](#cfn-sns-topic-tag-key)" : {{String}},
  "[Value](#cfn-sns-topic-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sns-topic-tag-syntax.yaml"></a>

```
  [Key](#cfn-sns-topic-tag-key): {{String}}
  [Value](#cfn-sns-topic-tag-value): {{String}}
```

## Properties
<a name="aws-properties-sns-topic-tag-properties"></a>

`Key`  <a name="cfn-sns-topic-tag-key"></a>
The required key portion of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sns-topic-tag-value"></a>
The optional value portion of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
