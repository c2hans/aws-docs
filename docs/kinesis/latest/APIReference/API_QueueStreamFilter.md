---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_QueueStreamFilter.html
---

# QueueStreamFilter

Filters the queues returned by [ListQueues](API_ListQueues.md) to those created on a particular data stream.

## Contents
<a name="API_QueueStreamFilter_Contents"></a>

 ** StreamARN **   <a name="Streams-Type-QueueStreamFilter-StreamARN"></a>
The ARN of the data stream to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

 ** StreamCreationTimestamp **   <a name="Streams-Type-QueueStreamFilter-StreamCreationTimestamp"></a>
The time the data stream was created. Specify this value to distinguish between a deleted stream and a stream that was recreated with the same name.
Type: Timestamp
Required: No

## See Also
<a name="API_QueueStreamFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/QueueStreamFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/QueueStreamFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/QueueStreamFilter)
