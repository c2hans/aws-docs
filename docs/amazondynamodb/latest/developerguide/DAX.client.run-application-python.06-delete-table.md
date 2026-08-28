---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.run-application-python.06-delete-table.html
---

# 06-delete-table.py
<a name="DAX.client.run-application-python.06-delete-table"></a>

The `06-delete-table.py` program deletes `TryDaxTable`. Run this program after you have finished testing Amazon DynamoDB Accelerator (DAX) functionality.

```
import boto3

def delete_dax_table(dyn_resource=None):
    """
    Deletes the demonstration table.

    :param dyn_resource: Either a Boto3 or DAX resource.
    """
    if dyn_resource is None:
        dyn_resource = boto3.resource("dynamodb")

    table = dyn_resource.Table("TryDaxTable")
    table.delete()

    print(f"Deleting {table.name}...")
    table.wait_until_not_exists()

if __name__ == "__main__":
    delete_dax_table()
    print("Table deleted!")
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
