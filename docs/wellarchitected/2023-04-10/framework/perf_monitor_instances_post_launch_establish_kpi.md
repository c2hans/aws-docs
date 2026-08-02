---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_monitor_instances_post_launch_establish_kpi.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF07-BP03 Establish key performance indicators (KPIs) to measure workload performance
<a name="perf_monitor_instances_post_launch_establish_kpi"></a>

 Identify the KPIs that quantitatively and qualitatively measures workload performance. KPIs help to measure the health of a workload as it relates to a business goal. KPIs allow business and engineering teams to align on the measurement of goals and strategies and how this combines to produce business outcomes. KPIs should be revisited when business goals, strategies, or end-user requirements change.

 For example, a website workload might use the page load time as an indication of overall performance. This metric would be one of the multiple data points which measure an end user experience. In addition to identifying the page load time thresholds, you should document the expected outcome or business risk if the performance is not met. A long page load time would affect your end users directly, decrease their user experience rating and might lead to a loss of customers. When you define your KPI thresholds, combine both industry benchmarks and your end user expectations. For example, if the current industry benchmark is a webpage loading within a two second time period, but your end users expect a webpage to load within a one second time period, then you should take both of these data points into consideration when establishing the KPI. Another example of a KPI might focus on meeting internal performance needs. A KPI threshold might be established on generating sales reports within one business day after production data has been generated. These reports might directly affect daily decisions and business outcomes.

 **Desired outcome:** Establishing KPIs involve different departments and stakeholders. Your team must evaluate your workload KPIs using real-time granular data and historical data for reference and create dashboards that perform metric math on your KPI data to derive operational and utilization insights. KPIs should be documented which explains the agreed upon KPIs and thresholds that support business goals and strategies as well as mapped to metrics being monitored. The KPIs are identifying performance requirements, reviewed intentionally and are frequently shared and understood with all teams. Risks and tradeoffs are clearly identified and understood how business is impact within KPI thresholds are not met.

 **Common anti-patterns:**
+  You only monitor system level metrics to gain insight into your workload and don’t understand business impacts to those metrics.
+  You assume that your KPIs are already being published and shared as standard metric data.
+  Defining KPIs but not sharing them with all the teams.
+  Not defining a quantitative, measurable KPI.
+  Not aligning KPIs with business goals or strategies.

 **Benefits of establishing this best practice:** Identifying specific metrics which represent workload health help to align teams on their priorities and defining successful business outcomes. Sharing those metrics with all departments provides visibility and alignment on thresholds, expectations, and business impact.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 All departments and business teams impacted by the health of the workload should contribute to defining KPIs. A single person should drive the collaboration, timelines, documentation, and information related to an organization’s KPIs. This single threaded owner will often share the business goals and strategies and assign business stakeholders tasks to create KPIs in their respective departments. Once KPIs are defined, the operations team will often help define the metrics that will support and inform the success of the different KPIs. KPIs are only effective if all team members supporting a workload are aware of the KPIs.

 **Implementation steps**

1.  Identify and document business stakeholders.

1.  Identify company goals and strategies.

1.  Review common industry KPIs that align with your company goals and strategies.

1.  Review end user expectations of your workload.

1.  Define and document KPIs that support company goals and strategies.

1.  Identify and document approved tradeoff strategies to meet the KPIs.

1.  Identify and document metrics that will inform the KPIs.

1.  Identify and document KPI thresholds for severity or alarm level.

1.  Identify and document the risk and impact if the KPI is not met.

1.  Identify the frequency of review per KPI.

1.  Communicate KPI documentation with all teams supporting the workload.

** Level of effort for the implementation guidance:** Defining and communicating the KPIs is a *low* amount of work. This can typically be done over a few weeks meeting with business stakeholders, reviewing goals, strategies, and workload metrics.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [CloudWatch documentation ](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [Monitoring, Logging, and Performance APN Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
+ [X-Ray Documentation ](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
+  [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html?ref=wellarchitected)
+  [Quick KPIs](https://docs.aws.amazon.com/quicksight/latest/user/kpi.html)

 **Related videos:**
+  [AWS re:Invent 2019: Scaling up to your first 10 million users (ARC211-R)](https://www.youtube.com/watch?v=kKjm4ehYiMs&ref=wellarchitected)
+  [Cut through the chaos: Gain operational visibility and insight (MGT301-R1)](https://www.youtube.com/watch?v=nLYGbotqHd0&ref=wellarchitected)
+  [Build a Monitoring Plan](https://www.youtube.com/watch?v=OMmiGETJpfU&ref=wellarchitected)

 **Related examples:**
+  [Creating a dashboard with Quick](https://github.com/aws-samples/amazon-quicksight-sdk-proserve)
