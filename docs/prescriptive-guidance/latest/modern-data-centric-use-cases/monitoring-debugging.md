---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/monitoring-debugging.html
---

# Monitoring and debugging
<a name="monitoring-debugging"></a>

Certain phases in the data lifecycle are not sequential but consistently present. This is true for the monitoring and debugging stage, as shown in the following diagram.

![Monitoring and debugging diagram](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/images/guide-img/058e3d2f-f726-4dc0-989b-0f15dcd3bc33/images/edf0cef6-2bc4-47c3-915b-9ac33972098d.png)

The process of data engineering must be continually monitored for correctness and performance. [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) plays a crucial role in monitoring data engineering, as it logs every error and info log to its log groups. You can use monitoring to build automated error recovery. For example, you can stop pipelines if you find that your data quality rules are not satisfied, or you can log successful runs and failed runs separately to enable a recovery action. Monitoring improves the overall reliability of the data engineering process (that is, the full ETL process) as well as the data.

Additionally, we recommend that you create CloudWatch dashboards that include the relevant metrics for the monitoring and debugging process. This can help ensure that the data engineering process is running smoothly and as expected. This is important for operations as well as reporting. For example, a CloudWatch dashboard can show users the status of loads to help them understand the reliability of their processes or what percentage of their data was dropped due to low quality or which sources have the maximum failures. A CloudWatch dashboard not only helps you visualize results but also helps you improve processes by identifying the pain points in the ETL process.
