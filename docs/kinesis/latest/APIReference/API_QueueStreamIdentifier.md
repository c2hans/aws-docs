---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_QueueStreamIdentifier.html
---

# QueueStreamIdentifier

Identifies a data stream associated with a queue.

## Contents
<a name="API_QueueStreamIdentifier_Contents"></a>

 ** StreamARN **   <a name="Streams-Type-QueueStreamIdentifier-StreamARN"></a>
The ARN of the data stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

 ** StreamCreationTimestamp **   <a name="Streams-Type-QueueStreamIdentifier-StreamCreationTimestamp"></a>
The time the data stream was created.
Type: Timestamp
Required: Yes

## See Also
<a name="API_QueueStreamIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/QueueStreamIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/QueueStreamIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/QueueStreamIdentifier)
