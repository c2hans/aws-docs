---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/sqs-message-operations.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Work with Amazon SQS messages
<a name="sqs-message-operations"></a>

A *message* is a piece of data that can be sent and received by distributed components. Messages are always delivered using an [SQS queue](sqs-queue-operations.md).

The `client` that is used in the following examples can be created from the snippet in [Set up the examples](services-sqs.md#sqs-shared-setup).

## Send a message
<a name="sqs-send-message"></a>

For request and response details, see the [send\_message()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sqs/operations/send_message/) API reference.

Send a message to a queue URL with `send_message`. Message attributes carry structured metadata separately from the body.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import MessageAttributeValue, SendMessageInput
```

 **Code**

```
async def send_message(
    client: AsyncSQSClient, queue_url: str, message_body: str
) -> str:
    """Send one message and return its service-assigned ID."""
    response = await client.send_message(
        input=SendMessageInput(
            queue_url=queue_url,
            message_body=message_body,
            message_attributes={
                "event_type": MessageAttributeValue(
                    data_type="String", string_value="order-created"
                ),
                "priority": MessageAttributeValue(
                    data_type="Number", string_value="7"
                ),
            },
        )
    )
    if not response.message_id:
        raise RuntimeError("SQS did not return a message ID")
    return response.message_id
```

## Receive messages
<a name="sqs-receive-messages"></a>

For request and response details, see the [receive\_message()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sqs/operations/receive_message/) API reference.

Receive up to 10 messages with `receive_message`. An empty response is valid, so poll with a bounded attempt count or an application shutdown condition. Message attributes are returned only when the request names them; this example requests all of them. To wait for messages instead of returning immediately, see [Configure long polling for Amazon SQS](sqs-long-polling.md).

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import Message, ReceiveMessageInput
```

 **Code**

```
async def receive_messages(
    client: AsyncSQSClient, queue_url: str, attempts: int = 3
) -> list[Message]:
    """Receive up to ten messages, stopping after the first nonempty response."""
    messages: list[Message] = []
    for _ in range(attempts):
        response = await client.receive_message(
            input=ReceiveMessageInput(
                queue_url=queue_url,
                max_number_of_messages=10,
                message_attribute_names=["All"],
            )
        )
        messages = response.messages or []
        if messages:
            break
    return messages
```

## Delete a message
<a name="sqs-delete-message"></a>

For request and response details, see the [delete\_message()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sqs/operations/delete_message/) API reference.

Receiving a message hides it for the visibility timeout but does not remove it. Process the body first, and call this function with the delivery's current receipt handle only after processing succeeds.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import DeleteMessageInput
```

 **Code**

```
async def delete_message(
    client: AsyncSQSClient, queue_url: str, receipt_handle: str
) -> None:
    """Delete one message delivery after successful processing."""
    await client.delete_message(
        input=DeleteMessageInput(
            queue_url=queue_url,
            receipt_handle=receipt_handle,
        )
    )
```

## Send and delete messages in batches
<a name="sqs-batch-operations"></a>

For request and response details, see the [send\_message\_batch()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sqs/operations/send_message_batch/) and [delete\_message\_batch()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/sqs/operations/delete_message_batch/) API references.

Use `send_message_batch` to send up to 10 entries to one queue. Entry IDs must be unique within the request. A successful request can contain per-entry failures, so associate failures with their IDs and retry only appropriate failed entries.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import SendMessageBatchInput, SendMessageBatchRequestEntry
```

 **Code**

```
async def send_message_batch(
    client: AsyncSQSClient, queue_url: str, message_bodies: list[str]
) -> None:
    """Send a message batch and raise if any entry fails."""
    if not 1 <= len(message_bodies) <= 10:
        raise ValueError("A message batch must contain between 1 and 10 entries")
    response = await client.send_message_batch(
        input=SendMessageBatchInput(
            queue_url=queue_url,
            entries=[
                SendMessageBatchRequestEntry(id=f"message-{index}", message_body=body)
                for index, body in enumerate(message_bodies)
            ],
        )
    )
    if response.failed:
        details = ", ".join(
            f"{failure.id}: {failure.code}" for failure in response.failed
        )
        raise RuntimeError(f"SQS batch send failed: {details}")
```

After each message has been processed successfully, use `delete_message_batch` with its receipt handle. Inspect per-entry failures just as you do for a batch send.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import DeleteMessageBatchInput, DeleteMessageBatchRequestEntry
```

 **Code**

```
async def delete_message_batch(
    client: AsyncSQSClient, queue_url: str, receipt_handles: list[str]
) -> None:
    """Delete a message batch and raise if any entry fails."""
    if not 1 <= len(receipt_handles) <= 10:
        raise ValueError("A delete batch must contain between 1 and 10 entries")
    response = await client.delete_message_batch(
        input=DeleteMessageBatchInput(
            queue_url=queue_url,
            entries=[
                DeleteMessageBatchRequestEntry(
                    id=f"delete-{index}", receipt_handle=receipt_handle
                )
                for index, receipt_handle in enumerate(receipt_handles)
            ],
        )
    )
    if response.failed:
        details = ", ".join(
            f"{failure.id}: {failure.code}" for failure in response.failed
        )
        raise RuntimeError(f"SQS batch delete failed: {details}")
```

## More information
<a name="sqs-message-more-info"></a>
+ [Message metadata for Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html) in the Amazon Simple Queue Service Developer Guide
+ [SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) in the Amazon Simple Queue Service API Reference
+ [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) in the Amazon Simple Queue Service API Reference
+ [DeleteMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html) in the Amazon Simple Queue Service API Reference
+ [SendMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html) in the Amazon Simple Queue Service API Reference
+ [DeleteMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessageBatch.html) in the Amazon Simple Queue Service API Reference
