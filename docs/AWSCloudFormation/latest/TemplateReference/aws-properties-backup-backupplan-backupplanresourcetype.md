---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-backupplan-backupplanresourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::BackupPlan BackupPlanResourceType
<a name="aws-properties-backup-backupplan-backupplanresourcetype"></a>

Specifies an object containing properties used to create a backup plan.

## Syntax
<a name="aws-properties-backup-backupplan-backupplanresourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-backupplan-backupplanresourcetype-syntax.json"></a>

```
{
  "[AdvancedBackupSettings](#cfn-backup-backupplan-backupplanresourcetype-advancedbackupsettings)" : {{[ AdvancedBackupSettingResourceType, ... ]}},
  "[BackupPlanName](#cfn-backup-backupplan-backupplanresourcetype-backupplanname)" : {{String}},
  "[BackupPlanRule](#cfn-backup-backupplan-backupplanresourcetype-backupplanrule)" : {{[ BackupRuleResourceType, ... ]}},
  "[ScanSettings](#cfn-backup-backupplan-backupplanresourcetype-scansettings)" : {{[ ScanSettingResourceType, ... ]}}
}
```

### YAML
<a name="aws-properties-backup-backupplan-backupplanresourcetype-syntax.yaml"></a>

```
  [AdvancedBackupSettings](#cfn-backup-backupplan-backupplanresourcetype-advancedbackupsettings): {{
    - AdvancedBackupSettingResourceType}}
  [BackupPlanName](#cfn-backup-backupplan-backupplanresourcetype-backupplanname): {{String}}
  [BackupPlanRule](#cfn-backup-backupplan-backupplanresourcetype-backupplanrule): {{
    - BackupRuleResourceType}}
  [ScanSettings](#cfn-backup-backupplan-backupplanresourcetype-scansettings): {{
    - ScanSettingResourceType}}
```

## Properties
<a name="aws-properties-backup-backupplan-backupplanresourcetype-properties"></a>

`AdvancedBackupSettings`  <a name="cfn-backup-backupplan-backupplanresourcetype-advancedbackupsettings"></a>
A list of backup options for each resource type.
*Required*: No
*Type*: Array of [AdvancedBackupSettingResourceType](aws-properties-backup-backupplan-advancedbackupsettingresourcetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BackupPlanName`  <a name="cfn-backup-backupplan-backupplanresourcetype-backupplanname"></a>
The display name of a backup plan.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BackupPlanRule`  <a name="cfn-backup-backupplan-backupplanresourcetype-backupplanrule"></a>
An array of `BackupRule` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
*Required*: Yes
*Type*: Array of [BackupRuleResourceType](aws-properties-backup-backupplan-backupruleresourcetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScanSettings`  <a name="cfn-backup-backupplan-backupplanresourcetype-scansettings"></a>
Property description not available.
*Required*: No
*Type*: Array of [ScanSettingResourceType](aws-properties-backup-backupplan-scansettingresourcetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
