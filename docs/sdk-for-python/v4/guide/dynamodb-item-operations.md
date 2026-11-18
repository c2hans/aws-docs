---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/dynamodb-item-operations.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Work with DynamoDB items
<a name="dynamodb-item-operations"></a>

In DynamoDB, an item is a collection of *attributes*, each of which has a *name* and a *value*. An attribute value can be a scalar, set, or document type. For more information, see [Naming Rules and Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html) in the Amazon DynamoDB Developer Guide.

The examples pass an item as a dictionary that maps each attribute name to a typed value. Each typed value is a dictionary with one key that names the attribute type, such as `"s"` for a string and `"n"` for a number. Numbers are strings to preserve decimal precision. Responses return each attribute as a typed `AttributeValue` model, such as `AttributeValueS` or `AttributeValueN`. Check the concrete model before you read its `value`, as shown in [Get an item](#dynamodb-get-item). For more information about dictionaries and model objects, see [Passing nested values](using-requests.md#using-requests-nested).

The examples on this page use the composite-key table created in [Create a table with a composite primary key](dynamodb-tables.md#dynamodb-create-composite-table). To create the `client` that the following examples use, see [Set up the examples](services-dynamodb.md#dynamodb-shared-setup). The identity that runs the examples needs the `dynamodb:PutItem`, `dynamodb:GetItem`, `dynamodb:UpdateItem`, and `dynamodb:DeleteItem` permissions on the table.

## Put an item
<a name="dynamodb-put-item"></a>

For request and response details, see the [put\_item()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/put_item/) API reference.

Pass a complete map of typed attributes to `put_item`. A put replaces an existing item with the same primary key unless you add a condition.

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient
```

 **Code**

```
def put_item(client: DynamoDBClient, table_name: str) -> None:
    """Put a book item, replacing any item with the same primary key."""
    client.put_item(
        table_name=table_name,
        item={
            "author": {"s": "Mary Major"},
            "title": {"s": "Notes on Example Data"},
            "year": {"n": "1843"},
            "copies": {"n": "0"},
        },
    )
```

## Get an item
<a name="dynamodb-get-item"></a>

For request and response details, see the [get\_item()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/get_item/) API reference.

Supply every primary-key attribute to `get_item`. This example requests a strongly consistent read and returns the optional item.

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import AttributeValue, AttributeValueS
```

 **Code**

```
def get_item(
    client: DynamoDBClient, table_name: str
) -> dict[str, AttributeValue] | None:
    """Get a book by its complete composite primary key."""
    response = client.get_item(
        table_name=table_name,
        key={
            "author": {"s": "Mary Major"},
            "title": {"s": "Notes on Example Data"},
        },
        consistent_read=True,
    )
    return response.item
```

Each returned attribute is a typed `AttributeValue` union. Narrow it to its concrete model before you read its `value`.

```
item = get_item(client, table_name)
if item:
    title = item.get("title")
    if isinstance(title, AttributeValueS):
        print(title.value)
```

## Update an item
<a name="dynamodb-update-item"></a>

For request and response details, see the [update\_item()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/update_item/) API reference.

Use an update expression to change selected attributes. The `#copies` placeholder in `expression_attribute_names` stands for the attribute name, so the expression can refer to any attribute name, including reserved words. `ALL_NEW` returns the item after the update.

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import AttributeValue
```

 **Code**

```
def update_item(
    client: DynamoDBClient, table_name: str
) -> dict[str, AttributeValue]:
    """Increment a book's copy count and return the updated item."""
    response = client.update_item(
        table_name=table_name,
        key={
            "author": {"s": "Mary Major"},
            "title": {"s": "Notes on Example Data"},
        },
        update_expression="SET #copies = #copies + :increment",
        expression_attribute_names={"#copies": "copies"},
        expression_attribute_values={":increment": {"n": "1"}},
        return_values="ALL_NEW",
    )
    return response.attributes or {}
```

## Delete an item
<a name="dynamodb-delete-item"></a>

For request and response details, see the [delete\_item()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/delete_item/) API reference.

Delete one item by supplying its complete primary key.

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient
```

 **Code**

```
def delete_item(client: DynamoDBClient, table_name: str) -> None:
    """Delete a book by its complete composite primary key."""
    client.delete_item(
        table_name=table_name,
        key={
            "author": {"s": "Mary Major"},
            "title": {"s": "Notes on Example Data"},
        },
    )
```

## Protect a write with a condition expression
<a name="dynamodb-expressions"></a>

For request and response details, see the [put\_item()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/put_item/) API reference.

DynamoDB evaluates a condition expression before it changes the item. This conditional put doesn't replace an item that already has the same key. If the condition is false, DynamoDB doesn't change the item. The client raises the modeled `ConditionalCheckFailedException`.

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import ConditionalCheckFailedException
```

 **Code**

```
def put_item_conditionally(
    client: DynamoDBClient, table_name: str
) -> bool:
    """Put a book only when no item has the same primary key."""
    try:
        client.put_item(
            table_name=table_name,
            item={
                "author": {"s": "Mary Major"},
                "title": {"s": "Notes on Example Data"},
            },
            condition_expression="attribute_not_exists(#author)",
            expression_attribute_names={"#author": "author"},
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
