---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_process_culture_establish_key_performance_indicators.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP01 Establish key performance indicators (KPIs) to measure workload health and performance
<a name="perf_process_culture_establish_key_performance_indicators"></a>

 Identify the KPIs that quantitatively and qualitatively measure workload performance. KPIs help you measure the health and performance of a workload related to a business goal.

 **Common anti-patterns:**
+  You only monitor system-level metrics to gain insight into your workload and don’t understand business impacts to those metrics.
+  You assume that your KPIs are already being published and shared as standard metric data.
+  You do not define a quantitative, measurable KPI.
+  You do not align KPIs with business goals or strategies.

 **Benefits of establishing this best practice:** Identifying specific KPIs that represent workload health and performance helps align teams on their priorities and define successful business outcomes. Sharing those metrics with all departments provides visibility and alignment on thresholds, expectations, and business impact.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 KPIs allow business and engineering teams to align on the measurement of goals and strategies and how these factors combine to produce business outcomes. For example, a website workload might use page load time as an indication of overall performance. This metric would be one of multiple data points that measures user experience. In addition to identifying the page load time thresholds, you should document the expected outcome or business risk if ideal performance is not met. A long page load time affects your end users directly, decreases their user experience rating, and can lead to a loss of customers. When you define your KPI thresholds, combine both industry benchmarks and your end user expectations. For example, if the current industry benchmark is a webpage loading within a two-second time period, but your end users expect a webpage to load within a one-second time period, then you should take both of these data points into consideration when establishing the KPI.

 Your team must evaluate your workload KPIs using real-time granular data and historical data for reference and create dashboards that perform metric math on your KPI data to derive operational and utilization insights. KPIs should be documented and include thresholds that support business goals and strategies, and should be mapped to metrics being monitored. KPIs should be revisited when business goals, strategies, or end user requirements change.

## Implementation steps
<a name="implementation-steps"></a>

1.  Identify and document key business stakeholders.

1.  Work with these stakeholders to define and document objectives of your workload.

1.  Review industry best practices to identify relevant KPIs aligned with your workload objectives.

1.  Use industry best practices and your workload objectives to set targets for your workload KPI. Use this information to set KPI thresholds for severity or alarm level.

1.  Identify and document the risk and impact if the KPI is not met.

1.  Identify and document metrics that can help you to establish the KPIs.

1.  Use monitoring tools such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) or [AWS Config](https://aws.amazon.com/config/) to collect metrics and measure KPIs.

1.  Use dashboards to visualize and communicate KPIs with stakeholders.

1.  Regularly review and analyze metrics to identify areas of workload that need to be improved.

1.  Revisit KPIs when business goals or workload performance changes.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [Monitoring, Logging, and Performance AWS Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
+  [X-Ray Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
+  [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html?ref=wellarchitected)
+  [Quick KPIs](https://docs.aws.amazon.com/quicksight/latest/user/kpi.html)

 **Related videos:**
+  [AWS re:Invent 2019: Scaling up to your first 10 million users](https://www.youtube.com/watch?v=kKjm4ehYiMs&ref=wellarchitected)
+  [Cut through the chaos: Gain operational visibility and insight](https://www.youtube.com/watch?v=nLYGbotqHd0&ref=wellarchitected)
+  [Build a Monitoring Plan](https://www.youtube.com/watch?v=OMmiGETJpfU&ref=wellarchitected)

 **Related examples:**
+  [Creating a dashboard with Quick](https://github.com/aws-samples/amazon-quicksight-sdk-proserve)
