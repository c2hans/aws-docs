---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ChannelStreamConfiguration.html
---

# ChannelStreamConfiguration
<a name="API_ChannelStreamConfiguration"></a>

Specifies the source stream and record configuration when creating a channel.

## Contents
<a name="API_ChannelStreamConfiguration_Contents"></a>

 ** RecordConfiguration **   <a name="Streams-Type-ChannelStreamConfiguration-RecordConfiguration"></a>
The record format configuration for the source stream.
Type: [RecordConfiguration](API_RecordConfiguration.md) object
Required: Yes

 ** StreamARN **   <a name="Streams-Type-ChannelStreamConfiguration-StreamARN"></a>
The Amazon Resource Name (ARN) of the source Kinesis data stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

## See Also
<a name="API_ChannelStreamConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ChannelStreamConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ChannelStreamConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ChannelStreamConfiguration)
