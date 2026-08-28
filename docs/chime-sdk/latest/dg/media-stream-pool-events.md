---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/media-stream-pool-events.html
---

# Understanding Kinesis Video Streams pool events for Amazon Chime SDK media stream pipelines
<a name="media-stream-pool-events"></a>

Media pipelines send the following events to Event Bridge when the pools' states change. Expand each section to learn more.

## Amazon Chime Media Pipeline Kinesis Video Pool Active
<a name="kvs-pool-active"></a>

The media pipeline sends this event is sent after the [CreateMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool.html) API creates a pool.

```
{
    "version": "0",
    "id": "5ee6265a-0a40-104e-d8fd-a3b4bdd78483",
    "detail-type": "Chime Media Pipeline Kinesis Video Pool State Change",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{2021-07-28T20:20:49Z}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "eventType": "chime:MediaPipelineKinesisVideoStreamPoolActive",
        "timestamp": {{1627503649251}},
        "mediaRegion": "{{ap-southeast-1}}",
        "poolArn" : "{{ARN of the KVS Pool}}"
    }
}
```

## Amazon Chime Chime Media Pipeline Kinesis Video Pool Updated
<a name="kvs-pool-updated"></a>

The media pipeline sends this event after the [UpdateMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaPipelineKinesisVideoStreamPool.html) API updates a pool.

```
{
    "version": "0",
    "id": "5ee6265a-0a40-104e-d8fd-a3b4bdd78483",
    "detail-type": "Chime Media Pipeline Kinesis Video Pool State Change",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{2021-07-28T20:20:49Z}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "eventType": "chime:MediaPipelineKinesisVideoStreamPoolUpdated",
        "timestamp": {{1627503649251}},
        "mediaRegion": "{{ap-southeast-1}}",
        "poolArn" : "{{ARN of the KVS Pool}}"
    }
}
```

## Amazon Chime Media Pipeline Kinesis Video Pool Deleted
<a name="kvs-pool-deleted"></a>

The media pipeline sends this event to Event Bridge when the [DeleteMediaPipelineKinesisVideoStreamPool](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaPipelineKinesisVideoStreamPool.html) deletes a pool.

For more information about deleting pools, refer to [Creating a Kinesis Video Streams pool for Amazon Chime SDK media stream pipelines](create-kvs-pool.md), in this section.

```
{
    "version": "0",
    "id": "5ee6265a-0a40-104e-d8fd-a3b4bdd78483",
    "detail-type": "Chime Media Pipeline Kinesis Video Pool State Change",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{2021-07-28T20:20:49Z}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "eventType": "chime:MediaPipelineKinesisVideoStreamPoolDeleted",
        "timestamp": {{1627503649251}},
        "mediaRegion": "{{ap-southeast-1}}",
        "poolArn" : "{{ARN of the KVS Pool}}"
    }
 }
```

## Amazon Chime Media Pipeline Kinesis Video Pool Temporary Failure
<a name="kvs-pool-temp-failure"></a>

The media pipeline sends the following event to Event Bridge when a video pool fails temporarily.

```
{
    "version": "0",
    "id": "5ee6265a-0a40-104e-d8fd-a3b4bdd78483",
    "detail-type": "Chime Media Pipeline Kinesis Video Pool State Change",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{2021-07-28T20:20:49Z}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "eventType": "chime:MediaPipelineKinesisVideoStreamPoolTemporaryFailure",
        "timestamp": {{1627503649251}},
        "mediaRegion": "{{ap-southeast-1}}",
        "poolArn" : "{{ARN of the KVS Pool}}"
    }
 }
```

## Amazon Chime Media Pipeline Kinesis Video Pool Permanent Failure
<a name="kvs-pool-perm-failure"></a>

The media pipeline sends the following event to Event Bridge when a video pool fails permanently.

```
{
    "version": "0",
    "id": "5ee6265a-0a40-104e-d8fd-a3b4bdd78483",
    "detail-type": "Chime Media Pipeline Kinesis Video Pool State Change",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{2021-07-28T20:20:49Z}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "eventType": "chime:MediaPipelineKinesisVideoStreamPoolPermanentFailure",
        "timestamp": {{1627503649251}},
        "mediaRegion": "{{ap-southeast-1}}",
        "poolArn" : "{{ARN of the KVS Pool}}"
    }
}
```

You will receive the following additional media pipeline event if your AWS account has exceeded its Amazon Kinesis video stream limit.

```
{
    "version": "0",
    "id": "5ee6265a-0a40-104e-d8fd-a3b4bdd78483",
    "detail-type": "Chime Media Pipeline Kinesis Video Pool State Change",
    "source": "aws.chime",
    "account": "{{111122223333}}",
    "time": "{{2021-07-28T20:20:49Z}}",
    "region": "{{us-east-1}}",
    "resources": [],
    "detail": {
        "eventType": "chime:MediaPipelineKinesisVideoStreamPoolStreamLimitExceeded",
        "timestamp": {{1627503649251}},
        "mediaRegion": "{{ap-southeast-1}}",
        "poolArn" : "{{ARN of the KVS Pool}}"
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
