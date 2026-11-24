---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedBackupsAWS.html
---

# Backing up and restoring DynamoDB tables with AWS Backup: How it works

You can use AWS Backup to create full and incremental backups of your Amazon DynamoDB tables. This section provides an overview of what happens during the backup and restore process.

## Backups
<a name="GettingStartedBackupsAWS.backups"></a>

When you create a backup, AWS Backup catalogs a time marker of the request and creates the backup asynchronously. There is no limit to the number of backups that you can create.

With AWS Backup, you can create the following types of backups of your DynamoDB tables:

Full backups
Each backup contains the entire table data.

Incremental backups
The first backup of a table is a full backup. Each subsequent backup stores only the data that changed since the previous backup.

To keep restores fast, AWS Backup periodically takes a new full backup of each table that uses incremental backups. This process is called periodic rebasing, and AWS Backup manages it automatically.

Incremental backups apply to backup plans with a frequency from 1 hour to 7 days. Backup plans with a frequency greater than 7 days continue to create full backups. Incremental backups don't require point-in-time recovery (PITR) to be turned on for the table. For continuous backups that you can restore to any second in the last 1 to 35 days, we recommend that you also turn on PITR. For more information, see [Point-in-time backups for DynamoDB](Point-in-time-recovery.md).

Incremental backups require AWS Backup advanced features for DynamoDB. If you start using AWS Backup with DynamoDB for the first time, incremental backups are turned on by default. If you turn on advanced features, incremental backups are turned on at the same time. If you already use advanced features, turn on incremental backups to start using them.

After you turn on incremental backups, your existing backups remain full backups until they expire. The next backup of each table is a full backup, and later backups are incremental. You can turn off incremental backups at any time. After you turn them off, new backups are full backups. For instructions on turning incremental backups on or off, see [Creating backups of DynamoDB tables with AWS Backup](CreateBackupAWS.md).

Every backup is independently restorable. You can restore the complete table from any incremental backup, even after earlier backups of the table have expired or been deleted.

**Note**
Unlike DynamoDB Backups, backups made with AWS Backup are not instantaneous.

While a backup is in progress, you can't do the following:
+ Pause or cancel the backup operation.
+ Delete the source table of the backup.
+ Disable backups on a table if a backup for that table is in progress.

AWS Backup provides automated backup schedules, retention management, and lifecycle management. This removes the need for custom scripts and manual processes. AWS Backup runs the backups and deletes them when they expire. For more information, see the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html).

If you're using the console, any backups created using AWS Backup are listed on the **Backups** tab with the **Backup type** set to `AWS_BACKUP`.

**Note**
You can't delete backups marked with a **Backup type** of `AWS_BACKUP` using the DynamoDB console. To manage these backups, use the AWS Backup console.

To learn how to perform a backup, see [Backing up a DynamoDB table](Backup.Tutorial.md).

## Restores
<a name="GettingStartedBackupsAWS-restore"></a>

You restore a table without consuming any provisioned throughput on the table. Every restore creates a new table with the complete table data as of the backup time, whether the backup is full or incremental. If you restore an incremental backup to a different Region, you must specify an AWS Key Management Service (AWS KMS) key for the new table. You can configure the destination table settings. When you do a restore, you can change the following table settings:
+ Encryption settings

**Important**
When you do a full table restore, the destination table is set with the same provisioned read capacity units and write capacity units that the source table had when the backup was requested. The restore process also restores the local secondary indexes and the global secondary indexes.

You can copy a backup of your DynamoDB table data to a different AWS Region and then restore it in that new Region. You can copy and then restore backups between AWS commercial Regions, AWS China Regions, and AWS GovCloud (US) Regions. You pay only for the data you copy from the source Region and the data you restore to a new table in the destination Region.

AWS Backup will restore the tables with all the original indexes.

You must manually set up the following on the restored table:
+ Auto scaling policies
+ AWS Identity and Access Management (IAM) policies
+ Amazon CloudWatch metrics and alarms
+ Tags
+ Stream settings
+ Time to Live (TTL) settings
+ Deletion protection settings
+ Point in time recovery (PITR) settings

You can only restore the entire table data to a new table from a backup. You can write to the restored table only after it becomes active.

**Note**
AWS Backup restores are nondestructive. You can't overwrite an existing table during a restore operation.

Restore times are directly related to the configuration of your tables (such as the size of your tables and the number of underlying partitions) and other related variables. A best practice when planning for disaster recovery is to regularly document average restore completion times and establish how these times affect your overall Recovery Time Objective.

To learn how to perform a restore, see [Restoring a DynamoDB table from a backup](Restore.Tutorial.md).

You can use IAM policies for access control. For more information, see [Using IAM with DynamoDB backup and restore](backuprestore_IAM.md).

All backup and restore console and API actions are captured and recorded in AWS CloudTrail for logging, continuous monitoring, and auditing.
