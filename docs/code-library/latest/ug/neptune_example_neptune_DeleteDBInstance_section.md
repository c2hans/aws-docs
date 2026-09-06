---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/neptune_example_neptune_DeleteDBInstance_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteDBInstance` with an AWS SDK
<a name="neptune_example_neptune_DeleteDBInstance_section"></a>

The following code examples show how to use `DeleteDBInstance`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](neptune_example_neptune_Scenario_section.md)

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Deletes a DB instance asynchronously.
     *
     * @param instanceId the identifier of the DB instance to be deleted
     * @return a {@link CompletableFuture} that completes when the DB instance has been deleted
     */
    public CompletableFuture<Void> deleteDBInstanceAsync(String instanceId) {
        DeleteDbInstanceRequest request = DeleteDbInstanceRequest.builder()
                .dbInstanceIdentifier(instanceId)
                .skipFinalSnapshot(true)
                .build();

        return getAsyncClient().deleteDBInstance(request)
                .thenAccept(response -> System.out.println("🗑️ Deleting DB Instance: " + instanceId));
    }
```
+  For API details, see [DeleteDBInstance](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBInstance) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def delete_db_instance(neptune_client, instance_id: str):
    """
    Deletes a Neptune DB instance and waits for its deletion to complete.
    Raises exception to be handled by calling code.
    """
    print(f"Initiating deletion of DB Instance: {instance_id}")
    try:
        neptune_client.delete_db_instance(
            DBInstanceIdentifier=instance_id,
            SkipFinalSnapshot=True
        )

        print(f"Waiting for DB Instance '{instance_id}' to be deleted...")
        waiter = neptune_client.get_waiter('db_instance_deleted')
        waiter.wait(
            DBInstanceIdentifier=instance_id,
            WaiterConfig={
                'Delay': 30,
                'MaxAttempts': 40
            }
        )

        print(f"DB Instance '{instance_id}' successfully deleted.")

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBInstanceNotFoundFault":
            print(f"Instance '{instance_id}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete DB instance. {code}: {message}")
        raise
```
+  For API details, see [DeleteDBInstance](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBInstance) in *AWS SDK for Python (Boto3) API Reference*.

------
