---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/dynamodb-query-operations.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Query DynamoDB items
<a name="dynamodb-query-operations"></a>

DynamoDB provides two operations for reading multiple items. A *query* finds items by their primary-key values and is the efficient access path: it reads only the items that match the key condition. A *scan* reads every item in the table and applies any filter afterward. Prefer key-based queries, and reserve scans for access patterns that a key cannot express. For more information, see [Querying tables in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) in the Amazon DynamoDB Developer Guide.

The examples on this page use the composite-key table created in [Create a table with a composite primary key](dynamodb-tables.md#dynamodb-create-composite-table). The `client` that is used in the following examples can be created from the snippet in [Set up the examples](services-dynamodb.md#dynamodb-shared-setup). Attributes in the returned items are typed `AttributeValue` unions; narrow each one to its concrete model before reading its value, as shown in [Get an item](dynamodb-item-operations.md#dynamodb-get-item).

## Query by partition key
<a name="dynamodb-query"></a>

For request and response details, see the [query()](clients/dynamodb/operations/query/) API reference.

Use `query` when you know the partition-key value. The key condition must include equality on the partition key and can also constrain the sort key.

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import AttributeValue, AttributeValueS, QueryInput
```

 **Code**

```
async def query_items(
    client: AsyncDynamoDBClient, table_name: str, author: str
) -> list[dict[str, AttributeValue]]:
    """Query one response page by partition-key value."""
    response = await client.query(
        input=QueryInput(
            table_name=table_name,
            key_condition_expression="#author = :author",
            expression_attribute_names={"#author": "author"},
            expression_attribute_values={
                ":author": AttributeValueS(value=author)
            },
            consistent_read=True,
        )
    )
    return response.items or []
```

## Paginate a query manually
<a name="dynamodb-query-pagination"></a>

For request and response details, see the [query()](clients/dynamodb/operations/query/) API reference.

A query can return a partial result. Continue while `last_evaluated_key` is present, and pass that key as `exclusive_start_key` on the next request.

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import AttributeValue, AttributeValueS, QueryInput
```

 **Code**

```
async def query_items_paginated(
    client: AsyncDynamoDBClient,
    table_name: str,
    author: str,
    max_pages: int = 100,
) -> list[dict[str, AttributeValue]]:
    """Query all pages, bounded by ``max_pages``."""
    items: list[dict[str, AttributeValue]] = []
    start_key = None
    for _ in range(max_pages):
        page = await client.query(
            input=QueryInput(
                table_name=table_name,
                key_condition_expression="#author = :author",
                expression_attribute_names={"#author": "author"},
                expression_attribute_values={
                    ":author": AttributeValueS(value=author)
                },
                exclusive_start_key=start_key,
            )
        )
        items.extend(page.items or [])
        start_key = page.last_evaluated_key
        if not start_key:
            return items
    raise RuntimeError("DynamoDB query exceeded the page limit")
```

## Scan with a filter
<a name="dynamodb-scan"></a>

For request and response details, see the [scan()](clients/dynamodb/operations/scan/) API reference.

Use `scan` only when a key-based query cannot express the access pattern. A filter is applied after DynamoDB reads each page, so it does not reduce the read capacity consumed. Continue with `last_evaluated_key` even when a filtered page returns no items.

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import AttributeValue, AttributeValueN, ScanInput
```

 **Code**

```
async def scan_items(
    client: AsyncDynamoDBClient,
    table_name: str,
    minimum_year: int,
    max_pages: int = 100,
) -> list[dict[str, AttributeValue]]:
    """Scan filtered pages, bounded by ``max_pages``."""
    items: list[dict[str, AttributeValue]] = []
    start_key = None
    for _ in range(max_pages):
        page = await client.scan(
            input=ScanInput(
                table_name=table_name,
                filter_expression="#year >= :minimum",
                expression_attribute_names={"#year": "year"},
                expression_attribute_values={
                    ":minimum": AttributeValueN(value=str(minimum_year))
                },
                exclusive_start_key=start_key,
            )
        )
        items.extend(page.items or [])
        start_key = page.last_evaluated_key
        if not start_key:
            return items
    raise RuntimeError("DynamoDB scan exceeded the page limit")
```

## More information
<a name="dynamodb-query-more-info"></a>
+ [Querying tables in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) in the Amazon DynamoDB Developer Guide
+ [Scanning tables in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html) in the Amazon DynamoDB Developer Guide
+ [Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html) in the Amazon DynamoDB API Reference
+ [Scan](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html) in the Amazon DynamoDB API Reference
