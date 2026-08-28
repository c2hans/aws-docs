---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch-container-insights-metrics.html
---

# Container Insights metrics
<a name="cloudwatch-container-insights-metrics"></a>

By default, the following metrics are displayed in the AWS Batch console under the **Container insights** tab on a compute environment detail page. For a full list of Amazon ECS Container Insights metrics, see [Amazon ECS Container Insights Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html) in the *Amazon CloudWatch User Guide*.

**Note**
These metrics are emitted for the Amazon ECS cluster associated with the AWS Batch compute environment. AWS Batch jobs run as Amazon ECS tasks on this cluster.
+ **`TaskCount`** – The number of Amazon ECS tasks running in the cluster. In the AWS Batch console, this metric is displayed as "Job Count".
+ **`ContainerInstanceCount`** – The number of Amazon Elastic Compute Cloud instances that run the Amazon ECS agent and are registered in the Amazon ECS cluster.
+ **`MemoryReserved`** – The memory that's reserved by Amazon ECS tasks in the cluster.
+ **`MemoryUtilized`** – The memory that's being used by Amazon ECS tasks in the cluster.
+ **`CpuReserved`** – The CPU units that are reserved by Amazon ECS tasks in the cluster.
+ **`CpuUtilized`** – The CPU units used by Amazon ECS tasks in the cluster.
+ **`NetworkRxBytes`** – The number of bytes that are received by Amazon ECS tasks in the cluster.
+ **`NetworkTxBytes`** – The number of bytes that are transmitted by Amazon ECS tasks in the cluster.
+ **`StorageReadBytes`** – The number of bytes that are read from storage.
+ **`StorageWriteBytes`** – The number of bytes that are written to storage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
