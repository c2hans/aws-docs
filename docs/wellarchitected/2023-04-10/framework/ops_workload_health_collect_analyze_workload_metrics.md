---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_workload_health_collect_analyze_workload_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS08-BP03 Collect and analyze workload metrics
<a name="ops_workload_health_collect_analyze_workload_metrics"></a>

Perform regular, proactive reviews of workload metrics to identify trends and determine if a response is necessary and validate the achievement of business outcomes. Aggregate metrics from your workload applications and components to a central location. Use dashboards and analytics tools to analyze telemetry and determine workload health. Implement a mechanism to conduct workload health reviews on periodic basis with stakeholders in your organization.

 **Desired outcome:**
+  Workload metrics are collected in a central location.
+  Dashboards and analytics tools are used to analyze workload health trends.
+  You conduct periodic workload metric reviews with your organization.

 **Common anti-patterns:**
+  Your organization collects metrics from the workload in two different observability platforms. You are unable to determine workload health because the platforms are incompatible.
+  Error rates for a component of your workload are slowly increasing. You fail to notice this trend because your organization does not conduct periodic workload metric reviews. The component fails after a week, impairing your workload.

 **Benefits of establishing this best practice:**
+  You have increased awareness of workload health and the achievement of business outcomes.
+  Workload health trends can be developed over time.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Collect workload metrics in a central location. Using dashboards and analytics tools, analyze workload metrics to gain insight into workload health, develop workload health trends, and validate the achievement of business outcomes. Implement a mechanism to conduct periodic reviews of workload metrics.

 **Customer example**

 AnyCompany Retail conducts workload metric reviews every week on Wednesday. They gather stakeholders from across the company and go through the previous week’s metrics. During the meeting, they highlight trends and insights gleaned from analytics tools. Internal dashboards are published with key workload metrics that any employee can view and search.

 **Implementation steps**

1.  Identify the workload metrics that are tied to workload health. Starting with business KPIs, identify the metrics for applications, components, and platforms that provide an overall view of workload health.

   1.  You can publish custom metrics to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html). You can leverage the [Amazon CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) to collect metrics and logs from Amazon EC2 instances and on-premises servers.

   1.  The [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) can collect metrics from existing applications and be used to add new metrics.

   1.  Customers with Enterprise Support can request the [Building a Monitoring Strategy Workshop](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/) from their Technical Account Manager. This workshop helps you build an observability strategy for your workload.

1.  Collect workload metrics in a central platform. If workload metrics are split between different platform, this can make it difficult to analyze and develop trends. The platform should have dashboards and analytic capabilities.

   1.  [Amazon CloudWatch](https://docs.aws.amazon.com/) can collect and store workload metrics. In multi-account topologies, it is recommended to have a [central logging and monitoring account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html), referred to as a *log archive account*.

1.  Build a consolidated dashboard of workload metrics. Use this view for metrics reviews and analysis of trends.

   1.  You can create custom [CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) to collect your workload metrics in a consolidated view.

1.  Implement a workload metric review process. On a weekly, bi-weekly, or monthly basis, review your workload metrics with stakeholders, including technical and non-technical personnel. Use these review sessions to identify trends and gain insight into workload health.

 **Level of effort for the implementation plan:** High. If workload metrics are not centrally collected, it could require significant investment to consolidate them in one platform.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS08-BP01 Identify key performance indicators](ops_workload_health_define_workload_kpis.md) - You must identify key performance indicators first before selecting workload metrics.
+  [OPS08-BP02 Define workload metrics](ops_workload_health_design_workload_metrics.md) - You must define workload metrics before collecting and analyzing them.

 **Related documents:**
+ [ Power operational insights with Amazon Quick ](https://aws.amazon.com/blogs/big-data/power-operational-insights-with-amazon-quicksight/)
+ [ Using Amazon CloudWatch dashboards custom widgets ](https://aws.amazon.com/blogs/mt/introducing-amazon-cloudwatch-dashboards-custom-widgets/)

 **Related videos:**
+ [ Create Cross Account & Cross Region CloudWatch Dashboards ](https://www.youtube.com/watch?v=eIUZdaqColg)
+ [ Monitor AWS Resources Using Amazon CloudWatch Dashboards ](https://www.youtube.com/watch?v=I7EFLChc07M)

 **Related examples:**
+ [AWS Management and Governance Tools Workshop - CloudWatch Dashboards ](https://mng.workshop.aws/operations-2022/detect/cwdashboard.html)
+ [ Well-Architected Labs - Level 100: Monitoring with CloudWatch Dashboards ](https://www.wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_with_cloudwatch_dashboards/)

 **Related services:**
+  [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [AWS Distro for OpenTelemetry](https://aws-otel.github.io/)
