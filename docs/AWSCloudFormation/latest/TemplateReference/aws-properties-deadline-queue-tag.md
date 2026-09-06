---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-queue-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue Tag
<a name="aws-properties-deadline-queue-tag"></a>

The tags to add to your queue. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.

## Syntax
<a name="aws-properties-deadline-queue-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-queue-tag-syntax.json"></a>

```
{
  "[Key](#cfn-deadline-queue-tag-key)" : {{String}},
  "[Value](#cfn-deadline-queue-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-queue-tag-syntax.yaml"></a>

```
  [Key](#cfn-deadline-queue-tag-key): {{String}}
  [Value](#cfn-deadline-queue-tag-value): {{String}}
```

## Properties
<a name="aws-properties-deadline-queue-tag-properties"></a>

`Key`  <a name="cfn-deadline-queue-tag-key"></a>
The key name of the tag. You can specify a value that's 1 to 127 Unicode characters in length and can't be prefixed with `aws:`. digits, whitespace, `_`, `.`, `:`, `/`, `=`, `+`, `@`, `-`, and `"`.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-deadline-queue-tag-value"></a>
The value for the tag. You can specify a value that's 1 to 255 characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
