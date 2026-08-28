---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/pipeline-creation-code.html
---

# Example code for Amazon Chime SDK media stream pipelines
<a name="pipeline-creation-code"></a>

The following examples show how to create media stream pipelines for mixed audio, individual audio, and both. Expand each section to learn more.

## CreateMediaStreamPipeline for mixed audio
<a name="create-mixed-sample"></a>

```
response = client.create_media_stream_pipeline(
    Sources=[
        {
            'SourceType': 'ChimeSdkMeeting',
            'SourceArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:meeting/{{bed804cf-8cf0-4991-9b8d-d1acc2987433}}'
        },
    ],
    Sinks=[
        {
            'SinkArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{foo}}',
            'SinkType': 'KinesisVideoStreamPool',
            'ReservedStreamCapacity': 1,
            'MediaStreamType': 'MixedAudio'
        },
    ],
    ClientRequestToken='{{sample token}}',
    Tags=[
        {
            'Key': '{{sample key}}',
            'Value': '{{sample value}}'
        },
    ]
)
```

**Response**:

```
{
    'MediaStreamPipeline': {
        'MediaPipelineId': '{{45bc79a0-4591-4ebe-a642-d42c4e279f2d}}',
        'MediaPipelineArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline/{{45bc79a0-4591-4ebe-a642-d42c4e279f2d}}',
        'CreatedTimestamp': '{{2023-07-25T21:48:48.265Z}}',
        'UpdatedTimestamp': '{{2023-07-25T21:48:48.376Z}}',
        'Status': 'Initializing',
        'Sources': [
            {
                'SourceType': 'ChimeSdkMeeting',
                'SourceArn': 'arn:aws:chime:{{us-east-1}}:account-ID:meeting/{{bed804cf-8cf0-4991-9b8d-d1acc2987433}}'
            },
        ],
        'Sinks': [
            {
                'SinkArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{foo}}',
                'SinkType': 'KinesisVideoStreamPool',
                'ReservedStreamCapacity': 1,
                'MediaStreamType': 'MixedAudio'
            },
        ]
    }
}
```

## CreateMediaStreamPipeline for individual audio
<a name="create-individual-sample"></a>

```
response = client.create_media_stream_pipeline(
    Sources=[
        {
            'SourceType': 'ChimeSdkMeeting',
            'SourceArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:meeting/{{bed804cf-8cf0-4991-9b8d-d1acc2987433}}'
        },
    ],
    Sinks=[
        {
            'SinkArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{foo}}',
            'SinkType': 'KinesisVideoStreamPool',
            'ReservedStreamCapacity': {{5}},
            'MediaStreamType': 'IndividualAudio'
        },
    ],
    ClientRequestToken='{{sample token}}',
    Tags=[
        {
            'Key': '{{sample key}}',
            'Value': '{{sample value}}'
        },
    ]
)
```

**Response**:

```
{
    'MediaStreamPipeline': {
        'MediaPipelineId': '{{45bc79a0-4591-4ebe-a642-d42c4e279f2d}}',
        'MediaPipelineArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline/{{45bc79a0-4591-4ebe-a642-d42c4e279f2d}}',
        'CreatedTimestamp': '{{2023-07-25T21:48:48.265Z}}',
        'UpdatedTimestamp': '{{2023-07-25T21:48:48.376Z}}',
        'Status': 'Initializing',
        'Sources': [
            {
                'SourceType': 'ChimeSdkMeeting',
                'SourceArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:meeting/{{bed804cf-8cf0-4991-9b8d-d1acc2987433}}'
            },
        ],
        'Sinks': [
            {
                'SinkArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{foo}}',
                'SinkType': 'KinesisVideoStreamPool',
                'ReservedStreamCapacity': {{5}},
                'MediaStreamType': 'IndividualAudio'
            },
        ]
    }
}
```

## CreateMediaStreamPipeline for mixed and individual audio
<a name="create-both-sample"></a>

```
response = client.create_media_stream_pipeline(
    Sources=[
        {
            'SourceType': 'ChimeSdkMeeting',
            'SourceArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:meeting/{{bed804cf-8cf0-4991-9b8d-d1acc2987433}}'
        },
    ],
    Sinks=[
        {
            'SinkArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{foo}}',
            'SinkType': 'KinesisVideoStreamPool',
            'ReservedStreamCapacity': 1,
            'MediaStreamType': 'MixedAudio'
        },
        {
            'SinkArn': 'arn:aws:{{chime:us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{foo}}',
            'SinkType': 'KinesisVideoStreamPool',
            'ReservedStreamCapacity': {{5}},
            'MediaStreamType': 'IndividualAudio'
        },
    ],
    ClientRequestToken='{{sample token}}',
    Tags=[
        {
            'Key': '{{sample key}}',
            'Value': '{{sample value}}'
        },
    ]
)
```

**Response**:

```
{
    'MediaStreamPipeline': {
        'MediaPipelineId': '{{45bc79a0-4591-4ebe-a642-d42c4e279f2d}}',
        'MediaPipelineArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline/{{45bc79a0-4591-4ebe-a642-d42c4e279f2d}}',
        'CreatedTimestamp': '{{2023-07-25T21:48:48.265Z}}',
        'UpdatedTimestamp': '{{2023-07-25T21:48:48.376Z}}',
        'Status': 'Initializing',
        'Sources': [
            {
                'SourceType': 'ChimeSdkMeeting',
                'SourceArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:meeting/{{bed804cf-8cf0-4991-9b8d-d1acc2987433}}'
            },
        ],
        'Sinks': [
            {
                'SinkArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{foo}}',
                'SinkType': 'KinesisVideoStreamPool',
                'ReservedStreamCapacity': 1,
                'MediaStreamType': 'MixedAudio'
            },
            {
                'SinkArn': 'arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{foo}}',
                'SinkType': 'KinesisVideoStreamPool',
                'ReservedStreamCapacity': {{5}},
                'MediaStreamType': 'IndividualAudio'
            },
        ]
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
