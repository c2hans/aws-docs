---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/sqs-queue-operations.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Work with Amazon SQS queues

In Amazon SQS, a *message queue* holds the messages that one component sends until another component receives and deletes them. Amazon SQS has two queue types: *standard* and *first-in, first-out* (FIFO). To learn more about queues and the differences between the two types, see the [Amazon Simple Queue Service Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html).

The following examples use the `client` from [Set up the examples](services-sqs.md#sqs-shared-setup). The identity that runs the examples needs the `sqs:CreateQueue`, `sqs:ListQueues`, `sqs:GetQueueUrl`, `sqs:GetQueueAttributes`, and `sqs:DeleteQueue` permissions.

## Create a queue
<a name="sqs-create-queue"></a>

For request and response details, see the [create\_queue()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sqs/operations/create_queue/) API reference.

Create a queue with `create_queue`. The response contains the queue URL. Message operations, such as `send_message` and `receive_message`, identify the queue by this URL. To configure long polling when you create a queue, see [Configure long polling for Amazon SQS](sqs-long-polling.md).

 **Imports**

```
from aws_sdk_sqs import SQSClient
```

 **Code**

```
def create_queue(client: SQSClient, queue_name: str) -> str:
    """Create a queue and return its URL."""
    response = client.create_queue(queue_name=queue_name)
    if not response.queue_url:
        raise RuntimeError("SQS did not return a queue URL")
    return response.queue_url
```

## List queues
<a name="sqs-list-queues"></a>

For request and response details, see the [list\_queues()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sqs/operations/list_queues/) API reference.

Use `list_queues` to find queues by name prefix. Pass the returned `next_token` to the next call until the response has no token.

 **Imports**

```
from aws_sdk_sqs import SQSClient
```

 **Code**

```
def list_queues(client: SQSClient, prefix: str) -> list[str]:
    """Return every queue URL whose queue name starts with the prefix."""
    queue_urls: list[str] = []
    next_token: str | None = None
    while True:
        page = client.list_queues(
            queue_name_prefix=prefix,
            next_token=next_token,
        )
        queue_urls.extend(page.queue_urls or [])
        next_token = page.next_token
        if not next_token:
            return queue_urls
```

## Get a queue URL
<a name="sqs-get-queue-url"></a>

For request and response details, see the [get\_queue\_url()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sqs/operations/get_queue_url/) API reference.

If you have a queue name instead of its URL, look up the URL with `get_queue_url`.

 **Imports**

```
from aws_sdk_sqs import SQSClient
```

 **Code**

```
def get_queue_url(client: SQSClient, queue_name: str) -> str:
    """Return the URL of an existing queue."""
    response = client.get_queue_url(queue_name=queue_name)
    if not response.queue_url:
        raise RuntimeError("SQS did not return a queue URL")
    return response.queue_url
```

## Get a queue ARN
<a name="sqs-get-queue-arn"></a>

For request and response details, see the [get\_queue\_attributes()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sqs/operations/get_queue_attributes/) API reference.

Message operations identify a queue by its URL. Resource policies and integrations with other AWS services identify the queue by its ARN. Retrieve the ARN with `get_queue_attributes`.

 **Imports**

```
from aws_sdk_sqs import SQSClient
```

 **Code**

```
def get_queue_arn(client: SQSClient, queue_url: str) -> str:
    """Return the ARN of an existing queue."""
    response = client.get_queue_attributes(
        queue_url=queue_url,
        attribute_names=["QueueArn"],
    )
    queue_arn = (response.attributes or {}).get("QueueArn")
    if not queue_arn:
        raise RuntimeError("SQS did not return the queue ARN")
    return queue_arn
```

## Delete a queue
<a name="sqs-delete-queue"></a>

For request and response details, see the [delete\_queue()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/sqs/operations/delete_queue/) API reference.

Delete a queue by its URL when you no longer need it. Deleting a queue also deletes the messages in it.

 **Imports**

```
from aws_sdk_sqs import SQSClient
```

 **Code**

```
def delete_queue(client: SQSClient, queue_url: str) -> None:
    """Delete the queue at the specified URL."""
    client.delete_queue(queue_url=queue_url)
```

## More information
<a name="sqs-queue-more-info"></a>
+ [CreateQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html) in the Amazon Simple Queue Service API Reference
+ [ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html) in the Amazon Simple Queue Service API Reference
+ [GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html) in the Amazon Simple Queue Service API Reference
+ [GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html) in the Amazon Simple Queue Service API Reference
+ [DeleteQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html) in the Amazon Simple Queue Service API Reference
