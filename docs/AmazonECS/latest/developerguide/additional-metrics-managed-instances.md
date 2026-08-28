---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/additional-metrics-managed-instances.html
---

# Additional metrics for Amazon ECS Managed Instances
<a name="additional-metrics-managed-instances"></a>

The following table lists the additional metrics available for Amazon ECS Managed Instances when using Container Insights.

| Metric | Description | Dimensions | Unit |
| --- | --- | --- | --- |
| InstanceOSFilesystemUtilization | The percentage of total disk space that is used (os volume). | `ClusterName` - when ContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName` - when ContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName`, `ContainerInstanceId`, `EC2InstanceId` - when EnhancedContainerInsights is enabled | Percent |
| InstanceDataFilesystemUtilization | The percentage of total disk space that is used (data volume). | `ClusterName` - when ContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName` - when ContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName`, `ContainerInstanceId`, `EC2InstanceId` - when EnhancedContainerInsights is enabled | Percent |
| InstanceGPULimit | The total number of GPUs available on the instance. Available only for Amazon ECS Managed Instances running NVIDIA GPU-enabled Amazon EC2 instance types. | `ClusterName` - when EnhancedContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName` - when EnhancedContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName`, `ContainerInstanceId`, `EC2InstanceId` - when EnhancedContainerInsights is enabled | Count |
| InstanceGPUUsageTotal | The number of GPUs currently allocated to running tasks on the instance. Available only for Amazon ECS Managed Instances running NVIDIA GPU-enabled Amazon EC2 instance types. | `ClusterName` - when EnhancedContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName` - when EnhancedContainerInsights is enabled<br />`ClusterName`, `CapacityProviderName`, `ContainerInstanceId`, `EC2InstanceId` - when EnhancedContainerInsights is enabled | Count |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
