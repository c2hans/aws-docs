---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/dynamodb-query-operations.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Query DynamoDB items

DynamoDB provides two operations for reading multiple items. A *query* finds items by their primary-key values and reads only the items that match the key condition. A *scan* reads every item in the table and applies any filter afterward. Prefer key-based queries. Reserve scans for access patterns that a key can't express. For more information, see [Querying tables in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html) in the Amazon DynamoDB Developer Guide.

The examples on this page use the composite-key table created in [Create a table with a composite primary key](dynamodb-tables.md#dynamodb-create-composite-table). To create the `client` that the following examples use, see [Set up the examples](services-dynamodb.md#dynamodb-shared-setup). The identity that runs the examples needs the `dynamodb:Query` and `dynamodb:Scan` permissions on the table.

## Query by partition key
<a name="dynamodb-query"></a>

For request and response details, see the [query()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/query/) API reference.

Use `query` when you know the partition-key value. The key condition must include equality on the partition key and can also constrain the sort key.

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import AttributeValue
```

 **Code**

```
def query_items(
    client: DynamoDBClient, table_name: str, author: str
) -> list[dict[str, AttributeValue]]:
    """Query one response page by partition-key value."""
    response = client.query(
        table_name=table_name,
        key_condition_expression="#author = :author",
        expression_attribute_names={"#author": "author"},
        expression_attribute_values={":author": {"s": author}},
        consistent_read=True,
    )
    return response.items or []
```

## Paginate a query manually
<a name="dynamodb-query-pagination"></a>

For request and response details, see the [query()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/query/) API reference.

A query can return a partial result. Continue while `last_evaluated_key` is present. Pass that key unchanged as `exclusive_start_key` on the next request.

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import AttributeValue
```

 **Code**

```
def query_items_paginated(
    client: DynamoDBClient,
    table_name: str,
    author: str,
    max_pages: int = 100,
) -> list[dict[str, AttributeValue]]:
    """Query all pages, bounded by ``max_pages``."""
    items: list[dict[str, AttributeValue]] = []
    start_key = None
    for _ in range(max_pages):
        page = client.query(
            table_name=table_name,
            key_condition_expression="#author = :author",
            expression_attribute_names={"#author": "author"},
            expression_attribute_values={":author": {"s": author}},
            exclusive_start_key=start_key,
        )
        items.extend(page.items or [])
        start_key = page.last_evaluated_key
        if not start_key:
            return items
    raise RuntimeError("DynamoDB query exceeded the page limit")
```

## Scan with a filter
<a name="dynamodb-scan"></a>

For request and response details, see the [scan()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/scan/) API reference.

Use `scan` only when a key-based query can't express the access pattern. DynamoDB applies the filter after it reads each page, so the filter doesn't reduce the read capacity that the scan consumes. Continue with `last_evaluated_key` even when a filtered page returns no items.

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import AttributeValue
```

 **Code**

```
def scan_items(
    client: DynamoDBClient,
    table_name: str,
    minimum_year: int,
    max_pages: int = 100,
) -> list[dict[str, AttributeValue]]:
    """Scan filtered pages, bounded by ``max_pages``."""
    items: list[dict[str, AttributeValue]] = []
    start_key = None
    for _ in range(max_pages):
        page = client.scan(
            table_name=table_name,
            filter_expression="#year >= :minimum",
            expression_attribute_names={"#year": "year"},
            expression_attribute_values={
                ":minimum": {"n": str(minimum_year)}
            },
            exclusive_start_key=start_key,
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
