---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-filter-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Filter Tag
<a name="aws-properties-personalize-filter-tag"></a>

The optional metadata that you apply to resources to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information see [Tagging Amazon Personalize resources](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html).

## Syntax
<a name="aws-properties-personalize-filter-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-filter-tag-syntax.json"></a>

```
{
  "[Key](#cfn-personalize-filter-tag-key)" : {{String}},
  "[Value](#cfn-personalize-filter-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-personalize-filter-tag-syntax.yaml"></a>

```
  [Key](#cfn-personalize-filter-tag-key): {{String}}
  [Value](#cfn-personalize-filter-tag-value): {{String}}
```

## Properties
<a name="aws-properties-personalize-filter-tag-properties"></a>

`Key`  <a name="cfn-personalize-filter-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-personalize-filter-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
