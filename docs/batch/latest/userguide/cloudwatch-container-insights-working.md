---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch-container-insights-working.html
---

# Turn on Container Insights
<a name="cloudwatch-container-insights-working"></a>

Complete the following steps to turn on Container Insights for AWS Batch compute environments.

1. Open the [AWS Batch console](https://console.aws.amazon.com/batch/home).

1. Choose **Environments**.

1. Choose the compute environment that you want.

1. On the **Container insights** tab, turn on **Container insights** for the compute environment.
**Tip**
You can select a default interval to aggregate the metrics or create a custom interval.

By default, the following metrics are displayed. For a full list of Amazon ECS Container Insights metrics, see [Amazon ECS Container Insights Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html) in the *Amazon CloudWatch User Guide*.
+ **`TaskCount`** – The number of AWS Batch jobs running in the cluster. In the AWS Batch console, this metric is displayed as "Job Count" because AWS Batch jobs run as Amazon ECS tasks.
+ **`ContainerInstanceCount`** – The number of Amazon Elastic Compute Cloud instances that run the Amazon ECS agent and are registered in the compute environment.
+ **`MemoryReserved`** – The memory that's reserved by compute environment jobs. This metric is collected only for the jobs that have a defined memory reservation in their job definition.
+ **`MemoryUtilized`** – The memory that's being used by compute environment jobs. This metric is collected only for jobs that have a defined memory reservation in their job definition.
+ **`CpuReserved`** – The CPU units that are reserved by compute environment jobs. This metric is collected only for jobs that have a defined CPU reservation in their job definition.
+ **`CpuUtilized`** – The CPU units used by jobs in the compute environment. This metric is collected only for jobs that have a defined CPU reservation in their job definition.
+ **`NetworkRxBytes`** - The number of bytes that are received. This metric is available only for containers in jobs that use the `awsvpc` or bridge network modes.
+ **`NetworkTxBytes`** – The number of bytes that are transmitted. This metric is available only for containers in jobs that use the `awsvpc` or bridge network modes.
+ **`StorageReadBytes`** – The number of bytes that are read from storage.
+ **`StorageWriteBytes`** – The number of bytes that are written to storage.
