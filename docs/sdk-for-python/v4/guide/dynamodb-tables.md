---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/dynamodb-tables.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Work with DynamoDB tables

Tables are the containers for all items in a DynamoDB database. Before you can add or remove data from DynamoDB, you must create a table.

Each table has a primary key and a name that is unique for your AWS account and AWS Region. A primary key is either a partition key or a partition key and a sort key. No two items in a table can have the same primary key value. For more information, see [Core components of Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html) in the Amazon DynamoDB Developer Guide.

To create the `client` that the following examples use, see [Set up the examples](services-dynamodb.md#dynamodb-shared-setup). The identity that runs the examples needs the `dynamodb:CreateTable`, `dynamodb:DescribeTable`, `dynamodb:ListTables`, `dynamodb:UpdateTable`, and `dynamodb:DeleteTable` permissions.

## Create a table
<a name="dynamodb-create-table"></a>

Use `create_table` to create a DynamoDB table. Pass attribute definitions and a key schema, which together identify the primary key of your table. Also pass a table name and initial provisioned throughput values. The example polls in a bounded loop until DynamoDB reports that the new table is active.

### Create a table with a composite primary key
<a name="dynamodb-create-composite-table"></a>

For request and response details, see the [create\_table()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/create_table/) and [describe\_table()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/describe_table/) API references.

A composite primary key contains a partition key and a sort key. The item and query examples use this schema.

 **Imports**

```
import time

from aws_sdk_dynamodb import DynamoDBClient
```

 **Code**

```
def create_table_composite_key(
    client: DynamoDBClient,
    table_name: str,
    max_attempts: int = 30,
    poll_delay: float = 2.0,
) -> None:
    """Create a table with an author partition key and title sort key."""
    client.create_table(
        table_name=table_name,
        attribute_definitions=[
            {"attribute_name": "author", "attribute_type": "S"},
            {"attribute_name": "title", "attribute_type": "S"},
        ],
        key_schema=[
            {"attribute_name": "author", "key_type": "HASH"},
            {"attribute_name": "title", "key_type": "RANGE"},
        ],
        provisioned_throughput={
            "read_capacity_units": 5,
            "write_capacity_units": 5,
        },
    )
    for _ in range(max_attempts):
        response = client.describe_table(table_name=table_name)
        if response.table and response.table.table_status == "ACTIVE":
            return
        time.sleep(poll_delay)
    raise TimeoutError(f"Table '{table_name}' did not become active")
```

## List tables
<a name="dynamodb-list-tables"></a>

For request and response details, see the [list\_tables()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/list_tables/) API reference.

`list_tables` can return a partial list. Pass each response's `last_evaluated_table_name` as `exclusive_start_table_name` on the next call. Stop when DynamoDB returns no continuation name.

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient
```

 **Code**

```
def list_tables(client: DynamoDBClient, max_pages: int = 100) -> list[str]:
    """Return table names from at most ``max_pages`` response pages."""
    table_names: list[str] = []
    start_name = None
    for _ in range(max_pages):
        response = client.list_tables(
            exclusive_start_table_name=start_name,
            limit=100,
        )
        table_names.extend(response.table_names or [])
        start_name = response.last_evaluated_table_name
        if not start_name:
            return table_names
    raise RuntimeError("DynamoDB table pagination exceeded the page limit")
```

## Describe a table
<a name="dynamodb-describe-table"></a>

For request and response details, see the [describe\_table()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/describe_table/) API reference.

Use `describe_table` to inspect table metadata such as status, key schema, item count, and provisioned throughput.

 **Imports**

```
from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import TableDescription
```

 **Code**

```
def describe_table(
    client: DynamoDBClient, table_name: str
) -> TableDescription:
    """Return the service's description of a table."""
    response = client.describe_table(table_name=table_name)
    if response.table is None:
        raise RuntimeError("DynamoDB returned no table description")
    return response.table
```

## Update a table
<a name="dynamodb-update-table"></a>

For request and response details, see the [update\_table()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/update_table/) and [describe\_table()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/describe_table/) API references.

You can change your table's provisioned throughput values at any time with `update_table`. This example changes the provisioned read and write capacity, then waits until the table is active and DynamoDB reports the requested values.

 **Imports**

```
import time

from aws_sdk_dynamodb import DynamoDBClient
```

 **Code**

```
def update_table(
    client: DynamoDBClient,
    table_name: str,
    capacity_units: int = 6,
    max_attempts: int = 30,
    poll_delay: float = 2.0,
) -> None:
    """Update throughput and wait a bounded time for the change."""
    client.update_table(
        table_name=table_name,
        provisioned_throughput={
            "read_capacity_units": capacity_units,
            "write_capacity_units": capacity_units,
        },
    )
    for _ in range(max_attempts):
        response = client.describe_table(table_name=table_name)
        table = response.table
        throughput = table.provisioned_throughput if table else None
        if (
            table and table.table_status == "ACTIVE" and throughput
            and throughput.read_capacity_units == capacity_units
            and throughput.write_capacity_units == capacity_units
        ):
            return
        time.sleep(poll_delay)
    raise TimeoutError(f"Table '{table_name}' was not updated")
```

## Delete a table
<a name="dynamodb-delete-table"></a>

For request and response details, see the [delete\_table()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/delete_table/) and [describe\_table()](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/operations/describe_table/) API references.

After you run the examples, delete each temporary table that you created. The bounded loop confirms cleanup by waiting for the modeled `ResourceNotFoundException`.

 **Imports**

```
import time

from aws_sdk_dynamodb import DynamoDBClient
from aws_sdk_dynamodb.models import ResourceNotFoundException
```

 **Code**

```
def delete_table(
    client: DynamoDBClient,
    table_name: str,
    max_attempts: int = 30,
    poll_delay: float = 2.0,
) -> None:
    """Delete a table if present and wait a bounded time for removal."""
    try:
        client.delete_table(table_name=table_name)
    except ResourceNotFoundException:
        return
    for _ in range(max_attempts):
        try:
            client.describe_table(table_name=table_name)
        except ResourceNotFoundException:
            return
        time.sleep(poll_delay)
    raise TimeoutError(f"Table '{table_name}' was not deleted")
```

## More information
<a name="dynamodb-tables-more-info"></a>
+ [Working with tables and data in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html) in the Amazon DynamoDB Developer Guide
+ [CreateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html) in the Amazon DynamoDB API Reference
+ [ListTables](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTables.html) in the Amazon DynamoDB API Reference
+ [DescribeTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html) in the Amazon DynamoDB API Reference
+ [UpdateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html) in the Amazon DynamoDB API Reference
+ [DeleteTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteTable.html) in the Amazon DynamoDB API Reference
