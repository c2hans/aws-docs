---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete-capacity-provider-managed-instances-console-v2.html
---

# Deleting an Amazon ECS Managed Instances capacity provider
<a name="delete-capacity-provider-managed-instances-console-v2"></a>

If you are finished using an Amazon ECS Managed Instances capacity provider, you can delete it. After the group is deleted, the Amazon ECS Managed Instances capacity provider transitions to the `INACTIVE` state. Capacity providers with an `INACTIVE` status may remain discoverable in your account for a period of time. However, this behavior is subject to change in the future, so you should not rely on `INACTIVE` capacity providers persisting. Before the Amazon ECS Managed Instances capacity provider is deleted, the capacity provider must be removed from the capacity provider strategy from all services. You can use the `UpdateService` API or the update service workflow in the Amazon ECS console to remove a capacity provider from a service's capacity provider strategy. Use the **Force new deployment** option to ensure that any tasks using the Amazon ECS Managed Instances capacity provided by the capacity provider are transitioned to use the capacity from the remaining capacity providers.

**To delete a capacity provider for the cluster (Amazon ECS console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, choose the cluster.

1. On the **Cluster : {{name}}** page, choose **Infrastructure**, the Amazon ECS Managed Instances capacity provider, and then choose **Delete**.

1. In the confirmation box, enter **delete {{Amazon ECS Managed Instances capacity provider name}}**

1. Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
