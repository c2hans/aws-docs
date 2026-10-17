---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wellarchitected-reviewtemplate-tagsitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::ReviewTemplate TagsItems
<a name="aws-properties-wellarchitected-reviewtemplate-tagsitems"></a>

<a name="aws-properties-wellarchitected-reviewtemplate-tagsitems-description"></a>The `TagsItems` property type specifies Property description not available. for an [AWS::WellArchitected::ReviewTemplate](aws-resource-wellarchitected-reviewtemplate.md).

## Syntax
<a name="aws-properties-wellarchitected-reviewtemplate-tagsitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wellarchitected-reviewtemplate-tagsitems-syntax.json"></a>

```
{
  "[Key](#cfn-wellarchitected-reviewtemplate-tagsitems-key)" : {{String}},
  "[Value](#cfn-wellarchitected-reviewtemplate-tagsitems-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-wellarchitected-reviewtemplate-tagsitems-syntax.yaml"></a>

```
  [Key](#cfn-wellarchitected-reviewtemplate-tagsitems-key): {{String}}
  [Value](#cfn-wellarchitected-reviewtemplate-tagsitems-value): {{String}}
```

## Properties
<a name="aws-properties-wellarchitected-reviewtemplate-tagsitems-properties"></a>

`Key`  <a name="cfn-wellarchitected-reviewtemplate-tagsitems-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-wellarchitected-reviewtemplate-tagsitems-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
