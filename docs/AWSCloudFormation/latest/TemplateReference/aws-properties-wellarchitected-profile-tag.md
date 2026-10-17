---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wellarchitected-profile-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::Profile Tag
<a name="aws-properties-wellarchitected-profile-tag"></a>

A key-value pair associated with a resource for cost allocation and access control.

## Syntax
<a name="aws-properties-wellarchitected-profile-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wellarchitected-profile-tag-syntax.json"></a>

```
{
  "[Key](#cfn-wellarchitected-profile-tag-key)" : {{String}},
  "[Value](#cfn-wellarchitected-profile-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-wellarchitected-profile-tag-syntax.yaml"></a>

```
  [Key](#cfn-wellarchitected-profile-tag-key): {{String}}
  [Value](#cfn-wellarchitected-profile-tag-value): {{String}}
```

## Properties
<a name="aws-properties-wellarchitected-profile-tag-properties"></a>

`Key`  <a name="cfn-wellarchitected-profile-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-wellarchitected-profile-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
