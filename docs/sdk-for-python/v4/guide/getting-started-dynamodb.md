---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/getting-started-dynamodb.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Example 1: Make calls to Amazon DynamoDB

This example uses `DynamoDBClient`, the synchronous Amazon DynamoDB client, to create a temporary table, wait until it is active, write an item, and read the item with a strongly consistent read. The `finally` block deletes the table if a later operation fails.

## Before you begin
<a name="getting-started-dynamodb-before"></a>

Complete [Prerequisites and installation](getting-started-prerequisites-installation.md) and [Authenticating with AWS](getting-started-authentication.md). This example also requires the following:
+ The identity selected by your authentication method must allow `dynamodb:CreateTable`, `dynamodb:DescribeTable`, `dynamodb:PutItem`, `dynamodb:GetItem`, and `dynamodb:DeleteTable`. To learn how IAM policies grant permissions like these, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.

**Warning**
Creating and using an Amazon DynamoDB table can incur charges. The example deletes the table when it finishes; confirm the deletion in its output.

## Write the code
<a name="getting-started-dynamodb-code"></a>

Create a file named `getting_started_dynamodb.py` with the following code:

```python
"""Make first DynamoDB calls with the AWS SDK for Python v4."""

import time
import uuid

from aws_sdk_dynamodb import DynamoDBClient, DynamoDBConfig
from aws_sdk_dynamodb.models import (
    AttributeValueN,
    AttributeValueS,
    ResourceNotFoundException,
)

TABLE_NAME = f"python-getting-started-{uuid.uuid4().hex[:8]}"

def main() -> None:
    config = DynamoDBConfig.resolve(region="us-east-1")
    with DynamoDBClient(config=config) as client:
        print(f"Creating table '{TABLE_NAME}'...")
        client.create_table(
            table_name=TABLE_NAME,
            attribute_definitions=[
                {"attribute_name": "pk", "attribute_type": "S"}
            ],
            key_schema=[{"attribute_name": "pk", "key_type": "HASH"}],
            provisioned_throughput={
                "read_capacity_units": 5,
                "write_capacity_units": 5,
            },
        )

        try:
            print("Waiting for the table to become active...")
            for _ in range(30):
                response = client.describe_table(table_name=TABLE_NAME)
                if response.table and response.table.table_status == "ACTIVE":
                    break
                time.sleep(2)
            else:
                raise TimeoutError(
                    f"Table '{TABLE_NAME}' did not become active in time"
                )

            client.put_item(
                table_name=TABLE_NAME,
                item={
                    "pk": {"s": "user-001"},
                    "name": {"s": "Mary Major"},
                    "visits": {"n": "1"},
                },
            )

            response = client.get_item(
                table_name=TABLE_NAME,
                key={"pk": {"s": "user-001"}},
                consistent_read=True,
            )
            if response.item is None:
                raise RuntimeError("DynamoDB returned no item")

            name = response.item.get("name")
            visits = response.item.get("visits")
            if not isinstance(name, AttributeValueS) or not isinstance(
                visits, AttributeValueN
            ):
                raise RuntimeError(
                    "DynamoDB returned unexpected attribute types"
                )

            print(f"Read item: name={name.value}, visits={visits.value}")
        finally:
            print(f"Deleting table '{TABLE_NAME}'...")
            try:
                client.delete_table(table_name=TABLE_NAME)
            except ResourceNotFoundException:
                pass
            else:
                for _ in range(30):
                    try:
                        client.describe_table(table_name=TABLE_NAME)
                    except ResourceNotFoundException:
                        break
                    time.sleep(2)
                else:
                    raise TimeoutError(
                        f"Table '{TABLE_NAME}' was not deleted"
                    )
            print("Table deleted.")

if __name__ == "__main__":
    main()
```

Each operation takes keyword arguments named after the members of its request, such as `table_name` and `consistent_read`. The `with` block closes the client when the block exits.

The `create_table` and `delete_table` operations return before DynamoDB finishes creating or deleting the table. The SDK doesn't provide waiters yet, so the example polls until the table is `ACTIVE` and again until the deletion completes.

The example passes the table settings and item attributes as dictionaries. DynamoDB numbers are strings, such as `{"n": "1"}`, to preserve precision. Responses contain model objects, so the example checks each attribute's type before it reads the value. For details, see [Passing nested values](using-requests.md#using-requests-nested).

## Run the application
<a name="getting-started-dynamodb-run"></a>

Run the program from the directory that contains `getting_started_dynamodb.py`:

```bash
python getting_started_dynamodb.py
```

## Success
<a name="getting-started-dynamodb-success"></a>

A successful run prints the generated table name, `Read item: name=Mary Major, visits=1`, and `Table deleted.`

## Cleanup
<a name="getting-started-dynamodb-cleanup"></a>

The `finally` block requests and confirms table deletion even if writing or reading fails. If the program doesn't print `Table deleted.`, open the DynamoDB console in `us-east-1` and delete the table whose name starts with `python-getting-started-`.

## Next steps
<a name="getting-started-dynamodb-next-steps"></a>
+ For more Amazon DynamoDB operations and examples, see [Amazon DynamoDB](services-dynamodb.md).
+ For generated client operations and model types, see the [Amazon DynamoDB API reference](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/dynamodb/).
+ For more information about keyword arguments and typed outputs, see [Making requests and handling responses](using-requests.md).
+ To make the same calls with an asynchronous client, see [Synchronous and asynchronous clients](using-sync-async.md).
