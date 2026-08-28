---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/dynamodb-item-operations.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Work with DynamoDB items
<a name="dynamodb-item-operations"></a>

In DynamoDB, an item is a collection of *attributes*, each of which has a *name* and a *value*. An attribute value can be a scalar, set, or document type. For more information, see [Naming Rules and Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html) in the Amazon DynamoDB Developer Guide.

The low-level client represents an item as a map of attribute names to typed `AttributeValue` models, such as `AttributeValueS` for a string and `AttributeValueN` for a number. Numbers are strings to preserve decimal precision. Response attributes use the same models, so check the concrete model before reading its `value`, as shown in [Get an item](#dynamodb-get-item).

The examples on this page use the composite-key table created in [Create a table with a composite primary key](dynamodb-tables.md#dynamodb-create-composite-table). The `client` that is used in the following examples can be created from the snippet in [Set up the examples](services-dynamodb.md#dynamodb-shared-setup).

## Put an item
<a name="dynamodb-put-item"></a>

For request and response details, see the [put\_item()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/put_item/) API reference.

Pass a complete map of typed attributes to `put_item`. A put replaces an existing item with the same primary key unless you add a condition.

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import (
    AttributeValueN,
    AttributeValueS,
    PutItemInput,
)
```

 **Code**

```
async def put_item(client: AsyncDynamoDBClient, table_name: str) -> None:
    """Put a book item, replacing any item with the same primary key."""
    await client.put_item(
        input=PutItemInput(
            table_name=table_name,
            item={
                "author": AttributeValueS(value="Ada Lovelace"),
                "title": AttributeValueS(value="Notes on the Analytical Engine"),
                "year": AttributeValueN(value="1843"),
                "copies": AttributeValueN(value="0"),
            },
        )
    )
```

## Get an item
<a name="dynamodb-get-item"></a>

For request and response details, see the [get\_item()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/get_item/) API reference.

Supply every primary-key attribute to `get_item`. This example requests a strongly consistent read and returns the optional item.

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import AttributeValue, AttributeValueS, GetItemInput
```

 **Code**

```
async def get_item(
    client: AsyncDynamoDBClient, table_name: str
) -> dict[str, AttributeValue] | None:
    """Get a book by its complete composite primary key."""
    response = await client.get_item(
        input=GetItemInput(
            table_name=table_name,
            key={
                "author": AttributeValueS(value="Ada Lovelace"),
                "title": AttributeValueS(value="Notes on the Analytical Engine"),
            },
            consistent_read=True,
        )
    )
    return response.item
```

Each returned attribute is a typed `AttributeValue` union. Narrow it to its concrete model before reading its `value`.

```
if item:
    title = item.get("title")
    if isinstance(title, AttributeValueS):
        print(title.value)
```

## Update an item
<a name="dynamodb-update-item"></a>

For request and response details, see the [update\_item()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/update_item/) API reference.

Use an update expression to change selected attributes. Expression-name placeholders safely represent attribute names, and `ALL_NEW` returns the item after the update.

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import (
    AttributeValue,
    AttributeValueN,
    AttributeValueS,
    UpdateItemInput,
)
```

 **Code**

```
async def update_item(
    client: AsyncDynamoDBClient, table_name: str
) -> dict[str, AttributeValue]:
    """Increment a book's copy count and return the updated item."""
    response = await client.update_item(
        input=UpdateItemInput(
            table_name=table_name,
            key={
                "author": AttributeValueS(value="Ada Lovelace"),
                "title": AttributeValueS(value="Notes on the Analytical Engine"),
            },
            update_expression="SET #copies = #copies + :increment",
            expression_attribute_names={"#copies": "copies"},
            expression_attribute_values={
                ":increment": AttributeValueN(value="1")
            },
            return_values="ALL_NEW",
        )
    )
    return response.attributes or {}
```

## Delete an item
<a name="dynamodb-delete-item"></a>

For request and response details, see the [delete\_item()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/delete_item/) API reference.

Delete one item by supplying its complete primary key.

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import AttributeValueS, DeleteItemInput
```

 **Code**

```
async def delete_item(client: AsyncDynamoDBClient, table_name: str) -> None:
    """Delete a book by its complete composite primary key."""
    await client.delete_item(
        input=DeleteItemInput(
            table_name=table_name,
            key={
                "author": AttributeValueS(value="Ada Lovelace"),
                "title": AttributeValueS(value="Notes on the Analytical Engine"),
            },
        )
    )
```

## Protect a write with a condition expression
<a name="dynamodb-expressions"></a>

For request and response details, see the [put\_item()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/put_item/) API reference.

A condition expression is evaluated before DynamoDB changes the item. This conditional put prevents replacement of an item that already has the same key. A false condition raises the modeled `ConditionalCheckFailedException` and does not change the item.

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import (
    AttributeValueS,
    ConditionalCheckFailedException,
    PutItemInput,
)
```

 **Code**

```
async def put_item_conditionally(
    client: AsyncDynamoDBClient, table_name: str
) -> bool:
    """Put a book only when its partition key does not already exist."""
    try:
        await client.put_item(
            input=PutItemInput(
                table_name=table_name,
                item={
                    "author": AttributeValueS(value="Ada Lovelace"),
                    "title": AttributeValueS(
                        value="Notes on the Analytical Engine"
                    ),
                },
                condition_expression="attribute_not_exists(#author)",
                expression_attribute_names={"#author": "author"},
            )
        )
        return True
    except ConditionalCheckFailedException:
        return False
```

## More information
<a name="dynamodb-items-more-info"></a>
+ [Using expressions in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.html) in the Amazon DynamoDB Developer Guide
+ [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html) in the Amazon DynamoDB API Reference
+ [GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html) in the Amazon DynamoDB API Reference
+ [UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html) in the Amazon DynamoDB API Reference
+ [DeleteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html) in the Amazon DynamoDB API Reference

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
