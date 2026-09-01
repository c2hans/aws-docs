---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ChannelStreamIdentifier.html
---

# ChannelStreamIdentifier
<a name="API_ChannelStreamIdentifier"></a>

Identifies a source stream associated with a channel.

## Contents
<a name="API_ChannelStreamIdentifier_Contents"></a>

 ** StreamARN **   <a name="Streams-Type-ChannelStreamIdentifier-StreamARN"></a>
The Amazon Resource Name (ARN) of the source Kinesis data stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

 ** StreamCreationTimestamp **   <a name="Streams-Type-ChannelStreamIdentifier-StreamCreationTimestamp"></a>
The time at which the source stream was created.
Type: Timestamp
Required: Yes

## See Also
<a name="API_ChannelStreamIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ChannelStreamIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ChannelStreamIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ChannelStreamIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
