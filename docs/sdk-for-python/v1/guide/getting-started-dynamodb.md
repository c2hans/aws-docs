---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/getting-started-dynamodb.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Example 1: Make asynchronous calls to Amazon DynamoDB
<a name="getting-started-dynamodb"></a>

This example uses `AsyncDynamoDBClient` to create a temporary Amazon DynamoDB table, wait until it is active, write an item, and read the item with a strongly consistent read. The `finally` block deletes the table if a later operation fails.

## Before you begin
<a name="getting-started-dynamodb-before"></a>

Complete [Prerequisites and installation](getting-started-prerequisites-installation.md) and [Authenticating with AWS using the AWS SDK for Python](getting-started-authentication.md). This example also requires the following:
+ The identity selected by your authentication method must allow `dynamodb:CreateTable`, `dynamodb:DescribeTable`, `dynamodb:PutItem`, `dynamodb:GetItem`, and `dynamodb:DeleteTable`. To learn how IAM policies grant permissions like these, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.

**Warning**
Creating and using an Amazon DynamoDB table can incur charges. The example deletes the table when it finishes; confirm the deletion in its output.

## Write the code
<a name="getting-started-dynamodb-code"></a>

Create a file named `getting_started_dynamodb.py` with the following code:

```
"""Make first asynchronous DynamoDB calls with the AWS SDK for Python."""

import asyncio
import uuid

from aws_sdk_dynamodb.client import AsyncDynamoDBClient
from aws_sdk_dynamodb.config import AsyncDynamoDBConfig
from aws_sdk_dynamodb.models import (
    AttributeDefinition,
    AttributeValueN,
    AttributeValueS,
    CreateTableInput,
    DeleteTableInput,
    DescribeTableInput,
    GetItemInput,
    KeySchemaElement,
    KeyType,
    ProvisionedThroughput,
    PutItemInput,
    ResourceNotFoundException,
    ScalarAttributeType,
)

TABLE_NAME = f"python-getting-started-{uuid.uuid4().hex[:8]}"

async def main() -> None:
    config = await AsyncDynamoDBConfig.resolve(region="us-east-1")
    async with AsyncDynamoDBClient(config=config) as client:
        print(f"Creating table '{TABLE_NAME}'...")
        await client.create_table(
            input=CreateTableInput(
                table_name=TABLE_NAME,
                attribute_definitions=[
                    AttributeDefinition(
                        attribute_name="pk",
                        attribute_type=ScalarAttributeType.S,
                    )
                ],
                key_schema=[
                    KeySchemaElement(
                        attribute_name="pk", key_type=KeyType.HASH
                    )
                ],
                provisioned_throughput=ProvisionedThroughput(
                    read_capacity_units=5,
                    write_capacity_units=5,
                ),
            )
        )

        try:
            print("Waiting for the table to become active...")
            for _ in range(30):
                response = await client.describe_table(
                    input=DescribeTableInput(table_name=TABLE_NAME)
                )
                if response.table and response.table.table_status == "ACTIVE":
                    break
                await asyncio.sleep(2)
            else:
                raise TimeoutError(
                    f"Table '{TABLE_NAME}' did not become active in time"
                )

            await client.put_item(
                input=PutItemInput(
                    table_name=TABLE_NAME,
                    item={
                        "pk": AttributeValueS(value="user-001"),
                        "name": AttributeValueS(value="Ada"),
                        "visits": AttributeValueN(value="1"),
                    },
                )
            )

            response = await client.get_item(
                input=GetItemInput(
                    table_name=TABLE_NAME,
                    key={"pk": AttributeValueS(value="user-001")},
                    consistent_read=True,
                )
            )
            if response.item is None:
                raise RuntimeError("DynamoDB returned no item")

            name = response.item.get("name")
            visits = response.item.get("visits")
            if not isinstance(name, AttributeValueS) or not isinstance(
                visits, AttributeValueN
            ):
                raise RuntimeError("DynamoDB returned unexpected attribute types")

            print(f"Read item: name={name.value}, visits={visits.value}")
        finally:
            print(f"Deleting table '{TABLE_NAME}'...")
            try:
                await client.delete_table(
                    input=DeleteTableInput(table_name=TABLE_NAME)
                )
            except ResourceNotFoundException:
                pass
            else:
                for _ in range(30):
                    try:
                        await client.describe_table(
                            input=DescribeTableInput(table_name=TABLE_NAME)
                        )
                    except ResourceNotFoundException:
                        break
                    await asyncio.sleep(2)
                else:
                    raise TimeoutError(
                        f"Table '{TABLE_NAME}' was not deleted"
                    )
            print("Table deleted.")

if __name__ == "__main__":
    asyncio.run(main())
```

DynamoDB creates and deletes tables asynchronously. The bounded polling loops wait for the table to become `ACTIVE` before writing and confirm that deletion completes before reporting success. A future release of the SDK will add waiters that replace this polling logic. Item attributes use generated union variants such as `AttributeValueS` and `AttributeValueN`; numbers are represented as strings to preserve precision.

## Run the application
<a name="getting-started-dynamodb-run"></a>

Run the program from the directory that contains `getting_started_dynamodb.py`:

```
python getting_started_dynamodb.py
```

## Success
<a name="getting-started-dynamodb-success"></a>

A successful run prints the generated table name, `Read item: name=Ada, visits=1`, and `Table deleted.`

## Cleanup
<a name="getting-started-dynamodb-cleanup"></a>

The `finally` block requests and confirms table deletion even if writing or reading fails. If the program doesn't print `Table deleted.`, open the DynamoDB console in `us-east-1` and delete the table whose name starts with `python-getting-started-`.

## Next steps
<a name="getting-started-dynamodb-next-steps"></a>
+ For more Amazon DynamoDB operations and examples, see [Amazon DynamoDB](services-dynamodb.md).
+ For generated client operations and model types, see the [Amazon DynamoDB API reference](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/dynamodb/).
+ For more information about typed inputs and outputs, see [Making requests and handling responses](using-requests.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
