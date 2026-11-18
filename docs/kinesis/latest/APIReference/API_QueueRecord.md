---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_QueueRecord.html
---

# QueueRecord
<a name="API_QueueRecord"></a>

A data stream record, as delivered through a queue.

## Contents
<a name="API_QueueRecord_Contents"></a>

 ** ApproximateArrivalTimestamp **   <a name="Streams-Type-QueueRecord-ApproximateArrivalTimestamp"></a>
The approximate time the record arrived in the data stream. The difference between this value and the current time is how long the record took to reach your queue consumer.
Type: Timestamp
Required: Yes

 ** Data **   <a name="Streams-Type-QueueRecord-Data"></a>
The data blob of the record. Amazon Kinesis Data Streams does not inspect, interpret, or change the data.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 10485760.
Required: Yes

 ** FirstReceiveTimestamp **   <a name="Streams-Type-QueueRecord-FirstReceiveTimestamp"></a>
The approximate time the record was first received from the queue.
Type: Timestamp
Required: Yes

 ** ReceiptHandle **   <a name="Streams-Type-QueueRecord-ReceiptHandle"></a>
The identifier you use to acknowledge this record, change its visibility, or restore it after it becomes a dead-letter record. A new receipt handle is issued each time the record is received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** ReceiveCount **   <a name="Streams-Type-QueueRecord-ReceiveCount"></a>
The number of times this record has been received without being acknowledged.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** RecordId **   <a name="Streams-Type-QueueRecord-RecordId"></a>
The unique identifier of the record. This value stays the same across every delivery of the record, and it is the same in every queue on the stream that delivers the record. To identify a single delivery, use `ReceiptHandle` instead.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9]+$`
Required: Yes

 ** PartitionKey **   <a name="Streams-Type-QueueRecord-PartitionKey"></a>
The partition key the record was written to the data stream with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_QueueRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/QueueRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/QueueRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/QueueRecord)
