---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ModifyDBCluster.html
---

# ModifyDBCluster
<a name="API_ModifyDBCluster"></a>

Modify a setting for a DB cluster. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.

## Request Parameters
<a name="API_ModifyDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AllowMajorVersionUpgrade **
A value that indicates whether upgrades between different major versions are allowed.
Constraints: You must set the allow-major-version-upgrade flag when providing an `EngineVersion` parameter that uses a different major version than the DB cluster's current version.
Type: Boolean
Required: No

 ** ApplyImmediately **
A value that specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the `PreferredMaintenanceWindow` setting for the DB cluster. If this parameter is set to `false`, changes to the DB cluster are applied during the next maintenance window.
The `ApplyImmediately` parameter only affects `NewDBClusterIdentifier` values. If you set the `ApplyImmediately` parameter value to false, then changes to `NewDBClusterIdentifier` values are applied during the next maintenance window. All other changes are applied immediately, regardless of the value of the `ApplyImmediately` parameter.
Default: `false`
Type: Boolean
Required: No

 ** BackupRetentionPeriod **
The number of days for which automated backups are retained. You must specify a minimum value of 1.
Default: 1
Constraints:
+ Must be a value from 1 to 35
Type: Integer
Required: No

 ** CloudwatchLogsExportConfiguration **
The configuration setting for the log types to be enabled for export to CloudWatch Logs for a specific DB cluster. See [Using the CLI to publish Neptune audit logs to CloudWatch Logs](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html#cloudwatch-logs-cli).
Type: [CloudwatchLogsExportConfiguration](API_CloudwatchLogsExportConfiguration.md) object
Required: No

 ** CopyTagsToSnapshot **
 *If set to `true`, tags are copied to any snapshot of the DB cluster that is created.*
Type: Boolean
Required: No

 ** DBClusterIdentifier **
The DB cluster identifier for the cluster being modified. This parameter is not case-sensitive.
Constraints:
+ Must match the identifier of an existing DBCluster.
Type: String
Required: Yes

 ** DBClusterParameterGroupName **
The name of the DB cluster parameter group to use for the DB cluster.
Type: String
Required: No

 ** DBInstanceParameterGroupName **
The name of the DB parameter group to apply to all instances of the DB cluster.
When you apply a parameter group using `DBInstanceParameterGroupName`, parameter changes aren't applied during the next maintenance window but instead are applied immediately.
Default: The existing name setting
Constraints:
+ The DB parameter group must be in the same DB parameter group family as the target DB cluster version.
+ The `DBInstanceParameterGroupName` parameter is only valid in combination with the `AllowMajorVersionUpgrade` parameter.
Type: String
Required: No

 ** DeletionProtection **
A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
Type: Boolean
Required: No

 ** EnableIAMDatabaseAuthentication **
True to enable mapping of Amazon Identity and Access Management (IAM) accounts to database accounts, and otherwise false.
Default: `false`
Type: Boolean
Required: No

 ** EngineVersion **
The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless the `ApplyImmediately` parameter is set to true.
For a list of valid engine versions, see [Engine Releases for Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases.html), or call [DescribeDBEngineVersions](API_DescribeDBEngineVersions.md).
Type: String
Required: No

 ** MasterUserPassword **
Not supported by Neptune.
Type: String
Required: No

 ** NewDBClusterIdentifier **
The new DB cluster identifier for the DB cluster when renaming a DB cluster. This value is stored as a lowercase string.
Constraints:
+ Must contain from 1 to 63 letters, numbers, or hyphens
+ The first character must be a letter
+ Cannot end with a hyphen or contain two consecutive hyphens
Example: `my-cluster2`
Type: String
Required: No

 ** OptionGroupName **
 *Not supported by Neptune.*
Type: String
Required: No

 ** Port **
The port number on which the DB cluster accepts connections.
Constraints: Value must be `1150-65535`
Default: The same port as the original DB cluster.
Type: Integer
Required: No

 ** PreferredBackupWindow **
The daily time range during which automated backups are created if automated backups are enabled, using the `BackupRetentionPeriod` parameter.
The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region.
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
The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Region, occurring on a random day of the week.
Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
Constraints: Minimum 30-minute window.
Type: String
Required: No

 ** ServerlessV2ScalingConfiguration **
Contains the scaling configuration of a Neptune Serverless DB cluster.
For more information, see [Using Amazon Neptune Serverless](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html) in the *Amazon Neptune User Guide*.
Type: [ServerlessV2ScalingConfiguration](API_ServerlessV2ScalingConfiguration.md) object
Required: No

 ** StorageType **
The storage type to associate with the DB cluster.
Valid Values:
+  ** `standard` **   –   ( *the default* ) Configures cost-effective database storage for applications with moderate to small I/O usage.
+  ** `iopt1` **   –   Enables [I/O-Optimized storage](https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage) that's designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput.

  Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.
Type: String
Required: No

 **VpcSecurityGroupIds.VpcSecurityGroupId.N**
A list of VPC security groups that the DB cluster will belong to.
Type: Array of strings
Required: No

## Response Elements
<a name="API_ModifyDBCluster_ResponseElements"></a>

The following element is returned by the service.

 ** DBCluster **
Contains the details of an Amazon Neptune DB cluster.
This data type is used as a response element in the [DescribeDBClusters](API_DescribeDBClusters.md).
Type: [DBCluster](API_DBCluster.md) object

## Errors
<a name="API_ModifyDBCluster_Errors"></a>

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

 ** DBSubnetGroupNotFoundFault **
 *DBSubnetGroupName* does not refer to an existing DB subnet group.
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

 ** InvalidDBInstanceState **
The specified DB instance is not in the *available* state.
HTTP Status Code: 400

 ** InvalidDBSecurityGroupState **
The state of the DB security group does not allow deletion.
HTTP Status Code: 400

 ** InvalidDBSubnetGroupStateFault **
The DB subnet group cannot be deleted because it is in use.
HTTP Status Code: 400

 ** InvalidSubnet **
The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **
DB subnet group does not cover all Availability Zones after it is created because users' change.
HTTP Status Code: 400

 ** StorageQuotaExceeded **
Request would result in user exceeding the allowed amount of storage available across all DB instances.
HTTP Status Code: 400

 ** StorageTypeNotSupported **
 *StorageType* specified cannot be associated with the DB Instance.
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/ModifyDBCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/ModifyDBCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ModifyDBCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/ModifyDBCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ModifyDBCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/ModifyDBCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/ModifyDBCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/ModifyDBCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ModifyDBCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ModifyDBCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
