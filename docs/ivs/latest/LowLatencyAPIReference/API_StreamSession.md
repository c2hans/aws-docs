---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamSession.html
---

# StreamSession
<a name="API_StreamSession"></a>

Object that captures the Amazon IVS configuration that the customer provisioned, the ingest configurations that the broadcaster used, and the most recent Amazon IVS stream events it encountered.

## Contents
<a name="API_StreamSession_Contents"></a>

 ** channel **   <a name="ivs-Type-StreamSession-channel"></a>
The properties of the channel at the time of going live.
Type: [Channel](API_Channel.md) object
Required: No

 ** endTime **   <a name="ivs-Type-StreamSession-endTime"></a>
Time when the channel went offline. This is an ISO 8601 timestamp; *note that this is returned as a string*. For live streams, this is `NULL`.
Type: Timestamp
Required: No

 ** ingestConfiguration **   <a name="ivs-Type-StreamSession-ingestConfiguration"></a>
The properties of the incoming RTMP stream.
 **Note:** `ingestConfiguration` is deprecated in favor of `ingestConfigurations` but retained to ensure backward compatibility. If multitrack is not enabled, `ingestConfiguration` and `ingestConfigurations` contain the same data, namely information about Track0 (the sole track). If multitrack is enabled, `ingestConfiguration` contains data for only the first track (Track0) and `ingestConfigurations` contains data for all tracks.
Type: [IngestConfiguration](API_IngestConfiguration.md) object
Required: No

 ** ingestConfigurations **   <a name="ivs-Type-StreamSession-ingestConfigurations"></a>
The properties of the incoming RTMP stream. If multitrack is enabled, `ingestConfigurations` contains data for all tracks; otherwise, it contains data only for Track0 (the sole track).
Type: [IngestConfigurations](API_IngestConfigurations.md) object
Required: No

 ** recordingConfiguration **   <a name="ivs-Type-StreamSession-recordingConfiguration"></a>
The properties of recording the live stream.
Type: [RecordingConfiguration](API_RecordingConfiguration.md) object
Required: No

 ** startTime **   <a name="ivs-Type-StreamSession-startTime"></a>
Time when the channel went live. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

 ** streamId **   <a name="ivs-Type-StreamSession-streamId"></a>
Unique identifier for a live or previously live stream in the specified channel.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `st-[a-zA-Z0-9]+`
Required: No

 ** truncatedEvents **   <a name="ivs-Type-StreamSession-truncatedEvents"></a>
List of Amazon IVS events that the stream encountered. The list is sorted by most recent events and contains up to 500 events. For Amazon IVS events, see [Using Amazon EventBridge with Amazon IVS](https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html).
Type: Array of [StreamEvent](API_StreamEvent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: No

## See Also
<a name="API_StreamSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/StreamSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/StreamSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/StreamSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
