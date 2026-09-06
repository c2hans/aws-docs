---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/dynamodb-tables.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Work with DynamoDB tables
<a name="dynamodb-tables"></a>

Tables are the containers for all items in a DynamoDB database. Before you can add or remove data from DynamoDB, you must create a table.

For each table, you must define:
+ A table *name* that is unique for your AWS account and AWS Region.
+ A *primary key* for which every value must be unique. No two items in your table can have the same primary key value.

  A primary key can be *simple*, consisting of a single partition (HASH) key, or *composite*, consisting of a partition and a sort (RANGE) key.

  Each key value has an associated data type, specified in its `AttributeDefinition` as the `attribute_type` value. The key value can be binary (`"B"`), numeric (`"N"`), or a string (`"S"`). For more information, see [Naming Rules and Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html) in the Amazon DynamoDB Developer Guide.
+ *Provisioned throughput* values that define the number of reserved read and write capacity units for the table.

**Note**
[Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/) is based on the provisioned throughput values that you set on your tables, so reserve only as much capacity as you think you'll need for your table. Provisioned throughput for a table can be modified at any time, so you can adjust capacity if your needs change.

The `client` that is used in the following examples can be created from the snippet in [Set up the examples](services-dynamodb.md#dynamodb-shared-setup).

## Create a table
<a name="dynamodb-create-table"></a>

Use `create_table` to create a new DynamoDB table. You construct table attributes and a table schema, both of which identify the primary key of your table. You must also supply initial provisioned throughput values and a table name. Each example polls with a bounded loop until DynamoDB reports that the new table is active.

### Create a table with a simple primary key
<a name="dynamodb-create-simple-table"></a>

For request and response details, see the [create\_table()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/create_table/) and [describe\_table()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/describe_table/) API references.

A simple primary key contains only a partition key.

 **Imports**

```
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import (
    AttributeDefinition,
    CreateTableInput,
    DescribeTableInput,
    KeySchemaElement,
    ProvisionedThroughput,
)
```

 **Code**

```
async def create_table(
    client: AsyncDynamoDBClient,
    table_name: str,
    max_attempts: int = 30,
    poll_delay: float = 2.0,
) -> None:
    """Create a table and wait a bounded time for it to become active."""
    await client.create_table(
        input=CreateTableInput(
            table_name=table_name,
            attribute_definitions=[
                AttributeDefinition(attribute_name="id", attribute_type="S")
            ],
            key_schema=[KeySchemaElement(attribute_name="id", key_type="HASH")],
            provisioned_throughput=ProvisionedThroughput(
                read_capacity_units=5, write_capacity_units=5
            ),
        )
    )
    for _ in range(max_attempts):
        response = await client.describe_table(
            input=DescribeTableInput(table_name=table_name)
        )
        if response.table and response.table.table_status == "ACTIVE":
            return
        await asyncio.sleep(poll_delay)
    raise TimeoutError(f"Table '{table_name}' did not become active")
```

### Create a table with a composite primary key
<a name="dynamodb-create-composite-table"></a>

For request and response details, see the [create\_table()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/create_table/) and [describe\_table()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/describe_table/) API references.

A composite primary key contains a partition key and a sort key. The item and query examples use this schema.

 **Imports**

```
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import (
    AttributeDefinition,
    CreateTableInput,
    DescribeTableInput,
    KeySchemaElement,
    ProvisionedThroughput,
)
```

 **Code**

```
async def create_table_composite_key(
    client: AsyncDynamoDBClient,
    table_name: str,
    max_attempts: int = 30,
    poll_delay: float = 2.0,
) -> None:
    """Create a table with an author partition key and title sort key."""
    await client.create_table(
        input=CreateTableInput(
            table_name=table_name,
            attribute_definitions=[
                AttributeDefinition(attribute_name="author", attribute_type="S"),
                AttributeDefinition(attribute_name="title", attribute_type="S"),
            ],
            key_schema=[
                KeySchemaElement(attribute_name="author", key_type="HASH"),
                KeySchemaElement(attribute_name="title", key_type="RANGE"),
            ],
            provisioned_throughput=ProvisionedThroughput(
                read_capacity_units=5, write_capacity_units=5
            ),
        )
    )
    for _ in range(max_attempts):
        response = await client.describe_table(
            input=DescribeTableInput(table_name=table_name)
        )
        if response.table and response.table.table_status == "ACTIVE":
            return
        await asyncio.sleep(poll_delay)
    raise TimeoutError(f"Table '{table_name}' did not become active")
```

**Note**
Applications normally create durable tables through an infrastructure deployment. This table setup is included so that the data-operation examples can use a consistent schema.

## List tables
<a name="dynamodb-list-tables"></a>

For request and response details, see the [list\_tables()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/list_tables/) API reference.

`list_tables` can return a partial list. Continue with `last_evaluated_table_name` until DynamoDB returns no continuation name.

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import ListTablesInput
```

 **Code**

```
async def list_tables(
    client: AsyncDynamoDBClient, max_pages: int = 100
) -> list[str]:
    """Return table names from at most ``max_pages`` response pages."""
    table_names: list[str] = []
    start_name = None
    for _ in range(max_pages):
        response = await client.list_tables(
            input=ListTablesInput(
                exclusive_start_table_name=start_name,
                limit=100,
            )
        )
        table_names.extend(response.table_names or [])
        start_name = response.last_evaluated_table_name
        if not start_name:
            return table_names
    raise RuntimeError("DynamoDB table pagination exceeded the page limit")
```

## Describe a table
<a name="dynamodb-describe-table"></a>

For request and response details, see the [describe\_table()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/describe_table/) API reference.

Use `describe_table` to inspect table metadata such as status, key schema, item count, and provisioned throughput.

 **Imports**

```
from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import DescribeTableInput, TableDescription
```

 **Code**

```
async def describe_table(
    client: AsyncDynamoDBClient, table_name: str
) -> TableDescription:
    """Return the service's description of a table."""
    response = await client.describe_table(
        input=DescribeTableInput(table_name=table_name)
    )
    if response.table is None:
        raise RuntimeError("DynamoDB returned no table description")
    return response.table
```

## Update a table
<a name="dynamodb-update-table"></a>

For request and response details, see the [update\_table()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/update_table/) and [describe\_table()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/describe_table/) API references.

You can modify your table's provisioned throughput values at any time with `update_table`. This example changes the provisioned read and write capacity, then waits until the table is active and confirms that DynamoDB reports the requested values.

 **Imports**

```
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import (
    DescribeTableInput,
    ProvisionedThroughput,
    UpdateTableInput,
)
```

 **Code**

```
async def update_table(
    client: AsyncDynamoDBClient,
    table_name: str,
    capacity_units: int = 6,
    max_attempts: int = 30,
    poll_delay: float = 2.0,
) -> None:
    """Update throughput and wait a bounded time for the change."""
    await client.update_table(
        input=UpdateTableInput(
            table_name=table_name,
            provisioned_throughput=ProvisionedThroughput(
                read_capacity_units=capacity_units,
                write_capacity_units=capacity_units,
            ),
        )
    )
    for _ in range(max_attempts):
        response = await client.describe_table(
            input=DescribeTableInput(table_name=table_name)
        )
        table = response.table
        throughput = table.provisioned_throughput if table else None
        if (
            table and table.table_status == "ACTIVE" and throughput
            and throughput.read_capacity_units == capacity_units
            and throughput.write_capacity_units == capacity_units
        ):
            return
        await asyncio.sleep(poll_delay)
    raise TimeoutError(f"Table '{table_name}' was not updated")
```

## Delete a table
<a name="dynamodb-delete-table"></a>

For request and response details, see the [delete\_table()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/delete_table/) and [describe\_table()](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/operations/describe_table/) API references.

Delete each temporary table that you created after running the examples. The bounded loop confirms cleanup by waiting for the modeled `ResourceNotFoundException`.

 **Imports**

```
import asyncio

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.models import (
    DeleteTableInput,
    DescribeTableInput,
    ResourceNotFoundException,
)
```

 **Code**

```
async def delete_table(
    client: AsyncDynamoDBClient,
    table_name: str,
    max_attempts: int = 30,
    poll_delay: float = 2.0,
) -> None:
    """Delete a table if present and wait a bounded time for removal."""
    try:
        await client.delete_table(input=DeleteTableInput(table_name=table_name))
    except ResourceNotFoundException:
        return
    for _ in range(max_attempts):
        try:
            await client.describe_table(
                input=DescribeTableInput(table_name=table_name)
            )
        except ResourceNotFoundException:
            return
        await asyncio.sleep(poll_delay)
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
