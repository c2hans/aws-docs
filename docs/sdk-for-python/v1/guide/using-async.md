---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/using-async.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Using the SDK asynchronously
<a name="using-async"></a>

Some AWS service requests spend significant time waiting on network I/O, such as streaming responses, batch writes, or calls to geographically distant endpoints. The SDK's asynchronous clients let your application continue running while these requests wait for responses. These asynchronous operations are currently the only form of operation that the SDK provides.

Calling an asynchronous operation creates a *coroutine*: an object that represents work that runs only when you await it. While one coroutine awaits, the event loop can run other operations. Running independent operations concurrently reduces the impact of network latency and improves throughput. This page explains how to await SDK operations, start asynchronous code from different entry points, and avoid common pitfalls.

## Understanding coroutines and await
<a name="using-async-coroutines"></a>

Calling an asynchronous client method creates a coroutine but does not send the request. Awaiting the coroutine starts the operation and pauses only the current coroutine until the response is ready; it does not block the entire event loop.

```
async def table_names(
    client: AsyncDynamoDBClient,
) -> list[str]:
    operation = client.list_tables(
        input=ListTablesInput(limit=25)
    )
    # No request has been sent yet. Awaiting starts the operation.
    response = await operation
    return response.table_names or []
```

To start multiple independent operations before awaiting their results, schedule them as tasks as described in [Running concurrent operations](using-concurrency.md).

## Running asynchronous code
<a name="using-async-run"></a>

Starting a coroutine depends on who owns the application's event loop. A standalone script creates the loop at its synchronous entry point, while an asynchronous framework or interactive environment provides a loop for your code.

### Starting from a script
<a name="using-async-entry-point"></a>

Use `asyncio.run()` once at the synchronous entry point of a script. Create the client inside the asynchronous application flow and await its operations.

```
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.config import AsyncDynamoDBConfig
from aws_sdk_dynamodb.models import ListTablesInput

async def main() -> None:
    config = await AsyncDynamoDBConfig.resolve(region="us-east-1")
    async with AsyncDynamoDBClient(config=config) as client:
        response = await client.list_tables(
            input=ListTablesInput(limit=25)
        )
        print(response.table_names or [])

if __name__ == "__main__":
    asyncio.run(main())
```

### Running inside an existing event loop
<a name="using-async-existing-loop"></a>

When an asynchronous framework invokes your handler, the framework already owns the event loop. Define an asynchronous handler and await SDK operations from it instead of calling `asyncio.run()` again.

```
async def handle_request(
    client: AsyncDynamoDBClient,
) -> dict[str, list[str]]:
    response = await client.list_tables(
        input=ListTablesInput(limit=25)
    )
    return {"table_names": response.table_names or []}
```

Interactive environments such as Jupyter notebooks also provide an event loop and support top-level `await`. In a notebook cell, call a coroutine directly, such as the `handle_request` function above: `result = await handle_request(client)`.

## Using asynchronous operations correctly
<a name="using-async-gotchas"></a>

### Awaiting or scheduling SDK operations
<a name="using-async-await-operations"></a>

Every coroutine returned by an SDK operation must be awaited directly or scheduled as a task that the application later awaits. If neither happens, the request is not sent.

```
# Incorrect: the request is not sent.
response = client.list_tables(input=ListTablesInput(limit=25))

# Correct: awaiting the coroutine sends the request.
response = await client.list_tables(
    input=ListTablesInput(limit=25)
)
```

### Keeping blocking work off the event loop
<a name="using-async-blocking-work"></a>

A blocking library call pauses every task on the event loop. When no asynchronous alternative exists, move the blocking call to a worker thread with `asyncio.to_thread()`.

```
from pathlib import Path

def read_template(path: Path) -> str:
    return path.read_text()

template = await asyncio.to_thread(
    read_template, Path("request-template.json")
)
```

### Closing event streams
<a name="using-async-stream-cleanup"></a>

A non-streaming operation returns a fully deserialized response, so application code has no response resource to close. An event-streaming operation remains open while events are received; close it with its asynchronous context manager as described in [Working with event streams](using-streaming.md).
