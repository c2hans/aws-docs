---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-backup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Backup
<a name="aws-resource-dynamodb-backup"></a>

Creates a backup for an existing table.

 Each time you create an on-demand backup, the entire table data is backed up. There is no limit to the number of on-demand backups that can be taken.

 When you create an on-demand backup, a time marker of the request is cataloged, and the backup is created asynchronously, by applying all changes until the time of the request to the last full table snapshot. Backup requests are processed instantaneously and become available for restore within minutes.

You can call `CreateBackup` at a maximum rate of 50 times per second.

All backups in DynamoDB work without consuming any provisioned throughput on the table.

 If you submit a backup request on 2018-12-14 at 14:25:00, the backup is guaranteed to contain all data committed to the table up to 14:24:00, and data committed after 14:26:00 will not be. The backup might contain data modifications made between 14:24:00 and 14:26:00. On-demand backup does not support causal consistency.

 Along with data, the following are also included on the backups:
+ Global secondary indexes (GSIs)
+ Local secondary indexes (LSIs)
+ Streams
+ Provisioned read and write capacity

## Syntax
<a name="aws-resource-dynamodb-backup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dynamodb-backup-syntax.json"></a>

```
{
  "Type" : "AWS::DynamoDB::Backup",
  "Properties" : {
      "[BackupName](#cfn-dynamodb-backup-backupname)" : {{String}},
      "[TableName](#cfn-dynamodb-backup-tablename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-dynamodb-backup-syntax.yaml"></a>

```
Type: AWS::DynamoDB::Backup
Properties:
  [BackupName](#cfn-dynamodb-backup-backupname): {{String}}
  [TableName](#cfn-dynamodb-backup-tablename): {{String}}
```

## Properties
<a name="aws-resource-dynamodb-backup-properties"></a>

`BackupName`  <a name="cfn-dynamodb-backup-backupname"></a>
Name of the specified backup.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-dynamodb-backup-tablename"></a>
Name of the table.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-dynamodb-backup-return-values"></a>

### Ref
<a name="aws-resource-dynamodb-backup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-dynamodb-backup-return-values-fn--getatt"></a>

####
<a name="aws-resource-dynamodb-backup-return-values-fn--getatt-fn--getatt"></a>

`BackupArn`  <a name="BackupArn-fn::getatt"></a>
ARN associated with the backup.

`BackupCreationDateTime`  <a name="BackupCreationDateTime-fn::getatt"></a>
Time at which the backup was created.

`BackupId`  <a name="BackupId-fn::getatt"></a>
Property description not available.

`BackupSizeBytes`  <a name="BackupSizeBytes-fn::getatt"></a>
Size of the backup in bytes.

`BackupStatus`  <a name="BackupStatus-fn::getatt"></a>
Backup can be in one of the following states: CREATING, ACTIVE, DELETED.

`BackupType`  <a name="BackupType-fn::getatt"></a>
BackupType:
+ `USER` - You create and manage these using the on-demand backup feature.
+ `SYSTEM` - If you delete a table with point-in-time recovery enabled, a `SYSTEM` backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion.
+ `AWS_BACKUP` - On-demand backup created by you from AWS Backup service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
