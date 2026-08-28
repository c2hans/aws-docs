---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/working-with-boto3-migration.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Convert Boto3 operations to the AWS SDK for Python
<a name="working-with-boto3-migration"></a>

The AWS SDK for Python is currently in Developer Preview. You can try your existing Boto3 application code with the new SDK to evaluate its asynchronous capabilities, modular packages, and generated types in development and test environments. Do not use the AWS SDK for Python for production workloads.

The two SDKs use separate packages and namespaces, so you can add the AWS SDK for Python alongside Boto3 and try one supported operation or workflow at a time.

What you can do today: Try converting your Boto3 application code to the AWS SDK for Python for prototyping and evaluation. This lets you assess the asynchronous model, generated types, and modular architecture of the new SDK before general availability.

What this page is not: A guide for migrating production deployments. Production workloads should remain on Boto3 until the AWS SDK for Python reaches General Availability.

For guidance on choosing between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

## Before you start
<a name="working-with-boto3-migration-readiness"></a>
+ Check [Supported services](welcome.md#supported-services) for current client availability, then confirm each required operation and generated type in the [AWS SDK for Python API Reference](https://docs.aws.amazon.com/sdk-for-python/v1/reference/). An available client or operation does not by itself establish support for Boto3 Resources, paginators, waiters, transfer utilities, or streaming.
+ Identify the complete workflow to migrate, including its callers, configuration, error handling, tests, and any Boto3-specific features. Review [Key differences](working-with-boto3-differences.md) before changing its API contracts.
+ Keep Boto3 installed alongside the new SDK. Pin the generated service-package versions used by your application and retest when you upgrade them.

## Try an operation
<a name="working-with-boto3-migration-foundation"></a>

1. Add the generated package for the service. Import its asynchronous client, configuration, input and output models, unions, and modeled exceptions.

1. Resolve the generated asynchronous service configuration and pass it to the client. Values held in a Boto3 `Session` or Botocore `Config` object do not transfer to the new client. Both SDKs can independently resolve environment variables and shared AWS files, so verify the effective settings for each implementation.

1. Move the path that calls the new SDK into `async def` functions. A synchronous script can call `asyncio.run()` once at its entry point; code running in an existing event loop must await the migrated function. See [Running asynchronous code](using-async.md#using-async-run).

1. Replace Boto3 keyword arguments and request dictionaries with the generated input model. Use snake-case member names and construct the appropriate generated union variants.

1. Replace response-dictionary access with generated output attributes. Check optional members for `None` and narrow generated unions before reading their values.

1. Replace `ClientError` parsing with generated modeled exceptions where applicable, and account for runtime exceptions raised while preparing, sending, or processing a request. Update tests for the new asynchronous and generated types. See [Handling errors](using-errors.md).

## Example: convert a DynamoDB GetItem operation
<a name="working-with-boto3-migration-example"></a>

This example applies the conversion sequence to one low-level DynamoDB `GetItem` call. Both versions request the same composite primary key with a strongly consistent read.

Before you run the example:
+ Create a DynamoDB table with string partition and sort keys named `author` and `title`.
+ Add an item with `author` set to "Ada Lovelace" and `title` set to "Notes on the Analytical Engine".

### Step 1: Add the service package
<a name="working-with-boto3-migration-install"></a>

Install both packages for side-by-side comparison:

```
python -m pip install boto3 aws-sdk-dynamodb
```

The configured identity needs `dynamodb:GetItem` permission for the table. Use a non-production table while comparing the implementations.

### Step 2: Identify the Boto3 request and response
<a name="working-with-boto3-migration-before"></a>

The original Boto3 code creates the client dynamically, runs the operation synchronously, accepts modeled request names as keyword arguments, and returns nested dictionaries.

```
from typing import Any

import boto3

AUTHOR = "Ada Lovelace"
TITLE = "Notes on the Analytical Engine"

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

The service function and its caller separate the SDK operation from application-level result handling. The conversion changes four SDK-facing parts: client construction, the synchronous boundary, request dictionaries, and response-dictionary access. The not-found message and title validation are application behavior that the migrated version preserves.

### Step 3: Replace the complete operation
<a name="working-with-boto3-migration-after"></a>

The migrated version preserves the same result handling. Its SDK-specific code imports the generated client, asynchronous configuration, input model, and attribute-value union variants; resolves the configuration; awaits `get_item()`; reads the optional `item` output attribute; and narrows the returned title to `AttributeValueS`.

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.config import AsyncDynamoDBConfig
from aws_sdk_dynamodb.models import (
    AttributeValue,
    AttributeValueS,
    GetItemInput,
)

AUTHOR = "Ada Lovelace"
TITLE = "Notes on the Analytical Engine"

async def get_book_with_sdk(
    client: AsyncDynamoDBClient,
    table_name: str,
) -> dict[str, AttributeValue] | None:
    response = await client.get_item(
        GetItemInput(
            table_name=table_name,
            key={
                "author": AttributeValueS(value=AUTHOR),
                "title": AttributeValueS(value=TITLE),
            },
            consistent_read=True,
        )
    )
    return response.item

async def run_sdk(table_name: str, region: str) -> None:
    config = await AsyncDynamoDBConfig.resolve(region=region)
    async with AsyncDynamoDBClient(config=config) as client:
        item = await get_book_with_sdk(client, table_name)
        if item is None:
            print("The book was not found.")
            return

        title = item.get("title")
        if not isinstance(title, AttributeValueS):
            raise RuntimeError("DynamoDB returned no string title")
        print(title.value)
```

The complete example keeps these SDK-specific functions separate from its shared command-line entry point. Code that is already running in an event loop should await `run_sdk()` instead of calling `asyncio.run()`.

### Step 4: Run and compare the implementations
<a name="working-with-boto3-migration-compare"></a>

The complete example uses one shared command-line parser and entry point for both implementations:

```
import argparse
import asyncio

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
        asyncio.run(run_sdk(args.table_name, args.region))

if __name__ == "__main__":
    main()
```

`--implementation boto3` calls the synchronous Boto3 branch directly. `--implementation sdk` starts one event loop for the asynchronous AWS SDK for Python branch.

Run each implementation against the same table, key, and Region:

```
python migrate_boto3_dynamodb.py Books --region us-east-1 --implementation boto3
python migrate_boto3_dynamodb.py Books --region us-east-1 --implementation sdk
```

Both commands should print the same title for the example item and should both report when that item is absent.

## Next steps
<a name="working-with-boto3-migration-next-steps"></a>
+ For guidance on choosing the best path for your application, see [Choosing the right AWS SDK for Python](choosing-sdk.md).
+ For current client availability, see [Supported services](welcome.md#supported-services).
+ For API-model and execution differences, see [Key differences](working-with-boto3-differences.md).
+ For workflows that continue to require both SDKs, see [Use both SDKs in one application](working-with-boto3-coexistence.md).
+ For asynchronous unit and integration testing patterns, see [Testing applications that use the SDK](using-testing.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
