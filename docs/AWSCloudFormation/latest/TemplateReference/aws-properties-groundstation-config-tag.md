---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config Tag
<a name="aws-properties-groundstation-config-tag"></a>

The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`. digits, whitespace, `_`, `.`, `:`, `/`, `=`, `+`, `@`, `-`, and `"`.

For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html)

## Syntax
<a name="aws-properties-groundstation-config-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-tag-syntax.json"></a>

```
{
  "[Key](#cfn-groundstation-config-tag-key)" : {{String}},
  "[Value](#cfn-groundstation-config-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-config-tag-syntax.yaml"></a>

```
  [Key](#cfn-groundstation-config-tag-key): {{String}}
  [Value](#cfn-groundstation-config-tag-value): {{String}}
```

## Properties
<a name="aws-properties-groundstation-config-tag-properties"></a>

`Key`  <a name="cfn-groundstation-config-tag-key"></a>
Name of the object key.
*Required*: No
*Type*: String
*Pattern*: `^[ a-zA-Z0-9\+\-=._:/@]{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-groundstation-config-tag-value"></a>
Value of the tag.
*Required*: No
*Type*: String
*Pattern*: `^[ a-zA-Z0-9\+\-=._:/@]{1,256}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
