---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/neptune_example_neptune_CreateDBCluster_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateDBCluster` with an AWS SDK
<a name="neptune_example_neptune_CreateDBCluster_section"></a>

The following code examples show how to use `CreateDBCluster`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](neptune_example_neptune_Scenario_section.md)

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Creates a new Amazon Neptune DB cluster asynchronously.
     *
     * @param dbName the name of the DB cluster to be created
     * @return a CompletableFuture that, when completed, provides the ID of the created DB cluster
     * @throws CompletionException if the operation fails for any reason, including if the request would exceed the maximum quota
     */
    public CompletableFuture<String> createDBClusterAsync(String dbName) {
        CreateDbClusterRequest request = CreateDbClusterRequest.builder()
                .dbClusterIdentifier(dbName)
                .engine("neptune")
                .deletionProtection(false)
                .backupRetentionPeriod(1)
                .build();

        return getAsyncClient().createDBCluster(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        if (cause instanceof ServiceQuotaExceededException) {
                            throw new CompletionException("The operation was denied because the request would exceed the maximum quota.", cause);
                        }
                        throw new CompletionException("Failed to create Neptune DB cluster: " + exception.getMessage(), exception);
                    }
                })
                .thenApply(response -> {
                    String clusterId = response.dbCluster().dbClusterIdentifier();
                    logger.info("DB Cluster created: " + clusterId);
                    return clusterId;
                });
    }
```
+  For API details, see [CreateDBCluster](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateDBCluster) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def create_db_cluster(neptune_client, db_name: str) -> str:
    """
    Creates a Neptune DB cluster and returns its identifier.

    Args:
        neptune_client (boto3.client): The Neptune client object.
        db_name (str): The desired cluster identifier.

    Returns:
        str: The DB cluster identifier.

    Raises:
        RuntimeError: For any failure or AWS error, with a user-friendly message.
    """
    request = {
        'DBClusterIdentifier': db_name,
        'Engine': 'neptune',
        'DeletionProtection': False,
        'BackupRetentionPeriod': 1
    }

    try:
        response = neptune_client.create_db_cluster(**request)
        cluster = response.get('DBCluster') or {}

        cluster_id = cluster.get('DBClusterIdentifier')
        if not cluster_id:
            raise RuntimeError("Cluster created but no ID returned.")

        print(f"DB Cluster created: {cluster_id}")
        return cluster_id

    except ClientError as e:
        code = e.response["Error"]["Code"]
        message = e.response["Error"]["Message"]

        if code in ("ServiceQuotaExceededException", "DBClusterQuotaExceededFault"):
            raise RuntimeError("You have exceeded the quota for Neptune DB clusters.") from e
        else:
            raise RuntimeError(f"AWS error [{code}]: {message}") from e

    except Exception as e:
        raise RuntimeError(f"Unexpected error creating DB cluster '{db_name}': {e}") from e
```
+  For API details, see [CreateDBCluster](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateDBCluster) in *AWS SDK for Python (Boto3) API Reference*.

------
