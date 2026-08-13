---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-stream-pipeline.html
---

# Creating Amazon Chime SDK media stream pipelines
<a name="create-stream-pipeline"></a>

The chime media stream pipeline must belong to the same AWS account as the Amazon Chime SDK meeting. You create the Amazon Chime SDK media stream pipeline by calling the [CreateMediaStreamPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaStreamPipeline.html) API and specifying a source and a sink.

The following diagram shows the architecture of an Amazon Chime SDK media stream pipeline. Numbers in the diagram correspond to the numbered text below.

![Diagram showing an API call that creates a media stream pool.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/media-stream-pipe-architecture.png)

In the diagram:

1. You call the `CreateMediaStreamPipeline` API. In the request, specify the sources and sinks for the streams. whether you want to capture individual audio, mixed audio, or both. Include the ARN of your KVS pool in the request.
   + The sources array consists of the `SourceType` and `SourceArn`. You must use the `ChimeSdkMeeting SourceType`. The `SourceArn` is the ARN of the `ChimeSdkMeeting`.
   + The sinks array consists of the `SinkType`, `SinkArn`, `ReservedStreamCapacity`, and `MediaStreamType`. We only support the `KinesisVideoStreamPoolSinkType`. The `SinkArn` is the ARN of the `KinesisVideoStreamPool`. The `MediaStreamType` controls the type of media streamed to the sink, either `MixedAudio` or `IndividualAudio`. `ReservedStreamCapacity` sets the number of streams allocated for the `MediaStreamType` from the `KinesisVideoStreamPool`.
     + If you want to stream both `IndividualAudio` and `MixedAudio`, create two sink objects in the `Sinks` array, one for `IndividualAudio`, another for `MixedAudio`. The `SinkArn` (the ARN of the `KinesisVideoStreamPool`) can vary for each sink.
     + To stream just individual audio or mixed audio, create one sink object with the desired `MediaStreamType`.
   + Note the following:
     + When invoking the [CreateMediaStreamPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaStreamPipeline.html) API with `KinesisVideoStreamPool` as the `SinkType`, the `SinkARN` must belong to the control plane region in which `CreateMediaStreamPipeline` is being invoked.

       For example, if you create a media stream pipeline in `us-east-1`, you must use a `KinesisVideoStreamPool` in `us-east-1`.
     + `ReservedStreamCapacity` should be **1** when you specify the `MixedAudio` `MediaStreamType`, and between **1-10** when you specify the `IndividualAudio` `MediaStreamType`.

1. The media pipeline data plane calls the KVS [ PutMedia ](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html) API to store individual audio in a KVS stream that belongs to the KVS pool that you specify.

1. The media pipeline data plane calls the KVS `PutMedia` API to store mixed audio in a stream that belongs to the KVS pool that you specify.

**Note**
After calling the [CreateMediaStreamPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaStreamPipeline.html) API, builders can use [media pipeline events](media-pipe-events.md) or call the [GetMediaPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaPipeline.html) API to determine if the pipeline state is `InProgress`.
Once the pipeline state reaches `InProgress`, the media—any combination of `IndividualAudio` and `MixedAudio`—streams to KVS.
For the `IndividualAudio` stream type, a 1:1 mapping exists between attendee IDs and the KVS stream allocated from the `KinesisVideoStreamPool`. The mapping applies for the life of the media pipeline.
To know which KVS stream maps to an attendee ID, or is assigned for MixedAudio, use one of the following techniques:
Use [Event Bridge Notifications](media-stream-event-bridge.md). Each notification provides information such as attendee IDs and the KVS ARN that streams the attendee’s audio. When a `IndividualAudio` or `MixedAudio` streaming session starts, we send a `chime:MediaPipelineKinesisVideoStreamStart` event. Streaming sessions end when an attendee leaves the call (for `IndividualAudio`), or when the meeting ends.
Use the persistent metadata that the Kinesis Video Streams send with each fragment. The metadata contains information similar to what Event Bridge sends. Builders need to parse all the streams of the `KinesisVideoStreamPool` by specifying the pool name as the prefix in the [ListStreams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListStreams.html) Kinesis Video Streams API using this solution.
Media Stream pipeline termination happens when the meeting is deleted, or the [DeleteMediaPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaPipeline.html) API is invoked for that media stream pipeline. An [Event Bridge notification](media-pipe-events.md) is also sent to indicate the media pipeline termination.
