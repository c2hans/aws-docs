---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamSessionSummary.html
---

# StreamSessionSummary
<a name="API_StreamSessionSummary"></a>

Summary information about a stream session.

## Contents
<a name="API_StreamSessionSummary_Contents"></a>

 ** endTime **   <a name="ivs-Type-StreamSessionSummary-endTime"></a>
Time when the channel went offline. This is an ISO 8601 timestamp; *note that this is returned as a string*. For live streams, this is `NULL`.
Type: Timestamp
Required: No

 ** hasErrorEvent **   <a name="ivs-Type-StreamSessionSummary-hasErrorEvent"></a>
If `true`, this stream encountered a quota breach or failure.
Type: Boolean
Required: No

 ** startTime **   <a name="ivs-Type-StreamSessionSummary-startTime"></a>
Time when the channel went live. This is an ISO 8601 timestamp; *note that this is returned as a string*.
Type: Timestamp
Required: No

 ** streamId **   <a name="ivs-Type-StreamSessionSummary-streamId"></a>
Unique identifier for a live or previously live stream in the specified channel.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `st-[a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_StreamSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/StreamSessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/StreamSessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/StreamSessionSummary)
