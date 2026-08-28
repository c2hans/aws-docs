---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/media-stream-tips-tricks.html
---

# Using Amazon Chime SDK media stream pipelines data
<a name="media-stream-tips-tricks"></a>

You can use the metadata in the notifications to get KVS ARNs, fragment numbers, and fragment timestamps. That information can help you to process the audio data in a KVS stream.

Also, you can use KVS ARNs with the KVS APIs to read data from a stream. Depending on the use case, you call the [GetMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_GetMedia.html) and [GetMediaForFragmentList](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetMediaForFragmentList.html) APIs. Typically, a `GetMediaForFragmentList` call is preceded by a call to the [ListFragments](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_ListFragments.html) API. For more information, refer [Reading data from streams](https://aws.amazon.com/kinesis/video-streams/faqs/), in the *Amazon Kinesis Video Streams FAQs*.

Depending on the use case, builders can use the Kinesis Video Streams parser library, which in turn uses the KVS [GetMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_GetMedia.html) API.

Media stream pipelines add the following meeting and attendee metadata to each fragment.

```
"meetingId"
"externalMeetingId"
"attendeeId"
"externalUserId"
"sampleRate"
"channels"
```

Media data is stored in MKV format. All MKV audio data is AAC encoded. For more information, see [Kinesis Video Streams data model](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-data.html), in the *Kinesis Video Streams Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
