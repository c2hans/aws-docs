---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/working-with-boto3-migration.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Convert AWS SDK for Python (Boto3) operations to the AWS SDK for Python v4

To evaluate the AWS SDK for Python v4, convert Boto3 code in development and test environments. Keep production workloads on Boto3 during the Developer Preview.

The two SDKs use separate packages and namespaces, so you can try one operation or workflow at a time.

For guidance on choosing between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

## Before you start
<a name="working-with-boto3-migration-readiness"></a>
+ Check [Supported services](welcome.md#supported-services) for current client availability, then confirm each required operation and generated type in the [AWS SDK for Python v4 API Reference](https://docs.aws.amazon.com/sdk-for-python/v4/reference/). The SDK doesn't provide paginators, waiters, or transfer utilities yet. Event streams are available only in asynchronous clients.
+ Identify the complete workflow to migrate, including its callers, configuration, error handling, tests, and any Boto3-specific features. Review [Key differences](working-with-boto3-differences.md) before changing its API contracts.
+ Keep Boto3 installed alongside the new SDK. Pin the generated service-package versions used by your application and retest when you upgrade them.

## Try an operation
<a name="working-with-boto3-migration-foundation"></a>

1. Add the generated package for the service. Import its synchronous client and configuration, plus the model classes and modeled exceptions that your code uses.

1. Resolve the generated service configuration with its `resolve()` method and pass it to the client. Values held in a Boto3 `Session` or Botocore `Config` object don't transfer to the new client. Both SDKs can independently resolve environment variables and shared AWS files, so verify the effective settings for each SDK.

1. Keep the synchronous structure of your code. A synchronous client call blocks like a Boto3 call, so you don't need `async def` functions or an event loop. If your application runs on `asyncio`, use the asynchronous client and `await` each call instead. For the differences between the client types, see [Synchronous and asynchronous clients](using-sync-async.md).

1. Rename each Boto3 keyword argument to its snake-case member name, such as `TableName` to `table_name`. Replace nested request dictionaries with generated model objects, including the generated variant for each union value.

1. Replace response-dictionary access with generated output attributes. Check optional members for `None` and narrow generated unions before reading their values.

1. Replace `ClientError` parsing with generated modeled exceptions where applicable. Account for runtime exceptions raised while preparing, sending, or processing a request. Update tests for the generated types. For more information, see [Handling errors](using-errors.md).

## Example: convert a DynamoDB GetItem operation
<a name="working-with-boto3-migration-example"></a>

This example applies the conversion sequence to one low-level DynamoDB `GetItem` call. Both versions request the same composite primary key with a strongly consistent read.

Before you run the example:
+ Create a DynamoDB table with string partition and sort keys named `author` and `title`.
+ Add an item with `author` set to "Mary Major" and `title` set to "Notes on Example Data".

### Step 1: Add the service package
<a name="working-with-boto3-migration-install"></a>

Install both packages for side-by-side comparison:

```bash
python -m pip install boto3 aws-sdk-dynamodb
```

The configured identity needs `dynamodb:GetItem` permission for the table. Use a non-production table while comparing the implementations.

### Step 2: Identify the Boto3 request and response
<a name="working-with-boto3-migration-before"></a>

The original Boto3 code creates the client dynamically, runs the operation synchronously, accepts modeled request names as keyword arguments, and returns nested dictionaries.

```python
from typing import Any

import boto3

AUTHOR = "Mary Major"
TITLE = "Notes on Example Data"

def get_book_with_boto3(
    client: Any,
    table_name: str,
) -> dict[str, Any] | None:
    response = client.get_item(
        TableName=table_name,
        Key={
            "author": {"S": AUTHOR},
            "title": {"S": TITLE},
        },
        ConsistentRead=True,
    )
    return response.get("Item")

def run_boto3(table_name: str, region: str) -> None:
    client = boto3.client("dynamodb", region_name=region)
    item = get_book_with_boto3(client, table_name)
    if item is None:
        print("The book was not found.")
        return

    title = item.get("title", {}).get("S")
    if not isinstance(title, str):
        raise RuntimeError("DynamoDB returned no string title")
    print(title)
```

The conversion changes three parts: client construction, request arguments, and response access.

### Step 3: Replace the complete operation
<a name="working-with-boto3-migration-after"></a>

The converted version uses the synchronous DynamoDB client of the AWS SDK for Python v4 and keeps the same result handling. It imports the generated client, configuration, and attribute-value union types. Then it resolves the configuration. It calls `get_item()` with keyword arguments and passes each key attribute as a dictionary with a snake-case union key, such as `{"s": AUTHOR}`. Then it reads the optional `item` output attribute and narrows the returned title to `AttributeValueS`.

```python
from aws_sdk_dynamodb import DynamoDBClient, DynamoDBConfig
from aws_sdk_dynamodb.models import AttributeValue, AttributeValueS

AUTHOR = "Mary Major"
TITLE = "Notes on Example Data"

def get_book_with_sdk(
    client: DynamoDBClient,
    table_name: str,
) -> dict[str, AttributeValue] | None:
    response = client.get_item(
        table_name=table_name,
        key={
            "author": {"s": AUTHOR},
            "title": {"s": TITLE},
        },
        consistent_read=True,
    )
    return response.item

def run_sdk(table_name: str, region: str) -> None:
    config = DynamoDBConfig.resolve(region=region)
    with DynamoDBClient(config=config) as client:
        item = get_book_with_sdk(client, table_name)
        if item is None:
            print("The book was not found.")
            return

        title = item.get("title")
        if not isinstance(title, AttributeValueS):
            raise RuntimeError("DynamoDB returned no string title")
        print(title.value)
```

The following table shows how each Boto3 part of the request and response maps to the AWS SDK for Python v4.

| AWS SDK for Python (Boto3) | AWS SDK for Python v4 |
| --- | --- |
| TableName=table\_name | table\_name=table\_name |
| Key={"author": {"S": AUTHOR}} | key={"author": {"s": AUTHOR}} |
| ConsistentRead=True | consistent\_read=True |
| response.get("Item") | response.item |
| item.get("title", {}).get("S") | item.get("title"), then check for AttributeValueS and read value |
| except ClientError, then read error.response["Error"]["Code"] | except ResourceNotFoundException or another generated exception class |

For the other accepted argument forms, see [Making requests and handling responses](using-requests.md). For error handling, see [Handling errors](using-errors.md).

### Step 4: Run and compare the implementations
<a name="working-with-boto3-migration-compare"></a>

The complete example uses one shared command-line parser and entry point for both implementations:

```python
import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("table_name")
    parser.add_argument("--region", required=True)
    parser.add_argument(
        "--implementation",
        choices=("boto3", "sdk"),
        default="sdk",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    if args.implementation == "boto3":
        run_boto3(args.table_name, args.region)
    else:
        run_sdk(args.table_name, args.region)

if __name__ == "__main__":
    main()
```

Run each implementation against the same table, key, and Region:

```bash
python migrate_boto3_dynamodb.py Books --region us-east-1 --implementation boto3
python migrate_boto3_dynamodb.py Books --region us-east-1 --implementation sdk
```

Both commands should print the same title for the example item and should both report when that item is absent.

## Next steps
<a name="working-with-boto3-migration-next-steps"></a>
+ For guidance on choosing the best path for your application, see [Choosing the right AWS SDK for Python](choosing-sdk.md).
+ For current client availability, see [Supported services](welcome.md#supported-services).
+ For API-model and execution differences, see [Key differences](working-with-boto3-differences.md).
+ For the differences between synchronous and asynchronous clients, see [Synchronous and asynchronous clients](using-sync-async.md).
+ For workflows that continue to require both SDKs, see [Use both SDKs in one application](working-with-boto3-coexistence.md).
+ For unit and integration testing patterns, see [Testing applications that use the SDK](using-testing.md).
