---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/pool-creation-code.html
---

# Example code for Kinesis Video Streams pools for Amazon Chime SDK media stream pipelines
<a name="pool-creation-code"></a>

The following examples show how to create, update, get, list, and delete Kinesis Video Streams (KVS) pools. Expand each section to learn more.

## Imports and common variables
<a name="imports-variables"></a>

```
'''
Define imports and common variables
'''

import boto3
from uuid import {{uuid4}}
import json

client = boto3.client("chime-sdk-media-pipelines", region_name='{{us-east-1}}')
pool_name = '{{MyDemoKvsPool}}'

def pretty_print_json(obj):
    print(json.dumps(obj, default=str, indent=4))
```

## CreateMediaPipelineKinesisVideoStreamPool
<a name="create-stream-sample"></a>

```
response = client.create_media_pipeline_kinesis_video_stream_pool(
        StreamConfiguration={
            'Region': '{{us-east-1}}',
            'DataRetentionInHours': {{24}}
        },
        PoolName={{pool_name}},
        ClientRequestToken=str({{uuid4}}()),
        Tags=[
            {
                'Key': '{{MyTagForAccessControl}}',
                'Value': '{{SomeTagValue}}'
            },
        ]
)

pretty_print_json(response['KinesisVideoStreamPoolConfiguration']){{}}
```

**Output**:

```
{
    "PoolArn": "arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{MyDemoKvsPool}}",
    "PoolName": "{{MyDemoKvsPool}}",
    "PoolId": "ChimeMediaPipelines-{{MyDemoKvsPool}}-{{1f4e1a69-e718-4884-bf92-8a393ac0405b}}",
    "PoolStatus": "CREATING",
    "StreamConfiguration": {
        "Region": "{{us-east-1}}",
        "DataRetentionInHours": {{24}}
    },
    "CreatedTimestamp": "{{2023-10-13 01:26:09.979000+00:00}}",
    "UpdatedTimestamp": "{{2023-10-13 01:26:09.979000+00:00}}"
}
```

## GetMediaPipelineKinesisVideoStream
<a name="get-stream-sample"></a>

```
response = client.get_media_pipeline_kinesis_video_stream_pool(
        Identifier={{pool_name}}
)

pretty_print_json(response['KinesisVideoStreamPoolConfiguration'])
```

**Output**:

```
{
    "PoolArn": "arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{MyDemoKvsPool}}",
    "PoolName": "{{MyDemoKvsPool}}",
    "PoolId": "ChimeMediaPipelines-{{MyDemoKvsPool}}-{{1f4e1a69-e718-4884-bf92-8a393ac0405b}}",
    "PoolStatus": "ACTIVE",
    "StreamConfiguration": {
        "Region": "{{us-east-1}}",
        "DataRetentionInHours": {{24}}
    },
    "CreatedTimestamp": "{{2023-10-13 01:26:09.979000+00:00}}",
    "UpdatedTimestamp": "{{2023-10-13 01:26:09.979000+00:00}}"
}
```

## UpdateMediaPipelineKinesisVideoStream
<a name="update-stream-sample"></a>

```
response = client.update_media_pipeline_kinesis_video_stream_pool(
    Identifier={{pool_name}},
    StreamConfiguration={
        'DataRetentionInHours': {{48}}
    }
)
pretty_print_json(response['KinesisVideoStreamPoolConfiguration'])
```

**Output**:

```
{
    "PoolArn": "arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{MyDemoKvsPool}}",
    "PoolName": "{{MyDemoKvsPool}}",
    "PoolId": "ChimeMediaPipelines-{{MyDemoKvsPool}}-{{d08c26ae-0336-4e2e-acdf-805a7d71b891}}",
    "PoolStatus": "UPDATING",
    "PoolSize": {{40}},
    "StreamConfiguration": {
        "Region": "{{us-east-1}}",
        "DataRetentionInHours": {{48}}
    },
    "CreatedTimestamp": "{{2023-10-13 01:44:23.010000+00:00}}",
    "UpdatedTimestamp": "{{2023-10-13 01:44:28.486000+00:00}}"
}
```

## ListMediaPipelineKinesisVideoStream
<a name="list-stream-sample"></a>

```
list_of_pools = []
max_results = {{100}}
next_token = None
while(True):
    if next_token:
        response = client.list_media_pipeline_kinesis_video_stream_pools(
            NextToken=next_token,
            MaxResults=max_results
        )
    else:
        response = client.list_media_pipeline_kinesis_video_stream_pools(
            MaxResults=max_results
        )

    list_of_pools.extend(response['KinesisVideoStreamPools'])
    next_token = response.get('NextToken')
    if not next_token:
        break
pretty_print_json(list_of_pools)
```

**Output**:

```
[
    {
        "PoolName": "{{MyDemoKvsPool}}",
        "PoolId": "ChimeMediaPipelines-{{MyDemoKvsPool}}-{{6588e703-f046-4288-ba7f-0c03de76a6bb}}",
        "PoolArn": "arn:aws:chime:{{us-east-1}}:{{account-ID}}:media-pipeline-kinesis-video-stream-pool/{{MyDemoKvsPool}}"
    }
]
```

## DeleteMediaPipelineKinesisVideoStream
<a name="delete-stream-sample"></a>

```
client.delete_media_pipeline_kinesis_video_stream_pool(
    Identifier={{pool_name}}
)
```

**Output**: A successful `delete_media_pipeline_kinesis_video_stream_pool` request has no body.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
