---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_monitor_instances_post_launch_review_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF07-BP02 Analyze metrics when events or incidents occur
<a name="perf_monitor_instances_post_launch_review_metrics"></a>

 In response to (or during) an event or incident, use monitoring dashboards or reports to understand and diagnose the impact. These views provide insight into which portions of the workload are not performing as expected.

 When you write critical user stories for your architecture, include performance requirements, such as specifying how quickly each critical story should run. For these critical stories, implement additional scripted user journeys to ensure that you know how these stories perform against your requirement.

 **Common anti-patterns:**
+  You assume that performance events are one-time issues and only related to anomalies.
+  You only evaluate existing performance metrics when responding to performance events.

 **Benefits of establishing this best practice:** In determine whether your workload is operating at expected levels, you must respond to performance events by gathering additional metric data for analysis. This data is used to understand the impact of the performance event and suggest changes to improve workload performance.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Prioritize experience concerns for critical user stories: When you write critical user stories for your architecture, include performance requirements, such as specifying how quickly each critical story should run. For these critical stories, implement additional scripted user journeys to ensure that you know how the user stories perform against your requirements.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
+  [Monitoring, Logging, and Performance APN Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
+  [X-Ray Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

 **Related videos:**
+  [Cut through the chaos: Gain operational visibility and insight (MGT301-R1)](https://www.youtube.com/watch?v=nLYGbotqHd0)
+  [Optimize applications through Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y)
+  [Demo of Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=hF3NM9j-u7I)

 **Related examples:**
+  [Measure page load time with Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance)
+  [Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
