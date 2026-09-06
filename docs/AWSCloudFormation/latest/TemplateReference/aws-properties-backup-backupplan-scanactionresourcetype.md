---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-backupplan-scanactionresourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::BackupPlan ScanActionResourceType
<a name="aws-properties-backup-backupplan-scanactionresourcetype"></a>

<a name="aws-properties-backup-backupplan-scanactionresourcetype-description"></a>The `ScanActionResourceType` property type specifies Property description not available. for an [AWS::Backup::BackupPlan](aws-resource-backup-backupplan.md).

## Syntax
<a name="aws-properties-backup-backupplan-scanactionresourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-backupplan-scanactionresourcetype-syntax.json"></a>

```
{
  "[MalwareScanner](#cfn-backup-backupplan-scanactionresourcetype-malwarescanner)" : {{String}},
  "[ScanMode](#cfn-backup-backupplan-scanactionresourcetype-scanmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-backupplan-scanactionresourcetype-syntax.yaml"></a>

```
  [MalwareScanner](#cfn-backup-backupplan-scanactionresourcetype-malwarescanner): {{String}}
  [ScanMode](#cfn-backup-backupplan-scanactionresourcetype-scanmode): {{String}}
```

## Properties
<a name="aws-properties-backup-backupplan-scanactionresourcetype-properties"></a>

`MalwareScanner`  <a name="cfn-backup-backupplan-scanactionresourcetype-malwarescanner"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `GUARDDUTY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScanMode`  <a name="cfn-backup-backupplan-scanactionresourcetype-scanmode"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `FULL_SCAN | INCREMENTAL_SCAN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
