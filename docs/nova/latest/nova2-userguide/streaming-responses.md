---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/streaming-responses.html
---

# Streaming responses
<a name="streaming-responses"></a>

Streaming allows you to receive model responses incrementally as they are generated, providing a more interactive user experience. Both the Converse API and Invoke API support streaming.

## Streaming with ConverseStream
<a name="streaming-converse"></a>

Use `ConverseStream` to receive responses as a stream of events:

```
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.converse_stream(
    modelId='us.amazon.nova-2-lite-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Write a short story about AI.'}]
        }
    ]
)

for event in response['stream']:
    if 'contentBlockDelta' in event:
        delta = event['contentBlockDelta']['delta']
        if 'text' in delta:
            print(delta['text'], end='', flush=True)
```

## Streaming with InvokeModelWithResponseStream
<a name="streaming-invoke"></a>

Use `InvokeModelWithResponseStream` for streaming with the Invoke API:

```
import boto3
import json

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

request_body = {
    'messages': [
        {
            'role': 'user',
            'content': [{'text': 'Explain quantum computing.'}]
        }
    ]
}

response = bedrock.invoke_model_with_response_stream(
    modelId='us.amazon.nova-2-lite-v1:0',
    body=json.dumps(request_body)
)

for event in response['body']:
    chunk = json.loads(event['chunk']['bytes'])
    if 'contentBlockDelta' in chunk:
        delta = chunk['contentBlockDelta']['delta']
        if 'text' in delta:
            print(delta['text'], end='', flush=True)
```

## Stream event types
<a name="streaming-events"></a>

Streaming responses include several event types:
+ `messageStart`: Indicates the start of a message
+ `contentBlockStart`: Indicates the start of a content block
+ `contentBlockDelta`: Contains incremental text or data
+ `contentBlockStop`: Indicates the end of a content block
+ `messageStop`: Indicates the end of the message with stop reason
+ `metadata`: Contains usage information (token counts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
