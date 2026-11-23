---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/sqs-message-operations.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Work with Amazon SQS messages

A *message* is data that one component sends to an [Amazon SQS queue](sqs-queue-operations.md) and another component receives from it.

The following examples use the `client` from [Set up the examples](services-sqs.md#sqs-shared-setup). The identity that runs the examples needs the `sqs:SendMessage`, `sqs:ReceiveMessage`, and `sqs:DeleteMessage` permissions on the queue. The batch operations use the same permissions as the single-message operations.

## Send a message
<a name="sqs-send-message"></a>

For request and response details, see the [send\_message()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sqs/operations/send_message/) API reference.

Send a message to a queue URL with `send_message`. Message attributes carry structured metadata separately from the message body.

 **Imports**

```python
from aws_sdk_sqs import SQSClient
```

 **Code**

```python
def send_message(
    client: SQSClient, queue_url: str, message_body: str
) -> str:
    """Send one message and return its service-assigned ID."""
    response = client.send_message(
        queue_url=queue_url,
        message_body=message_body,
        message_attributes={
            "event_type": {
                "data_type": "String",
                "string_value": "order-created",
            },
            "priority": {"data_type": "Number", "string_value": "7"},
        },
    )
    if not response.message_id:
        raise RuntimeError("SQS did not return a message ID")
    return response.message_id
```

## Receive messages
<a name="sqs-receive-messages"></a>

For request and response details, see the [receive\_message()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sqs/operations/receive_message/) API reference.

Receive up to 10 messages with `receive_message`. An empty response is valid, so poll with a bounded number of attempts or until your application shuts down. The response includes message attributes only when the request names them. This example requests all of them. To wait for messages instead of returning immediately, see [Configure long polling for Amazon SQS](sqs-long-polling.md).

 **Imports**

```python
from aws_sdk_sqs import SQSClient
from aws_sdk_sqs.models import Message
```

 **Code**

```python
def receive_messages(
    client: SQSClient, queue_url: str, attempts: int = 3
) -> list[Message]:
    """Receive up to ten messages, stopping after the first nonempty response."""
    messages: list[Message] = []
    for _ in range(attempts):
        response = client.receive_message(
            queue_url=queue_url,
            max_number_of_messages=10,
            message_attribute_names=["All"],
        )
        messages = response.messages or []
        if messages:
            break
    return messages
```

## Delete a message
<a name="sqs-delete-message"></a>

For request and response details, see the [delete\_message()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sqs/operations/delete_message/) API reference.

Receiving a message hides it for the visibility timeout but doesn't remove it from the queue. Process the message first. Call this function only after processing succeeds. Pass the receipt handle from the most recent receive.

 **Imports**

```python
from aws_sdk_sqs import SQSClient
```

 **Code**

```python
def delete_message(
    client: SQSClient, queue_url: str, receipt_handle: str
) -> None:
    """Delete one message delivery after successful processing."""
    client.delete_message(
        queue_url=queue_url,
        receipt_handle=receipt_handle,
    )
```

## Send and delete messages in batches
<a name="sqs-batch-operations"></a>

For request and response details, see the [send\_message\_batch()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sqs/operations/send_message_batch/) and [delete\_message\_batch()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sqs/operations/delete_message_batch/) API references.

Use `send_message_batch` to send up to 10 entries to one queue. Entry IDs must be unique within the request. A successful request might still report failed entries in `failed`, so match each failure to its entry ID before you retry that entry. This example raises an error if any entry fails.

 **Imports**

```python
from aws_sdk_sqs import SQSClient
```

 **Code**

```python
def send_message_batch(
    client: SQSClient, queue_url: str, message_bodies: list[str]
) -> None:
    """Send a message batch and raise if any entry fails."""
    if not 1 <= len(message_bodies) <= 10:
        raise ValueError("A message batch must contain between 1 and 10 entries")
    response = client.send_message_batch(
        queue_url=queue_url,
        entries=[
            {"id": f"message-{index}", "message_body": body}
            for index, body in enumerate(message_bodies)
        ],
    )
    if response.failed:
        details = ", ".join(
            f"{failure.id}: {failure.code}" for failure in response.failed
        )
        raise RuntimeError(f"SQS batch send failed: {details}")
```

After you process the messages, delete them with `delete_message_batch` by passing their receipt handles. Check `failed` in the response, as you do for a batch send.

 **Imports**

```python
from aws_sdk_sqs import SQSClient
```

 **Code**

```python
def delete_message_batch(
    client: SQSClient, queue_url: str, receipt_handles: list[str]
) -> None:
    """Delete a message batch and raise if any entry fails."""
    if not 1 <= len(receipt_handles) <= 10:
        raise ValueError("A delete batch must contain between 1 and 10 entries")
    response = client.delete_message_batch(
        queue_url=queue_url,
        entries=[
            {"id": f"delete-{index}", "receipt_handle": receipt_handle}
            for index, receipt_handle in enumerate(receipt_handles)
        ],
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
