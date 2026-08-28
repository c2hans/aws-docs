---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbInstanceDetails.html
---

# AwsRdsDbInstanceDetails
<a name="API_AwsRdsDbInstanceDetails"></a>

Contains the details of an Amazon RDS DB instance.

## Contents
<a name="API_AwsRdsDbInstanceDetails_Contents"></a>

 ** AllocatedStorage **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-AllocatedStorage"></a>
The amount of storage (in gigabytes) to initially allocate for the DB instance.
Type: Integer
Required: No

 ** AssociatedRoles **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-AssociatedRoles"></a>
The IAM roles associated with the DB instance.
Type: Array of [AwsRdsDbInstanceAssociatedRole](API_AwsRdsDbInstanceAssociatedRole.md) objects
Required: No

 ** AutoMinorVersionUpgrade **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-AutoMinorVersionUpgrade"></a>
Indicates whether minor version patches are applied automatically.
Type: Boolean
Required: No

 ** AvailabilityZone **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-AvailabilityZone"></a>
The Availability Zone where the DB instance will be created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BackupRetentionPeriod **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-BackupRetentionPeriod"></a>
The number of days for which to retain automated backups.
Type: Integer
Required: No

 ** CACertificateIdentifier **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-CACertificateIdentifier"></a>
The identifier of the CA certificate for this DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CharacterSetName **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-CharacterSetName"></a>
The name of the character set that this DB instance is associated with.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CopyTagsToSnapshot **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-CopyTagsToSnapshot"></a>
Whether to copy resource tags to snapshots of the DB instance.
Type: Boolean
Required: No

 ** DBClusterIdentifier **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DBClusterIdentifier"></a>
If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DBInstanceClass **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DBInstanceClass"></a>
Contains the name of the compute and memory capacity class of the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DBInstanceIdentifier **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DBInstanceIdentifier"></a>
Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbInstancePort **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DbInstancePort"></a>
Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.
Type: Integer
Required: No

 ** DbInstanceStatus **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DbInstanceStatus"></a>
The current status of the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbiResourceId **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DbiResourceId"></a>
The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DBName **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DBName"></a>
The meaning of this parameter differs according to the database engine you use.
 **MySQL, MariaDB, SQL Server, PostgreSQL**
Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.
 **Oracle**
Contains the Oracle System ID (SID) of the created DB instance. Not shown when the returned parameters don't apply to an Oracle DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbParameterGroups **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DbParameterGroups"></a>
A list of the DB parameter groups to assign to the DB instance.
Type: Array of [AwsRdsDbParameterGroup](API_AwsRdsDbParameterGroup.md) objects
Required: No

 ** DbSecurityGroups **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DbSecurityGroups"></a>
A list of the DB security groups to assign to the DB instance.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** DbSubnetGroup **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DbSubnetGroup"></a>
Information about the subnet group that is associated with the DB instance.
Type: [AwsRdsDbSubnetGroup](API_AwsRdsDbSubnetGroup.md) object
Required: No

 ** DeletionProtection **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DeletionProtection"></a>
Indicates whether the DB instance has deletion protection enabled.
When deletion protection is enabled, the database cannot be deleted.
Type: Boolean
Required: No

 ** DomainMemberships **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-DomainMemberships"></a>
The Active Directory domain membership records associated with the DB instance.
Type: Array of [AwsRdsDbDomainMembership](API_AwsRdsDbDomainMembership.md) objects
Required: No

 ** EnabledCloudWatchLogsExports **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-EnabledCloudWatchLogsExports"></a>
A list of log types that this DB instance is configured to export to CloudWatch Logs.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Endpoint **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-Endpoint"></a>
Specifies the connection endpoint.
Type: [AwsRdsDbInstanceEndpoint](API_AwsRdsDbInstanceEndpoint.md) object
Required: No

 ** Engine **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-Engine"></a>
Provides the name of the database engine to use for this DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EngineVersion **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-EngineVersion"></a>
Indicates the database engine version.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EnhancedMonitoringResourceArn **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-EnhancedMonitoringResourceArn"></a>
The ARN of the CloudWatch Logs log stream that receives the enhanced monitoring metrics data for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IAMDatabaseAuthenticationEnabled **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-IAMDatabaseAuthenticationEnabled"></a>
True if mapping of IAM accounts to database accounts is enabled, and otherwise false.
IAM database authentication can be enabled for the following database engines.
+ For MySQL 5.6, minor version 5.6.34 or higher
+ For MySQL 5.7, minor version 5.7.16 or higher
+ Aurora 5.6 or higher
Type: Boolean
Required: No

 ** InstanceCreateTime **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-InstanceCreateTime"></a>
Indicates when the DB instance was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Iops **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-Iops"></a>
Specifies the provisioned IOPS (I/O operations per second) for this DB instance.
Type: Integer
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-KmsKeyId"></a>
If `StorageEncrypted` is true, the AWS KMS key identifier for the encrypted DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LatestRestorableTime **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-LatestRestorableTime"></a>
Specifies the latest time to which a database can be restored with point-in-time restore.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** LicenseModel **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-LicenseModel"></a>
License model information for this DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ListenerEndpoint **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-ListenerEndpoint"></a>
Specifies the connection endpoint.
Type: [AwsRdsDbInstanceEndpoint](API_AwsRdsDbInstanceEndpoint.md) object
Required: No

 ** MasterUsername **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-MasterUsername"></a>
The master user name of the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MaxAllocatedStorage **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-MaxAllocatedStorage"></a>
The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.
Type: Integer
Required: No

 ** MonitoringInterval **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-MonitoringInterval"></a>
The interval, in seconds, between points when enhanced monitoring metrics are collected for the DB instance.
Type: Integer
Required: No

 ** MonitoringRoleArn **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-MonitoringRoleArn"></a>
The ARN for the IAM role that permits Amazon RDS to send enhanced monitoring metrics to CloudWatch Logs.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MultiAz **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-MultiAz"></a>
Whether the DB instance is a multiple Availability Zone deployment.
Type: Boolean
Required: No

 ** OptionGroupMemberships **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-OptionGroupMemberships"></a>
The list of option group memberships for this DB instance.
Type: Array of [AwsRdsDbOptionGroupMembership](API_AwsRdsDbOptionGroupMembership.md) objects
Required: No

 ** PendingModifiedValues **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-PendingModifiedValues"></a>
Changes to the DB instance that are currently pending.
Type: [AwsRdsDbPendingModifiedValues](API_AwsRdsDbPendingModifiedValues.md) object
Required: No

 ** PerformanceInsightsEnabled **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-PerformanceInsightsEnabled"></a>
Indicates whether Performance Insights is enabled for the DB instance.
Type: Boolean
Required: No

 ** PerformanceInsightsKmsKeyId **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-PerformanceInsightsKmsKeyId"></a>
The identifier of the AWS KMS key used to encrypt the Performance Insights data.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PerformanceInsightsRetentionPeriod **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-PerformanceInsightsRetentionPeriod"></a>
The number of days to retain Performance Insights data.
Type: Integer
Required: No

 ** PreferredBackupWindow **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-PreferredBackupWindow"></a>
The range of time each day when automated backups are created, if automated backups are enabled.
Uses the format `HH:MM-HH:MM`. For example, `04:52-05:22`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PreferredMaintenanceWindow **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-PreferredMaintenanceWindow"></a>
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
Uses the format `<day>:HH:MM-<day>:HH:MM`.
For the day values, use `mon`\|`tue`\|`wed`\|`thu`\|`fri`\|`sat`\|`sun`.
For example, `sun:09:32-sun:10:02`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProcessorFeatures **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-ProcessorFeatures"></a>
The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
Type: Array of [AwsRdsDbProcessorFeature](API_AwsRdsDbProcessorFeature.md) objects
Required: No

 ** PromotionTier **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-PromotionTier"></a>
The order in which to promote an Aurora replica to the primary instance after a failure of the existing primary instance.
Type: Integer
Required: No

 ** PubliclyAccessible **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-PubliclyAccessible"></a>
Specifies the accessibility options for the DB instance.
A value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address.
A value of false specifies an internal instance with a DNS name that resolves to a private IP address.
Type: Boolean
Required: No

 ** ReadReplicaDBClusterIdentifiers **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-ReadReplicaDBClusterIdentifiers"></a>
List of identifiers of Aurora DB clusters to which the RDS DB instance is replicated as a read replica.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** ReadReplicaDBInstanceIdentifiers **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-ReadReplicaDBInstanceIdentifiers"></a>
List of identifiers of the read replicas associated with this DB instance.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** ReadReplicaSourceDBInstanceIdentifier **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-ReadReplicaSourceDBInstanceIdentifier"></a>
If this DB instance is a read replica, contains the identifier of the source DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecondaryAvailabilityZone **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-SecondaryAvailabilityZone"></a>
For a DB instance with multi-Availability Zone support, the name of the secondary Availability Zone.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StatusInfos **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-StatusInfos"></a>
The status of a read replica. If the instance isn't a read replica, this is empty.
Type: Array of [AwsRdsDbStatusInfo](API_AwsRdsDbStatusInfo.md) objects
Required: No

 ** StorageEncrypted **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-StorageEncrypted"></a>
Specifies whether the DB instance is encrypted.
Type: Boolean
Required: No

 ** StorageType **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-StorageType"></a>
The storage type for the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TdeCredentialArn **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-TdeCredentialArn"></a>
The ARN from the key store with which the instance is associated for TDE encryption.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Timezone **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-Timezone"></a>
The time zone of the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcSecurityGroups **   <a name="securityhub-Type-AwsRdsDbInstanceDetails-VpcSecurityGroups"></a>
A list of VPC security groups that the DB instance belongs to.
Type: Array of [AwsRdsDbInstanceVpcSecurityGroup](API_AwsRdsDbInstanceVpcSecurityGroup.md) objects
Required: No

## See Also
<a name="API_AwsRdsDbInstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbInstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbInstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbInstanceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
