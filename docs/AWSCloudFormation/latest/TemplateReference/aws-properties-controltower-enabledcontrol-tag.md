---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-controltower-enabledcontrol-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ControlTower::EnabledControl Tag
<a name="aws-properties-controltower-enabledcontrol-tag"></a>

A key-value pair to associate with a resource.

## Syntax
<a name="aws-properties-controltower-enabledcontrol-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-controltower-enabledcontrol-tag-syntax.json"></a>

```
{
  "[Key](#cfn-controltower-enabledcontrol-tag-key)" : {{String}},
  "[Value](#cfn-controltower-enabledcontrol-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-controltower-enabledcontrol-tag-syntax.yaml"></a>

```
  [Key](#cfn-controltower-enabledcontrol-tag-key): {{String}}
  [Value](#cfn-controltower-enabledcontrol-tag-value): {{String}}
```

## Properties
<a name="aws-properties-controltower-enabledcontrol-tag-properties"></a>

`Key`  <a name="cfn-controltower-enabledcontrol-tag-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-controltower-enabledcontrol-tag-value"></a>
The value for the tag. You can specify a value that's 0 to 256 Unicode characters in length.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
