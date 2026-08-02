---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/ops_workload_observability_analyze_workload_logs.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS08-BP02 Analyze workload logs
<a name="ops_workload_observability_analyze_workload_logs"></a>

 Regularly analyzing workload logs is essential for gaining a deeper understanding of the operational aspects of your application. By efficiently sifting through, visualizing, and interpreting log data, you can continually optimize application performance and security.

 **Desired outcome:** Rich insights into application behavior and operations derived from thorough log analysis, ensuring proactive issue detection and mitigation.

 **Common anti-patterns:**
+ Neglecting the analysis of logs until a critical issue arises.
+ Not using the full suite of tools available for log analysis, missing out on critical insights.
+  Solely relying on manual review of logs without leveraging automation and querying capabilities.

 **Benefits of establishing this best practice:**
+ Proactive identification of operational bottlenecks, security threats, and other potential issues.
+ Efficient utilization of log data for continuous application optimization.
+  Enhanced understanding of application behavior, aiding in debugging and troubleshooting.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) is a powerful tool for log analysis. Integrated features like CloudWatch Logs Insights and Contributor Insights make the process of deriving meaningful information from logs intuitive and efficient.

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up CloudWatch Logs:** Configure applications and services to send logs to CloudWatch Logs.

1.  **Set up CloudWatch Logs Insights:** Use [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to interactively search and analyze your log data.

   1.  Craft queries to extract patterns, visualize log data, and derive actionable insights.

1.  **Leverage Contributor Insights:** Use [CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) to identify top talkers in high cardinality dimensions like IP addresses or user-agents.

1.  **Implement CloudWatch Logs metric filters:** Configure [CloudWatch log metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) to convert log data into actionable metrics. This allows you to set alarms or further analyze patterns.

1.  **Regular review and refinement:** Periodically review your log analysis strategies to capture all relevant information and continually optimize application performance.

 **Level of effort for the implementation plan:** Medium

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS04-BP01 Identify key performance indicators](ops_observability_identify_kpis.md)
+  [OPS04-BP02 Implement application telemetry](ops_observability_application_telemetry.md)
+  [OPS08-BP01 Analyze workload metrics](ops_workload_observability_analyze_workload_metrics.md)

 **Related documents:**
+ [ Analyzing Log Data with CloudWatch Logs Insights ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
+ [ Using CloudWatch Contributor Insights ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html)
+ [ Creating and Managing CloudWatch Logs Log Metric Filters ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)

 **Related videos:**
+ [ Analyze Log Data with CloudWatch Logs Insights ](https://www.youtube.com/watch?v=2s2xcwm8QrM)
+ [ Use CloudWatch Contributor Insights to Analyze High-Cardinality Data ](https://www.youtube.com/watch?v=ErWRBLFkjGI)

 **Related examples:**
+ [ CloudWatch Logs Sample Queries ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html)
+ [ One Observability Workshop ](https://catalog.workshops.aws/observability/en-US/intro)
