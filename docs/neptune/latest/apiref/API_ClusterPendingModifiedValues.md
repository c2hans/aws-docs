---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ClusterPendingModifiedValues.html
---

# ClusterPendingModifiedValues
<a name="API_ClusterPendingModifiedValues"></a>

This data type is used as a response element in the `ModifyDBCluster` operation and contains changes that will be applied during the next maintenance window.

## Contents
<a name="API_ClusterPendingModifiedValues_Contents"></a>

 ** AllocatedStorage **
The allocated storage size in gibibytes (GiB) for database engines. For Neptune, `AllocatedStorage` always returns 1, because Neptune DB cluster storage size isn't fixed, but instead automatically adjusts as needed.
Type: Integer
Required: No

 ** BackupRetentionPeriod **
The number of days for which automatic DB snapshots are retained.
Type: Integer
Required: No

 ** DBClusterIdentifier **
The DBClusterIdentifier value for the DB cluster.
Type: String
Required: No

 ** EngineVersion **
The database engine version.
Type: String
Required: No

 ** IAMDatabaseAuthenticationEnabled **
A value that indicates whether mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.
Type: Boolean
Required: No

 ** Iops **
The Provisioned IOPS (I/O operations per second) value. This setting is only for Multi-AZ DB clusters.
Type: Integer
Required: No

 ** PendingCloudwatchLogsExports **
This `PendingCloudwatchLogsExports` structure specifies pending changes to which CloudWatch logs are enabled and which are disabled.
Type: [PendingCloudwatchLogsExports](API_PendingCloudwatchLogsExports.md) object
Required: No

 ** StorageType **
The pending change in storage type for the DB cluster.   Valid Values:
+  ** `standard` **   –   ( *the default* ) Configures cost-effective database storage for applications with moderate to small I/O usage.
+  ** `iopt1` **   –   Enables [I/O-Optimized storage](https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage) that's designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput.

  Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.
Type: String
Required: No

## See Also
<a name="API_ClusterPendingModifiedValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ClusterPendingModifiedValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ClusterPendingModifiedValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ClusterPendingModifiedValues)
