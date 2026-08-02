---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShardEvent.html
---

# SubscribeToShardEvent
<a name="API_SubscribeToShardEvent"></a>

After you call [SubscribeToShard](API_SubscribeToShard.md), Kinesis Data Streams sends events of this type over an HTTP/2 connection to your consumer.

## Contents
<a name="API_SubscribeToShardEvent_Contents"></a>

 ** ContinuationSequenceNumber **   <a name="Streams-Type-SubscribeToShardEvent-ContinuationSequenceNumber"></a>
Use this as `SequenceNumber` in the next call to [SubscribeToShard](API_SubscribeToShard.md), with `StartingPosition` set to `AT_SEQUENCE_NUMBER` or `AFTER_SEQUENCE_NUMBER`. Use `ContinuationSequenceNumber` for checkpointing because it captures your shard progress even when no data is written to the shard.
Type: String
Pattern: `0|([1-9]\d{0,128})`
Required: Yes

 ** MillisBehindLatest **   <a name="Streams-Type-SubscribeToShardEvent-MillisBehindLatest"></a>
The number of milliseconds the read records are from the tip of the stream, indicating how far behind current time the consumer is. A value of zero indicates that record processing is caught up, and there are no new records to process at this moment.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** Records **   <a name="Streams-Type-SubscribeToShardEvent-Records"></a>

Type: Array of [Record](API_Record.md) objects
Required: Yes

 ** ChildShards **   <a name="Streams-Type-SubscribeToShardEvent-ChildShards"></a>
The list of the child shards of the current shard, returned only at the end of the current shard.
Type: Array of [ChildShard](API_ChildShard.md) objects
Required: No

## See Also
<a name="API_SubscribeToShardEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/SubscribeToShardEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/SubscribeToShardEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/SubscribeToShardEvent)
