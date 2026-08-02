---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ShardConfiguration.html
---

# ShardConfiguration
<a name="API_ShardConfiguration"></a>

Shard configuration options. Each shard configuration has the following: Slots and ReplicaCount.

## Contents
<a name="API_ShardConfiguration_Contents"></a>

 ** ReplicaCount **   <a name="MemoryDB-Type-ShardConfiguration-ReplicaCount"></a>
The number of read replica nodes in this shard.
Type: Integer
Required: No

 ** Slots **   <a name="MemoryDB-Type-ShardConfiguration-Slots"></a>
A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format startkey-endkey.
Type: String
Required: No

## See Also
<a name="API_ShardConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ShardConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ShardConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ShardConfiguration)
