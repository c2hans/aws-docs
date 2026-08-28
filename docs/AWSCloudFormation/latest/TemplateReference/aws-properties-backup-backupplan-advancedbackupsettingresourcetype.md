---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::BackupPlan AdvancedBackupSettingResourceType
<a name="aws-properties-backup-backupplan-advancedbackupsettingresourcetype"></a>

Specifies an object containing resource type and backup options. This is only supported for Windows VSS backups.

## Syntax
<a name="aws-properties-backup-backupplan-advancedbackupsettingresourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-backupplan-advancedbackupsettingresourcetype-syntax.json"></a>

```
{
  "[BackupOptions](#cfn-backup-backupplan-advancedbackupsettingresourcetype-backupoptions)" : {{Json}},
  "[ResourceType](#cfn-backup-backupplan-advancedbackupsettingresourcetype-resourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-backupplan-advancedbackupsettingresourcetype-syntax.yaml"></a>

```
  [BackupOptions](#cfn-backup-backupplan-advancedbackupsettingresourcetype-backupoptions): {{Json}}
  [ResourceType](#cfn-backup-backupplan-advancedbackupsettingresourcetype-resourcetype): {{String}}
```

## Properties
<a name="aws-properties-backup-backupplan-advancedbackupsettingresourcetype-properties"></a>

`BackupOptions`  <a name="cfn-backup-backupplan-advancedbackupsettingresourcetype-backupoptions"></a>
The backup option for the resource. Each option is a key-value pair. This option is only available for Windows VSS backup jobs.
Valid values:
Set to `"WindowsVSS":"enabled"` to enable the `WindowsVSS` backup option and create a Windows VSS backup.
Set to `"WindowsVSS":"disabled"` to create a regular backup. The `WindowsVSS` option is not enabled by default.
If you specify an invalid option, you get an `InvalidParameterValueException` exception.
For more information about Windows VSS backups, see [Creating a VSS-Enabled Windows Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html).
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-backup-backupplan-advancedbackupsettingresourcetype-resourcetype"></a>
The name of a resource type. The only supported resource type is EC2.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
