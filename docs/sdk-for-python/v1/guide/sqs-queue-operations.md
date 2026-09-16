---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/sqs-queue-operations.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Work with Amazon SQS queues
<a name="sqs-queue-operations"></a>

A *message queue* is the logical container used for sending messages reliably in Amazon Simple Queue Service. There are two types of queues: *standard* and *first-in, first-out* (FIFO). To learn more about queues and the differences between these types, see the [Amazon Simple Queue Service Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html).

The `client` that is used in the following examples can be created from the snippet in [Set up the examples](services-sqs.md#sqs-shared-setup).

## Create a queue
<a name="sqs-create-queue"></a>

For request and response details, see the [create\_queue()](clients/sqs/operations/create_queue/) API reference.

Create a queue with `create_queue`. The response returns the queue URL, which SQS data-plane operations use. To configure long polling when creating a queue, see [Configure long polling for Amazon SQS](sqs-long-polling.md).

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import CreateQueueInput
```

 **Code**

```
async def create_queue(client: AsyncSQSClient, queue_name: str) -> str:
    """Create a queue and return its URL."""
    response = await client.create_queue(
        input=CreateQueueInput(queue_name=queue_name)
    )
    if not response.queue_url:
        raise RuntimeError("SQS did not return a queue URL")
    return response.queue_url
```

## List queues
<a name="sqs-list-queues"></a>

For request and response details, see the [list\_queues()](clients/sqs/operations/list_queues/) API reference.

Use `list_queues` to discover queues by name prefix. Continue with `next_token` until the service returns no token.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import ListQueuesInput
```

 **Code**

```
async def list_queues(client: AsyncSQSClient, prefix: str) -> list[str]:
    """Return every queue URL whose queue name starts with the prefix."""
    queue_urls: list[str] = []
    next_token = None
    while True:
        page = await client.list_queues(
            input=ListQueuesInput(
                queue_name_prefix=prefix,
                next_token=next_token,
            )
        )
        queue_urls.extend(page.queue_urls or [])
        next_token = page.next_token
        if not next_token:
            return queue_urls
```

## Get a queue URL
<a name="sqs-get-queue-url"></a>

For request and response details, see the [get\_queue\_url()](clients/sqs/operations/get_queue_url/) API reference.

If you have a queue name instead of its URL, resolve it with `get_queue_url`.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import GetQueueUrlInput
```

 **Code**

```
async def get_queue_url(client: AsyncSQSClient, queue_name: str) -> str:
    """Return the URL of an existing queue."""
    response = await client.get_queue_url(
        input=GetQueueUrlInput(queue_name=queue_name)
    )
    if not response.queue_url:
        raise RuntimeError("SQS did not return a queue URL")
    return response.queue_url
```

## Get a queue ARN
<a name="sqs-get-queue-arn"></a>

For request and response details, see the [get\_queue\_attributes()](clients/sqs/operations/get_queue_attributes/) API reference.

SQS data-plane operations use the queue URL. Resource policies and service integrations use the same queue's ARN. Retrieve it with `get_queue_attributes`.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import GetQueueAttributesInput
```

 **Code**

```
async def get_queue_arn(client: AsyncSQSClient, queue_url: str) -> str:
    """Return the ARN of an existing queue."""
    response = await client.get_queue_attributes(
        input=GetQueueAttributesInput(
            queue_url=queue_url,
            attribute_names=["QueueArn"],
        )
    )
    queue_arn = (response.attributes or {}).get("QueueArn")
    if not queue_arn:
        raise RuntimeError("SQS did not return the queue ARN")
    return queue_arn
```

## Delete a queue
<a name="sqs-delete-queue"></a>

For request and response details, see the [delete\_queue()](clients/sqs/operations/delete_queue/) API reference.

Delete a temporary queue by URL after its messages and integrations are no longer needed.

 **Imports**

```
from aws_sdk_sqs.client import AsyncSQSClient
from aws_sdk_sqs.models import DeleteQueueInput
```

 **Code**

```
async def delete_queue(client: AsyncSQSClient, queue_url: str) -> None:
    """Delete the queue at the specified URL."""
    await client.delete_queue(input=DeleteQueueInput(queue_url=queue_url))
```

## More information
<a name="sqs-queue-more-info"></a>
+ [CreateQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html) in the Amazon Simple Queue Service API Reference
+ [ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html) in the Amazon Simple Queue Service API Reference
+ [GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html) in the Amazon Simple Queue Service API Reference
+ [GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html) in the Amazon Simple Queue Service API Reference
+ [DeleteQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html) in the Amazon Simple Queue Service API Reference
