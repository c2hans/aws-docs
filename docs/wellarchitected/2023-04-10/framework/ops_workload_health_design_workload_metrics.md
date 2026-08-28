---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_workload_health_design_workload_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS08-BP02 Define workload metrics
<a name="ops_workload_health_design_workload_metrics"></a>

Define metrics that measure the health of the workload. Workload health is measured by the achievement of business outcomes (KPIs) and the state of workload components and applications. Examples of KPIs are abandoned shopping carts, orders placed, cost, price, and allocated workload expense. While you may collect telemetry from multiple components, select a subset that provides insight into the overall workload health. Adjust workload metrics over time as business needs change.

 **Desired outcome:**
+  You have identified metrics that validate the achievement of KPIs that reflect business outcomes.
+  You have metrics that show a consistent view of workload health.
+  Workload metrics are evaluated periodically as business needs change.

 **Common anti-patterns:**
+ You are monitoring all the applications in your workload but are unable to determine if your workload is achieving business outcomes.
+ You have defined workload metrics but they are not associated to any business KPIs.

 **Benefits of establishing this best practice:**
+  You can measure your workload against the achievement of business outcomes.
+  You know if your workload is in a healthy state or needs intervention.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 The goal of this best practice is that you can answer the following question: is my workload healthy? Workload health is determined by the achievement of business outcomes and the state of applications and components in the workload. Work backwards from business KPIs to identify metrics. Identify key metrics from components and applications. Periodically review workload metrics as business needs change.

 **Customer example**

 Workload health is determined at AnyCompany Retail by a collection of application and component metrics. Starting with business KPIs, they identify metrics like order rate that can show they are achieving business outcomes. They also include key application metrics like page response and component metrics like open database connections. On a quarterly basis, they re-evaluate workload metrics to make sure they are still valid in determining workload health.

 **Implementation steps**

1.  Starting with business KPIs, identify metrics that show you are achieving business outcomes. If there are KPIs that do not have metrics, instrument your workload with additional metrics for any missing business KPIs.

   1.  You can publish custom metrics from your applications to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

   1.  The [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) can collect metrics from existing applications and be used to add new metrics.

   1.  Customers with Enterprise Support can request the [Building a Monitoring Strategy Workshop](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/) from their Technical Account Manager. This workshop will help you build an observability strategy for your workload.

1.  Identify metrics for applications and components in the workload. What are key metrics that show the health of individual components and applications? Applications and components may emit many different metrics, but choose one to three key metrics that show their overall health.

1.  Implement a mechanism to evaluate workload metrics periodically. When business KPIs change, work with stakeholders to update workload metrics. As your workload components and applications evolve, adjust your workload metrics.

 **Level of effort for the implementation plan:** Medium. Adding metrics for business KPIs to applications may require moderate effort.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS04-BP01 Implement application telemetry](ops_telemetry_application_telemetry.md) - Your application must emit telemetry that supports business outcomes.
+  [OPS04-BP02 Implement and configure workload telemetry](ops_telemetry_workload_telemetry.md) - You must instrument your workload to emit telemetry before you can define workload metrics that support business outcomes.
+  [OPS08-BP01 Identify key performance indicators](ops_workload_health_define_workload_kpis.md) - You must identify key performance indicators first before selecting workload metrics.

 **Related documents:**
+ [ Adding metrics and traces to your application on Amazon EKS with AWS Distro for OpenTelemetry, AWS X-Ray, and Amazon CloudWatch ](https://aws.amazon.com/blogs/mt/adding-metrics-and-traces-to-your-application-on-amazon-eks-with-aws-distro-for-opentelemetry-aws-x-ray-and-amazon-cloudwatch/)
+ [ Instrumenting distributed systems for operational visibility ](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/)
+ [ Implementing health checks ](https://aws.amazon.com/builders-library/implementing-health-checks/)
+ [ How to Monitor your Applications Effectively ](https://aws.amazon.com/startups/start-building/how-to-monitor-applications/)
+ [ How to better monitor your custom application metrics using Amazon CloudWatch Agent ](https://aws.amazon.com/blogs/devops/new-how-to-better-monitor-your-custom-application-metrics-using-amazon-cloudwatch-agent/)

 **Related videos:**
+ [AWS re:Invent 2020: Monitoring production services at Amazon ](https://www.youtube.com/watch?v=hnPcf_Czbvw)
+ [AWS re:Invent 2022 - Building observable applications with OpenTelemetry (BOA310) ](https://www.youtube.com/watch?v=efk8XFJrW2c)
+ [ How to Easily Setup Application Monitoring for Your AWS Workloads - AWS Online Tech Talks ](https://www.youtube.com/watch?v=LKCth30RqnA)
+ [ Mastering Observability of Your Serverless Applications - AWS Online Tech Talks ](https://www.youtube.com/watch?v=CtsiXhiAUq8)

 **Related examples:**
+ [ One Observability Workshop ](https://catalog.workshops.aws/observability/en-US/intro)

 **Related services:**
+ [ Amazon CloudWatch ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [AWS Distro for OpenTelemetry ](https://aws-otel.github.io/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
