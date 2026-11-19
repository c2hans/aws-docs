---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/services-dynamodb.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Amazon DynamoDB

[Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a serverless NoSQL database service. This section has runnable examples for common DynamoDB tasks. The examples create tables, read and write items, run queries and scans, and group writes and reads in batches and transactions.

Install the `aws-sdk-dynamodb` package before you run the examples.

```
python -m pip install aws-sdk-dynamodb
```

## Set up the examples
<a name="dynamodb-shared-setup"></a>

The examples on the following pages use a `client` that the following `create_client()` function returns. Call it in a `with` statement, such as `with create_client() as client:`, or call `client.close()` after the last operation, as described in [Creating a service client](using-requests.md#using-requests-client).

Configure an AWS Region and credentials before you run the examples. For more information, see [Configuration variables](configuration-variables.md) and [Credential providers](credential-providers.md).

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient, DynamoDBConfig
```

 **Code**

```
def create_client() -> DynamoDBClient:
    config = DynamoDBConfig.resolve()
    return DynamoDBClient(config=config)
```

**Topics**
+ [Set up the examples](#dynamodb-shared-setup)
+ [Work with DynamoDB tables](dynamodb-tables.md)
+ [Work with DynamoDB items](dynamodb-item-operations.md)
+ [Query DynamoDB items](dynamodb-query-operations.md)
+ [Use DynamoDB batch operations and transactions](dynamodb-grouped-operations.md)
