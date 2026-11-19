---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_QueueDescription.html
---

# QueueDescription

A description of a queue. Returned by [CreateQueue](API_CreateQueue.md), [UpdateQueue](API_UpdateQueue.md), and [DescribeQueue](API_DescribeQueue.md).

## Contents
<a name="API_QueueDescription_Contents"></a>

 ** QueueARN **   <a name="Streams-Type-QueueDescription-QueueARN"></a>
The ARN of the queue. The resource identifier in the ARN is generated when the queue is created and is not derived from `QueueName`. Use the returned `QueueARN` to identify the queue in subsequent requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:queue/\S+`
Required: Yes

 ** QueueCreationTimestamp **   <a name="Streams-Type-QueueDescription-QueueCreationTimestamp"></a>
The time the queue was created.
Type: Timestamp
Required: Yes

 ** QueueName **   <a name="Streams-Type-QueueDescription-QueueName"></a>
The name of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** QueueStatus **   <a name="Streams-Type-QueueDescription-QueueStatus"></a>
The current status of the queue.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING`
Required: Yes

 ** StreamConfigurationList **   <a name="Streams-Type-QueueDescription-StreamConfigurationList"></a>
The data stream the queue delivers records from, and the position in that stream where delivery begins. The list contains exactly one entry, because a queue delivers records from a single data stream.
Type: Array of [QueueStreamConfiguration](API_QueueStreamConfiguration.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** QueueAttributes **   <a name="Streams-Type-QueueDescription-QueueAttributes"></a>
The configuration attributes of the queue.
Type: [QueueAttributes](API_QueueAttributes.md) object
Required: No

## See Also
<a name="API_QueueDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/QueueDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/QueueDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/QueueDescription)
