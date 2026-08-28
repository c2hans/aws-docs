---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Channel.html
---

# Channel
<a name="API_Channel"></a>

Object specifying a channel.

## Contents
<a name="API_Channel_Contents"></a>

 ** adConfigurationArn **   <a name="ivs-Type-Channel-adConfigurationArn"></a>
ARN of the ad configuration associated with the channel.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:ad-configuration/[a-zA-Z0-9-]+$`
Required: No

 ** arn **   <a name="ivs-Type-Channel-arn"></a>
Channel ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: No

 ** authorized **   <a name="ivs-Type-Channel-authorized"></a>
Whether the channel is private (enabled for playback authorization). Default: `false`.
Type: Boolean
Required: No

 ** containerFormat **   <a name="ivs-Type-Channel-containerFormat"></a>
Indicates which content-packaging format is used (MPEG-TS or fMP4). If `multitrackInputConfiguration` is specified and `enabled` is `true`, then `containerFormat` is required and must be set to `FRAGMENTED_MP4`. Otherwise, `containerFormat` may be set to `TS` or `FRAGMENTED_MP4`. Default: `TS`.
Type: String
Valid Values: `TS | FRAGMENTED_MP4`
Required: No

 ** ingestEndpoint **   <a name="ivs-Type-Channel-ingestEndpoint"></a>
Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.
Type: String
Required: No

 ** insecureIngest **   <a name="ivs-Type-Channel-insecureIngest"></a>
Whether the channel allows insecure RTMP ingest. Default: `false`.
Type: Boolean
Required: No

 ** latencyMode **   <a name="ivs-Type-Channel-latencyMode"></a>
Channel latency mode. Use `NORMAL` to broadcast and deliver live video up to Full HD. Use `LOW` for near-real-time interaction with viewers. Default: `LOW`.
Type: String
Valid Values: `NORMAL | LOW`
Required: No

 ** multitrackInputConfiguration **   <a name="ivs-Type-Channel-multitrackInputConfiguration"></a>
Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.
Type: [MultitrackInputConfiguration](API_MultitrackInputConfiguration.md) object
Required: No

 ** name **   <a name="ivs-Type-Channel-name"></a>
Channel name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** playbackRestrictionPolicyArn **   <a name="ivs-Type-Channel-playbackRestrictionPolicyArn"></a>
Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. Default: "" (empty string, no playback restriction policy is applied).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:playback-restriction-policy/[a-zA-Z0-9-]+$`
Required: No

 ** playbackUrl **   <a name="ivs-Type-Channel-playbackUrl"></a>
Channel playback URL.
Type: String
Required: No

 ** preset **   <a name="ivs-Type-Channel-preset"></a>
Optional transcode preset for the channel. This is selectable only for `ADVANCED_HD` and `ADVANCED_SD` channel types. For those channel types, the default `preset` is `HIGHER_BANDWIDTH_DELIVERY`. For other channel types (`BASIC` and `STANDARD`), `preset` is the empty string (`""`).
Type: String
Valid Values: `HIGHER_BANDWIDTH_DELIVERY | CONSTRAINED_BANDWIDTH_DELIVERY`
Required: No

 ** recordingConfigurationArn **   <a name="ivs-Type-Channel-recordingConfigurationArn"></a>
Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. Default: "" (empty string, recording is disabled).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$`
Required: No

 ** srt **   <a name="ivs-Type-Channel-srt"></a>
Specifies the endpoint and optional passphrase for streaming with the SRT protocol.
Type: [Srt](API_Srt.md) object
Required: No

 ** tags **   <a name="ivs-Type-Channel-tags"></a>
Tags attached to the resource. Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** type **   <a name="ivs-Type-Channel-type"></a>
Channel type, which determines the allowable resolution and bitrate. *If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.* Default: `STANDARD`. For details, see [Channel Types](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/channel-types.html).
Type: String
Valid Values: `BASIC | STANDARD | ADVANCED_SD | ADVANCED_HD`
Required: No

## See Also
<a name="API_Channel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/Channel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/Channel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/Channel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
