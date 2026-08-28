---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBSnapshot.html
---

# DBSnapshot
<a name="API_DBSnapshot"></a>

Contains the details of an Amazon RDS DB snapshot.

This data type is used as a response element in the `DescribeDBSnapshots` action.

## Contents
<a name="API_DBSnapshot_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AdditionalStorageVolumes.member.N **
The additional storage volumes associated with the DB snapshot. RDS supports additional storage volumes for RDS for Oracle and RDS for SQL Server.
Type: Array of [AdditionalStorageVolume](API_AdditionalStorageVolume.md) objects
Required: No

 ** AllocatedStorage **
Specifies the allocated storage size in gibibytes (GiB).
Type: Integer
Required: No

 ** AvailabilityZone **
Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
Type: String
Required: No

 ** BackupRetentionPeriod **
The number of days for which automatic DB snapshots are retained.
Type: Integer
Required: No

 ** DBInstanceIdentifier **
Specifies the DB instance identifier of the DB instance this DB snapshot was created from.
Type: String
Required: No

 ** DbiResourceId **
The identifier for the source DB instance, which can't be changed and which is unique to an AWS Region.
Type: String
Required: No

 ** DBSnapshotArn **
The Amazon Resource Name (ARN) for the DB snapshot.
Type: String
Required: No

 ** DBSnapshotIdentifier **
Specifies the identifier for the DB snapshot.
Type: String
Required: No

 ** DBSystemId **
The Oracle system identifier (SID), which is the name of the Oracle database instance that manages your database files. The Oracle SID is also the name of your CDB.
Type: String
Required: No

 ** DedicatedLogVolume **
Indicates whether the DB instance has a dedicated log volume (DLV) enabled.
Type: Boolean
Required: No

 ** Encrypted **
Indicates whether the DB snapshot is encrypted.
Type: Boolean
Required: No

 ** Engine **
Specifies the name of the database engine.
Type: String
Required: No

 ** EngineVersion **
Specifies the version of the database engine.
Type: String
Required: No

 ** IAMDatabaseAuthenticationEnabled **
Indicates whether mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.
Type: Boolean
Required: No

 ** InstanceCreateTime **
Specifies the time in Coordinated Universal Time (UTC) when the DB instance, from which the snapshot was taken, was created.
Type: Timestamp
Required: No

 ** Iops **
Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
Type: Integer
Required: No

 ** KmsKeyId **
If `Encrypted` is true, the AWS KMS key identifier for the encrypted DB snapshot.
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.
Type: String
Required: No

 ** LicenseModel **
License model information for the restored DB instance.
Type: String
Required: No

 ** MasterUsername **
Provides the master username for the DB snapshot.
Type: String
Required: No

 ** MultiTenant **
Indicates whether the snapshot is of a DB instance using the multi-tenant configuration (TRUE) or the single-tenant configuration (FALSE).
Type: Boolean
Required: No

 ** OptionGroupName **
Provides the option group name for the DB snapshot.
Type: String
Required: No

 ** OriginalSnapshotCreateTime **
Specifies the time of the CreateDBSnapshot operation in Coordinated Universal Time (UTC). Doesn't change when the snapshot is copied.
Type: Timestamp
Required: No

 ** PercentProgress **
The percentage of the estimated data that has been transferred.
Type: Integer
Required: No

 ** Port **
Specifies the port that the database engine was listening on at the time of the snapshot.
Type: Integer
Required: No

 ** PreferredBackupWindow **
The daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod`.
Type: String
Required: No

 ** ProcessorFeatures.ProcessorFeature.N **
The number of CPU cores and the number of threads per core for the DB instance class of the DB instance when the DB snapshot was created.
Type: Array of [ProcessorFeature](API_ProcessorFeature.md) objects
Required: No

 ** SnapshotAvailabilityZone **
Specifies the name of the Availability Zone where RDS stores the DB snapshot. This value is valid only for snapshots that RDS stores on a Dedicated Local Zone.
Type: String
Required: No

 ** SnapshotCreateTime **
Specifies when the snapshot was taken in Coordinated Universal Time (UTC). Changes for the copy when the snapshot is copied.
Type: Timestamp
Required: No

 ** SnapshotDatabaseTime **
The timestamp of the most recent transaction applied to the database that you're backing up. Thus, if you restore a snapshot, SnapshotDatabaseTime is the most recent transaction in the restored DB instance. In contrast, originalSnapshotCreateTime specifies the system time that the snapshot completed.
If you back up a read replica, you can determine the replica lag by comparing SnapshotDatabaseTime with originalSnapshotCreateTime. For example, if originalSnapshotCreateTime is two hours later than SnapshotDatabaseTime, then the replica lag is two hours.
Type: Timestamp
Required: No

 ** SnapshotTarget **
Specifies where manual snapshots are stored: Dedicated Local Zones, AWS Outposts or the AWS Region.
Type: String
Required: No

 ** SnapshotType **
Provides the type of the DB snapshot.
Type: String
Required: No

 ** SourceDBSnapshotIdentifier **
The DB snapshot Amazon Resource Name (ARN) that the DB snapshot was copied from. It only has a value in the case of a cross-account or cross-Region copy.
Type: String
Required: No

 ** SourceRegion **
The AWS Region that the DB snapshot was created in or copied from.
Type: String
Required: No

 ** Status **
Specifies the status of this DB snapshot.
Type: String
Required: No

 ** StorageEncryptionType **
The type of encryption used to protect data at rest in the DB snapshot. Possible values:
+  `none` - The DB snapshot is not encrypted.
+  `sse-rds` - The DB snapshot is encrypted using an AWS owned KMS key.
+  `sse-kms` - The DB snapshot is encrypted using a customer managed KMS key or AWS managed KMS key.
Type: String
Valid Values: `none | sse-kms | sse-rds`
Required: No

 ** StorageThroughput **
Specifies the storage throughput for the DB snapshot.
Type: Integer
Required: No

 ** StorageType **
Specifies the storage type associated with DB snapshot.
Type: String
Required: No

 ** TagList.Tag.N **
A list of tags.
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TdeCredentialArn **
The ARN from the key store with which to associate the instance for TDE encryption.
Type: String
Required: No

 ** Timezone **
The time zone of the DB snapshot. In most cases, the `Timezone` element is empty. `Timezone` content appears only for snapshots taken from Microsoft SQL Server DB instances that were created with a time zone specified.
Type: String
Required: No

 ** VpcId **
Provides the VPC ID associated with the DB snapshot.
Type: String
Required: No

## See Also
<a name="API_DBSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
