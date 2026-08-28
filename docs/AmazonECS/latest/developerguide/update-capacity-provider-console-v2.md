---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-capacity-provider-console-v2.html
---

# Updating an Amazon ECS capacity provider
<a name="update-capacity-provider-console-v2"></a>

When you use an Auto Scaling group as a capacity provider, you can modify the group's scaling policy.

**To update a capacity provider for the cluster (Amazon ECS console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, choose the cluster.

1. On the **Cluster : {{name}}** page, choose **Infrastructure**, and then choose **Update**.

1. On the **Create capacity providers** page, configure the following options.

   1. Under **Auto Scaling group**, under **Scaling policies**, configure the following options.
     + To have Amazon ECS manage the scale-in and scale-out actions, select **Turn on managed scaling**.
     + To prevent EC2 instances with running Amazon ECS tasks from being terminated, select **Turn on scaling protection**.
     + For **Set target capacity**, enter the target value for the CloudWatch metric used in the Amazon ECS-managed target tracking scaling policy.

1. Choose **Update**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
