---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_AutoParticipantRecordingConfiguration.html
---

# AutoParticipantRecordingConfiguration
<a name="API_AutoParticipantRecordingConfiguration"></a>

Object specifying a configuration for individual participant recording.

## Contents
<a name="API_AutoParticipantRecordingConfiguration_Contents"></a>

 ** storageConfigurationArn **   <a name="ivsrealtimeeapireference-Type-AutoParticipantRecordingConfiguration-storageConfigurationArn"></a>
ARN of the [StorageConfiguration](API_StorageConfiguration.md) resource to use for individual participant recording. Default: `""` (empty string, no storage configuration is specified). Individual participant recording cannot be started unless a storage configuration is specified, when a [Stage](API_Stage.md) is created or updated. To disable individual participant recording, set this to `""`; other fields in this object will get reset to their defaults when sending `""`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:storage-configuration/[a-zA-Z0-9-]+$`
Required: Yes

 ** hlsConfiguration **   <a name="ivsrealtimeeapireference-Type-AutoParticipantRecordingConfiguration-hlsConfiguration"></a>
HLS configuration object for individual participant recording.
Type: [ParticipantRecordingHlsConfiguration](API_ParticipantRecordingHlsConfiguration.md) object
Required: No

 ** mediaTypes **   <a name="ivsrealtimeeapireference-Type-AutoParticipantRecordingConfiguration-mediaTypes"></a>
Types of media to be recorded. Default: `AUDIO_VIDEO`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `AUDIO_VIDEO | AUDIO_ONLY | NONE`
Required: No

 ** recordingReconnectWindowSeconds **   <a name="ivsrealtimeeapireference-Type-AutoParticipantRecordingConfiguration-recordingReconnectWindowSeconds"></a>
If a stage publisher disconnects and then reconnects within the specified interval, the multiple recordings will be considered a single recording and merged together.
The default value is 0, which disables merging.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 300.
Required: No

 ** recordParticipantReplicas **   <a name="ivsrealtimeeapireference-Type-AutoParticipantRecordingConfiguration-recordParticipantReplicas"></a>
Optional field to disable replica participant recording. If this is set to `false` when a participant is a replica, replica participants are not recorded. Default: `true`.
Type: Boolean
Required: No

 ** thumbnailConfiguration **   <a name="ivsrealtimeeapireference-Type-AutoParticipantRecordingConfiguration-thumbnailConfiguration"></a>
A complex type that allows you to enable/disable the recording of thumbnails for individual participant recording and modify the interval at which thumbnails are generated for the live session.
Type: [ParticipantThumbnailConfiguration](API_ParticipantThumbnailConfiguration.md) object
Required: No

## See Also
<a name="API_AutoParticipantRecordingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/AutoParticipantRecordingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/AutoParticipantRecordingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/AutoParticipantRecordingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
