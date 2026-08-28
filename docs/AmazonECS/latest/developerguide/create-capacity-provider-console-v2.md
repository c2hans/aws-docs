---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity-provider-console-v2.html
---

# Creating a capacity provider for Amazon ECS
<a name="create-capacity-provider-console-v2"></a>

After the cluster creation completes, you can create a new capacity provider (Auto Scaling group) for EC2. Capacity providers help to manage and scale your the infrastructure for your applications.

Before you create the capacity provider, you need to create an Auto Scaling group. For more information, see[ Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) in the *Amazon EC2 Auto Scaling User Guide*.

**To create a capacity provider for the cluster (Amazon ECS console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, choose the cluster.

1. On the **Cluster : {{name}}** page, choose **Infrastructure**, and then choose **Create**.

1. On the **Create capacity providers** page, configure the following options.

   1. Under **Basic details**, for **Capacity provider name**, enter a unique capacity provider name.

   1. Under **Auto Scaling group**, for **Use an existing Auto Scaling group**, choose the Auto Scaling group.

   1. (Optional) To configure a scaling policy, under **Scaling policies**, configure the following options.
      + To have Amazon ECS manage the scale-in and scale-out actions, select **Turn on managed scaling**.
      + To prevent EC2 instance with running Amazon ECS tasks from being terminated, select **Turn on scaling protection**.
      + For **Set target capacity**, enter the target value for the CloudWatch metric used in the Amazon ECS-managed target tracking scaling policy.

1. Choose **Create**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
