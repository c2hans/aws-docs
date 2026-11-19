---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_QueueSummary.html
---

# QueueSummary

A summary of a queue. Returned by [ListQueues](API_ListQueues.md). To retrieve a queue's configuration attributes, use [DescribeQueue](API_DescribeQueue.md).

## Contents
<a name="API_QueueSummary_Contents"></a>

 ** QueueARN **   <a name="Streams-Type-QueueSummary-QueueARN"></a>
The ARN of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:queue/\S+`
Required: Yes

 ** QueueCreationTimestamp **   <a name="Streams-Type-QueueSummary-QueueCreationTimestamp"></a>
The time the queue was created.
Type: Timestamp
Required: Yes

 ** QueueName **   <a name="Streams-Type-QueueSummary-QueueName"></a>
The name of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** QueueStatus **   <a name="Streams-Type-QueueSummary-QueueStatus"></a>
The current status of the queue.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING`
Required: Yes

 ** Streams **   <a name="Streams-Type-QueueSummary-Streams"></a>
The data stream the queue delivers records from.
Type: Array of [QueueStreamIdentifier](API_QueueStreamIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: Yes

## See Also
<a name="API_QueueSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/QueueSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/QueueSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/QueueSummary)
