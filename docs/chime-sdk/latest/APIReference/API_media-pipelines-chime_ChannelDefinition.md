---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ChannelDefinition.html
---

# ChannelDefinition
<a name="API_media-pipelines-chime_ChannelDefinition"></a>

Defines an audio channel in a Kinesis video stream.

## Contents
<a name="API_media-pipelines-chime_ChannelDefinition_Contents"></a>

 ** ChannelId **   <a name="chimesdk-Type-media-pipelines-chime_ChannelDefinition-ChannelId"></a>
The channel ID.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** ParticipantRole **   <a name="chimesdk-Type-media-pipelines-chime_ChannelDefinition-ParticipantRole"></a>
Specifies whether the audio in a channel belongs to the `AGENT` or `CUSTOMER`.
Type: String
Valid Values: `AGENT | CUSTOMER`
Required: No

## See Also
<a name="API_media-pipelines-chime_ChannelDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/ChannelDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/ChannelDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/ChannelDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
