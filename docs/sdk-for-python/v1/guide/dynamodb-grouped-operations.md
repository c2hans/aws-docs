---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/dynamodb-grouped-operations.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use DynamoDB batch operations and transactions
<a name="dynamodb-grouped-operations"></a>

DynamoDB provides two ways to group item writes and reads. A *batch* operation sends up to 25 writes or 100 reads in one request; each item succeeds or fails independently, so your application must resubmit unprocessed entries. A *transaction* applies up to 100 write actions as a single all-or-nothing unit. For more information, see [DynamoDB transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html) in the Amazon DynamoDB Developer Guide.

The examples on this page use the composite-key table created in [Create a table with a composite primary key](dynamodb-tables.md#dynamodb-create-composite-table). The `client` that is used in the following examples can be created from the snippet in [Set up the examples](services-dynamodb.md#dynamodb-shared-setup).

## Write items in a batch
<a name="dynamodb-batch-write"></a>

For request and response details, see the [batch\_write\_item()](clients/dynamodb/operations/batch_write_item/) API reference.

A successful `batch_write_item` response can still contain unprocessed writes. Resubmit only those writes, cap the number of attempts, and delay between attempts.

 **Imports**

```
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import (
    AttributeValueS,
    BatchWriteItemInput,
    PutRequest,
    WriteRequest,
)
```

 **Code**

```
async def batch_write_items(
    client: AsyncDynamoDBClient,
    table_name: str,
    max_attempts: int = 5,
) -> None:
    """Write items with bounded retries for unprocessed writes."""
    pending = {
        table_name: [
            WriteRequest(
                put_request=PutRequest(
                    item={
                        "author": AttributeValueS(value="Grace Hopper"),
                        "title": AttributeValueS(
                            value="The Education of a Computer"
                        ),
                    }
                )
            ),
            WriteRequest(
                put_request=PutRequest(
                    item={
                        "author": AttributeValueS(value="Edsger Dijkstra"),
                        "title": AttributeValueS(
                            value="Go To Statement Considered Harmful"
                        ),
                    }
                )
            ),
        ]
    }
    for attempt in range(max_attempts):
        response = await client.batch_write_item(
            input=BatchWriteItemInput(request_items=pending)
        )
        pending = response.unprocessed_items or {}
        if not pending:
            return
        await asyncio.sleep(0.2 * (2**attempt))
    raise RuntimeError("DynamoDB did not process every batch write")
```

## Get items in a batch
<a name="dynamodb-batch-get"></a>

For request and response details, see the [batch\_get\_item()](clients/dynamodb/operations/batch_get_item/) API reference.

`batch_get_item` can also return unprocessed keys. Collect each response page, resubmit only those keys with a bounded delay, and identify returned items by key because DynamoDB does not guarantee their order.

 **Imports**

```
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import (
    AttributeValue,
    AttributeValueS,
    BatchGetItemInput,
    KeysAndAttributes,
)
```

 **Code**

```
async def batch_get_items(
    client: AsyncDynamoDBClient,
    table_name: str,
    max_attempts: int = 5,
) -> list[dict[str, AttributeValue]]:
    """Get items with bounded retries for unprocessed keys."""
    pending = {
        table_name: KeysAndAttributes(
            keys=[
                {
                    "author": AttributeValueS(value="Grace Hopper"),
                    "title": AttributeValueS(value="The Education of a Computer"),
                },
                {
                    "author": AttributeValueS(value="Edsger Dijkstra"),
                    "title": AttributeValueS(
                        value="Go To Statement Considered Harmful"
                    ),
                },
            ],
            consistent_read=True,
        )
    }
    items: list[dict[str, AttributeValue]] = []
    for attempt in range(max_attempts):
        response = await client.batch_get_item(
            input=BatchGetItemInput(request_items=pending)
        )
        items.extend((response.responses or {}).get(table_name, []))
        pending = response.unprocessed_keys or {}
        if not pending:
            return items
        await asyncio.sleep(0.2 * (2**attempt))
    raise RuntimeError("DynamoDB did not process every batch key")
```

## Write items in an idempotent transaction
<a name="dynamodb-transactions"></a>

For request and response details, see the [transact\_write\_items()](clients/dynamodb/operations/transact_write_items/) API reference.

`transact_write_items` applies all actions as one unit. Generate the client request token once, and reuse that same token only when retrying the identical transaction. This keeps an identical retry idempotent during DynamoDB's token window.

 **Imports**

```
import uuid

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import (
    AttributeValueS,
    Put,
    TransactWriteItem,
    TransactWriteItemsInput,
)
```

 **Code**

```
async def transact_write_items(
    client: AsyncDynamoDBClient,
    table_name: str,
    request_token: str | None = None,
) -> None:
    """Atomically put two books, using one token for identical retries."""
    request = TransactWriteItemsInput(
        transact_items=[
            TransactWriteItem(
                put=Put(
                    table_name=table_name,
                    item={
                        "author": AttributeValueS(value="Alan Turing"),
                        "title": AttributeValueS(value="On Computable Numbers"),
                    },
                    condition_expression="attribute_not_exists(#author)",
                    expression_attribute_names={"#author": "author"},
                )
            ),
            TransactWriteItem(
                put=Put(
                    table_name=table_name,
                    item={
                        "author": AttributeValueS(value="Katherine Johnson"),
                        "title": AttributeValueS(value="Orbital Mechanics Notes"),
                    },
                    condition_expression="attribute_not_exists(#author)",
                    expression_attribute_names={"#author": "author"},
                )
            ),
        ],
        client_request_token=request_token or str(uuid.uuid4()),
    )
    await client.transact_write_items(input=request)
```

## More information
<a name="dynamodb-grouped-more-info"></a>
+ [DynamoDB transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html) in the Amazon DynamoDB Developer Guide
+ [BatchWriteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html) in the Amazon DynamoDB API Reference
+ [BatchGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html) in the Amazon DynamoDB API Reference
+ [TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html) in the Amazon DynamoDB API Reference
