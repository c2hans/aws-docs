---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBInstance.html
---

# DBInstance
<a name="API_DBInstance"></a>

Contains the details of an Amazon Neptune DB instance.

This data type is used as a response element in the [DescribeDBInstances](API_DescribeDBInstances.md) action.

## Contents
<a name="API_DBInstance_Contents"></a>

 ** AllocatedStorage **
Not supported by Neptune.
Type: Integer
Required: No

 ** AutoMinorVersionUpgrade **
Indicates that minor version patches are applied automatically.
Type: Boolean
Required: No

 ** AvailabilityZone **
Specifies the name of the Availability Zone the DB instance is located in.
Type: String
Required: No

 ** BackupRetentionPeriod **
Specifies the number of days for which automatic DB snapshots are retained.
Type: Integer
Required: No

 ** CACertificateIdentifier **
The identifier of the CA certificate for this DB instance.
Type: String
Required: No

 ** CharacterSetName **
 *(Not supported by Neptune)*
Type: String
Required: No

 ** CopyTagsToSnapshot **
Specifies whether tags are copied from the DB instance to snapshots of the DB instance.
Type: Boolean
Required: No

 ** DBClusterIdentifier **
If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
Type: String
Required: No

 ** DBInstanceArn **
The Amazon Resource Name (ARN) for the DB instance.
Type: String
Required: No

 ** DBInstanceClass **
Contains the name of the compute and memory capacity class of the DB instance.
Type: String
Required: No

 ** DBInstanceIdentifier **
Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.
Type: String
Required: No

 ** DbInstancePort **
Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.
Type: Integer
Required: No

 ** DBInstanceStatus **
Specifies the current state of this database.
Type: String
Required: No

 ** DbiResourceId **
The Amazon Region-unique, immutable identifier for the DB instance. This identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS key for the DB instance is accessed.
Type: String
Required: No

 ** DBName **
The database name.
Type: String
Required: No

 ** DBParameterGroups.DBParameterGroup.N **
Provides the list of DB parameter groups applied to this DB instance.
Type: Array of [DBParameterGroupStatus](API_DBParameterGroupStatus.md) objects
Required: No

 ** DBSecurityGroups.DBSecurityGroup.N **
 Provides List of DB security group elements containing only `DBSecurityGroup.Name` and `DBSecurityGroup.Status` subelements.
Type: Array of [DBSecurityGroupMembership](API_DBSecurityGroupMembership.md) objects
Required: No

 ** DBSubnetGroup **
Specifies information on the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.
Type: [DBSubnetGroup](API_DBSubnetGroup.md) object
Required: No

 ** DeletionProtection **
Indicates whether or not the DB instance has deletion protection enabled. The instance can't be deleted when deletion protection is enabled. See [Deleting a DB Instance](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html).
Type: Boolean
Required: No

 ** DomainMemberships.DomainMembership.N **
Not supported
Type: Array of [DomainMembership](API_DomainMembership.md) objects
Required: No

 ** EnabledCloudwatchLogsExports.member.N **
A list of log types that this DB instance is configured to export to CloudWatch Logs.
Type: Array of strings
Required: No

 ** Endpoint **
Specifies the connection endpoint.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** Engine **
Provides the name of the database engine to be used for this DB instance.
Type: String
Required: No

 ** EngineVersion **
Indicates the database engine version.
Type: String
Required: No

 ** EnhancedMonitoringResourceArn **
The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.
Type: String
Required: No

 ** IAMDatabaseAuthenticationEnabled **
True if Amazon Identity and Access Management (IAM) authentication is enabled, and otherwise false.
Type: Boolean
Required: No

 ** InstanceCreateTime **
Provides the date and time the DB instance was created.
Type: Timestamp
Required: No

 ** Iops **
Specifies the Provisioned IOPS (I/O operations per second) value.
Type: Integer
Required: No

 ** KmsKeyId **
 Not supported: The encryption for DB instances is managed by the DB cluster.
Type: String
Required: No

 ** LatestRestorableTime **
Specifies the latest time to which a database can be restored with point-in-time restore.
Type: Timestamp
Required: No

 ** LicenseModel **
License model information for this DB instance.
Type: String
Required: No

 ** MasterUsername **
Not supported by Neptune.
Type: String
Required: No

 ** MonitoringInterval **
The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.
Type: Integer
Required: No

 ** MonitoringRoleArn **
The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
Type: String
Required: No

 ** MultiAZ **
Specifies if the DB instance is a Multi-AZ deployment.
Type: Boolean
Required: No

 ** OptionGroupMemberships.OptionGroupMembership.N **
 *(Not supported by Neptune)*
Type: Array of [OptionGroupMembership](API_OptionGroupMembership.md) objects
Required: No

 ** PendingModifiedValues **
Specifies that changes to the DB instance are pending. This element is only included when changes are pending. Specific changes are identified by subelements.
Type: [PendingModifiedValues](API_PendingModifiedValues.md) object
Required: No

 ** PerformanceInsightsEnabled **
 *(Not supported by Neptune)*
Type: Boolean
Required: No

 ** PerformanceInsightsKMSKeyId **
 *(Not supported by Neptune)*
Type: String
Required: No

 ** PreferredBackupWindow **
 Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod`.
Type: String
Required: No

 ** PreferredMaintenanceWindow **
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
Type: String
Required: No

 ** PromotionTier **
A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance.
Type: Integer
Required: No

 ** PubliclyAccessible **
Indicates whether the DB instance is publicly accessible.
When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.
When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.
Type: Boolean
Required: No

 ** ReadReplicaDBClusterIdentifiers.ReadReplicaDBClusterIdentifier.N **
Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.
Type: Array of strings
Required: No

 ** ReadReplicaDBInstanceIdentifiers.ReadReplicaDBInstanceIdentifier.N **
Contains one or more identifiers of the Read Replicas associated with this DB instance.
Type: Array of strings
Required: No

 ** ReadReplicaSourceDBInstanceIdentifier **
Contains the identifier of the source DB instance if this DB instance is a Read Replica.
Type: String
Required: No

 ** SecondaryAvailabilityZone **
If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.
Type: String
Required: No

 ** StatusInfos.DBInstanceStatusInfo.N **
The status of a Read Replica. If the instance is not a Read Replica, this is blank.
Type: Array of [DBInstanceStatusInfo](API_DBInstanceStatusInfo.md) objects
Required: No

 ** StorageEncrypted **
Not supported: The encryption for DB instances is managed by the DB cluster.
Type: Boolean
Required: No

 ** StorageType **
Specifies the storage type associated with the DB instance.
Type: String
Required: No

 ** TdeCredentialArn **
The ARN from the key store with which the instance is associated for TDE encryption.
Type: String
Required: No

 ** Timezone **
Not supported.
Type: String
Required: No

 ** VpcSecurityGroups.VpcSecurityGroupMembership.N **
Provides a list of VPC security group elements that the DB instance belongs to.
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects
Required: No

## See Also
<a name="API_DBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
