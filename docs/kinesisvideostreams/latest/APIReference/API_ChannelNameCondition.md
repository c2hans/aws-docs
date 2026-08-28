---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_ChannelNameCondition.html
---

# ChannelNameCondition
<a name="API_ChannelNameCondition"></a>

An optional input parameter for the `ListSignalingChannels` API. When this parameter is specified while invoking `ListSignalingChannels`, the API returns only the channels that satisfy a condition specified in `ChannelNameCondition`.

## Contents
<a name="API_ChannelNameCondition_Contents"></a>

 ** ComparisonOperator **   <a name="KinesisVideo-Type-ChannelNameCondition-ComparisonOperator"></a>
A comparison operator. Currently, you can only specify the `BEGINS_WITH` operator, which finds signaling channels whose names begin with a given prefix.
Type: String
Valid Values: `BEGINS_WITH`
Required: No

 ** ComparisonValue **   <a name="KinesisVideo-Type-ChannelNameCondition-ComparisonValue"></a>
A value to compare.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_ChannelNameCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/ChannelNameCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/ChannelNameCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/ChannelNameCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
