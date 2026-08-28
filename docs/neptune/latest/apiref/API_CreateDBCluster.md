---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_CreateDBCluster.html
---

# CreateDBCluster
<a name="API_CreateDBCluster"></a>

Creates a new Amazon Neptune DB cluster.

You can use the `ReplicationSourceIdentifier` parameter to create the DB cluster as a Read Replica of another DB cluster or Amazon Neptune DB instance.

Note that when you create a new cluster using `CreateDBCluster` directly, deletion protection is disabled by default (when you create a new production cluster in the console, deletion protection is enabled by default). You can only delete a DB cluster if its `DeletionProtection` field is set to `false`.

## Request Parameters
<a name="API_CreateDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AvailabilityZones.AvailabilityZone.N**
A list of EC2 Availability Zones that instances in the DB cluster can be created in.
Type: Array of strings
Required: No

 ** BackupRetentionPeriod **
The number of days for which automated backups are retained. You must specify a minimum value of 1.
Default: 1
Constraints:
+ Must be a value from 1 to 35
Type: Integer
Required: No

 ** CharacterSetName **
 *(Not supported by Neptune)*
Type: String
Required: No

 ** CopyTagsToSnapshot **
 *If set to `true`, tags are copied to any snapshot of the DB cluster that is created.*
Type: Boolean
Required: No

 ** DatabaseName **
The name for your database of up to 64 alpha-numeric characters. If you do not provide a name, Amazon Neptune will not create a database in the DB cluster you are creating.
Type: String
Required: No

 ** DBClusterIdentifier **
The DB cluster identifier. This parameter is stored as a lowercase string.
Constraints:
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster1`
Type: String
Required: Yes

 ** DBClusterParameterGroupName **
 The name of the DB cluster parameter group to associate with this DB cluster. If this argument is omitted, the default is used.
Constraints:
+ If supplied, must match the name of an existing DBClusterParameterGroup.
Type: String
Required: No

 ** DBSubnetGroupName **
A DB subnet group to associate with this DB cluster.
Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.
Example: `mySubnetgroup`
Type: String
Required: No

 ** DeletionProtection **
A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is enabled.
Type: Boolean
Required: No

 **EnableCloudwatchLogsExports.member.N**
A list of the log types that this DB cluster should export to CloudWatch Logs. Valid log types are: `audit` (to publish audit logs) and `slowquery` (to publish slow-query logs). See [Publishing Neptune logs to Amazon CloudWatch logs](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html).
Type: Array of strings
Required: No

 ** EnableIAMDatabaseAuthentication **
If set to `true`, enables Amazon Identity and Access Management (IAM) authentication for the entire DB cluster (this cannot be set at an instance level).
Default: `false`.
Type: Boolean
Required: No

 ** Engine **
The name of the database engine to be used for this DB cluster.
Valid Values: `neptune`
Type: String
Required: Yes

 ** EngineVersion **
The version number of the database engine to use for the new DB cluster.
Example: `1.2.1.0`
Type: String
Required: No

 ** GlobalClusterIdentifier **
The ID of the Neptune global database to which this new DB cluster should be added.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: No

 ** KmsKeyId **
The Amazon KMS key identifier for an encrypted DB cluster.
The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a DB cluster with the same Amazon account that owns the KMS encryption key used to encrypt the new DB cluster, then you can use the KMS key alias instead of the ARN for the KMS encryption key.
If an encryption key is not specified in `KmsKeyId`:
+ If `ReplicationSourceIdentifier` identifies an encrypted source, then Amazon Neptune will use the encryption key used to encrypt the source. Otherwise, Amazon Neptune will use your default encryption key.
+ If the `StorageEncrypted` parameter is true and `ReplicationSourceIdentifier` is not specified, then Amazon Neptune will use your default encryption key.
Amazon KMS creates the default encryption key for your Amazon account. Your Amazon account has a different default encryption key for each Amazon Region.
If you create a Read Replica of an encrypted DB cluster in another Amazon Region, you must set `KmsKeyId` to a KMS key ID that is valid in the destination Amazon Region. This key is used to encrypt the Read Replica in that Amazon Region.
Type: String
Required: No

 ** MasterUsername **
Not supported by Neptune.
Type: String
Required: No

 ** MasterUserPassword **
Not supported by Neptune.
Type: String
Required: No

 ** OptionGroupName **
 *(Not supported by Neptune)*
Type: String
Required: No

 ** Port **
The port number on which the instances in the DB cluster accept connections.
 Default: `8182`
Type: Integer
Required: No

 ** PreferredBackupWindow **
The daily time range during which automated backups are created if automated backups are enabled using the `BackupRetentionPeriod` parameter.
The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region. To see the time blocks available, see [Neptune Maintenance Window](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-maintaining.html#manage-console-maintaining-window) in the *Amazon Neptune User Guide.*
Constraints:
+ Must be in the format `hh24:mi-hh24:mi`.
+ Must be in Universal Coordinated Time (UTC).
+ Must not conflict with the preferred maintenance window.
+ Must be at least 30 minutes.
Type: String
Required: No

 ** PreferredMaintenanceWindow **
The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
Format: `ddd:hh24:mi-ddd:hh24:mi`
The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region, occurring on a random day of the week. To see the time blocks available, see [Neptune Maintenance Window](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-maintaining.html#manage-console-maintaining-window) in the *Amazon Neptune User Guide.*
Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
Constraints: Minimum 30-minute window.
Type: String
Required: No

 ** PreSignedUrl **
This parameter is not currently supported.
Type: String
Required: No

 ** ReplicationSourceIdentifier **
The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
Type: String
Required: No

 ** ServerlessV2ScalingConfiguration **
Contains the scaling configuration of a Neptune Serverless DB cluster.
For more information, see [Using Amazon Neptune Serverless](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html) in the *Amazon Neptune User Guide*.
Type: [ServerlessV2ScalingConfiguration](API_ServerlessV2ScalingConfiguration.md) object
Required: No

 ** StorageEncrypted **
Specifies whether the DB cluster is encrypted.
Type: Boolean
Required: No

 ** StorageType **
The storage type for the new DB cluster.
Valid Values:
+  ** `standard` **   –   ( *the default* ) Configures cost-effective database storage for applications with moderate to small I/O usage. When set to `standard`, the storage type is not returned in the response.
+  ** `iopt1` **   –   Enables [I/O-Optimized storage](https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage) that's designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput.

  Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.
Type: String
Required: No

 **Tags.Tag.N**
The tags to assign to the new DB cluster.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**
A list of EC2 VPC security groups to associate with this DB cluster.
Type: Array of strings
Required: No

## Response Elements
<a name="API_CreateDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **
Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the [DescribeDBClusters](API_DescribeDBClusters.md).
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_CreateDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterAlreadyExistsFault **
User already has a DB cluster with the given identifier.
HTTP Status Code: 400

 ** DBClusterNotFoundFault **
 *DBClusterIdentifier* does not refer to an existing DB cluster.
HTTP Status Code: 404

 ** DBClusterParameterGroupNotFound **
 *DBClusterParameterGroupName* does not refer to an existing DB Cluster parameter group.
HTTP Status Code: 404

 ** DBClusterQuotaExceededFault **
User attempted to create a new DB cluster and the user has already reached the maximum allowed DB cluster quota.
HTTP Status Code: 403

 ** DBInstanceNotFound **
 *DBInstanceIdentifier* does not refer to an existing DB instance.
HTTP Status Code: 404

 ** DBSubnetGroupDoesNotCoverEnoughAZs **
Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.
HTTP Status Code: 400

 ** DBSubnetGroupNotFoundFault **
 *DBSubnetGroupName* does not refer to an existing DB subnet group.
HTTP Status Code: 404

 ** GlobalClusterNotFoundFault **
The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster.
HTTP Status Code: 404

 ** InsufficientStorageClusterCapacity **
There is insufficient storage available for the current action. You may be able to resolve this error by updating your subnet group to use different Availability Zones that have more storage available.
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

 ** InvalidDBInstanceState **
The specified DB instance is not in the *available* state.
HTTP Status Code: 400

 ** InvalidDBSubnetGroupStateFault **
The DB subnet group cannot be deleted because it is in use.
HTTP Status Code: 400

 ** InvalidGlobalClusterStateFault **
The global cluster is in an invalid state and can't perform the requested operation.
HTTP Status Code: 400

 ** InvalidSubnet **
The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **
DB subnet group does not cover all Availability Zones after it is created because users' change.
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **
Error accessing KMS key.
HTTP Status Code: 400

 ** StorageQuotaExceeded **
Request would result in user exceeding the allowed amount of storage available across all DB instances.
HTTP Status Code: 400

## See Also
<a name="API_CreateDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/CreateDBCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/CreateDBCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/CreateDBCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/CreateDBCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/CreateDBCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/CreateDBCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/CreateDBCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/CreateDBCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
