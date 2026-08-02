---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_ShardFilter.html
---

# ShardFilter
<a name="API_ShardFilter"></a>

A filter used to limit the shards returned by a `GetStream` operation.

## Contents
<a name="API_ShardFilter_Contents"></a>

 ** shardId **   <a name="keyspaces-Type-ShardFilter-shardId"></a>
The identifier of a specific shard used to filter results based on the specified filter type.
Type: String
Length Constraints: Minimum length of 28. Maximum length of 65.
Required: No

 ** type **   <a name="keyspaces-Type-ShardFilter-type"></a>
The type of shard filter to use, which determines how the shardId parameter is interpreted.
Type: String
Valid Values: `CHILD_SHARDS`
Required: No

## See Also
<a name="API_ShardFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/ShardFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/ShardFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/ShardFilter)
