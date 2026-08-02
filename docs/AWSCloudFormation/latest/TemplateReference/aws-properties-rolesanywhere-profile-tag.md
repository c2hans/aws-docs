---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rolesanywhere-profile-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RolesAnywhere::Profile Tag
<a name="aws-properties-rolesanywhere-profile-tag"></a>

A label that consists of a key and value you define.

## Syntax
<a name="aws-properties-rolesanywhere-profile-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rolesanywhere-profile-tag-syntax.json"></a>

```
{
  "[Key](#cfn-rolesanywhere-profile-tag-key)" : {{String}},
  "[Value](#cfn-rolesanywhere-profile-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-rolesanywhere-profile-tag-syntax.yaml"></a>

```
  [Key](#cfn-rolesanywhere-profile-tag-key): {{String}}
  [Value](#cfn-rolesanywhere-profile-tag-value): {{String}}
```

## Properties
<a name="aws-properties-rolesanywhere-profile-tag-properties"></a>

`Key`  <a name="cfn-rolesanywhere-profile-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-rolesanywhere-profile-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
