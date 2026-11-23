---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/using-async.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Using the SDK asynchronously

When you use the asynchronous client, your application can run other work while a request waits for a response. This helps with requests that spend most of their time waiting on the network, such as streaming responses, batch writes, and calls to distant endpoints. To compare it with the synchronous client, see [Synchronous and asynchronous clients](using-sync-async.md).

Calling an asynchronous operation creates a *coroutine*, an object that represents work that runs only when you await it. This page explains how to await SDK operations, start asynchronous code from different entry points, and avoid common mistakes.

## Understanding coroutines and await
<a name="using-async-coroutines"></a>

Calling an asynchronous client method creates a coroutine but doesn't send the request. Awaiting the coroutine starts the operation and pauses only the current coroutine until the response is ready. Other tasks on the event loop keep running.

```python
from aws_sdk_dynamodb import AsyncDynamoDBClient

async def table_names(
    client: AsyncDynamoDBClient,
) -> list[str]:
    operation = client.list_tables(limit=25)
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

Call `asyncio.run()` once at the synchronous entry point of a script. Create the client inside the asynchronous application flow and await its operations. If a script doesn't otherwise use `asyncio`, the synchronous client is simpler.

```python
import asyncio

from aws_sdk_dynamodb import AsyncDynamoDBClient, AsyncDynamoDBConfig

async def main() -> None:
    config = await AsyncDynamoDBConfig.resolve(region="us-east-1")
    async with AsyncDynamoDBClient(config=config) as client:
        response = await client.list_tables(limit=25)
        print(response.table_names or [])

if __name__ == "__main__":
    asyncio.run(main())
```

### Running inside an existing event loop
<a name="using-async-existing-loop"></a>

When an asynchronous framework invokes your handler, the framework already owns the event loop. Define an asynchronous handler and await SDK operations from it instead of calling `asyncio.run()` again.

```python
async def handle_request(
    client: AsyncDynamoDBClient,
) -> dict[str, list[str]]:
    response = await client.list_tables(limit=25)
    return {"table_names": response.table_names or []}
```

Interactive environments such as Jupyter notebooks also provide an event loop and support top-level `await`. In a notebook cell, await the coroutine directly, such as `result = await handle_request(client)` for the preceding `handle_request` function.

## Using asynchronous operations correctly
<a name="using-async-gotchas"></a>

### Awaiting or scheduling SDK operations
<a name="using-async-await-operations"></a>

Await each coroutine that an SDK operation returns, or schedule it as a task that the application awaits later. Otherwise, the SDK doesn't send the request.

```python
# Incorrect: the request is not sent.
response = client.list_tables(limit=25)

# Correct: awaiting the coroutine sends the request.
response = await client.list_tables(limit=25)
```

### Keeping blocking work off the event loop
<a name="using-async-blocking-work"></a>

A blocking library call pauses every task on the event loop. A call on a synchronous SDK client also blocks, so use the asynchronous client in asynchronous code. When a library has no asynchronous alternative, move the blocking call to a worker thread with `asyncio.to_thread()`.

```python
import asyncio
from pathlib import Path

def read_template(path: Path) -> str:
    return path.read_text()

async def load_template() -> str:
    return await asyncio.to_thread(
        read_template, Path("request-template.json")
    )
```

### Closing event streams
<a name="using-async-stream-cleanup"></a>

An operation that doesn't stream its response returns a fully deserialized response, so your code has no response resource to close. An event-stream operation stays open while you receive events. Close it with its asynchronous context manager, as described in [Working with event streams](using-streaming.md).
