---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/using-testing.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Testing applications that use the SDK

Tests for an application that uses the SDK should verify the behavior that the application owns. They check that application code sends the right requests, interprets responses correctly, and recovers from expected errors. They don't need to test serialization, signing, or transport, because the SDK handles those. This page describes three testing patterns. Operation mocks are the fastest and most isolated. Integration tests are the most realistic.

Choose the narrowest boundary that verifies the behavior your application owns:
+ Mock a client operation to test application request construction, response handling, and error paths.
+ Inject a mock HTTP client when application behavior must run through the generated client pipeline without making a network request.
+ Use an integration test when application behavior depends on service-side state or validation.

The examples use pytest. Where the code differs by client type, the examples show a synchronous version and an asynchronous version. The asynchronous examples also use pytest-asyncio. Mark asynchronous tests with `pytest.mark.asyncio`, or set `asyncio_mode = auto` in the pytest configuration. Keep application logic in functions that receive a client so that each test can supply the appropriate client implementation.

## Mocking client operations
<a name="using-testing-async-mock"></a>

A mock client operation gives you a fast unit test of how application code calls an SDK operation and handles its modeled output. Use `unittest.mock.Mock` for a synchronous client and `unittest.mock.AsyncMock` for an asynchronous client. When you pass the client class as `spec`, accessing an operation that the client doesn't define raises `AttributeError`.

------
#### [ Synchronous client ]

```
from unittest.mock import Mock

from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import ListTablesOutput

def first_table(client: DynamoDBClient) -> str | None:
    response = client.list_tables(limit=1)
    return (response.table_names or [None])[0]

def test_first_table() -> None:
    client = Mock(spec=DynamoDBClient)
    client.list_tables.return_value = ListTablesOutput(
        table_names=["Books"]
    )

    assert first_table(client) == "Books"
    client.list_tables.assert_called_once_with(limit=1)
```

------
#### [ Asynchronous client ]

```
from unittest.mock import AsyncMock

import pytest

from aws_sdk_dynamodb import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import ListTablesOutput

async def first_table(client: AsyncDynamoDBClient) -> str | None:
    response = await client.list_tables(limit=1)
    return (response.table_names or [None])[0]

@pytest.mark.asyncio
async def test_first_table() -> None:
    client = AsyncMock(spec=AsyncDynamoDBClient)
    client.list_tables.return_value = ListTablesOutput(
        table_names=["Books"]
    )

    assert await first_table(client) == "Books"
    client.list_tables.assert_awaited_once_with(limit=1)
```

------

This test verifies the application's request and response logic. It doesn't test serialization, signing, transport behavior, or service behavior.

## Testing through the generated client
<a name="using-testing-http"></a>

An operation mock replaces the SDK operation and bypasses the generated client's internal processing. A mock HTTP client keeps the generated client in the test but replaces the component that sends requests over the network. The client still converts the operation arguments into an HTTP request, applies authentication and interceptors, and converts the HTTP response into an output model.

Use `MockHTTPClient` from `smithy_http.testing` with a synchronous client and `AsyncMockHTTPClient` from `smithy_http.aio.testing` with an asynchronous client. Both classes work the same way:
+ `add_response()` queues a response with a status code, a list of header name and value tuples, and a body in bytes. The mock returns queued responses in the order that you add them.
+ `call_count` is the number of requests that the client sent.
+ `captured_requests` is a list of copies of the HTTP requests that the client sent, for assertions about the request.

If the client sends a request when no response is queued, the mock raises `MockHTTPClientError`. The operation then raises a `SmithyError` whose cause is the `MockHTTPClientError`.

Use a mock HTTP client only when the application behavior depends on the client's processing. Because this is a low-level test, supply a raw HTTP response with the status, headers, and body that the service protocol requires. The following example queues that response in the mock HTTP client and passes the mock as the `transport` when it resolves the configuration.

------
#### [ Synchronous client ]

```
from aws_sdk_dynamodb import DynamoDBClient, DynamoDBConfig
from smithy_http.testing import MockHTTPClient

def first_table(client: DynamoDBClient) -> str | None:
    response = client.list_tables(limit=1)
    return (response.table_names or [None])[0]

def test_first_table_through_client() -> None:
    transport = MockHTTPClient()
    transport.add_response(
        status=200,
        headers=[
            ("content-type", "application/x-amz-json-1.0"),
            ("x-amzn-requestid", "test-request-id"),
        ],
        body=b'{"TableNames":["Books"]}',
    )

    config = DynamoDBConfig.resolve(
        region="us-east-1",
        aws_access_key_id="TEST_ONLY",
        aws_secret_access_key="TEST_ONLY",
        transport=transport,
    )
    with DynamoDBClient(config=config) as client:
        assert first_table(client) == "Books"
        assert transport.call_count == 1
```

------
#### [ Asynchronous client ]

```
import pytest

from aws_sdk_dynamodb import AsyncDynamoDBClient, AsyncDynamoDBConfig
from smithy_http.aio.testing import AsyncMockHTTPClient

async def first_table(client: AsyncDynamoDBClient) -> str | None:
    response = await client.list_tables(limit=1)
    return (response.table_names or [None])[0]

@pytest.mark.asyncio
async def test_first_table_through_client() -> None:
    transport = AsyncMockHTTPClient()
    transport.add_response(
        status=200,
        headers=[
            ("content-type", "application/x-amz-json-1.0"),
            ("x-amzn-requestid", "test-request-id"),
        ],
        body=b'{"TableNames":["Books"]}',
    )

    config = await AsyncDynamoDBConfig.resolve(
        region="us-east-1",
        aws_access_key_id="TEST_ONLY",
        aws_secret_access_key="TEST_ONLY",
        transport=transport,
    )
    async with AsyncDynamoDBClient(config=config) as client:
        assert await first_table(client) == "Books"
        assert transport.call_count == 1
```

------

Request signing requires credentials, so the test passes placeholder values. When you set both `aws_access_key_id` and `aws_secret_access_key`, the SDK creates a static credentials resolver for them. Never use placeholder values as application credentials.

A mock HTTP client isn't a modeled service stub or a service emulator. The test depends on the service's HTTP protocol. Prefer an operation mock unless the application deliberately customizes or depends on the generated client pipeline.

## Running application integration tests
<a name="using-testing-integration"></a>

Integration tests call application code with a real SDK client and dedicated non-production resources. Use them for application workflows that depend on service-side state transitions, validation, or modeled errors.
+ Pass the client for the non-production test environment into the same functions or classes that receive a mock client in unit tests. Avoid constructing a fixed client inside the application logic.
+ Generate unique resource names so that parallel and repeated test runs don't collide.
+ Use pytest fixtures to create the resources that the application workflow requires, wait until they are ready, yield them to tests, and delete them in a `finally` block.
+ Assert application-visible outcomes and error-handling behavior, including how application code handles modeled errors returned by the client.
+ Run integration tests separately from unit tests because they require credentials, network access, and additional execution time.

Keep resource setup and cleanup in fixtures so that each test stays focused on one application behavior. Some resources, such as DynamoDB tables, finish deleting after the delete call returns. Wait for deletion to finish. Make sure that cleanup still runs when setup partially succeeds or a test assertion fails.
