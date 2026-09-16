---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/using-concurrency.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Running concurrent operations
<a name="using-concurrency"></a>

The [Using the SDK asynchronously](using-async.md) page showed how to await a single operation without blocking the event loop. When your application has multiple independent calls to make, you can go further: schedule them as concurrent tasks so their network wait time overlaps.

This page demonstrates patterns to run multiple operations using existing client APIs or with concurrency primitives provided by Python's `asyncio` library.

## Using service batch operations when available
<a name="using-concurrency-batch"></a>

Before scheduling one SDK call for each input item, check whether the service provides a batch operation. A batch operation is a service API, not a Python concurrency mechanism: it reduces the number of service requests by accepting multiple items in one request. When no suitable batch operation exists, independent SDK calls can make progress concurrently while they wait for service responses.

Examples of batch operations include:
+ **DynamoDB:** [batch\_get\_item()](clients/dynamodb/operations/batch_get_item/) and [batch\_write\_item()](clients/dynamodb/operations/batch_write_item/)
+ **Amazon SQS:** [send\_message\_batch()](clients/sqs/operations/send_message_batch/)

A batch operation isn't necessarily atomic or all-or-nothing. Follow the operation-specific size limits and inspect its modeled response for failed entries or unprocessed work. Resubmit only eligible failed or unprocessed entries, with bounded attempts and a delay between attempts.

When an input exceeds an operation's batch-size limit, divide it into valid batches. If you submit multiple batches concurrently, use [Bounding fan-out for a finite collection](#using-concurrency-bounded) to limit the number of batch requests in flight.

## Running a small number of operations concurrently
<a name="using-concurrency-gather"></a>

When the number of independent operations is small and known before scheduling, and it's appropriate for all of them to be in flight at once, pass their coroutines to `asyncio.gather()`. Awaiting `gather()` lets the operations make progress concurrently and returns successful results in input order.

```
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import DescribeTableInput

async def describe_two_tables(
    client: AsyncDynamoDBClient,
    first_table_name: str,
    second_table_name: str,
):
    responses = await asyncio.gather(
        client.describe_table(
            input=DescribeTableInput(table_name=first_table_name)
        ),
        client.describe_table(
            input=DescribeTableInput(table_name=second_table_name)
        ),
    )
    return [response.table for response in responses]
```

If one operation raises an exception, `gather()` propagates it but doesn't automatically cancel the other operations. If the input size can vary or might be large, use [Bounding fan-out for a finite collection](#using-concurrency-bounded) instead.

## Bounding fan-out for a finite collection
<a name="using-concurrency-bounded"></a>

Fan-out creates one request for each input item. For a finite input collection of manageable size, this pattern uses `gather()` to collect the results and a semaphore to limit how many SDK calls are active at once.

```
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import DescribeTableInput

async def describe_tables_bounded(
    client: AsyncDynamoDBClient,
    table_names: list[str],
    maximum_concurrency: int = 10,
):
    if maximum_concurrency < 1:
        raise ValueError("maximum_concurrency must be at least 1")
    limit = asyncio.Semaphore(maximum_concurrency)

    async def describe(table_name: str):
        async with limit:
            response = await client.describe_table(
                input=DescribeTableInput(table_name=table_name)
            )
            return response.table

    return await asyncio.gather(*(
        describe(name) for name in table_names
    ))
```

The semaphore bounds active SDK calls, but `gather()` still creates and schedules one coroutine for every item in `table_names`. This pattern also has the exception behavior described in the preceding section.

For a very large collection or input that arrives over time, don't pass the entire source to `gather()`. Use a bounded producer and worker pattern instead. For example, a producer can add items to an `asyncio.Queue` with a fixed `maxsize`, and a fixed number of workers can remove items and invoke the SDK operation. The producer waits when the queue is full and reads or generates more input as workers finish. This bounds both active SDK calls and work waiting in memory.

Choose the concurrency or worker limit based on the service quota, operation cost, expected latency, and the application's available memory. Higher concurrency doesn't bypass service quotas and can increase throttling.
