---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/services-dynamodb.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Amazon DynamoDB
<a name="services-dynamodb"></a>

This chapter provides runnable examples for common [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) workflows — creating tables, reading and writing items, running queries, and coordinating batch operations and transactions. Each example uses the SDK's asynchronous DynamoDB client with typed inputs and outputs, so you can adapt them to your application without translating from raw JSON. Start here to install the client package and configure shared setup that the remaining pages build on.

Install the DynamoDB client before running the asynchronous examples on this page:

```
python -m pip install aws-sdk-dynamodb
```

## Set up the examples
<a name="dynamodb-shared-setup"></a>

The `client` that is used in the following examples can be created from the following snippet by calling `client = await create_client()` from your asynchronous code. Use the client as an asynchronous context manager, or call `await client.close()` after the last operation, as described in [Creating a service client](using-requests.md#using-requests-client). When you resolve the generated asynchronous configuration with `resolve()`, the SDK reads the AWS Region from standard AWS settings, such as environment variables and shared AWS configuration files. The SDK also reads credentials from the same settings. Configure both before running the examples: if no Region is configured, `resolve()` fails before the client is created, and if no credentials are configured, requests fail when the SDK signs them. For more information about the Region and other settings, see [Configuration variables](configuration-variables.md). For how the SDK finds credentials, see [Credential providers](credential-providers.md).

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.config import AsyncDynamoDBConfig
```

 **Code**

```
async def create_client() -> AsyncDynamoDBClient:
    config = await AsyncDynamoDBConfig.resolve()
    return AsyncDynamoDBClient(config=config)
```

**Topics**
+ [Set up the examples](#dynamodb-shared-setup)
+ [Work with DynamoDB tables](dynamodb-tables.md)
+ [Work with DynamoDB items](dynamodb-item-operations.md)
+ [Query DynamoDB items](dynamodb-query-operations.md)
+ [Use DynamoDB batch operations and transactions](dynamodb-grouped-operations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
