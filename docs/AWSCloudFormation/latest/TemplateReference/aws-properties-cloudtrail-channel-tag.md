---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-channel-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::Channel Tag
<a name="aws-properties-cloudtrail-channel-tag"></a>

A custom key-value pair associated with a resource such as a CloudTrail trail, event data store, dashboard, or channel.

## Syntax
<a name="aws-properties-cloudtrail-channel-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-channel-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cloudtrail-channel-tag-key)" : {{String}},
  "[Value](#cfn-cloudtrail-channel-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudtrail-channel-tag-syntax.yaml"></a>

```
  [Key](#cfn-cloudtrail-channel-tag-key): {{String}}
  [Value](#cfn-cloudtrail-channel-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cloudtrail-channel-tag-properties"></a>

`Key`  <a name="cfn-cloudtrail-channel-tag-key"></a>
The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cloudtrail-channel-tag-value"></a>
The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
