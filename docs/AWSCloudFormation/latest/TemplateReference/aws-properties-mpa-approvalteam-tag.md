---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mpa-approvalteam-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MPA::ApprovalTeam Tag
<a name="aws-properties-mpa-approvalteam-tag"></a>

Tags that you have added to the specified resource.

## Syntax
<a name="aws-properties-mpa-approvalteam-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mpa-approvalteam-tag-syntax.json"></a>

```
{
  "[Key](#cfn-mpa-approvalteam-tag-key)" : {{String}},
  "[Value](#cfn-mpa-approvalteam-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-mpa-approvalteam-tag-syntax.yaml"></a>

```
  [Key](#cfn-mpa-approvalteam-tag-key): {{String}}
  [Value](#cfn-mpa-approvalteam-tag-value): {{String}}
```

## Properties
<a name="aws-properties-mpa-approvalteam-tag-properties"></a>

`Key`  <a name="cfn-mpa-approvalteam-tag-key"></a>
One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-mpa-approvalteam-tag-value"></a>
One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
