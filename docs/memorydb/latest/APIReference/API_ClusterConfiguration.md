---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ClusterConfiguration.html
---

# ClusterConfiguration
<a name="API_ClusterConfiguration"></a>

A list of cluster configuration options.

## Contents
<a name="API_ClusterConfiguration_Contents"></a>

 ** Description **   <a name="MemoryDB-Type-ClusterConfiguration-Description"></a>
The description of the cluster configuration
Type: String
Required: No

 ** Engine **   <a name="MemoryDB-Type-ClusterConfiguration-Engine"></a>
The name of the engine used by the cluster configuration.
Type: String
Required: No

 ** EngineVersion **   <a name="MemoryDB-Type-ClusterConfiguration-EngineVersion"></a>
The Redis OSS engine version used by the cluster
Type: String
Required: No

 ** MaintenanceWindow **   <a name="MemoryDB-Type-ClusterConfiguration-MaintenanceWindow"></a>
The specified maintenance window for the cluster
Type: String
Required: No

 ** MultiRegionClusterName **   <a name="MemoryDB-Type-ClusterConfiguration-MultiRegionClusterName"></a>
The name for the multi-Region cluster associated with the cluster configuration.
Type: String
Required: No

 ** MultiRegionParameterGroupName **   <a name="MemoryDB-Type-ClusterConfiguration-MultiRegionParameterGroupName"></a>
The name of the multi-Region parameter group associated with the cluster configuration.
Type: String
Required: No

 ** Name **   <a name="MemoryDB-Type-ClusterConfiguration-Name"></a>
The name of the cluster
Type: String
Required: No

 ** NodeType **   <a name="MemoryDB-Type-ClusterConfiguration-NodeType"></a>
The node type used for the cluster
Type: String
Required: No

 ** NumShards **   <a name="MemoryDB-Type-ClusterConfiguration-NumShards"></a>
The number of shards in the cluster
Type: Integer
Required: No

 ** ParameterGroupName **   <a name="MemoryDB-Type-ClusterConfiguration-ParameterGroupName"></a>
The name of parameter group used by the cluster
Type: String
Required: No

 ** Port **   <a name="MemoryDB-Type-ClusterConfiguration-Port"></a>
The port used by the cluster
Type: Integer
Required: No

 ** Shards **   <a name="MemoryDB-Type-ClusterConfiguration-Shards"></a>
The list of shards in the cluster
Type: Array of [ShardDetail](API_ShardDetail.md) objects
Required: No

 ** SnapshotRetentionLimit **   <a name="MemoryDB-Type-ClusterConfiguration-SnapshotRetentionLimit"></a>
The snapshot retention limit set by the cluster
Type: Integer
Required: No

 ** SnapshotWindow **   <a name="MemoryDB-Type-ClusterConfiguration-SnapshotWindow"></a>
The snapshot window set by the cluster
Type: String
Required: No

 ** SubnetGroupName **   <a name="MemoryDB-Type-ClusterConfiguration-SubnetGroupName"></a>
The name of the subnet group used by the cluster
Type: String
Required: No

 ** TopicArn **   <a name="MemoryDB-Type-ClusterConfiguration-TopicArn"></a>
The Amazon Resource Name (ARN) of the SNS notification topic for the cluster
Type: String
Required: No

 ** VpcId **   <a name="MemoryDB-Type-ClusterConfiguration-VpcId"></a>
The ID of the VPC the cluster belongs to
Type: String
Required: No

## See Also
<a name="API_ClusterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ClusterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ClusterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ClusterConfiguration)
