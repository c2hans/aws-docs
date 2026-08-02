---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Shard.html
---

# Shard
<a name="API_Shard"></a>

Represents a collection of nodes in a cluster. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

## Contents
<a name="API_Shard_Contents"></a>

 ** Name **   <a name="MemoryDB-Type-Shard-Name"></a>
The name of the shard
Type: String
Required: No

 ** Nodes **   <a name="MemoryDB-Type-Shard-Nodes"></a>
A list containing information about individual nodes within the shard
Type: Array of [Node](API_Node.md) objects
Required: No

 ** NumberOfNodes **   <a name="MemoryDB-Type-Shard-NumberOfNodes"></a>
The number of nodes in the shard
Type: Integer
Required: No

 ** Slots **   <a name="MemoryDB-Type-Shard-Slots"></a>
The keyspace for this shard.
Type: String
Required: No

 ** Status **   <a name="MemoryDB-Type-Shard-Status"></a>
The current state of this replication group - creating, available, modifying, deleting.
Type: String
Required: No

## See Also
<a name="API_Shard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/Shard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/Shard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/Shard)
