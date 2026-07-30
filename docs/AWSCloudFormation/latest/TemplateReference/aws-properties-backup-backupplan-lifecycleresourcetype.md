---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-backupplan-lifecycleresourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::BackupPlan LifecycleResourceType
<a name="aws-properties-backup-backupplan-lifecycleresourcetype"></a>

Specifies an object containing an array of `Transition` objects that determine how long in days before a recovery point transitions to cold storage or is deleted.

## Syntax
<a name="aws-properties-backup-backupplan-lifecycleresourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-backupplan-lifecycleresourcetype-syntax.json"></a>

```
{
  "[DeleteAfterDays](#cfn-backup-backupplan-lifecycleresourcetype-deleteafterdays)" : {{Number}},
  "[MoveToColdStorageAfterDays](#cfn-backup-backupplan-lifecycleresourcetype-movetocoldstorageafterdays)" : {{Number}},
  "[OptInToArchiveForSupportedResources](#cfn-backup-backupplan-lifecycleresourcetype-optintoarchiveforsupportedresources)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-backup-backupplan-lifecycleresourcetype-syntax.yaml"></a>

```
  [DeleteAfterDays](#cfn-backup-backupplan-lifecycleresourcetype-deleteafterdays): {{Number}}
  [MoveToColdStorageAfterDays](#cfn-backup-backupplan-lifecycleresourcetype-movetocoldstorageafterdays): {{Number}}
  [OptInToArchiveForSupportedResources](#cfn-backup-backupplan-lifecycleresourcetype-optintoarchiveforsupportedresources): {{Boolean}}
```

## Properties
<a name="aws-properties-backup-backupplan-lifecycleresourcetype-properties"></a>

`DeleteAfterDays`  <a name="cfn-backup-backupplan-lifecycleresourcetype-deleteafterdays"></a>
The number of days after creation that a recovery point is deleted. This value must be at least 90 days after the number of days specified in `MoveToColdStorageAfterDays`.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MoveToColdStorageAfterDays`  <a name="cfn-backup-backupplan-lifecycleresourcetype-movetocoldstorageafterdays"></a>
The number of days after creation that a recovery point is moved to cold storage.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OptInToArchiveForSupportedResources`  <a name="cfn-backup-backupplan-lifecycleresourcetype-optintoarchiveforsupportedresources"></a>
If the value is true, your backup plan transitions supported resources to archive (cold) storage tier in accordance with your lifecycle settings.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
