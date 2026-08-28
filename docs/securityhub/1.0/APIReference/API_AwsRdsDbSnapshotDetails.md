---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbSnapshotDetails.html
---

# AwsRdsDbSnapshotDetails
<a name="API_AwsRdsDbSnapshotDetails"></a>

Provides details about an Amazon RDS DB cluster snapshot.

## Contents
<a name="API_AwsRdsDbSnapshotDetails_Contents"></a>

 ** AllocatedStorage **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-AllocatedStorage"></a>
The amount of storage (in gigabytes) to be initially allocated for the database instance.
Type: Integer
Required: No

 ** AvailabilityZone **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-AvailabilityZone"></a>
Specifies the name of the Availability Zone in which the DB instance was located at the time of the DB snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbInstanceIdentifier **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-DbInstanceIdentifier"></a>
A name for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbiResourceId **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-DbiResourceId"></a>
The identifier for the source DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbSnapshotIdentifier **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-DbSnapshotIdentifier"></a>
The name or ARN of the DB snapshot that is used to restore the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Encrypted **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-Encrypted"></a>
Whether the DB snapshot is encrypted.
Type: Boolean
Required: No

 ** Engine **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-Engine"></a>
The name of the database engine to use for this DB instance. Valid values are as follows:
+  `aurora`
+  `aurora-mysql`
+  `aurora-postgresql`
+  `c`
+  `mariadb`
+  `mysql`
+  `oracle-ee`
+  `oracle-se`
+  `oracle-se1`
+  `oracle-se2`
+  `sqlserver-ee`
+  `sqlserver-ex`
+  `sqlserver-se`
+  `sqlserver-web`
Type: String
Pattern: `.*\S.*`
Required: No

 ** EngineVersion **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-EngineVersion"></a>
The version of the database engine.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IamDatabaseAuthenticationEnabled **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-IamDatabaseAuthenticationEnabled"></a>
Whether mapping of IAM accounts to database accounts is enabled.
Type: Boolean
Required: No

 ** InstanceCreateTime **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-InstanceCreateTime"></a>
Specifies the time in Coordinated Universal Time (UTC) when the DB instance, from which the snapshot was taken, was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Iops **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-Iops"></a>
The provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
Type: Integer
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-KmsKeyId"></a>
If `Encrypted` is `true`, the AWS KMS key identifier for the encrypted DB snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LicenseModel **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-LicenseModel"></a>
License model information for the restored DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MasterUsername **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-MasterUsername"></a>
The master user name for the DB snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OptionGroupName **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-OptionGroupName"></a>
The option group name for the DB snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PercentProgress **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-PercentProgress"></a>
The percentage of the estimated data that has been transferred.
Type: Integer
Required: No

 ** Port **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-Port"></a>
The port that the database engine was listening on at the time of the snapshot.
Type: Integer
Required: No

 ** ProcessorFeatures **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-ProcessorFeatures"></a>
The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
Type: Array of [AwsRdsDbProcessorFeature](API_AwsRdsDbProcessorFeature.md) objects
Required: No

 ** SnapshotCreateTime **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-SnapshotCreateTime"></a>
When the snapshot was taken in Coordinated Universal Time (UTC).
Type: String
Pattern: `.*\S.*`
Required: No

 ** SnapshotType **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-SnapshotType"></a>
The type of the DB snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceDbSnapshotIdentifier **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-SourceDbSnapshotIdentifier"></a>
The DB snapshot ARN that the DB snapshot was copied from.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceRegion **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-SourceRegion"></a>
The AWS Region that the DB snapshot was created in or copied from.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-Status"></a>
The status of this DB snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StorageType **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-StorageType"></a>
The storage type associated with the DB snapshot. Valid values are as follows:
+  `gp2`
+  `io1`
+  `standard`
Type: String
Pattern: `.*\S.*`
Required: No

 ** TdeCredentialArn **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-TdeCredentialArn"></a>
The ARN from the key store with which to associate the instance for TDE encryption.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Timezone **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-Timezone"></a>
The time zone of the DB snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsRdsDbSnapshotDetails-VpcId"></a>
The VPC ID associated with the DB snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsDbSnapshotDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbSnapshotDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbSnapshotDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbSnapshotDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
