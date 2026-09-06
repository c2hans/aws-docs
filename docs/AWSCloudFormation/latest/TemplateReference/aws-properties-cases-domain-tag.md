---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-domain-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Domain Tag
<a name="aws-properties-cases-domain-tag"></a>

A key-value pair to associate with a resource.

## Syntax
<a name="aws-properties-cases-domain-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-domain-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cases-domain-tag-key)" : {{String}},
  "[Value](#cfn-cases-domain-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cases-domain-tag-syntax.yaml"></a>

```
  [Key](#cfn-cases-domain-tag-key): {{String}}
  [Value](#cfn-cases-domain-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cases-domain-tag-properties"></a>

`Key`  <a name="cfn-cases-domain-tag-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`. You can use any of the following characters: the set of Unicode letters, digits, whitespace, `_`, `.`, `:`, `/`, `=`, `+`, `@`, `-`, and `"`.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cases-domain-tag-value"></a>
The value for the tag. You can specify a value that's 1 to 256 characters in length.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
