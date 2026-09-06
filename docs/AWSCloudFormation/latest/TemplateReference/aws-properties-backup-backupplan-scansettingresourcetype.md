---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-backupplan-scansettingresourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::BackupPlan ScanSettingResourceType
<a name="aws-properties-backup-backupplan-scansettingresourcetype"></a>

<a name="aws-properties-backup-backupplan-scansettingresourcetype-description"></a>The `ScanSettingResourceType` property type specifies Property description not available. for an [AWS::Backup::BackupPlan](aws-resource-backup-backupplan.md).

## Syntax
<a name="aws-properties-backup-backupplan-scansettingresourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-backupplan-scansettingresourcetype-syntax.json"></a>

```
{
  "[MalwareScanner](#cfn-backup-backupplan-scansettingresourcetype-malwarescanner)" : {{String}},
  "[ResourceTypes](#cfn-backup-backupplan-scansettingresourcetype-resourcetypes)" : {{[ String, ... ]}},
  "[ScannerRoleArn](#cfn-backup-backupplan-scansettingresourcetype-scannerrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-backupplan-scansettingresourcetype-syntax.yaml"></a>

```
  [MalwareScanner](#cfn-backup-backupplan-scansettingresourcetype-malwarescanner): {{String}}
  [ResourceTypes](#cfn-backup-backupplan-scansettingresourcetype-resourcetypes): {{
    - String}}
  [ScannerRoleArn](#cfn-backup-backupplan-scansettingresourcetype-scannerrolearn): {{String}}
```

## Properties
<a name="aws-properties-backup-backupplan-scansettingresourcetype-properties"></a>

`MalwareScanner`  <a name="cfn-backup-backupplan-scansettingresourcetype-malwarescanner"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `GUARDDUTY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTypes`  <a name="cfn-backup-backupplan-scansettingresourcetype-resourcetypes"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScannerRoleArn`  <a name="cfn-backup-backupplan-scansettingresourcetype-scannerrolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
