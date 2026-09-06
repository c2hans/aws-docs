---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-thesaurus-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::Thesaurus Tag
<a name="aws-properties-kendra-thesaurus-tag"></a>

A key-value pair that identifies or categorizes an index, FAQ, data source, or other resource. TA tag key and value can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.

## Syntax
<a name="aws-properties-kendra-thesaurus-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-thesaurus-tag-syntax.json"></a>

```
{
  "[Key](#cfn-kendra-thesaurus-tag-key)" : {{String}},
  "[Value](#cfn-kendra-thesaurus-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-kendra-thesaurus-tag-syntax.yaml"></a>

```
  [Key](#cfn-kendra-thesaurus-tag-key): {{String}}
  [Value](#cfn-kendra-thesaurus-tag-value): {{String}}
```

## Properties
<a name="aws-properties-kendra-thesaurus-tag-properties"></a>

`Key`  <a name="cfn-kendra-thesaurus-tag-key"></a>
The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, data source, or other resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-kendra-thesaurus-tag-value"></a>
The value associated with the tag. The value may be an empty string but it can't be null.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
