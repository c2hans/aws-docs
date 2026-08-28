---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ChannelDestinationConfiguration.html
---

# ChannelDestinationConfiguration
<a name="API_ChannelDestinationConfiguration"></a>

Object specifying a channel as a destination.

## Contents
<a name="API_ChannelDestinationConfiguration_Contents"></a>

 ** channelArn **   <a name="ivsrealtimeeapireference-Type-ChannelDestinationConfiguration-channelArn"></a>
ARN of the channel to use for broadcasting. The channel and stage resources must be in the same AWS account and region. The channel must be offline (not broadcasting).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

 ** encoderConfigurationArn **   <a name="ivsrealtimeeapireference-Type-ChannelDestinationConfiguration-encoderConfigurationArn"></a>
ARN of the [EncoderConfiguration](API_EncoderConfiguration.md) resource. The encoder configuration and stage resources must be in the same AWS account and region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:encoder-configuration/[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_ChannelDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ChannelDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ChannelDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ChannelDestinationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
