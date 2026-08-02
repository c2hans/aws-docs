---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbClusterDetails.html
---

# AwsRdsDbClusterDetails
<a name="API_AwsRdsDbClusterDetails"></a>

Information about an Amazon RDS DB cluster.

## Contents
<a name="API_AwsRdsDbClusterDetails_Contents"></a>

 ** ActivityStreamStatus **   <a name="securityhub-Type-AwsRdsDbClusterDetails-ActivityStreamStatus"></a>
The status of the database activity stream. Valid values are as follows:
+  `started`
+  `starting`
+  `stopped`
+  `stopping`
Type: String
Pattern: `.*\S.*`
Required: No

 ** AllocatedStorage **   <a name="securityhub-Type-AwsRdsDbClusterDetails-AllocatedStorage"></a>
For all database engines except Aurora, specifies the allocated storage size in gibibytes (GiB).
Type: Integer
Required: No

 ** AssociatedRoles **   <a name="securityhub-Type-AwsRdsDbClusterDetails-AssociatedRoles"></a>
A list of the IAM roles that are associated with the DB cluster.
Type: Array of [AwsRdsDbClusterAssociatedRole](API_AwsRdsDbClusterAssociatedRole.md) objects
Required: No

 ** AutoMinorVersionUpgrade **   <a name="securityhub-Type-AwsRdsDbClusterDetails-AutoMinorVersionUpgrade"></a>
 Indicates if minor version upgrades are automatically applied to the cluster.
Type: Boolean
Required: No

 ** AvailabilityZones **   <a name="securityhub-Type-AwsRdsDbClusterDetails-AvailabilityZones"></a>
A list of Availability Zones (AZs) where instances in the DB cluster can be created.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** BackupRetentionPeriod **   <a name="securityhub-Type-AwsRdsDbClusterDetails-BackupRetentionPeriod"></a>
The number of days for which automated backups are retained.
Type: Integer
Required: No

 ** ClusterCreateTime **   <a name="securityhub-Type-AwsRdsDbClusterDetails-ClusterCreateTime"></a>
Indicates when the DB cluster was created, in Universal Coordinated Time (UTC).
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** CopyTagsToSnapshot **   <a name="securityhub-Type-AwsRdsDbClusterDetails-CopyTagsToSnapshot"></a>
Whether tags are copied from the DB cluster to snapshots of the DB cluster.
Type: Boolean
Required: No

 ** CrossAccountClone **   <a name="securityhub-Type-AwsRdsDbClusterDetails-CrossAccountClone"></a>
Whether the DB cluster is a clone of a DB cluster owned by a different AWS account.
Type: Boolean
Required: No

 ** CustomEndpoints **   <a name="securityhub-Type-AwsRdsDbClusterDetails-CustomEndpoints"></a>
A list of custom endpoints for the DB cluster.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** DatabaseName **   <a name="securityhub-Type-AwsRdsDbClusterDetails-DatabaseName"></a>
The name of the database.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbClusterIdentifier **   <a name="securityhub-Type-AwsRdsDbClusterDetails-DbClusterIdentifier"></a>
The DB cluster identifier that the user assigned to the cluster. This identifier is the unique key that identifies a DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbClusterMembers **   <a name="securityhub-Type-AwsRdsDbClusterDetails-DbClusterMembers"></a>
The list of instances that make up the DB cluster.
Type: Array of [AwsRdsDbClusterMember](API_AwsRdsDbClusterMember.md) objects
Required: No

 ** DbClusterOptionGroupMemberships **   <a name="securityhub-Type-AwsRdsDbClusterDetails-DbClusterOptionGroupMemberships"></a>
The list of option group memberships for this DB cluster.
Type: Array of [AwsRdsDbClusterOptionGroupMembership](API_AwsRdsDbClusterOptionGroupMembership.md) objects
Required: No

 ** DbClusterParameterGroup **   <a name="securityhub-Type-AwsRdsDbClusterDetails-DbClusterParameterGroup"></a>
The name of the DB cluster parameter group for the DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbClusterResourceId **   <a name="securityhub-Type-AwsRdsDbClusterDetails-DbClusterResourceId"></a>
The identifier of the DB cluster. The identifier must be unique within each AWS Region and is immutable.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DbSubnetGroup **   <a name="securityhub-Type-AwsRdsDbClusterDetails-DbSubnetGroup"></a>
The subnet group that is associated with the DB cluster, including the name, description, and subnets in the subnet group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeletionProtection **   <a name="securityhub-Type-AwsRdsDbClusterDetails-DeletionProtection"></a>
Whether the DB cluster has deletion protection enabled.
Type: Boolean
Required: No

 ** DomainMemberships **   <a name="securityhub-Type-AwsRdsDbClusterDetails-DomainMemberships"></a>
The Active Directory domain membership records that are associated with the DB cluster.
Type: Array of [AwsRdsDbDomainMembership](API_AwsRdsDbDomainMembership.md) objects
Required: No

 ** EnabledCloudWatchLogsExports **   <a name="securityhub-Type-AwsRdsDbClusterDetails-EnabledCloudWatchLogsExports"></a>
A list of log types that this DB cluster is configured to export to CloudWatch Logs.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Endpoint **   <a name="securityhub-Type-AwsRdsDbClusterDetails-Endpoint"></a>
The connection endpoint for the primary instance of the DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Engine **   <a name="securityhub-Type-AwsRdsDbClusterDetails-Engine"></a>
The name of the database engine to use for this DB cluster. Valid values are as follows:
+  `aurora`
+  `aurora-mysql`
+  `aurora-postgresql`
Type: String
Pattern: `.*\S.*`
Required: No

 ** EngineMode **   <a name="securityhub-Type-AwsRdsDbClusterDetails-EngineMode"></a>
The database engine mode of the DB cluster.Valid values are as follows:
+  `global`
+  `multimaster`
+  `parallelquery`
+  `provisioned`
+  `serverless`
Type: String
Pattern: `.*\S.*`
Required: No

 ** EngineVersion **   <a name="securityhub-Type-AwsRdsDbClusterDetails-EngineVersion"></a>
The version number of the database engine to use.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HostedZoneId **   <a name="securityhub-Type-AwsRdsDbClusterDetails-HostedZoneId"></a>
Specifies the identifier that Amazon Route 53 assigns when you create a hosted zone.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HttpEndpointEnabled **   <a name="securityhub-Type-AwsRdsDbClusterDetails-HttpEndpointEnabled"></a>
Whether the HTTP endpoint for an Aurora Serverless DB cluster is enabled.
Type: Boolean
Required: No

 ** IamDatabaseAuthenticationEnabled **   <a name="securityhub-Type-AwsRdsDbClusterDetails-IamDatabaseAuthenticationEnabled"></a>
Whether the mapping of IAM accounts to database accounts is enabled.
Type: Boolean
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsRdsDbClusterDetails-KmsKeyId"></a>
The ARN of the AWS KMS master key that is used to encrypt the database instances in the DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MasterUsername **   <a name="securityhub-Type-AwsRdsDbClusterDetails-MasterUsername"></a>
The name of the master user for the DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MultiAz **   <a name="securityhub-Type-AwsRdsDbClusterDetails-MultiAz"></a>
Whether the DB cluster has instances in multiple Availability Zones.
Type: Boolean
Required: No

 ** Port **   <a name="securityhub-Type-AwsRdsDbClusterDetails-Port"></a>
The port number on which the DB instances in the DB cluster accept connections.
Type: Integer
Required: No

 ** PreferredBackupWindow **   <a name="securityhub-Type-AwsRdsDbClusterDetails-PreferredBackupWindow"></a>
The range of time each day when automated backups are created, if automated backups are enabled.
Uses the format `HH:MM-HH:MM`. For example, `04:52-05:22`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PreferredMaintenanceWindow **   <a name="securityhub-Type-AwsRdsDbClusterDetails-PreferredMaintenanceWindow"></a>
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
Uses the format `<day>:HH:MM-<day>:HH:MM`.
For the day values, use `mon`\|`tue`\|`wed`\|`thu`\|`fri`\|`sat`\|`sun`.
For example, `sun:09:32-sun:10:02`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReaderEndpoint **   <a name="securityhub-Type-AwsRdsDbClusterDetails-ReaderEndpoint"></a>
The reader endpoint for the DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReadReplicaIdentifiers **   <a name="securityhub-Type-AwsRdsDbClusterDetails-ReadReplicaIdentifiers"></a>
The identifiers of the read replicas that are associated with this DB cluster.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsRdsDbClusterDetails-Status"></a>
The current status of this DB cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StorageEncrypted **   <a name="securityhub-Type-AwsRdsDbClusterDetails-StorageEncrypted"></a>
Whether the DB cluster is encrypted.
Type: Boolean
Required: No

 ** VpcSecurityGroups **   <a name="securityhub-Type-AwsRdsDbClusterDetails-VpcSecurityGroups"></a>
A list of VPC security groups that the DB cluster belongs to.
Type: Array of [AwsRdsDbInstanceVpcSecurityGroup](API_AwsRdsDbInstanceVpcSecurityGroup.md) objects
Required: No

## See Also
<a name="API_AwsRdsDbClusterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbClusterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbClusterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbClusterDetails)
