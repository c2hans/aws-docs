---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StreamSummary.html
---

# StreamSummary
<a name="API_StreamSummary"></a>

The summary of a stream.

## Contents
<a name="API_StreamSummary_Contents"></a>

 ** StreamARN **   <a name="Streams-Type-StreamSummary-StreamARN"></a>
The ARN of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

 ** StreamName **   <a name="Streams-Type-StreamSummary-StreamName"></a>
The name of a stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** StreamStatus **   <a name="Streams-Type-StreamSummary-StreamStatus"></a>
The status of the stream.
Type: String
Valid Values: `CREATING | DELETING | ACTIVE | UPDATING`
Required: Yes

 ** StreamCreationTimestamp **   <a name="Streams-Type-StreamSummary-StreamCreationTimestamp"></a>
The timestamp at which the stream was created.
Type: Timestamp
Required: No

 ** StreamModeDetails **   <a name="Streams-Type-StreamSummary-StreamModeDetails"></a>
 Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an **on-demand** capacity mode and a **provisioned** capacity mode for your data streams.
Type: [StreamModeDetails](API_StreamModeDetails.md) object
Required: No

## See Also
<a name="API_StreamSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/StreamSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/StreamSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/StreamSummary)
