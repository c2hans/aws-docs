---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accessanalyzer-analyzer-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer Tag
<a name="aws-properties-accessanalyzer-analyzer-tag"></a>

A key-value pair to associate with a resource. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

## Syntax
<a name="aws-properties-accessanalyzer-analyzer-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accessanalyzer-analyzer-tag-syntax.json"></a>

```
{
  "[Key](#cfn-accessanalyzer-analyzer-tag-key)" : {{String}},
  "[Value](#cfn-accessanalyzer-analyzer-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-accessanalyzer-analyzer-tag-syntax.yaml"></a>

```
  [Key](#cfn-accessanalyzer-analyzer-tag-key): {{String}}
  [Value](#cfn-accessanalyzer-analyzer-tag-value): {{String}}
```

## Properties
<a name="aws-properties-accessanalyzer-analyzer-tag-properties"></a>

`Key`  <a name="cfn-accessanalyzer-analyzer-tag-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`. digits, whitespace, `_`, `.`, `:`, `/`, `=`, `+`, `@`, `-`, and `"`.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Value`  <a name="cfn-accessanalyzer-analyzer-tag-value"></a>
The value for the tag. You can specify a value that's 1 to 256 characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
