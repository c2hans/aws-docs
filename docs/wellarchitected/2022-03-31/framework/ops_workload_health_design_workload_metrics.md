---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_workload_health_design_workload_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS08-BP02 Define workload metrics
<a name="ops_workload_health_design_workload_metrics"></a>

 Define workload metrics to measure the achievement of KPIs (for example, abandoned shopping carts, orders placed, cost, price, and allocated workload expense). Define workload metrics to measure the health of the workload (for example, interface response time, error rate, requests made, requests completed, and utilization). Evaluate metrics to determine if the workload is achieving desired outcomes, and to understand the health of the workload.

 You should send log data to a service such as CloudWatch Logs, and generate metrics from observations of necessary log content.

 CloudWatch has specialized features such as [Amazon CloudWatch Insights for .NET and SQL Server](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-what-is.html) and [Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) that can assist you by identifying and setting up key metrics, logs, and alarms across your specifically supported application resources and technology stack.

 **Common anti-patterns:**
+  You have defined standard metrics, not associated to any KPIs or tailored to any workload.
+  You have errors in your metrics calculations that will yield invalid results.
+  You don't have any metrics defined for your workload.
+  You only measure for availability.

 **Benefits of establishing this best practice:** By defining and evaluating workload metrics you can determine the health of your workload and measure the achievement of business outcomes.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Define workload metrics: Define workload metrics to measure the achievement of KPIs. Define workload metrics to measure the health of the workload and its individual components. Evaluate metrics to determine if the workload is achieving desired outcomes, and to understand the health of the workload.
  +  [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
  +  [Searching and filtering log data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)
  +  [Amazon CloudWatch metrics and dimensions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon CloudWatch metrics and dimensions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)
+  [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
+  [Searching and filtering log data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)
