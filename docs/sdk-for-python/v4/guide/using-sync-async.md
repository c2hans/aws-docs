---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/using-sync-async.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Synchronous and asynchronous clients

Every service package of the AWS SDK for Python v4 contains a synchronous client and an asynchronous client. A synchronous client call blocks until the response arrives. An asynchronous client call returns a coroutine that you `await` on an `asyncio` event loop. Both clients take the same keyword arguments and use the same model classes from the package's `models` module.

## Importing and using each client
<a name="using-sync-async-imports"></a>

The synchronous classes are named after the service, such as `S3Client` and `S3Config`. The asynchronous classes have an `Async` prefix, such as `AsyncS3Client` and `AsyncS3Config`. Import the client and configuration classes from the top-level package, such as `from aws_sdk_s3 import S3Client, S3Config`. Import request and response types from the package's `models` module. The following table compares the two DynamoDB clients.

| Task | Synchronous client | Asynchronous client |
| --- | --- | --- |
| Import the client and configuration | from aws\_sdk\_dynamodb import DynamoDBClient, DynamoDBConfig | from aws\_sdk\_dynamodb import AsyncDynamoDBClient, AsyncDynamoDBConfig |
| Resolve the configuration | config = DynamoDBConfig.resolve(region="us-east-1") | config = await AsyncDynamoDBConfig.resolve(region="us-east-1") |
| Open the client in a block | with DynamoDBClient(config=config) as client: | async with AsyncDynamoDBClient(config=config) as client: |
| Call an operation | client.list\_tables(limit=25) | await client.list\_tables(limit=25) |
| Close the client explicitly | client.close() | await client.close() |
| Import models | from aws\_sdk\_dynamodb.models import ... | from aws\_sdk\_dynamodb.models import ... |

Both clients hold network resources until you close them. Leaving the `with` or `async with` block closes the client. If you call an operation on a closed client, the client raises a `RuntimeError`. The following example lists DynamoDB tables with each client.

------
#### [ Synchronous client ]

```python
from aws_sdk_dynamodb import DynamoDBClient, DynamoDBConfig

def main() -> None:
    config = DynamoDBConfig.resolve(region="us-east-1")
    with DynamoDBClient(config=config) as client:
        response = client.list_tables(limit=25)
        print(response.table_names or [])

if __name__ == "__main__":
    main()
```

------
#### [ Asynchronous client ]

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

------

## Choosing a client type
<a name="using-sync-async-choose"></a>

Use the synchronous client for scripts, AWS Lambda function handlers, and code that is already synchronous. It doesn't need an event loop.

Use the asynchronous client if your application already runs on `asyncio`, if it runs many requests concurrently, or if it uses event streams. Event-stream operations exist only on the asynchronous client. For more information, see [Using the SDK asynchronously](using-async.md), [Running concurrent operations](using-concurrency.md), and [Working with event streams](using-streaming.md).

## Using components that match the client mode
<a name="using-sync-async-components"></a>

Some components that you pass to a client have a synchronous form and an asynchronous form. Use components that match the client mode. A synchronous client raises an error when it receives an asynchronous component. An asynchronous client also accepts synchronous credential resolvers and endpoint resolvers.

| Component | Synchronous client | Asynchronous client |
| --- | --- | --- |
| HTTP client | smithy\_http.urllib3.Urllib3HTTPClient | smithy\_http.aio.aiohttp.AIOHTTPClient or smithy\_http.aio.crt.AWSCRTHTTPClient |
| Credential resolvers | Classes in smithy\_aws\_core.identity, such as EnvironmentCredentialsResolver | Classes in smithy\_aws\_core.aio.identity, such as AsyncEnvironmentCredentialsResolver |
| Endpoint resolvers | Implementations of smithy\_core.interfaces.EndpointResolver | Implementations of smithy\_core.aio.interfaces.AsyncEndpointResolver |
| Mock HTTP client for tests | smithy\_http.testing.MockHTTPClient | smithy\_http.aio.testing.AsyncMockHTTPClient |

For more information, see [HTTP configuration](http-configuration.md), [Credential providers](credential-providers.md), [Use a custom endpoint resolver](config-endpoints.md#endpoints-custom-resolver), and [Testing applications that use the SDK](using-testing.md).
