---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_workload_health_workload_metric_baselines.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS08-BP04 Establish workload metrics baselines
<a name="ops_workload_health_workload_metric_baselines"></a>

Establishing a baseline for workload metrics aids in understanding workload health and performance. Using baselines, you can identify under- and over-performing applications and components. A workload baseline adds to your ability to mitigate issues before they become incidents. Baselines are foundational in developing patterns of activity and implementing anomaly detection when metrics deviate from expected values.

 **Desired outcome:**
+  You have a baseline level of metrics for your workload under normal conditions.
+  You can determine if your workload is functioning normally.

 **Common anti-patterns:**
+  After deploying a new feature, there is drop in request latency. A baseline was not established for a composite metric of incoming processed requests and overall latency. You are unable to determine if the change caused an improvement or caused a defect.
+  A sudden spike in user activity occurs, but you have not established a metric baseline. The activity spike slowly leads to a memory leak in an application. Eventually this takes your workload offline.

 **Benefits of establishing this best practice:**
+  You understand the normal pattern of activity for your workload using metrics for key components and applications.
+  You can determine if your workload, its applications, and components, are behaving normally or may require intervention.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Use historical data to establish a baseline of workload metrics for applications and components in your workload. Leverage the metric baseline in metric review meetings and troubleshooting. Periodically review workload performance and adjust the baseline as the architecture evolves.

 **Customer example**

 Baselines are established for all components and applications at AnyCompany Retail. Using historical data, AnyCompany Retail developed their workload metric baselines over a two-month metric window. Every two months they re-assess baselines and adjust them based on real-world data.

 **Implementation steps**

1.  Working backwards from your workload metrics, establish a metric baseline for key components and applications using historical data. Limit the number of metrics per component or application and avoid monitor fatigue.

   1.  You can use [Amazon CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html) to query metrics at scale and identify trends and patterns.

   1.  [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) uses machine learning algorithms to identify patterns of behavior for metrics, determine baselines, and surfaces anomalies.

   1.  [Amazon DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html) provides the ability to detect operational issues with your workload using machine learning.

   1.  Customers with Enterprise Support can request the [Building a Monitoring Strategy Workshop](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/) from their Technical Account Manager. This workshop will help you build an observability strategy for your workload.

1.  Put in place a mechanism to periodically review workload metric baselines, especially before significant business events. At least once a quarter, evaluate your workload metric baseline using historical data. Use the baseline in your metric review meetings.

 **Level of effort for the implementation plan:** Low. Having established workload metrics, establishing baselines may require you to collect enough data to identify normal patterns of behavior.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS08-BP02 Define workload metrics](ops_workload_health_design_workload_metrics.md) - Workload metrics must be established first before determining baselines.
+  [OPS08-BP03 Collect and analyze workload metrics](ops_workload_health_collect_analyze_workload_metrics.md) - Collecting and analyzing workload metrics is necessary to have in place before establishing metric baselines.
+  [OPS08-BP05 Learn expected patterns of activity for workload](ops_workload_health_learn_workload_usage_patterns.md) - This best practice builds on top of the baseline to develop usage trends.
+  [OPS08-BP06 Alert when workload outcomes are at risk](ops_workload_health_workload_outcome_alerts.md) - Metric baselines are necessary to identifying thresholds and developing alerts.
+  [OPS08-BP07 Alert when workload anomalies are detected](ops_workload_health_workload_anomaly_alerts.md) - Anomaly detection requires the establishment of metric baselines.

 **Related documents:**
+ [AWS Observability Best Practices - Alarms ](https://aws-observability.github.io/observability-best-practices/tools/alarms/)
+ [ How to Monitor your Applications Effectively ](https://aws.amazon.com/startups/start-building/how-to-monitor-applications/)
+ [ How to set up CloudWatch Anomaly Detection to set dynamic alarms, automate actions, and drive online sales ](https://aws.amazon.com/blogs/mt/how-to-set-up-cloudwatch-anomaly-detection-to-set-dynamic-alarms-automate-actions-and-drive-online-sales/)
+ [ Operationalizing CloudWatch Anomaly Detection ](https://aws.amazon.com/blogs/mt/operationalizing-cloudwatch-anomaly-detection/)

 **Related videos:**
+ [AWS re:Invent 2020: Monitoring production services at Amazon ](https://www.youtube.com/watch?v=hnPcf_Czbvw)
+ [AWS re:Invent 2021- Get insights from operational metrics at scale with CloudWatch Metrics Insights ](https://www.youtube.com/watch?v=xKib0xvbIfo)
+ [AWS re:Invent 2022 - Developing an observability strategy (COP302) ](https://www.youtube.com/watch?v=Ub3ATriFapQ)
+ [AWS Summit DC 2022 - Monitoring and observability for modern applications ](https://www.youtube.com/watch?v=AHiuyT0B5Gk)
+ [AWS Summit SF 2022 - Full-stack observability and application monitoring with AWS (COP310) ](https://www.youtube.com/watch?v=or7uFFyHIX0)

 **Related examples:**
+ [AWS CloudTrail and Amazon CloudWatch Integration Workshop ](https://catalog.us-east-1.prod.workshops.aws/workshops/2e48b9fc-f721-4417-b811-962b7f31b61c/en-US)

 **Related services:**
+ [ Amazon CloudWatch ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [ Amazon DevOps Guru ](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
