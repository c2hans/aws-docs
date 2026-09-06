---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisvideo-stream-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisVideo::Stream Tag
<a name="aws-properties-kinesisvideo-stream-tag"></a>

A key and value pair that is associated with the specified signaling channel.

## Syntax
<a name="aws-properties-kinesisvideo-stream-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisvideo-stream-tag-syntax.json"></a>

```
{
  "[Key](#cfn-kinesisvideo-stream-tag-key)" : {{String}},
  "[Value](#cfn-kinesisvideo-stream-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisvideo-stream-tag-syntax.yaml"></a>

```
  [Key](#cfn-kinesisvideo-stream-tag-key): {{String}}
  [Value](#cfn-kinesisvideo-stream-tag-value): {{String}}
```

## Properties
<a name="aws-properties-kinesisvideo-stream-tag-properties"></a>

`Key`  <a name="cfn-kinesisvideo-stream-tag-key"></a>
The key of the tag that is associated with the specified signaling channel.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-kinesisvideo-stream-tag-value"></a>
The value of the tag that is associated with the specified signaling channel.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
