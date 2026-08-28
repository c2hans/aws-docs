---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/encrypt-an-existing-amazon-rds-for-postgresql-db-instance.html
---

# Encrypt an existing Amazon RDS for PostgreSQL DB instance
<a name="encrypt-an-existing-amazon-rds-for-postgresql-db-instance"></a>

*Piyush Goyal, Shobana Raghu, and Yaser Raja, Amazon Web Services*

## Summary
<a name="encrypt-an-existing-amazon-rds-for-postgresql-db-instance-summary"></a>

This pattern explains how to encrypt an existing Amazon Relational Database Service (Amazon RDS) for PostgreSQL DB instance in the AWS Cloud with minimal downtime. This process works for Amazon RDS for MySQL DB instances as well.

You can enable encryption for an Amazon RDS DB instance when you create it, but not after it's created. However, you can add encryption to an unencrypted DB instance by creating a snapshot of your DB instance, and then creating an encrypted copy of that snapshot. You can then restore a DB instance from the encrypted snapshot to get an encrypted copy of your original DB instance. If your project allows for downtime (at least for write transactions) during this activity, this is all you need to do. When the new, encrypted copy of the DB instance becomes available, you can point your applications to the new database. However, if your project doesn’t allow for significant downtime for this activity, you need an alternate approach that helps minimize the downtime. This pattern uses the AWS Database Migration Service (AWS DMS) to migrate and continuously replicate the data so that the cutover to the new, encrypted database can be done with minimal downtime.

Amazon RDS encrypted DB instances use the industry standard AES-256 encryption algorithm to encrypt your data on the server that hosts your Amazon RDS DB instances. After your data is encrypted, Amazon RDS handles authentication of access and decryption of your data transparently, with minimal impact on performance. You don't need to modify your database client applications to use encryption.

## Prerequisites and limitations
<a name="encrypt-an-existing-amazon-rds-for-postgresql-db-instance-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An unencrypted Amazon RDS for PostgreSQL DB instance
+ Experience working with (creating, modifying, or stopping) AWS DMS tasks (see [Working with AWS DMS tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the AWS DMS documentation)
+ Familiarity with AWS Key Management Service (AWS KMS) for encrypting databases (see the [AWS KMS documentation](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html))

**Limitations**
+ You can enable encryption for an Amazon RDS DB instance only when you create it, not after the DB instance is created.
+ Data in [unlogged tables](https://www.postgresql.org/docs/current/sql-createtable.html) will not be restored using snapshots. For more information, review [Best practices for working with PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html#CHAP_BestPractices.PostgreSQL).
+ You can't have an encrypted read replica of an unencrypted DB instance or an unencrypted read replica of an encrypted DB instance.
+ You can't restore an unencrypted backup or snapshot to an encrypted DB instance.
+ AWS DMS does not automatically transfers the Sequences therefore additional steps are required to handle this.

For more information, see [Limitations of Amazon RDS encrypted DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html#Overview.Encryption.Limitations) in the Amazon RDS documentation.

## Architecture
<a name="encrypt-an-existing-amazon-rds-for-postgresql-db-instance-architecture"></a>

**Source architecture**
+ Unencrypted RDS DB instance

**Target architecture **
+ Encrypted RDS DB instance
  + The destination RDS DB instance is created by restoring the DB snapshot copy of the source RDS DB instance.
  + An AWS KMS key is used for encryption while restoring the snapshot.
  + An AWS DMS replication task is used to migrate the data.

![Process uses AWS DMS to encrypt an existing Amazon RDS for PostgreSQL DB instance to a new DB.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/820d17c0-0eed-4ed9-9f43-cbada081d924/images/44dd8420-d89d-466e-b7fb-1bdafab8f7f9.png)

## Tools
<a name="encrypt-an-existing-amazon-rds-for-postgresql-db-instance-tools"></a>

**Tools used to enable encryption:**
+ AWS KMS key for encryption – When you create an encrypted DB instance, you can choose a customer managed key or the AWS managed key for Amazon RDS to encrypt your DB instance. If you don't specify the key identifier for a customer managed key, Amazon RDS uses the AWS managed key for your new DB instance. Amazon RDS creates an AWS managed key for Amazon RDS for your AWS account. Your AWS account has a different AWS managed key for Amazon RDS for each AWS Region. For more information about using KMS keys for Amazon RDS encryption, see [Encrypting Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html).

**Tools used for ongoing replication**:
+ AWS DMS – You can use AWS Database Migration Service (AWS DMS) to replicate changes from the source DB to the target DB. It is important to keep the source and target DB in sync to keep downtime to a minimum. For information about setting up AWS DMS and creating tasks, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

## Epics
<a name="encrypt-an-existing-amazon-rds-for-postgresql-db-instance-epics"></a>

### Create a snapshot of the source DB instance and encrypt it
<a name="create-a-snapshot-of-the-source-db-instance-and-encrypt-it"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check the details for the source PostgreSQL DB instance. | On the Amazon RDS console, choose the source PostgreSQL DB instance. On the **Configuration **tab, make sure that encryption isn't enabled for the instance. For a screen illustration, see the [Additional information](#encrypt-an-existing-amazon-rds-for-postgresql-db-instance-additional) section. | DBA |
| Create the DB snapshot. | Create a DB snapshot of the instance you want to encrypt. The amount of time it takes to create a snapshot depends on the size of your database. For instructions, see [Creating a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html) in the Amazon RDS documentation. | DBA |
| Encrypt the snapshot. | In the Amazon RDS console navigation pane, choose **Snapshots**, and select the DB snapshot you created. For **Actions**, choose **Copy Snapshot**. Provide the destination AWS Region and the name of the DB snapshot copy in the corresponding fields. Select the **Enable Encryption** checkbox. For **Master Key**, specify the KMS key identifier to use to encrypt the DB snapshot copy. Choose **Copy Snapshot**. For more information, see [Copying a snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html) in the Amazon RDS documentation. | DBA |

### Prepare the target DB instance
<a name="prepare-the-target-db-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Restore the DB snapshot. | On the Amazon RDS console, choose **Snapshots**. Choose the encrypted snapshot that you created. For **Actions**, choose **Restore Snapshot**. For **DB Instance Identifier**, provide a unique name for the new DB instance. Review the instance details, and then choose **Restore DB Instance**. A new, encrypted DB Instance will be created from your snapshot. For more information, see [Restoring from a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html) in the Amazon RDS documentation. | DBA |
| Migrate data by using AWS DMS. | On the AWS DMS console, create an AWS DMS task. For **Migration type**, choose **Migrate existing data and replicate ongoing changes**. In **Task Settings**, for **Target table preparation mode**, choose **Truncate**. For more information, see [Creating a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html) in the AWS DMS documentation. | DBA |
| Enable data validation. | In **Task Settings**, choose **Enable validation**. This enables you to compare the source data to the target data to verify that the data was migrated accurately.  | DBA |
| Disable constraints on the target DB instance. | [Disable any triggers and foreign key constraints](https://www.postgresql.org/docs/current/sql-altertable.html) on the target DB instance, and then start the AWS DMS task. For more information about disabling triggers and foreign key constraints, see the [AWS DMS documentation.](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html) | DBA |
| Verify data.  | After the full load is complete, verify the data on the target DB instance to see if it matches the source data. For more information, see [AWS DMS data validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html) in the AWS DMS documentation. | DBA |

### Cut over to the target DB instance
<a name="cut-over-to-the-target-db-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop write operations on the source DB instance. | Stop the write operations on the source DB instance so that application downtime can begin. Verify that AWS DMS has completed the replication for the data in the pipeline. Enable triggers and foreign keys on the target DB instance. | DBA |
| Update database sequences | If the source database contains any sequence numbers, verify and update the sequences in the target database. | DBA |
| Configure the application endpoint. | Configure your application connections to use the new Amazon RDS DB instance endpoints. The DB instance is now encrypted. | DBA, Application owner |

## Related resources
<a name="encrypt-an-existing-amazon-rds-for-postgresql-db-instance-resources"></a>
+ [Creating an AWS DMS task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html)
+ [Monitoring replication tasks using Amazon CloudWatch](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html#CHAP_Monitoring.CloudWatch)
+ [Monitoring AWS DMS tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html)
+ [Updating the Amazon RDS encryption key](https://aws.amazon.com/premiumsupport/knowledge-center/update-encryption-key-rds/)

## Additional information
<a name="encrypt-an-existing-amazon-rds-for-postgresql-db-instance-additional"></a>

Checking the encryption for the source PostgreSQL DB instance:

![The Summary page of source PostgreSQL DB instance shows encryption not enabled for storage.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/820d17c0-0eed-4ed9-9f43-cbada081d924/images/d53d1dab-b5c2-452d-b823-ba3d6508ad15.png)

Additional notes for this pattern:
+ Enable replication on PostgreSQL by setting the `rds.logical_replication` parameter to 1.

**Important note:** Replication slots retain the write ahead log (WAL) files until the files are externally consumed—for example, by `pg_recvlogical`; by extract, transform, and load (ETL) jobs; or by AWS DMS. When you set the `rds.logical_replication` parameter value to 1, AWS DMS sets the `wal_level`, `max_wal_senders`, `max_replication_slots`, and `max_connections` parameters. If logical replication slots are present but there is no consumer for the WAL files retained by the replication slot, you might see an increase in the transaction log disk usage and a constant decrease in free storage space. For more information and steps to resolve this issue, see the article [How can I identify what is causing the "No space left on device" or "DiskFull" error on Amazon RDS for PostgreSQL?](https://aws.amazon.com/premiumsupport/knowledge-center/diskfull-error-rds-postgresql/) in the AWS Support Knowledge Center.
+ Any schema changes that you make to the source DB instance after you create the DB snapshot will not be present on the target DB instance.
+ After you create an encrypted DB instance, you can't change the KMS key used by that DB instance. Be sure to determine your KMS key requirements before you create your encrypted DB instance.
+ You must disable triggers and foreign keys on the target DB instance before you run the AWS DMS task. You can re-enable these when the task is complete.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
