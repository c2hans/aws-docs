---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/ops_observability_application_telemetry.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS04-BP02 Implement application telemetry
<a name="ops_observability_application_telemetry"></a>

 Application telemetry serves as the foundation for observability of your workload. It's crucial to emit telemetry that offers actionable insights into the state of your application and the achievement of both technical and business outcomes. From troubleshooting to measuring the impact of a new feature or ensuring alignment with business key performance indicators (KPIs), application telemetry informs the way you build, operate, and evolve your workload.

 Metrics, logs, and traces form the three primary pillars of observability. These serve as diagnostic tools that describe the state of your application. Over time, they assist in creating baselines and identifying anomalies. However, to ensure alignment between monitoring activities and business objectives, it's pivotal to define and monitor KPIs. Business KPIs often make it easier to identify issues compared to technical metrics alone.

 Other telemetry types, like real user monitoring (RUM) and synthetic transactions, complement these primary data sources. RUM offers insights into real-time user interactions, whereas synthetic transactions simulate potential user behaviors, helping detect bottlenecks before real users encounter them.

 **Desired outcome:** Derive actionable insights into the performance of your workload. These insights allow you to make proactive decisions about performance optimization, achieve increased workload stability, streamline CI/CD processes, and utilize resources effectively.

 **Common anti-patterns:**
+  Incomplete observability: Neglecting to incorporate observability at every layer of the workload, resulting in blind spots that can obscure vital system performance and behavior insights.
+  Fragmented data view: When data is scattered across multiple tools and systems, it becomes challenging to maintain a holistic view of your workload's health and performance.
+  User-reported issues: A sign that proactive issue detection through telemetry and business KPI monitoring is lacking.

 **Benefits of establishing this best practice:**
+  Informed decision-making: With insights from telemetry and business KPIs, you can make data-driven decisions.
+  Improved operational efficiency: Data-driven resource utilization leads to cost-effectiveness.
+  Enhanced workload stability: Faster detection and resolution of issues leading to improved uptime.
+  Streamlined CI/CD processes: Insights from telemetry data facilitate refinement of processes and reliable code delivery.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 To implement application telemetry for your workload, use AWS services like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [AWS X-Ray](https://aws.amazon.com/xray/). Amazon CloudWatch provides a comprehensive suite of monitoring tools, allowing you to observe your resources and applications in AWS and on-premises environments. It collects, tracks, and analyzes metrics, consolidates and monitors log data, and responds to changes in your resources, enhancing your understanding of how your workload operates. In tandem, AWS X-Ray lets you trace, analyze, and debug your applications, giving you a deep understanding of your workload's behavior. With features like service maps, latency distributions, and trace timelines, X-Ray provides insights into your workload's performance and the bottlenecks affecting it.

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify what data to collect:** Ascertain the essential metrics, logs, and traces that would offer substantial insights into your workload's health, performance, and behavior.

1.  **Deploy the [CloudWatch](https://aws.amazon.com/cloudwatch/) agent:** The CloudWatch agent is instrumental in procuring system and application metrics and logs from your workload and its underlying infrastructure. The CloudWatch agent can also be used to collect OpenTelemetry or X-Ray traces and send them to X-Ray.

1.  **Define and monitor business KPIs:** Establish [custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) that align with your [business outcomes](https://aws-observability.github.io/observability-best-practices/guides/operational/business/monitoring-for-business-outcomes/).

1.  **Instrument your application with AWS X-Ray:** In addition to deploying the CloudWatch agent, it's crucial to [instrument your application](https://docs.aws.amazon.com/xray/latest/devguide/xray-instrumenting-your-app.html) to emit trace data. This process can provide further insights into your workload's behavior and performance.

1.  **Standardize data collection across your application:** Standardize data collection practices across your entire application. Uniformity aids in correlating and analyzing data, providing a comprehensive view of your application's behavior.

1.  **Analyze and act on the data:** Once data collection and normalization are in place, use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/features/) for metrics and logs analysis, and [AWS X-Ray](https://aws.amazon.com/xray/features/) for trace analysis. Such analysis can yield crucial insights into your workload's health, performance, and behavior, guiding your decision-making process.

 **Level of effort for the implementation plan:** High

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS04-BP01 Identify key performance indicators](ops_observability_identify_kpis.md)
+  [OPS04-BP03 Implement user experience telemetry](ops_observability_customer_telemetry.md)
+  [OPS04-BP04 Implement dependency telemetry](ops_observability_dependency_telemetry.md)
+  [OPS04-BP05 Implement distributed tracing](ops_observability_dist_trace.md)

 **Related documents:**
+ [AWS Observability Best Practices ](https://aws-observability.github.io/observability-best-practices/)
+ [ CloudWatch User Guide ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [AWS X-Ray Developer Guide ](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
+ [ Instrumenting distributed systems for operational visibility ](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility)
+ [AWS Observability Skill Builder Course ](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14688/aws-observability)
+ [ What's New with Amazon CloudWatch ](https://aws.amazon.com/about-aws/whats-new/management-and-governance/?whats-new-content.sort-by=item.additionalFields.postDateTime&whats-new-content.sort-order=desc&awsf.whats-new-products=general-products%23amazon-cloudwatch)
+ [ What's New with AWS X-Ray](https://aws.amazon.com/about-aws/whats-new/developer-tools/?whats-new-content.sort-by=item.additionalFields.postDateTime&whats-new-content.sort-order=desc&awsf.whats-new-products=general-products%23aws-x-ray)

 **Related videos:**
+ [AWS re:Invent 2022 - Observability best practices at Amazon ](https://youtu.be/zZPzXEBW4P8)
+ [AWS re:Invent 2022 - Developing an observability strategy ](https://youtu.be/Ub3ATriFapQ)

 **Related examples:**
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US)
+ [AWS Solutions Library: Application Monitoring with Amazon CloudWatch ](https://aws.amazon.com/solutions/implementations/application-monitoring-with-cloudwatch)
