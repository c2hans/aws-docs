---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-reportplan-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::ReportPlan Tag
<a name="aws-properties-backup-reportplan-tag"></a>

Metadata that you can assign to help organize your report plans. Each tag is a key-value pair.

## Syntax
<a name="aws-properties-backup-reportplan-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-reportplan-tag-syntax.json"></a>

```
{
  "[Key](#cfn-backup-reportplan-tag-key)" : {{String}},
  "[Value](#cfn-backup-reportplan-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-reportplan-tag-syntax.yaml"></a>

```
  [Key](#cfn-backup-reportplan-tag-key): {{String}}
  [Value](#cfn-backup-reportplan-tag-value): {{String}}
```

## Properties
<a name="aws-properties-backup-reportplan-tag-properties"></a>

`Key`  <a name="cfn-backup-reportplan-tag-key"></a>
The tag key.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-backup-reportplan-tag-value"></a>
The tag value.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
