---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_Shard.html
---

# Shard
<a name="API_streams_Shard"></a>

A uniquely identified group of stream records within a stream.

## Contents
<a name="API_streams_Shard_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ParentShardId **   <a name="DDB-Type-streams_Shard-ParentShardId"></a>
The shard ID of the current shard's parent.
Type: String
Length Constraints: Minimum length of 28. Maximum length of 65.
Required: No

 ** SequenceNumberRange **   <a name="DDB-Type-streams_Shard-SequenceNumberRange"></a>
The range of possible sequence numbers for the shard.
Type: [SequenceNumberRange](API_streams_SequenceNumberRange.md) object
Required: No

 ** ShardId **   <a name="DDB-Type-streams_Shard-ShardId"></a>
The system-generated identifier for this shard.
Type: String
Length Constraints: Minimum length of 28. Maximum length of 65.
Required: No

## See Also
<a name="API_streams_Shard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/streams-dynamodb-2012-08-10/Shard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/streams-dynamodb-2012-08-10/Shard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/streams-dynamodb-2012-08-10/Shard)
