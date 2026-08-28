---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_FragmentSelector.html
---

# FragmentSelector
<a name="API_media-pipelines-chime_FragmentSelector"></a>

Describes the timestamp range and timestamp origin of a range of fragments.

Only fragments with a start timestamp greater than or equal to the given start time and less than or equal to the end time are returned. For example, say a stream contains fragments with the following start timestamps:
+ 00:00:00
+ 00:00:02
+ 00:00:04
+ 00:00:06

A fragment selector range with a start time of 00:00:01 and end time of 00:00:04 would return the fragments with start times of 00:00:02 and 00:00:04.

## Contents
<a name="API_media-pipelines-chime_FragmentSelector_Contents"></a>

 ** FragmentSelectorType **   <a name="chimesdk-Type-media-pipelines-chime_FragmentSelector-FragmentSelectorType"></a>
The origin of the timestamps to use, `Server` or `Producer`. For more information, see [StartSelectorType](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_StartSelector.html) in the *Amazon Kinesis Video Streams Developer Guide*.
Type: String
Valid Values: `ProducerTimestamp | ServerTimestamp`
Required: Yes

 ** TimestampRange **   <a name="chimesdk-Type-media-pipelines-chime_FragmentSelector-TimestampRange"></a>
The range of timestamps to return.
Type: [TimestampRange](API_media-pipelines-chime_TimestampRange.md) object
Required: Yes

## See Also
<a name="API_media-pipelines-chime_FragmentSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/FragmentSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/FragmentSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/FragmentSelector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
