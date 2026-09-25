---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-recommenderschema-tagsitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::RecommenderSchema TagsItems
<a name="aws-properties-customerprofiles-recommenderschema-tagsitems"></a>

<a name="aws-properties-customerprofiles-recommenderschema-tagsitems-description"></a>The `TagsItems` property type specifies Property description not available. for an [AWS::CustomerProfiles::RecommenderSchema](aws-resource-customerprofiles-recommenderschema.md).

## Syntax
<a name="aws-properties-customerprofiles-recommenderschema-tagsitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-recommenderschema-tagsitems-syntax.json"></a>

```
{
  "[Key](#cfn-customerprofiles-recommenderschema-tagsitems-key)" : {{String}},
  "[Value](#cfn-customerprofiles-recommenderschema-tagsitems-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-recommenderschema-tagsitems-syntax.yaml"></a>

```
  [Key](#cfn-customerprofiles-recommenderschema-tagsitems-key): {{String}}
  [Value](#cfn-customerprofiles-recommenderschema-tagsitems-value): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-recommenderschema-tagsitems-properties"></a>

`Key`  <a name="cfn-customerprofiles-recommenderschema-tagsitems-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-customerprofiles-recommenderschema-tagsitems-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
