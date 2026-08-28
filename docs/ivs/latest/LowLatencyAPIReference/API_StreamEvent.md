---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamEvent.html
---

# StreamEvent
<a name="API_StreamEvent"></a>

Object specifying a stream’s events. For a list of events, see [Using Amazon EventBridge with Amazon IVS](https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html).

## Contents
<a name="API_StreamEvent_Contents"></a>

 ** code **   <a name="ivs-Type-StreamEvent-code"></a>
Provides additional details about the stream event. There are several values; the long descriptions are provided in the IVS console but not delivered through the IVS API or EventBridge. Multitrack-related codes are used only for certain Session Ended events.
+  `MultitrackInputNotAllowed` — The broadcast client attempted to connect with multitrack input, but multitrack input was not enabled on the channel. Check your broadcast software settings or set `MultitrackInputConfiguration.Policy` to `ALLOW` or `REQUIRE`.
+  `MultitrackInputRequired` — The broadcast client attempted to connect with single-track video, but multitrack input is required on this channel. Enable multitrack video in your broadcast software or configure the channel’s `MultitrackInputConfiguration.Policy` to `ALLOW`.
+  `InvalidGetClientConfigurationStreamKey` — The broadcast client attempted to connect with an invalid, expired, or corrupt stream key.
+  `GetClientConfigurationStreamKeyRequired` — The broadcast client attempted to stream multitrack video without providing an authenticated stream key from GetClientConfiguration.
+  `InvalidMultitrackInputTrackCount` — The multitrack input stream contained an invalid number of tracks.
+  `InvalidMultitrackInputVideoTrackMediaProperties` — The multitrack input stream contained one or more tracks with an invalid codec, resolution, bitrate, or framerate.
+  `StreamTakeoverMediaMismatch` — The broadcast client attempted to take over with different media properties (e.g., codec, resolution, or video track type) from the original stream.
+  `StreamTakeoverInvalidPriority` — The broadcast client attempted a takeover with either a priority integer value equal to or lower than the original stream's value or a value outside the allowed range of 1 to 2,147,483,647.

   `StreamTakeoverLimitBreached` — The broadcast client reached the maximum allowed takeover attempts for this stream.
Type: String
Required: No

 ** eventTime **   <a name="ivs-Type-StreamEvent-eventTime"></a>
Time when the event occurred. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

 ** name **   <a name="ivs-Type-StreamEvent-name"></a>
Name that identifies the stream event within a `type`.
Type: String
Required: No

 ** type **   <a name="ivs-Type-StreamEvent-type"></a>
Logical group for certain events.
Type: String
Required: No

## See Also
<a name="API_StreamEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/StreamEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/StreamEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/StreamEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
