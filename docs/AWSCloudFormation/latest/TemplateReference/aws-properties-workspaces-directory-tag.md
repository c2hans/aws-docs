---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory Tag
<a name="aws-properties-workspaces-directory-tag"></a>

Describes a tag.

## Syntax
<a name="aws-properties-workspaces-directory-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-tag-syntax.json"></a>

```
{
  "[Key](#cfn-workspaces-directory-tag-key)" : {{String}},
  "[Value](#cfn-workspaces-directory-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-tag-syntax.yaml"></a>

```
  [Key](#cfn-workspaces-directory-tag-key): {{String}}
  [Value](#cfn-workspaces-directory-tag-value): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-tag-properties"></a>

`Key`  <a name="cfn-workspaces-directory-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-workspaces-directory-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
