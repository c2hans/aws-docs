---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-kvs-pool.html
---

# Creating a Kinesis Video Streams pool for Amazon Chime SDK media stream pipelines
<a name="create-kvs-pool"></a>

The Kinesis Video Streams (KVS) pool for your media stream pipeline must belong to the same AWS account as the Amazon Chime SDK meeting. You create a Kinesis Video Streams pool by calling the [CreateMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool.html) API.

The following diagram shows the architecture of a media pipeline Kinesis Video Streams pool. Numbers in the image correspond to the numbered text below:

![Diagram showing an API call that creates a Kinesis Video Streams pool.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/media-stream-pool-architecture.png)

In the diagram:

1. You call the [CreateMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool.html) API.

1. The media pipeline control plane creates and manages the Kinesis Video Streams (KVS) and the pool on your behalf in your account.

KVS pool operation, the process of creating, updating, and deleting streams in the pool, is asynchronous. As a result, Event Bridge notifications use the `Chime Media Pipeline Kinesis Video Pool State Change` detail type to communicate the status of the streams in a pool.

You can create a pool once and reuse it across different meetings. You can also create different pools as needed, and delete pools when you don't need them.

Pools scale up automatically, based on your concurrent call burst. You can delete any unneeded pools.

**Note**
When you delete a pool, you must wait for pool to be completely deleted before you delete the KVS streams in the pool. An Event Bridge notification will indicate when the pool has been completely deleted. That happens after all the meetings that use the pool have ended. You can also call the [GetMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaPipelineKinesisVideoStreamPool.html) API to view the `PoolId` for a given KVS pool.
When you invoke the Kinesis Video Streams [DeleteStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DeleteStream.html) API, you can use that naming string to search for and delete the streams in a pool. You can also call the [GetMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaPipelineKinesisVideoStreamPool.html) API to view the `PoolId` for a given KVS pool. The examples in the next section explain how.
