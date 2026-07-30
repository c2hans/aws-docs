---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-restoretestingplan-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::RestoreTestingPlan Tag
<a name="aws-properties-backup-restoretestingplan-tag"></a>

The tags to assign to the restore testing plan.

## Syntax
<a name="aws-properties-backup-restoretestingplan-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-restoretestingplan-tag-syntax.json"></a>

```
{
  "[Key](#cfn-backup-restoretestingplan-tag-key)" : {{String}},
  "[Value](#cfn-backup-restoretestingplan-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-restoretestingplan-tag-syntax.yaml"></a>

```
  [Key](#cfn-backup-restoretestingplan-tag-key): {{String}}
  [Value](#cfn-backup-restoretestingplan-tag-value): {{String}}
```

## Properties
<a name="aws-properties-backup-restoretestingplan-tag-properties"></a>

`Key`  <a name="cfn-backup-restoretestingplan-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-backup-restoretestingplan-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
