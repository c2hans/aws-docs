---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/increase-container-resources.html
---

# Increase the container resources
<a name="increase-container-resources"></a>

To increase the number of concurrent virtual users (concurrency) your load tests can simulate, you need to increase the CPU and memory resources allocated to each Amazon ECS task. This involves creating a new task definition revision with higher resource limits, then updating the solution’s DynamoDB configuration to use the new task definition for future test runs.

## Create a new task definition revision
<a name="create-new-task-definition"></a>

Follow these steps to create a new task definition with increased CPU and memory resources:

1. Sign in to the [Amazon Elastic Container Service console](https://console.aws.amazon.com/ecs/home).

1. In the left navigation menu, select **Task Definitions**.

1. Select the checkbox next to the task definition that corresponds to this solution. For example, `[replaceable]`<stackName>`-EcsTaskDefinition-{{<system-generated-random-Hash>}}.

1. Choose **Create new revision**.

1. On the **Create new revision** page, take the following actions:

   1. Under **Task size**, modify the **Task memory** and **Task CPU** to your desired values. Higher values allow more concurrent virtual users per task.

   1. Under **Container Definitions**, review the **Hard/Soft memory limits**. If this limit is lower than your desired memory, choose the container.

   1. In the **Edit container** dialog box, go to **Memory Limits** and update the **Hard Limit** to match or be less than your task memory allocation.

   1. Choose **Update**.

1. On the **Create new revision** page, choose **Create**.

1. After the task definition is successfully created, record the complete task definition ARN including the version number. For example: `[replaceable]`<stackName>`-EcsTaskDefinition-{{<system-generated-random-Hash>}}:[replaceable]`<system-generated-versionNumber>`.

## Update the DynamoDB table
<a name="update-dynamodb-table"></a>

After creating the new task definition revision, you must update the solution’s DynamoDB table so that future test runs use the new task definition. Repeat these steps for each AWS Region where you want to use the updated task definition:

1. Navigate to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/home).

1. From the left navigation pane, select **Explore Items** under **Tables**.

1. Select the `scenarios-table` DynamoDB table associated with this solution. For example, `[replaceable]`<stackName>`-DLTTestRunnerStorageDLTScenariosTable-{{<system-generated-random-Hash>}}.

1. Select the item that corresponds to the Region in which you created the new task definition revision. For example, `region-[replaceable]`<region-name>`.

1. In the item editor, locate the **taskDefinition** attribute and update its value with the complete task definition ARN you recorded in the previous section (including the version number).

1. Choose **Save changes**.

**Note**
The updated task definition will only be used for new test runs. Any tests that are currently running or scheduled will continue to use the previous task definition.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Distributed Load Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
