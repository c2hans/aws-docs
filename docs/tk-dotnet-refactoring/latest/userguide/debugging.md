---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/debugging.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Debugging
<a name="debugging"></a>

This section contains debugging information for Toolkit for .NET Refactoring.

## Debugging the deployment using Amazon ECS execute-command
<a name="debugging-information"></a>

You can use Amazon ECS to run commands, such as bash and sh commands, in a task that is running.

1. To use Amazon ECS to run a command, open Amazon ECS in the AWS Management Console and navigate to the cluster and the task that contains the application. The cluster will be named `{{<application_id>}}-cluster`.

1. Locate a single service in the cluster and locate an active task in the cluster. Use the cluster name and task ID in an AWS CLI command:

   ```
   aws ecs execute-command --cluster {{<cluster_name>}} \
       --task {{<task_id>}} \
       --container app \
       --interactive \
       --command "bash"
   ```

For more information, see the **Running commands using Amazon ECS Exec** section of [Using Amazon ECS Exec for debugging](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html) in the *Amazon ECS User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for NET Refactoring. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tk-dotnet-refactoring` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
