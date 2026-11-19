---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_QueueStreamConfiguration.html
---

# QueueStreamConfiguration

The data stream a queue delivers records from, and the position in that stream where delivery begins.

## Contents
<a name="API_QueueStreamConfiguration_Contents"></a>

 ** StreamARN **   <a name="Streams-Type-QueueStreamConfiguration-StreamARN"></a>
The ARN of the data stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

 ** StartingPosition **   <a name="Streams-Type-QueueStreamConfiguration-StartingPosition"></a>
The position in the stream from which the queue begins delivering records. The default is `LATEST`.
Type: [QueueStartingPosition](API_QueueStartingPosition.md) object
Required: No

## See Also
<a name="API_QueueStreamConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/QueueStreamConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/QueueStreamConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/QueueStreamConfiguration)
