---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ecs_example_ecs_ListTasks_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListTasks` with an AWS SDK or CLI
<a name="ecs_example_ecs_ListTasks_section"></a>

The following code examples show how to use `ListTasks`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Configure container service connectivity](ecs_example_ecs_ServiceConnect_085_section.md)
+  [Create a container task for the serverless launch type](ecs_example_ecs_GettingStarted_086_section.md)
+  [Creating a container service for virtual machine instances](ecs_example_ecs_GettingStarted_018_section.md)
+  [Get ARN information for clusters, services, and tasks](ecs_example_ecs_Scenario_GetClustersServicesAndTasks_section.md)
+  [Learn Amazon ECS basics](ecs_example_ecs_Scenario_section.md)

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/ECS#code-examples).

```
    /// <summary>
    /// List task ARNs available.
    /// </summary>
    /// <param name="clusterARN">The arn of the ECS cluster.</param>
    /// <returns>The ARN list of tasks in given cluster.</returns>
    public async Task<List<string>> GetTaskARNsAsync(string clusterARN)
    {
        // Set up the request to describe the tasks in the service
        var listTasksRequest = new ListTasksRequest
        {
            Cluster = clusterARN
        };
        List<string> taskArns = new List<string>();

        // Call the ListTasks API operation and get the list of task ARNs
        var tasks = _ecsClient.Paginators.ListTasks(listTasksRequest);

        await foreach (var task in tasks.TaskArns)
        {
            if (task is null)
                continue;

            taskArns.Add(task);
        }

        if (taskArns.Count == 0)
        {
            _logger.LogWarning("No tasks found in cluster: " + clusterARN);
        }

        return taskArns;
    }
```
+  For API details, see [ListTasks](https://docs.aws.amazon.com/goto/DotNetSDKV3/ecs-2014-11-13/ListTasks) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To list the tasks in a cluster**
The following `list-tasks` example lists all of the tasks in a cluster.

```
aws ecs list-tasks --cluster {{default}}
```
Output:

```
{
    "taskArns": [
        "arn:aws:ecs:us-west-2:123456789012:task/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
        "arn:aws:ecs:us-west-2:123456789012:task/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE"
    ]
}
```
**Example 2: To list the tasks on a particular container instance**
The following `list-tasks` example lists the tasks on a container instance, using the container instance UUID as a filter.

```
aws ecs list-tasks --cluster {{default}} --container-instance {{a1b2c3d4-5678-90ab-cdef-33333EXAMPLE}}
```
Output:

```
{
    "taskArns": [
        "arn:aws:ecs:us-west-2:123456789012:task/a1b2c3d4-5678-90ab-cdef-44444EXAMPLE"
    ]
}
```
For more information, see [Amazon ECS Task Definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) in the *Amazon ECS Developer Guide*.
+  For API details, see [ListTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-tasks.html) in *AWS CLI Command Reference*.

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

    def list_tasks(
        self,
        cluster: str,
        service_name: Optional[str] = None,
    ) -> List[str]:
        """
        Lists task ARNs for a cluster, optionally filtered by service.
        Uses paginator to handle large result sets.

        :param cluster: The cluster name or ARN.
        :param service_name: The service name to filter by (optional).
        :return: A list of task ARN strings.
        :raises ClientError: If the request fails (e.g., InvalidParameterException).
        """
        try:
            task_arns = list()
            paginator = self.ecs_client.get_paginator("list_tasks")
            params = dict()
            params["cluster"] = cluster
            if service_name is not None:
                params["serviceName"] = service_name
            for page in paginator.paginate(**params):
                task_arns.extend(page.get("taskArns", list()))
            logger.info(
                "Listed %d tasks for cluster '%s'%s",
                len(task_arns),
                cluster,
                f" (service='{service_name}')" if service_name else "",
            )
            return task_arns
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidParameterException":
                logger.error(
                    "Invalid parameter when listing tasks: %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListTasks](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListTasks) in *AWS SDK for Python (Boto3) API Reference*.

------
