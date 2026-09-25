---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ecs_example_ecs_RegisterTaskDefinition_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RegisterTaskDefinition` with an AWS SDK or CLI
<a name="ecs_example_ecs_RegisterTaskDefinition_section"></a>

The following code examples show how to use `RegisterTaskDefinition`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Configure container service connectivity](ecs_example_ecs_ServiceConnect_085_section.md)
+  [Create a container task for the serverless launch type](ecs_example_ecs_GettingStarted_086_section.md)
+  [Creating a container service for virtual machine instances](ecs_example_ecs_GettingStarted_018_section.md)
+  [Learn Amazon ECS basics](ecs_example_ecs_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**Example 1: To register a task definition with a JSON file**
The following `register-task-definition` example registers a task definition to the specified family. The container definitions are saved in JSON format at the specified file location.

```
aws ecs register-task-definition \
    --cli-input-json {{file://<path_to_json_file>/sleep360.json}}
```
Contents of `sleep360.json`:

```
{
    "containerDefinitions": [
        {
            "name": "sleep",
            "image": "busybox",
            "cpu": 10,
            "command": [
                "sleep",
                "360"
            ],
            "memory": 10,
            "essential": true
        }
    ],
    "family": "sleep360"
}
```
Output:

```
{
    "taskDefinition": {
        "status": "ACTIVE",
        "family": "sleep360",
        "placementConstraints": [],
        "compatibilities": [
                "EXTERNAL",
                "EC2"
        ],
        "volumes": [],
        "taskDefinitionArn": "arn:aws:ecs:us-east-1:123456789012:task-definition/sleep360:1",
        "containerDefinitions": [
            {
                "environment": [],
                "name": "sleep",
                "mountPoints": [],
                "image": "busybox",
                "cpu": 10,
                "portMappings": [],
                "command": [
                    "sleep",
                    "360"
                ],
        "memory": 10,
        "essential": true,
        "volumesFrom": []
        }
    ],
        "revision": 1
    }
}
```
For more information, see [Example task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/example_task_definitions.html) in the *Amazon ECS Developer Guide*.
**Example 2: To register a task definition with a JSON string parameter**
The following `register-task-definition` example registers a task definition using container definitions provided as a JSON string parameter with escaped double quotes.

```
aws ecs register-task-definition \
    --family {{sleep360}} \
    --container-definitions "[{\"name\":\"sleep\",\"image\":\"busybox\",\"cpu\":10,\"command\":[\"sleep\",\"360\"],\"memory\":10,\"essential\":true}]"
```
The output is identical to the previous example.
For more information, see [Creating a Task Definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html) in the *Amazon ECS Developer Guide*.
+  For API details, see [RegisterTaskDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/register-task-definition.html) in *AWS CLI Command Reference*.

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

    def register_task_definition(
        self,
        family: str,
        execution_role_arn: str,
        container_definitions: Optional[List[Dict[str, Any]]] = None,
        cpu: str = "256",
        memory: str = "512",
    ) -> Dict[str, Any]:
        """
        Registers a new task definition for Fargate.

        :param family: The family name for the task definition.
        :param execution_role_arn: The ARN of the task execution IAM role.
        :param container_definitions: List of container definitions. If None, a
            default httpd container is used.
        :param cpu: The task-level CPU units (e.g., '256').
        :param memory: The task-level memory in MiB (e.g., '512').
        :return: The task definition details from the response.
        :raises ClientError: If the request fails (e.g., InvalidParameterException).
        """
        if container_definitions is None:
            container_definitions = [
                {
                    "name": "sample-app",
                    "image": "public.ecr.aws/docker/library/httpd:2.4",
                    "essential": True,
                    "portMappings": [
                        {
                            "containerPort": 80,
                            "hostPort": 80,
                            "protocol": "tcp",
                        }
                    ],
                    "cpu": 256,
                    "memory": 512,
                }
            ]
        try:
            response = self.ecs_client.register_task_definition(
                family=family,
                networkMode="awsvpc",
                requiresCompatibilities=["FARGATE"],
                cpu=cpu,
                memory=memory,
                executionRoleArn=execution_role_arn,
                containerDefinitions=container_definitions,
            )
            task_def = response["taskDefinition"]
            logger.info(
                "Registered task definition '%s' revision %s, ARN: %s",
                task_def["family"],
                task_def["revision"],
                task_def["taskDefinitionArn"],
            )
            return task_def
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidParameterException":
                logger.error(
                    "Invalid parameter when registering task definition '%s': %s",
                    family,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [RegisterTaskDefinition](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/RegisterTaskDefinition) in *AWS SDK for Python (Boto3) API Reference*.

------
