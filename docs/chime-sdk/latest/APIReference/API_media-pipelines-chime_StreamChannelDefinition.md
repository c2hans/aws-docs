---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StreamChannelDefinition.html
---

# StreamChannelDefinition
<a name="API_media-pipelines-chime_StreamChannelDefinition"></a>

Defines a streaming channel.

## Contents
<a name="API_media-pipelines-chime_StreamChannelDefinition_Contents"></a>

 ** NumberOfChannels **   <a name="chimesdk-Type-media-pipelines-chime_StreamChannelDefinition-NumberOfChannels"></a>
The number of channels in a streaming channel.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2.
Required: Yes

 ** ChannelDefinitions **   <a name="chimesdk-Type-media-pipelines-chime_StreamChannelDefinition-ChannelDefinitions"></a>
The definitions of the channels in a streaming channel.
Type: Array of [ChannelDefinition](API_media-pipelines-chime_ChannelDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

## See Also
<a name="API_media-pipelines-chime_StreamChannelDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/StreamChannelDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/StreamChannelDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/StreamChannelDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
