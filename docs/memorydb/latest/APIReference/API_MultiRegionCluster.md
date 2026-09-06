---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_MultiRegionCluster.html
---

# MultiRegionCluster
<a name="API_MultiRegionCluster"></a>

Represents a multi-Region cluster.

## Contents
<a name="API_MultiRegionCluster_Contents"></a>

 ** ARN **   <a name="MemoryDB-Type-MultiRegionCluster-ARN"></a>
The Amazon Resource Name (ARN) of the multi-Region cluster.
Type: String
Required: No

 ** Clusters **   <a name="MemoryDB-Type-MultiRegionCluster-Clusters"></a>
The clusters in this multi-Region cluster.
Type: Array of [RegionalCluster](API_RegionalCluster.md) objects
Required: No

 ** Description **   <a name="MemoryDB-Type-MultiRegionCluster-Description"></a>
The description of the multi-Region cluster.
Type: String
Required: No

 ** Engine **   <a name="MemoryDB-Type-MultiRegionCluster-Engine"></a>
The name of the engine used by the multi-Region cluster.
Type: String
Required: No

 ** EngineVersion **   <a name="MemoryDB-Type-MultiRegionCluster-EngineVersion"></a>
The version of the engine used by the multi-Region cluster.
Type: String
Required: No

 ** MultiRegionClusterName **   <a name="MemoryDB-Type-MultiRegionCluster-MultiRegionClusterName"></a>
The name of the multi-Region cluster.
Type: String
Required: No

 ** MultiRegionParameterGroupName **   <a name="MemoryDB-Type-MultiRegionCluster-MultiRegionParameterGroupName"></a>
The name of the multi-Region parameter group associated with the cluster.
Type: String
Required: No

 ** NodeType **   <a name="MemoryDB-Type-MultiRegionCluster-NodeType"></a>
The node type used by the multi-Region cluster.
Type: String
Required: No

 ** NumberOfShards **   <a name="MemoryDB-Type-MultiRegionCluster-NumberOfShards"></a>
The number of shards in the multi-Region cluster.
Type: Integer
Required: No

 ** Status **   <a name="MemoryDB-Type-MultiRegionCluster-Status"></a>
The current status of the multi-Region cluster.
Type: String
Required: No

 ** TLSEnabled **   <a name="MemoryDB-Type-MultiRegionCluster-TLSEnabled"></a>
Indiciates if the multi-Region cluster is TLS enabled.
Type: Boolean
Required: No

## See Also
<a name="API_MultiRegionCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/MultiRegionCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/MultiRegionCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/MultiRegionCluster)
