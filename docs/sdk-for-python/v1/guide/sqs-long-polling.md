---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/sqs-long-polling.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Configure long polling for Amazon SQS
<a name="sqs-long-polling"></a>

Long polling waits for a message to become available instead of returning immediately. Configure it at two levels: set `ReceiveMessageWaitTimeSeconds` as the queue default, or set `wait_time_seconds` on an individual `receive_message` request. A request-level value overrides the queue default.

The `client` that is used in the following examples can be created from the snippet in [Set up the examples](services-sqs.md#sqs-shared-setup).

Queue attribute values are strings. Valid values for `ReceiveMessageWaitTimeSeconds` are `"0"` through `"20"`. Values greater than `"0"` enable long polling, and `"0"` uses short polling. The corresponding request-level values are integers from `0` through `20`.

## Enable long polling when creating a queue
<a name="sqs-long-polling-create"></a>

For request and response details, see the [create\_queue()](clients/sqs/operations/create_queue/) API reference.

Set `ReceiveMessageWaitTimeSeconds` in the queue attributes to establish the default when the queue is created.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import CreateQueueInput
```

 **Code**

```
async def create_long_polling_queue(
    client: AsyncSQSClient, queue_name: str, wait_time_seconds: int = 20
) -> str:
    """Create a queue with a default long-poll wait and return its URL."""
    if not 0 <= wait_time_seconds <= 20:
        raise ValueError("The long-poll wait must be between 0 and 20 seconds")
    response = await client.create_queue(
        input=CreateQueueInput(
            queue_name=queue_name,
            attributes={
                "ReceiveMessageWaitTimeSeconds": str(wait_time_seconds)
            },
        )
    )
    if not response.queue_url:
        raise RuntimeError("SQS did not return a queue URL")
    return response.queue_url
```

## Enable long polling on an existing queue
<a name="sqs-long-polling-existing"></a>

For request and response details, see the [set\_queue\_attributes()](clients/sqs/operations/set_queue_attributes/) API reference.

Use `set_queue_attributes` to change the default for an existing queue. Queue attribute changes can take up to 60 seconds to propagate.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import SetQueueAttributesInput
```

 **Code**

```
async def set_long_polling(
    client: AsyncSQSClient, queue_url: str, wait_time_seconds: int = 20
) -> None:
    """Set the queue's default receive wait time."""
    if not 0 <= wait_time_seconds <= 20:
        raise ValueError("The long-poll wait must be between 0 and 20 seconds")
    await client.set_queue_attributes(
        input=SetQueueAttributesInput(
            queue_url=queue_url,
            attributes={"ReceiveMessageWaitTimeSeconds": str(wait_time_seconds)},
        )
    )
```

## Enable long polling for a receive request
<a name="sqs-long-polling-request"></a>

For request and response details, see the [receive\_message()](clients/sqs/operations/receive_message/) API reference.

Set `wait_time_seconds` on `receive_message` to configure one request. Ensure that the client's response timeout is longer than the wait time. An empty response is still valid when the wait time expires.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import Message, ReceiveMessageInput
```

 **Code**

```
async def receive_with_long_polling(
    client: AsyncSQSClient, queue_url: str, wait_time_seconds: int = 20
) -> list[Message]:
    """Receive up to ten messages using a request-specific wait time."""
    if not 0 <= wait_time_seconds <= 20:
        raise ValueError("The long-poll wait must be between 0 and 20 seconds")
    response = await client.receive_message(
        input=ReceiveMessageInput(
            queue_url=queue_url,
            max_number_of_messages=10,
            wait_time_seconds=wait_time_seconds,
        )
    )
    return response.messages or []
```

## More information
<a name="sqs-long-polling-more-info"></a>
+ [Amazon SQS short and long polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html) in the Amazon Simple Queue Service Developer Guide
+ [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html) in the Amazon Simple Queue Service API Reference
+ [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) in the Amazon Simple Queue Service API Reference
