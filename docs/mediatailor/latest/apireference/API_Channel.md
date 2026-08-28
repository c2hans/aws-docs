---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_Channel.html
---

# Channel
<a name="API_Channel"></a>

The configuration parameters for a channel. For information about MediaTailor channels, see [Working with channels](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html) in the *MediaTailor User Guide*.

## Contents
<a name="API_Channel_Contents"></a>

 ** Arn **   <a name="mediatailor-Type-Channel-Arn"></a>
The ARN of the channel.
Type: String
Required: Yes

 ** ChannelName **   <a name="mediatailor-Type-Channel-ChannelName"></a>
The name of the channel.
Type: String
Required: Yes

 ** ChannelState **   <a name="mediatailor-Type-Channel-ChannelState"></a>
Returns the state whether the channel is running or not.
Type: String
Required: Yes

 ** LogConfiguration **   <a name="mediatailor-Type-Channel-LogConfiguration"></a>
The log configuration.
Type: [LogConfigurationForChannel](API_LogConfigurationForChannel.md) object
Required: Yes

 ** Outputs **   <a name="mediatailor-Type-Channel-Outputs"></a>
The channel's output properties.
Type: Array of [ResponseOutputItem](API_ResponseOutputItem.md) objects
Required: Yes

 ** PlaybackMode **   <a name="mediatailor-Type-Channel-PlaybackMode"></a>
The type of playback mode for this channel.
 `LINEAR` - Programs play back-to-back only once.
 `LOOP` - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule.
Type: String
Required: Yes

 ** Tier **   <a name="mediatailor-Type-Channel-Tier"></a>
The tier for this channel. STANDARD tier channels can contain live programs.
Type: String
Required: Yes

 ** Audiences **   <a name="mediatailor-Type-Channel-Audiences"></a>
The list of audiences defined in channel.
Type: Array of strings
Required: No

 ** CreationTime **   <a name="mediatailor-Type-Channel-CreationTime"></a>
The timestamp of when the channel was created.
Type: Timestamp
Required: No

 ** FillerSlate **   <a name="mediatailor-Type-Channel-FillerSlate"></a>
The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the `LINEAR` `PlaybackMode`. MediaTailor doesn't support filler slate for channels using the `LOOP` `PlaybackMode`.
Type: [SlateSource](API_SlateSource.md) object
Required: No

 ** LastModifiedTime **   <a name="mediatailor-Type-Channel-LastModifiedTime"></a>
The timestamp of when the channel was last modified.
Type: Timestamp
Required: No

 ** tags **   <a name="mediatailor-Type-Channel-tags"></a>
The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

## See Also
<a name="API_Channel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/Channel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/Channel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/Channel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
