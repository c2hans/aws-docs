---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ecs_example_ecs_DeleteCluster_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteCluster` with an AWS SDK or CLI
<a name="ecs_example_ecs_DeleteCluster_section"></a>

The following code examples show how to use `DeleteCluster`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Configure container service connectivity](ecs_example_ecs_ServiceConnect_085_section.md)
+  [Create a container task for the serverless launch type](ecs_example_ecs_GettingStarted_086_section.md)
+  [Creating a container service for virtual machine instances](ecs_example_ecs_GettingStarted_018_section.md)
+  [Learn Amazon ECS basics](ecs_example_ecs_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To delete an empty cluster**
The following `delete-cluster` example deletes the specified empty cluster.

```
aws ecs delete-cluster --cluster {{MyCluster}}
```
Output:

```
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/MyCluster",
        "status": "INACTIVE",
        "clusterName": "MyCluster",
        "registeredContainerInstancesCount": 0,
        "pendingTasksCount": 0,
        "runningTasksCount": 0,
        "activeServicesCount": 0
        "statistics": [],
        "tags": []
    }
}
```
For more information, see [Deleting a Cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete_cluster.html) in the *Amazon ECS Developer Guide*.
+  For API details, see [DeleteCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-cluster.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This cmdlet deletes the specified ECS cluster. You must deregister all container instances from this cluster before you may delete it. **

```
Remove-ECSCluster -Cluster "LAB-ECS"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-ECSCluster (DeleteCluster)" on target "LAB-ECS".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteCluster](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This cmdlet deletes the specified ECS cluster. You must deregister all container instances from this cluster before you may delete it. **

```
Remove-ECSCluster -Cluster "LAB-ECS"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-ECSCluster (DeleteCluster)" on target "LAB-ECS".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteCluster](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
class EcsWrapper:
    """Encapsulates Amazon ECS operations."""

    def __init__(self, ecs_client: BaseClient):
        """
        Initializes the EcsWrapper with an ECS client.

        :param ecs_client: A Boto3 Amazon ECS client. Boto3 clients are created
            by the ``boto3.client`` factory function and are instances of
            ``botocore.client.BaseClient``, which is the correct type to
            annotate here (``boto3.client`` itself is a function, not a type).
        """
        self.ecs_client = ecs_client

    @classmethod
    def from_client(cls) -> "EcsWrapper":
        """Creates an EcsWrapper using a default Boto3 ECS client."""
        ecs_client = boto3.client("ecs")
        return cls(ecs_client)

    def delete_cluster(self, cluster: str) -> Dict[str, Any]:
        """
        Deletes an ECS cluster.

        :param cluster: The cluster name or ARN.
        :return: The deleted cluster details.
        :raises ClientError: If the request fails (e.g., ClusterContainsServicesException).
        """
        try:
            response = self.ecs_client.delete_cluster(
                cluster=cluster,
            )
            cluster_info = response["cluster"]
            logger.info(
                "Deleted cluster '%s' (status: %s)",
                cluster_info["clusterName"],
                cluster_info["status"],
            )
            return cluster_info
        except ClientError as err:
            if err.response["Error"]["Code"] == "ClusterContainsServicesException":
                logger.error(
                    "Cluster '%s' still contains services. Delete services first: %s",
                    cluster,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeleteCluster](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeleteCluster) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ Rust ]

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ecs#code-examples).

```
async fn remove_cluster(
    client: &aws_sdk_ecs::Client,
    name: &str,
) -> Result<(), aws_sdk_ecs::Error> {
    let cluster_deleted = client.delete_cluster().cluster(name).send().await?;
    println!("cluster deleted: {:?}", cluster_deleted);

    Ok(())
}
```
+  For API details, see [DeleteCluster](https://docs.rs/aws-sdk-ecs/latest/aws_sdk_ecs/client/struct.Client.html#method.delete_cluster) in *AWS SDK for Rust API reference*.

------
