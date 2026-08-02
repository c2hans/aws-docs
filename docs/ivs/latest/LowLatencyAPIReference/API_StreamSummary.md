---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamSummary.html
---

# StreamSummary
<a name="API_StreamSummary"></a>

Summary information about a stream.

## Contents
<a name="API_StreamSummary_Contents"></a>

 ** channelArn **   <a name="ivs-Type-StreamSummary-channelArn"></a>
Channel ARN for the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: No

 ** health **   <a name="ivs-Type-StreamSummary-health"></a>
The stream’s health.
Type: String
Valid Values: `HEALTHY | STARVING | UNKNOWN`
Required: No

 ** startTime **   <a name="ivs-Type-StreamSummary-startTime"></a>
Time of the stream’s start. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

 ** state **   <a name="ivs-Type-StreamSummary-state"></a>
The stream’s state. Do not rely on the `OFFLINE` state, as the API may not return it; instead, a "NotBroadcasting" error will indicate that the stream is not live.
Type: String
Valid Values: `LIVE | OFFLINE`
Required: No

 ** streamId **   <a name="ivs-Type-StreamSummary-streamId"></a>
Unique identifier for a live or previously live stream in the specified channel.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `st-[a-zA-Z0-9]+`
Required: No

 ** viewerCount **   <a name="ivs-Type-StreamSummary-viewerCount"></a>
A count of concurrent views of the stream. Typically, a new view appears in `viewerCount` within 15 seconds of when video playback starts and a view is removed from `viewerCount` within 1 minute of when video playback ends. A value of -1 indicates that the request timed out; in this case, retry.
Type: Long
Required: No

## See Also
<a name="API_StreamSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/StreamSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/StreamSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/StreamSummary)
