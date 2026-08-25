---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-querysuggestionsblocklist-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::QuerySuggestionsBlockList Tag
<a name="aws-properties-kendra-querysuggestionsblocklist-tag"></a>

A key-value pair that identifies or categorizes an index, FAQ, data source, or other resource. TA tag key and value can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.

## Syntax
<a name="aws-properties-kendra-querysuggestionsblocklist-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-querysuggestionsblocklist-tag-syntax.json"></a>

```
{
  "[Key](#cfn-kendra-querysuggestionsblocklist-tag-key)" : {{String}},
  "[Value](#cfn-kendra-querysuggestionsblocklist-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-kendra-querysuggestionsblocklist-tag-syntax.yaml"></a>

```
  [Key](#cfn-kendra-querysuggestionsblocklist-tag-key): {{String}}
  [Value](#cfn-kendra-querysuggestionsblocklist-tag-value): {{String}}
```

## Properties
<a name="aws-properties-kendra-querysuggestionsblocklist-tag-properties"></a>

`Key`  <a name="cfn-kendra-querysuggestionsblocklist-tag-key"></a>
The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, data source, or other resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-kendra-querysuggestionsblocklist-tag-value"></a>
The value associated with the tag. The value may be an empty string but it can't be null.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
