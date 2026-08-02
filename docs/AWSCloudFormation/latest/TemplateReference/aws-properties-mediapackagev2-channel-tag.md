---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-channel-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::Channel Tag
<a name="aws-properties-mediapackagev2-channel-tag"></a>

A comma-separated list of tag key:value pairs that you define.

## Syntax
<a name="aws-properties-mediapackagev2-channel-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-channel-tag-syntax.json"></a>

```
{
  "[Key](#cfn-mediapackagev2-channel-tag-key)" : {{String}},
  "[Value](#cfn-mediapackagev2-channel-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-channel-tag-syntax.yaml"></a>

```
  [Key](#cfn-mediapackagev2-channel-tag-key): {{String}}
  [Value](#cfn-mediapackagev2-channel-tag-value): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-channel-tag-properties"></a>

`Key`  <a name="cfn-mediapackagev2-channel-tag-key"></a>
The key in the key:value pair for the tag.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-mediapackagev2-channel-tag-value"></a>
The value in the key:value pair for the tag.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
