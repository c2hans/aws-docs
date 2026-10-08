---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_Hello_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Hello Athena
<a name="athena_example_athena_Hello_section"></a>

The following code example shows how to get started using Athena.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
def hello_athena(athena_client: BaseClient) -> None:
    """
    Lists Amazon Athena workgroups. Demonstrates basic connectivity to the
    Athena service.

    :param athena_client: A Boto3 Athena client.
    """
    print("Listing Athena workgroups...\n")
    try:
        workgroup_count = 0
        next_token = None
        while True:
            kwargs = dict()
            if next_token is not None:
                kwargs["NextToken"] = next_token
            response = athena_client.list_work_groups(**kwargs)
            for wg in response.get("WorkGroups", list()):
                name = wg.get("Name", "Unknown")
                state = wg.get("State", "Unknown")
                print(f"  Workgroup: {name} (State: {state})")
                workgroup_count += 1
            next_token = response.get("NextToken", None)
            if next_token is None:
                break
        print(f"\nFound {workgroup_count} workgroup(s).")
    except ClientError as err:
        logger.error(
            "Error listing Athena workgroups. %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    hello_athena(boto3.client("athena"))
```
+  For API details, see [ListWorkGroups](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/ListWorkGroups) in *AWS SDK for Python (Boto3) API Reference*.

------
