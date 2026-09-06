---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic Tag
<a name="aws-properties-quicksight-topic-tag"></a>

A key-value pair to associate with a resource.

## Syntax
<a name="aws-properties-quicksight-topic-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-tag-syntax.json"></a>

```
{
  "[Key](#cfn-quicksight-topic-tag-key)" : {{String}},
  "[Value](#cfn-quicksight-topic-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-tag-syntax.yaml"></a>

```
  [Key](#cfn-quicksight-topic-tag-key): {{String}}
  [Value](#cfn-quicksight-topic-tag-value): {{String}}
```

## Properties
<a name="aws-properties-quicksight-topic-tag-properties"></a>

`Key`  <a name="cfn-quicksight-topic-tag-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length. The key is case-sensitive and can't be prefixed with `aws:`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-quicksight-topic-tag-value"></a>
The value for the tag. You can specify a value that's 0 to 256 Unicode characters in length. The value is case-sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
