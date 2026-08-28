---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-backupplan-backupruleresourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::BackupPlan BackupRuleResourceType
<a name="aws-properties-backup-backupplan-backupruleresourcetype"></a>

Specifies an object containing properties used to schedule a task to back up a selection of resources.

## Syntax
<a name="aws-properties-backup-backupplan-backupruleresourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-backupplan-backupruleresourcetype-syntax.json"></a>

```
{
  "[CompletionWindowMinutes](#cfn-backup-backupplan-backupruleresourcetype-completionwindowminutes)" : {{Number}},
  "[CopyActions](#cfn-backup-backupplan-backupruleresourcetype-copyactions)" : {{[ CopyActionResourceType, ... ]}},
  "[EnableContinuousBackup](#cfn-backup-backupplan-backupruleresourcetype-enablecontinuousbackup)" : {{Boolean}},
  "[IndexActions](#cfn-backup-backupplan-backupruleresourcetype-indexactions)" : {{[ IndexActionsResourceType, ... ]}},
  "[Lifecycle](#cfn-backup-backupplan-backupruleresourcetype-lifecycle)" : {{LifecycleResourceType}},
  "[RecoveryPointTags](#cfn-backup-backupplan-backupruleresourcetype-recoverypointtags)" : {{{{{Key}}: {{Value}}, ...}}},
  "[RuleName](#cfn-backup-backupplan-backupruleresourcetype-rulename)" : {{String}},
  "[ScanActions](#cfn-backup-backupplan-backupruleresourcetype-scanactions)" : {{[ ScanActionResourceType, ... ]}},
  "[ScheduleExpression](#cfn-backup-backupplan-backupruleresourcetype-scheduleexpression)" : {{String}},
  "[ScheduleExpressionTimezone](#cfn-backup-backupplan-backupruleresourcetype-scheduleexpressiontimezone)" : {{String}},
  "[StartWindowMinutes](#cfn-backup-backupplan-backupruleresourcetype-startwindowminutes)" : {{Number}},
  "[TargetBackupVault](#cfn-backup-backupplan-backupruleresourcetype-targetbackupvault)" : {{String}},
  "[TargetLogicallyAirGappedBackupVaultArn](#cfn-backup-backupplan-backupruleresourcetype-targetlogicallyairgappedbackupvaultarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-backupplan-backupruleresourcetype-syntax.yaml"></a>

```
  [CompletionWindowMinutes](#cfn-backup-backupplan-backupruleresourcetype-completionwindowminutes): {{Number}}
  [CopyActions](#cfn-backup-backupplan-backupruleresourcetype-copyactions): {{
    - CopyActionResourceType}}
  [EnableContinuousBackup](#cfn-backup-backupplan-backupruleresourcetype-enablecontinuousbackup): {{Boolean}}
  [IndexActions](#cfn-backup-backupplan-backupruleresourcetype-indexactions): {{
    - IndexActionsResourceType}}
  [Lifecycle](#cfn-backup-backupplan-backupruleresourcetype-lifecycle): {{
    LifecycleResourceType}}
  [RecoveryPointTags](#cfn-backup-backupplan-backupruleresourcetype-recoverypointtags): {{
    {{Key}}: {{Value}}}}
  [RuleName](#cfn-backup-backupplan-backupruleresourcetype-rulename): {{String}}
  [ScanActions](#cfn-backup-backupplan-backupruleresourcetype-scanactions): {{
    - ScanActionResourceType}}
  [ScheduleExpression](#cfn-backup-backupplan-backupruleresourcetype-scheduleexpression): {{String}}
  [ScheduleExpressionTimezone](#cfn-backup-backupplan-backupruleresourcetype-scheduleexpressiontimezone): {{String}}
  [StartWindowMinutes](#cfn-backup-backupplan-backupruleresourcetype-startwindowminutes): {{Number}}
  [TargetBackupVault](#cfn-backup-backupplan-backupruleresourcetype-targetbackupvault): {{String}}
  [TargetLogicallyAirGappedBackupVaultArn](#cfn-backup-backupplan-backupruleresourcetype-targetlogicallyairgappedbackupvaultarn): {{String}}
```

## Properties
<a name="aws-properties-backup-backupplan-backupruleresourcetype-properties"></a>

`CompletionWindowMinutes`  <a name="cfn-backup-backupplan-backupruleresourcetype-completionwindowminutes"></a>
A value in minutes after a backup job is successfully started before it must be completed or it is canceled by AWS Backup.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CopyActions`  <a name="cfn-backup-backupplan-backupruleresourcetype-copyactions"></a>
An array of CopyAction objects, which contains the details of the copy operation.
*Required*: No
*Type*: Array of [CopyActionResourceType](aws-properties-backup-backupplan-copyactionresourcetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableContinuousBackup`  <a name="cfn-backup-backupplan-backupruleresourcetype-enablecontinuousbackup"></a>
Enables continuous backup and point-in-time restores (PITR).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexActions`  <a name="cfn-backup-backupplan-backupruleresourcetype-indexactions"></a>
There can up to one IndexAction in each BackupRule, as each backup can have 0 or 1 backup index associated with it.
Within the array is ResourceTypes. Only 1 resource type will be accepted for each BackupRule. Valid values:
+ `EBS` for Amazon Elastic Block Store
+ `S3` for Amazon Simple Storage Service (Amazon S3)
*Required*: No
*Type*: Array of [IndexActionsResourceType](aws-properties-backup-backupplan-indexactionsresourcetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lifecycle`  <a name="cfn-backup-backupplan-backupruleresourcetype-lifecycle"></a>
The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
*Required*: No
*Type*: [LifecycleResourceType](aws-properties-backup-backupplan-lifecycleresourcetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecoveryPointTags`  <a name="cfn-backup-backupplan-backupruleresourcetype-recoverypointtags"></a>
The tags to assign to the resources.
*Required*: No
*Type*: Object of String
*Pattern*: `^.{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleName`  <a name="cfn-backup-backupplan-backupruleresourcetype-rulename"></a>
A display name for a backup rule.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScanActions`  <a name="cfn-backup-backupplan-backupruleresourcetype-scanactions"></a>
Property description not available.
*Required*: No
*Type*: Array of [ScanActionResourceType](aws-properties-backup-backupplan-scanactionresourcetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpression`  <a name="cfn-backup-backupplan-backupruleresourcetype-scheduleexpression"></a>
A CRON expression specifying when AWS Backup initiates a backup job.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpressionTimezone`  <a name="cfn-backup-backupplan-backupruleresourcetype-scheduleexpressiontimezone"></a>
This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartWindowMinutes`  <a name="cfn-backup-backupplan-backupruleresourcetype-startwindowminutes"></a>
An optional value that specifies a period of time in minutes after a backup is scheduled before a job is canceled if it doesn't start successfully.
If this value is included, it must be at least 60 minutes to avoid errors.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetBackupVault`  <a name="cfn-backup-backupplan-backupruleresourcetype-targetbackupvault"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of letters, numbers, and hyphens.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetLogicallyAirGappedBackupVaultArn`  <a name="cfn-backup-backupplan-backupruleresourcetype-targetlogicallyairgappedbackupvaultarn"></a>
The ARN of a logically air-gapped vault. ARN must be in the same account and Region. If provided, supported fully managed resources back up directly to logically air-gapped vault, while other supported resources create a temporary (billable) snapshot in backup vault, then copy it to logically air-gapped vault. Unsupported resources only back up to the specified backup vault.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
