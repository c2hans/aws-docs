---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-amazon-rds-for-oracle-database-to-another-aws-account-and-aws-region-using-aws-dms-for-ongoing-replication.html
---

# Migrate an Amazon RDS for Oracle database to another AWS account and AWS Region using AWS DMS for ongoing replication
<a name="migrate-an-amazon-rds-for-oracle-database-to-another-aws-account-and-aws-region-using-aws-dms-for-ongoing-replication"></a>

*Durga Prasad Cheepuri and Eduardo Valentim, Amazon Web Services*

## Summary
<a name="migrate-an-amazon-rds-for-oracle-database-to-another-aws-account-and-aws-region-using-aws-dms-for-ongoing-replication-summary"></a>

|
|
| Warning: IAM users have long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. |
| --- |

This pattern walks you through the steps for migrating an Amazon Relational Database Service (Amazon RDS) for Oracle source database to a different AWS account and AWS Region. The pattern uses a DB snapshot for a one-time full data load, and enables AWS Database Migration Service (AWS DMS) for ongoing replication.

## Prerequisites and limitations
<a name="migrate-an-amazon-rds-for-oracle-database-to-another-aws-account-and-aws-region-using-aws-dms-for-ongoing-replication-prereqs"></a>

**Prerequisites**
+ An active AWS account that contains the source Amazon RDS for Oracle database, which has been encrypted using a non-default AWS Key Management Service (AWS KMS) key
+ An active AWS account in a different AWS Region from the source database, to use for the target Amazon RDS for Oracle database
+ Virtual private cloud (VPC) peering between the source and target VPCs
+ Familiarity with [using an Oracle database as a source for AWS DMS](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
+ Familiarity with [using an Oracle database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html)

**Product versions**
+ Oracle versions 11g (versions 11.2.0.3.v1 and later) and up to 12.2, and 18c. For the latest list of supported versions and editions, see [Using an Oracle Database as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) and with [Using an Oracle database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html)  in the AWS documentation. For Oracle versions supported by Amazon RDS, see [Oracle on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html).

## Architecture
<a name="migrate-an-amazon-rds-for-oracle-database-to-another-aws-account-and-aws-region-using-aws-dms-for-ongoing-replication-architecture"></a>

**Source and target technology stacks**
+ Amazon RDS for Oracle DB instance

![Source AWS account connecting to target AWS account that contains source and target Regions](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5ecd5359-884e-455c-b5d0-ef08eda2ea1f/images/e17fa7fe-d924-4f35-9707-b93572fa1227.png)

**Ongoing replication architecture**

![DB on an EC2 instance connecting through VPC peering to a replication instance and Amazon RDS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5ecd5359-884e-455c-b5d0-ef08eda2ea1f/images/b60b3500-5d29-487a-bbab-0ae9f3f386aa.png)

## Tools
<a name="migrate-an-amazon-rds-for-oracle-database-to-another-aws-account-and-aws-region-using-aws-dms-for-ongoing-replication-tools"></a>

**Tools used for one-time full data load**
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) creates a storage volume snapshot of your DB instance, backing up the entire DB instance and not just individual databases. When you create a DB snapshot, you need to identify which DB instance you are going to back up, and then give your DB snapshot a name so you can restore from it later. The amount of time it takes to create a snapshot varies with the size of your databases. Because the snapshot includes the entire storage volume, the size of files, such as temporary files, also affects the amount of time it takes to create the snapshot. For more information about using DB snapshots, see [Creating a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html) in the Amazon RDS documentation.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) creates a** **key for** **Amazon RDS**  **encryption. When you create an encrypted DB instance, you can also supply the [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) key identifier for your encryption key. If you don't specify an [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) key identifier, Amazon RDS uses your default encryption key for your new DB instance. [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) creates your default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region. For this pattern, the Amazon RDS DB instance should be encrypted using the non-default [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) key. For more information about using [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) keys for Amazon RDS encryption, see [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) in the Amazon RDS documentation.

**Tools used for ongoing replication**
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) is used to replicate ongoing changes and to keep the source and target databases in sync. For more information about using AWS DMS for ongoing replication, see [Working with an AWS DMS replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) in the AWS DMS documentation.

## Epics
<a name="migrate-an-amazon-rds-for-oracle-database-to-another-aws-account-and-aws-region-using-aws-dms-for-ongoing-replication-epics"></a>

### Configure your source AWS account
<a name="configure-your-source-aws-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the source Oracle DB instance. | Let the Amazon RDS for Oracle DB instance run in ARCHIVELOG mode, and set the retention period. For details, see [Working with an AWS managed Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Amazon-Managed). | DBA |
| Set supplemental logging for the source Oracle DB instance. | Set database-level and table-level supplemental logging for the Amazon RDS for Oracle DB instance. For details, see [Working with an AWS managed Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Amazon-Managed). | DBA |
| Update the AWS KMS key policy in the source account. | Update the AWS KMS key policy in the source AWS account to allow the target AWS account to use the encrypted Amazon RDS AWS KMS key. For details, see the [AWS KMS documentation](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html#key-policy-modifying-external-accounts). | SysAdmin |
| Create a manual Amazon RDS DB snapshot of the source DB instance. |  | AWS IAM user |
| Share the manual, encrypted Amazon RDS snapshot with the target AWS account. | For details, see [Sharing a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html). | AWS IAM user |

### Configure your target AWS account
<a name="configure-your-target-aws-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Attach a policy. | In the target AWS account, attach an AWS Identity and Access Management (IAM) policy to the root IAM user, to allow the IAM user to copy an encrypted DB snapshot using the shared AWS KMS key. | SysAdmin |
| Switch to the source AWS Region. |  | AWS IAM user |
| Copy the shared snapshot. | In the Amazon RDS console, in the **Snapshots** pane, choose **Shared with Me**, and select the shared snapshot. Copy the snapshot to the same AWS Region as the source database by using the Amazon Resource Name (ARN) for the AWS KMS key used by the source database. For details, see [Copying a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html). | AWS IAM user |
| Switch to the target AWS Region, and create a new AWS KMS key. |  | AWS IAM user |
| Copy the snapshot. | Switch to the source AWS Region. On the Amazon RDS console, in the **Snapshots** pane, choose **Owned by Me**, and select the copied snapshot. Copy the snapshot to the target AWS Region by using the AWS KMS key for the new target AWS Region. | AWS IAM user |
| Restore the snapshot. | Switch to the target AWS Region. On the Amazon RDS console, in the **Snapshots** pane, choose **Owned by Me**. Select the copied snapshot and restore it to an Amazon RDS for Oracle DB instance. For details, see [Restoring from a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html). | AWS IAM user |

### Prepare your source database for ongoing replication
<a name="prepare-your-source-database-for-ongoing-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Oracle user with the appropriate permissions. | Create an Oracle user with the required privileges for Oracle as a source for AWS DMS. For details, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html). | DBA |
| Configure the source database for Oracle LogMiner or Oracle Binary Reader. |  | DBA |

### Prepare your target database for ongoing replication
<a name="prepare-your-target-database-for-ongoing-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Oracle user with the appropriate permissions. | Create an Oracle user with the required privileges for Oracle as a target for AWS DMS. For details, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.Privileges). | DBA |

### Create AWS DMS components
<a name="create-dms-components"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a replication instance in the target AWS Region. | Create a replication instance in the VPC of the target AWS Region. For details, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html#CHAP_GettingStarted.ReplicationInstance). | AWS IAM user |
| Create source and target endpoints with required encryption, and test connections. | For details, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html#CHAP_GettingStarted.Endpoints). | DBA |
| Create replication tasks. | 1. For the migration type, choose ongoing replication. <br />2. For the change data capture (CDC) start point, use the Oracle system change number (SCN) when the Amazon RDS snapshot was taken for full load, or the timestamp when the full load was taken. <br />3. For `TargetTablePrepMode`, choose **DO\_NOTHING**. If the task has large binary object (LOB) data tables, choose **Limited LOB mode**, and set the **max LOB size** to the maximum size of the LOB data in the table. <br />4. Enable logging. <br />5. Group tables that are related through keys into a single task. If there are tables with a large amount of LOB data and the table has no relationship with other tables, create a separate task for it with the LOB settings described previously. For details, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html#CHAP_GettingStarted.Tasks). | IAM user |
| Start the tasks and monitor them. | For details, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html). | AWS IAM user |
| Enable validation on the task if needed. | Note that enabling validation does have a performance impact on the replication. For details, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html). | AWS IAM user |

## Related resources
<a name="migrate-an-amazon-rds-for-oracle-database-to-another-aws-account-and-aws-region-using-aws-dms-for-ongoing-replication-resources"></a>
+ [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html#key-policy-modifying-external-accounts)
+ [Creating a manual Amazon RDS DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html)
+ [Sharing a manual Amazon RDS DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html)
+ [Copying a snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html)
+ [Restoring from an Amazon RDS DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html)
+ [Getting started with AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html)
+ [Using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html)
+ [Using an Oracle database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html)
+ [AWS DMS setup using VPC peering](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html#CHAP_ReplicationInstance.VPC.Configurations.ScenarioVPCPeer)
+ [How do I share manual Amazon RDS DB snapshots or DB cluster snapshots with another AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/rds-snapshots-share-account/) (AWS Knowledge Center article)
