---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/dynamodb-grouped-operations.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use DynamoDB batch operations and transactions
<a name="dynamodb-grouped-operations"></a>

DynamoDB provides two ways to group item writes and reads. A *batch* operation sends up to 25 writes or 100 reads in one request. Each item succeeds or fails independently, so your application must resubmit unprocessed entries. A *transaction* applies up to 100 write actions as a single all-or-nothing unit. For more information, see [DynamoDB transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html) in the Amazon DynamoDB Developer Guide.

The examples on this page use the composite-key table created in [Create a table with a composite primary key](dynamodb-tables.md#dynamodb-create-composite-table). To create the `client` that the following examples use, see [Set up the examples](services-dynamodb.md#dynamodb-shared-setup). The identity that runs the examples needs the `dynamodb:BatchWriteItem`, `dynamodb:BatchGetItem`, and `dynamodb:PutItem` permissions on the table. A transaction doesn't have its own permission. DynamoDB checks the permission for each action in it, such as `dynamodb:PutItem` for a put.

## Write items in a batch
<a name="dynamodb-batch-write"></a>

For request and response details, see the [batch\_write\_item()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/batch_write_item/) API reference.

A successful `batch_write_item` response can still contain unprocessed writes. Resubmit only those writes, cap the number of attempts, and delay between attempts. You can pass the response's `unprocessed_items` value directly as `request_items` on the next call.

 **Imports**

```
import time

from aws_sdk_dynamodb import DynamoDBClient
```

 **Code**

```
def batch_write_items(
    client: DynamoDBClient,
    table_name: str,
    max_attempts: int = 5,
) -> None:
    """Write items with bounded retries for unprocessed writes."""
    response = client.batch_write_item(
        request_items={
            table_name: [
                {
                    "put_request": {
                        "item": {
                            "author": {"s": "John Stiles"},
                            "title": {"s": "Example Systems"},
                        }
                    }
                },
                {
                    "put_request": {
                        "item": {
                            "author": {"s": "Jorge Souza"},
                            "title": {"s": "Structured Examples"},
                        }
                    }
                },
            ]
        }
    )
    attempt = 1
    while response.unprocessed_items:
        if attempt == max_attempts:
            raise RuntimeError("DynamoDB did not process every batch write")
        time.sleep(0.1 * (2**attempt))
        response = client.batch_write_item(
            request_items=response.unprocessed_items
        )
        attempt += 1
```

## Get items in a batch
<a name="dynamodb-batch-get"></a>

For request and response details, see the [batch\_get\_item()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/batch_get_item/) API reference.

`batch_get_item` can also return unprocessed keys. Collect the items from each response. Then pass `unprocessed_keys` as `request_items` on the next call, after a bounded delay. DynamoDB doesn't guarantee the order of returned items, so identify each item by its key.

 **Imports**

```
import time

from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import AttributeValue
```

 **Code**

```
def batch_get_items(
    client: DynamoDBClient,
    table_name: str,
    max_attempts: int = 5,
) -> list[dict[str, AttributeValue]]:
    """Get items with bounded retries for unprocessed keys."""
    response = client.batch_get_item(
        request_items={
            table_name: {
                "keys": [
                    {
                        "author": {"s": "John Stiles"},
                        "title": {"s": "Example Systems"},
                    },
                    {
                        "author": {"s": "Jorge Souza"},
                        "title": {"s": "Structured Examples"},
                    },
                ],
                "consistent_read": True,
            }
        }
    )
    items = list((response.responses or {}).get(table_name, []))
    attempt = 1
    while response.unprocessed_keys:
        if attempt == max_attempts:
            raise RuntimeError("DynamoDB did not process every batch key")
        time.sleep(0.1 * (2**attempt))
        response = client.batch_get_item(
            request_items=response.unprocessed_keys
        )
        items.extend((response.responses or {}).get(table_name, []))
        attempt += 1
    return items
```

## Write items in an idempotent transaction
<a name="dynamodb-transactions"></a>

For request and response details, see the [transact\_write\_items()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/transact_write_items/) API reference.

`transact_write_items` applies all actions as one unit. Generate the client request token once. Reuse that same token only when you retry the identical transaction. DynamoDB then treats the retry as the same request for the duration of its token window.

 **Imports**

```
import uuid

from aws_sdk_dynamodb import DynamoDBClient
```

 **Code**

```
def transact_write_items(
    client: DynamoDBClient,
    table_name: str,
    request_token: str | None = None,
) -> None:
    """Atomically put two books, using one token for identical retries."""
    client.transact_write_items(
        transact_items=[
            {
                "put": {
                    "table_name": table_name,
                    "item": {
                        "author": {"s": "Shirley Rodriguez"},
                        "title": {"s": "Example Numbers"},
                    },
                    "condition_expression": "attribute_not_exists(#author)",
                    "expression_attribute_names": {"#author": "author"},
                }
            },
            {
                "put": {
                    "table_name": table_name,
                    "item": {
                        "author": {"s": "Paulo Santos"},
                        "title": {"s": "Example Orbits"},
                    },
                    "condition_expression": "attribute_not_exists(#author)",
                    "expression_attribute_names": {"#author": "author"},
                }
            },
        ],
        client_request_token=request_token or str(uuid.uuid4()),
    )
```

## More information
<a name="dynamodb-grouped-more-info"></a>
+ [DynamoDB transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html) in the Amazon DynamoDB Developer Guide
+ [BatchWriteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html) in the Amazon DynamoDB API Reference
+ [BatchGetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html) in the Amazon DynamoDB API Reference
+ [TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html) in the Amazon DynamoDB API Reference
