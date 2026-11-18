---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeadLetterConfiguration.html
---

# DeadLetterConfiguration
<a name="API_DeadLetterConfiguration"></a>

The dead-letter handling configuration for a queue. Each queue has built-in dead-letter handling. When a record has been received `MaxReceiveCount` times without being acknowledged, it becomes a dead-letter record, and [ReceiveQueueRecords](API_ReceiveQueueRecords.md) no longer returns it. The dead-letter record stays in the same queue, and you work with it through [ReceiveDeadLetterQueueRecords](API_ReceiveDeadLetterQueueRecords.md), [AcknowledgeDeadLetterQueueRecords](API_AcknowledgeDeadLetterQueueRecords.md), [UpdateDeadLetterQueueRecordsVisibility](API_UpdateDeadLetterQueueRecordsVisibility.md), and [RestoreDeadLetterQueueRecords](API_RestoreDeadLetterQueueRecords.md), which use the same queue ARN.

Dead-letter handling is enabled by default, with a `MaxReceiveCount` of 6. To use a different value, or to turn dead-letter handling off, specify this configuration in `QueueAttributes`.

## Contents
<a name="API_DeadLetterConfiguration_Contents"></a>

 ** TargetType **   <a name="Streams-Type-DeadLetterConfiguration-TargetType"></a>
Whether dead-letter handling is enabled for the queue. `BUILT_IN` enables it: when a record has been received `MaxReceiveCount` times without being acknowledged, it becomes a dead-letter record and [ReceiveQueueRecords](API_ReceiveQueueRecords.md) no longer returns it. `NONE` disables it, and an unacknowledged record continues to be redelivered until it is acknowledged or its retention period ends.
Type: String
Valid Values: `BUILT_IN | NONE`
Required: Yes

 ** MaxReceiveCount **   <a name="Streams-Type-DeadLetterConfiguration-MaxReceiveCount"></a>
The number of times a record can be received without being acknowledged before it becomes a dead-letter record. Required when `TargetType` is `BUILT_IN`. A queue that you create without `DeadLetterConfiguration` gets a `MaxReceiveCount` of 6.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

## See Also
<a name="API_DeadLetterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/DeadLetterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/DeadLetterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/DeadLetterConfiguration)
