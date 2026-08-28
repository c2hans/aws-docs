---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_reader_ClipTimestampRange.html
---

# ClipTimestampRange
<a name="API_reader_ClipTimestampRange"></a>

The range of timestamps for which to return fragments.

## Contents
<a name="API_reader_ClipTimestampRange_Contents"></a>

 ** EndTimestamp **   <a name="KinesisVideo-Type-reader_ClipTimestampRange-EndTimestamp"></a>
The end of the timestamp range for the requested media.
This value must be within 24 hours of the specified `StartTimestamp`, and it must be later than the `StartTimestamp` value. If `FragmentSelectorType` for the request is `SERVER_TIMESTAMP`, this value must be in the past.
This value is inclusive. The `EndTimestamp` is compared to the (starting) timestamp of the fragment. Fragments that start before the `EndTimestamp` value and continue past it are included in the session.
Type: Timestamp
Required: Yes

 ** StartTimestamp **   <a name="KinesisVideo-Type-reader_ClipTimestampRange-StartTimestamp"></a>
The starting timestamp in the range of timestamps for which to return fragments.
Only fragments that start exactly at or after `StartTimestamp` are included in the session. Fragments that start before `StartTimestamp` and continue past it aren't included in the session. If `FragmentSelectorType` is `SERVER_TIMESTAMP`, the `StartTimestamp` must be later than the stream head.
Type: Timestamp
Required: Yes

## See Also
<a name="API_reader_ClipTimestampRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/ClipTimestampRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/ClipTimestampRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/ClipTimestampRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
