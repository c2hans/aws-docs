---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-logicallyairgappedbackupvault-notificationobjecttype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::LogicallyAirGappedBackupVault NotificationObjectType
<a name="aws-properties-backup-logicallyairgappedbackupvault-notificationobjecttype"></a>

<a name="aws-properties-backup-logicallyairgappedbackupvault-notificationobjecttype-description"></a>The `NotificationObjectType` property type specifies Property description not available. for an [AWS::Backup::LogicallyAirGappedBackupVault](aws-resource-backup-logicallyairgappedbackupvault.md).

## Syntax
<a name="aws-properties-backup-logicallyairgappedbackupvault-notificationobjecttype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-logicallyairgappedbackupvault-notificationobjecttype-syntax.json"></a>

```
{
  "[BackupVaultEvents](#cfn-backup-logicallyairgappedbackupvault-notificationobjecttype-backupvaultevents)" : {{[ String, ... ]}},
  "[SNSTopicArn](#cfn-backup-logicallyairgappedbackupvault-notificationobjecttype-snstopicarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-backup-logicallyairgappedbackupvault-notificationobjecttype-syntax.yaml"></a>

```
  [BackupVaultEvents](#cfn-backup-logicallyairgappedbackupvault-notificationobjecttype-backupvaultevents): {{
    - String}}
  [SNSTopicArn](#cfn-backup-logicallyairgappedbackupvault-notificationobjecttype-snstopicarn): {{String}}
```

## Properties
<a name="aws-properties-backup-logicallyairgappedbackupvault-notificationobjecttype-properties"></a>

`BackupVaultEvents`  <a name="cfn-backup-logicallyairgappedbackupvault-notificationobjecttype-backupvaultevents"></a>
An array of events that indicate the status of jobs to back up resources to the backup vault.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SNSTopicArn`  <a name="cfn-backup-logicallyairgappedbackupvault-notificationobjecttype-snstopicarn"></a>
The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events; for example, `arn:aws:sns:us-west-2:111122223333:MyVaultTopic`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
