---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-workspace-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Workspace Tag
<a name="aws-properties-workspaces-workspace-tag"></a>

Describes a tag.

## Syntax
<a name="aws-properties-workspaces-workspace-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-workspace-tag-syntax.json"></a>

```
{
  "[Key](#cfn-workspaces-workspace-tag-key)" : {{String}},
  "[Value](#cfn-workspaces-workspace-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-workspace-tag-syntax.yaml"></a>

```
  [Key](#cfn-workspaces-workspace-tag-key): {{String}}
  [Value](#cfn-workspaces-workspace-tag-value): {{String}}
```

## Properties
<a name="aws-properties-workspaces-workspace-tag-properties"></a>

`Key`  <a name="cfn-workspaces-workspace-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-workspaces-workspace-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
