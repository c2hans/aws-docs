---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-index-valueimportanceitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::Index ValueImportanceItem
<a name="aws-properties-kendra-index-valueimportanceitem"></a>

Specifies a key-value pair of the search boost value for a document when the key is part of the metadata of a document.

## Syntax
<a name="aws-properties-kendra-index-valueimportanceitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-index-valueimportanceitem-syntax.json"></a>

```
{
  "[Key](#cfn-kendra-index-valueimportanceitem-key)" : {{String}},
  "[Value](#cfn-kendra-index-valueimportanceitem-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kendra-index-valueimportanceitem-syntax.yaml"></a>

```
  [Key](#cfn-kendra-index-valueimportanceitem-key): {{String}}
  [Value](#cfn-kendra-index-valueimportanceitem-value): {{Integer}}
```

## Properties
<a name="aws-properties-kendra-index-valueimportanceitem-properties"></a>

`Key`  <a name="cfn-kendra-index-valueimportanceitem-key"></a>
The document metadata value used for the search boost.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-kendra-index-valueimportanceitem-value"></a>
The boost value for a document when the key is part of the metadata of a document.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
