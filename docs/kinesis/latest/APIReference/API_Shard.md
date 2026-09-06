---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Shard.html
---

# Shard
<a name="API_Shard"></a>

A uniquely identified group of data records in a Kinesis data stream.

## Contents
<a name="API_Shard_Contents"></a>

 ** HashKeyRange **   <a name="Streams-Type-Shard-HashKeyRange"></a>
The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.
Type: [HashKeyRange](API_HashKeyRange.md) object
Required: Yes

 ** SequenceNumberRange **   <a name="Streams-Type-Shard-SequenceNumberRange"></a>
The range of possible sequence numbers for the shard.
Type: [SequenceNumberRange](API_SequenceNumberRange.md) object
Required: Yes

 ** ShardId **   <a name="Streams-Type-Shard-ShardId"></a>
The unique identifier of the shard within the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** AdjacentParentShardId **   <a name="Streams-Type-Shard-AdjacentParentShardId"></a>
The shard ID of the shard adjacent to the shard's parent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** ParentShardId **   <a name="Streams-Type-Shard-ParentShardId"></a>
The shard ID of the shard's parent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_Shard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/Shard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/Shard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/Shard)
