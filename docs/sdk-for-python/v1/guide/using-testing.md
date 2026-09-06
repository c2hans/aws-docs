---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/using-testing.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Testing applications that use the SDK
<a name="using-testing"></a>

A well-structured test suite clearly distinguishes what the application owns versus what the SDK handles. Your tests should verify that application code constructs the right requests, interprets responses correctly, and recovers from expected errors, without reimplementing serialization, signing, or transport logic. This page presents three testing patterns, from the fastest and most isolated (operation mocks) to the most realistic (integration tests).

Choose the narrowest boundary that verifies the behavior your application owns:
+ Mock a client operation to test application request construction, response handling, and error paths.
+ Inject a mock HTTP transport when application behavior must run through the generated client pipeline without making a network request.
+ Use an integration test when application behavior depends on service-side state or validation.

The examples use pytest with pytest-asyncio. Mark asynchronous tests with `pytest.mark.asyncio`, or configure pytest-asyncio with `asyncio_mode = auto`. Keep application logic in functions that receive a client so each test can supply the appropriate client implementation.

## Mocking an asynchronous operation
<a name="using-testing-async-mock"></a>

Use `unittest.mock.AsyncMock` for a fast unit test of how application code calls an SDK operation and handles its modeled output.

```
from unittest.mock import AsyncMock

import pytest

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import ListTablesInput, ListTablesOutput

async def first_table(client: AsyncDynamoDBClient) -> str | None:
    response = await client.list_tables(
        input=ListTablesInput(limit=1)
    )
    return (response.table_names or [None])[0]

@pytest.mark.asyncio
async def test_first_table() -> None:
    client = AsyncMock(spec=AsyncDynamoDBClient)
    client.list_tables.return_value = ListTablesOutput(
        table_names=["Books"]
    )

    assert await first_table(client) == "Books"
    client.list_tables.assert_awaited_once_with(
        input=ListTablesInput(limit=1)
    )
```

This test verifies the application's request and response logic. It intentionally does not test serialization, signing, transport behavior, or service behavior.

## Testing through the generated client
<a name="using-testing-http"></a>

An operation mock replaces the SDK operation and bypasses the generated client's internal processing. A mock HTTP transport keeps the generated client in the test but replaces the component that sends requests over the network. The client still converts the input model into an HTTP request, applies authentication and interceptors, and converts the HTTP response into an output model.

Use `MockHTTPClient` only when the application behavior depends on that client processing. Because this is a low-level test, supply a raw HTTP response with the status, headers, and body required by the service protocol. The following example places that response in the mock transport and supplies the transport when it resolves the configuration.

```
import pytest

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.config import AsyncDynamoDBConfig
from aws_sdk_dynamodb.models import ListTablesInput
from smithy_http.testing import MockHTTPClient

async def first_table(client: AsyncDynamoDBClient) -> str | None:
    response = await client.list_tables(
        input=ListTablesInput(limit=1)
    )
    return (response.table_names or [None])[0]

@pytest.mark.asyncio
async def test_first_table_through_client() -> None:
    transport = MockHTTPClient()
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

The static values in this isolated test are placeholders required by request authentication; the SDK attaches a static credentials resolver for them automatically. Never use placeholder values as application credentials. `MockHTTPClient` is not a modeled service stub or service emulator, and the test is coupled to the service's HTTP protocol. Prefer an operation mock unless the application deliberately customizes or depends on the generated client pipeline.

## Running application integration tests
<a name="using-testing-integration"></a>

Integration tests call application code with a real SDK client and dedicated non-production resources. Use them for application workflows that depend on service-side state transitions, validation, or modeled errors.
+ Pass the client for the non-production test environment into the same functions or classes that receive a mock client in unit tests. Avoid constructing a fixed client inside the application logic.
+ Generate unique resource names so parallel and repeated test runs do not collide.
+ Use pytest fixtures to create the resources required by the application workflow, wait until they are ready, yield them to tests, and delete them in a `finally` block.
+ Assert application-visible outcomes and error-handling behavior, including how application code handles modeled errors returned by the client.
+ Run integration tests separately from unit tests because they require credentials, network access, and additional execution time.

Keep resource setup and cleanup in fixtures so each test remains focused on one application behavior. Wait for asynchronous deletion to finish, and ensure cleanup still runs when setup partially succeeds or a test assertion fails.
