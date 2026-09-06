---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/neptune_example_neptune_DeleteDBCluster_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteDBCluster` with an AWS SDK
<a name="neptune_example_neptune_DeleteDBCluster_section"></a>

The following code examples show how to use `DeleteDBCluster`.

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
     * @param clusterId the identifier of the cluster to delete
     * @return a {@link CompletableFuture} that completes when the cluster has been deleted
     */
    public CompletableFuture<Void> deleteDBClusterAsync(String clusterId) {
        DeleteDbClusterRequest request = DeleteDbClusterRequest.builder()
                .dbClusterIdentifier(clusterId)
                .skipFinalSnapshot(true)
                .build();

        return getAsyncClient().deleteDBCluster(request)
                .thenAccept(response -> System.out.println("🗑️ Deleting DB Cluster: " + clusterId));
    }
```
+  For API details, see [DeleteDBCluster](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DeleteDBCluster) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def delete_db_cluster(neptune_client, cluster_id: str):
    """
    Deletes a Neptune DB cluster and throws exceptions to the caller.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        cluster_id (str): The ID of the Neptune DB cluster to be deleted.

    Raises:
        ClientError: If the delete operation fails.
    """
    request = {
        'DBClusterIdentifier': cluster_id,
        'SkipFinalSnapshot': True
    }

    try:
        print(f"Deleting DB Cluster: {cluster_id}")
        neptune_client.delete_db_cluster(**request)

    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]

        if code == "DBClusterNotFoundFault":
            print(f"Cluster '{cluster_id}' not found or already deleted.")
        elif code == "AccessDeniedException":
            print("Access denied. Please ensure you have the necessary permissions.")
        else:
            print(f"Couldn't delete DB cluster. {code}: {message}")
        raise
```
+  For API details, see [DeleteDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DeleteDBCluster) in *AWS SDK for Python (Boto3) API Reference*.

------
