---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-controltower-enabledbaseline-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ControlTower::EnabledBaseline Tag
<a name="aws-properties-controltower-enabledbaseline-tag"></a>

A key-value pair to associate with a resource.

## Syntax
<a name="aws-properties-controltower-enabledbaseline-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-controltower-enabledbaseline-tag-syntax.json"></a>

```
{
  "[Key](#cfn-controltower-enabledbaseline-tag-key)" : {{String}},
  "[Value](#cfn-controltower-enabledbaseline-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-controltower-enabledbaseline-tag-syntax.yaml"></a>

```
  [Key](#cfn-controltower-enabledbaseline-tag-key): {{String}}
  [Value](#cfn-controltower-enabledbaseline-tag-value): {{String}}
```

## Properties
<a name="aws-properties-controltower-enabledbaseline-tag-properties"></a>

`Key`  <a name="cfn-controltower-enabledbaseline-tag-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-controltower-enabledbaseline-tag-value"></a>
The value for the tag. You can specify a value that's 0 to 256 Unicode characters in length.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
