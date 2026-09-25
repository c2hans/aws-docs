---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ecs_example_ecs_DeregisterTaskDefinition_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeregisterTaskDefinition` with an AWS SDK or CLI
<a name="ecs_example_ecs_DeregisterTaskDefinition_section"></a>

The following code examples show how to use `DeregisterTaskDefinition`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Configure container service connectivity](ecs_example_ecs_ServiceConnect_085_section.md)
+  [Create a container task for the serverless launch type](ecs_example_ecs_GettingStarted_086_section.md)
+  [Creating a container service for virtual machine instances](ecs_example_ecs_GettingStarted_018_section.md)
+  [Learn Amazon ECS basics](ecs_example_ecs_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To deregister a task definition**
The following `deregister-task-definition` example deregisters the first revision of the `curler` task definition in your default region.

```
aws ecs deregister-task-definition --task-definition {{curler:1}}
```
Note that in the resulting output, the task definition status shows `INACTIVE`:

```
{
    "taskDefinition": {
        "status": "INACTIVE",
        "family": "curler",
        "volumes": [],
        "taskDefinitionArn": "arn:aws:ecs:us-west-2:123456789012:task-definition/curler:1",
        "containerDefinitions": [
            {
                "environment": [],
                "name": "curler",
                "mountPoints": [],
                "image": "curl:latest",
                "cpu": 100,
                "portMappings": [],
                "entryPoint": [],
                "memory": 256,
                "command": [
                    "curl -v http://example.com/"
                ],
                "essential": true,
                "volumesFrom": []
            }
        ],
        "revision": 1
    }
}
```
For more information, see [Amazon ECS Task Definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) in the *Amazon ECS Developer Guide*.
+  For API details, see [DeregisterTaskDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/deregister-task-definition.html) in *AWS CLI Command Reference*.

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

    def deregister_task_definition(self, task_definition: str) -> Dict[str, Any]:
        """
        Deregisters a task definition.

        :param task_definition: The family:revision of the task definition.
        :return: The deregistered task definition details.
        :raises ClientError: If the request fails (e.g., InvalidParameterException).
        """
        try:
            response = self.ecs_client.deregister_task_definition(
                taskDefinition=task_definition,
            )
            task_def = response["taskDefinition"]
            logger.info(
                "Deregistered task definition '%s' (status: %s)",
                task_def["taskDefinitionArn"],
                task_def["status"],
            )
            return task_def
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidParameterException":
                logger.error(
                    "Invalid parameter when deregistering task definition '%s': %s",
                    task_definition,
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeregisterTaskDefinition](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DeregisterTaskDefinition) in *AWS SDK for Python (Boto3) API Reference*.

------
