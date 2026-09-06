---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-workspace-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace Tag
<a name="aws-properties-aps-workspace-tag"></a>

A tag associated with a resource.

## Syntax
<a name="aws-properties-aps-workspace-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-workspace-tag-syntax.json"></a>

```
{
  "[Key](#cfn-aps-workspace-tag-key)" : {{String}},
  "[Value](#cfn-aps-workspace-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-aps-workspace-tag-syntax.yaml"></a>

```
  [Key](#cfn-aps-workspace-tag-key): {{String}}
  [Value](#cfn-aps-workspace-tag-value): {{String}}
```

## Properties
<a name="aws-properties-aps-workspace-tag-properties"></a>

`Key`  <a name="cfn-aps-workspace-tag-key"></a>
The key of the tag. Must not begin with `aws:`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-aps-workspace-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
