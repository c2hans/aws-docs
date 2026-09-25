---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ecs_example_ecs_DescribeServices_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeServices` with an AWS SDK or CLI
<a name="ecs_example_ecs_DescribeServices_section"></a>

The following code examples show how to use `DescribeServices`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Configure container service connectivity](ecs_example_ecs_ServiceConnect_085_section.md)
+  [Create a container task for the serverless launch type](ecs_example_ecs_GettingStarted_086_section.md)
+  [Creating a container service for virtual machine instances](ecs_example_ecs_GettingStarted_018_section.md)
+  [Learn Amazon ECS basics](ecs_example_ecs_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To describe a service**
The following `describe-services` example retrieves details for the `my-http-service` service in the default cluster.

```
aws ecs describe-services --services {{my-http-service}}
```
Output:

```
{
    "services": [
        {
            "status": "ACTIVE",
            "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/amazon-ecs-sample:1",
            "pendingCount": 0,
            "loadBalancers": [],
            "desiredCount": 10,
            "createdAt": 1466801808.595,
            "serviceName": "my-http-service",
            "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/default",
            "serviceArn": "arn:aws:ecs:us-west-2:123456789012:service/my-http-service",
            "deployments": [
                {
                    "status": "PRIMARY",
                    "pendingCount": 0,
                    "createdAt": 1466801808.595,
                    "desiredCount": 10,
                    "taskDefinition": "arn:aws:ecs:us-west-2:123456789012:task-definition/amazon-ecs-sample:1",
                    "updatedAt": 1428326312.703,
                    "id": "ecs-svc/1234567890123456789",
                    "runningCount": 10
                }
            ],
            "events": [
                {
                    "message": "(service my-http-service) has reached a steady state.",
                    "id": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
                    "createdAt": 1466801812.435
                }
            ],
            "runningCount": 10
        }
    ],
    "failures": []
}
```
For more information, see [Services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) in the *Amazon ECS Developer Guide*.
+  For API details, see [DescribeServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-services.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example shows how to retrieve details of a specific service from your default cluster.**

```
Get-ECSService -Service my-hhtp-service
```
**Example 2: This example shows how to retrieve details of a specific service running in the named cluster.**

```
Get-ECSService -Cluster myCluster -Service my-hhtp-service
```
+  For API details, see [DescribeServices](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example shows how to retrieve details of a specific service from your default cluster.**

```
Get-ECSService -Service my-hhtp-service
```
**Example 2: This example shows how to retrieve details of a specific service running in the named cluster.**

```
Get-ECSService -Cluster myCluster -Service my-hhtp-service
```
+  For API details, see [DescribeServices](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

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

    def describe_services(
        self, cluster: str, service_names: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Describes the specified services running in a cluster.

        :param cluster: The cluster name or ARN.
        :param service_names: A list of service names or ARNs.
        :return: A list of service details.
        :raises ClientError: If the request fails (e.g., ClusterNotFoundException).
        """
        try:
            response = self.ecs_client.describe_services(
                cluster=cluster,
                services=service_names,
            )
            services = response.get("services", list())
            for svc in services:
                logger.info(
                    "Service '%s': status=%s, desired=%s, running=%s",
                    svc["serviceName"],
                    svc["status"],
                    svc["desiredCount"],
                    svc["runningCount"],
                )
            return services
        except ClientError as err:
            if err.response["Error"]["Code"] == "ClusterNotFoundException":
                logger.error(
                    "Cluster '%s' not found when describing services: %s",
                    cluster,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DescribeServices](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeServices) in *AWS SDK for Python (Boto3) API Reference*.

------
