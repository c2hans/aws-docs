---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_telemetry_application_telemetry.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS04-BP01 Implement application telemetry
<a name="ops_telemetry_application_telemetry"></a>

 Application telemetry is the foundation for observability of your workload. Your application should emit telemetry that provides insight into the state of the application and the achievement of business outcomes. From troubleshooting to measuring the impact of a new feature, application telemetry informs the way you build, operate, and evolve your workload.

 Application telemetry consists of metrics and logs. Metrics are diagnostic information, such as your pulse or temperature. Metrics are used collectively to describe the state of your application. Collecting metrics over time can be used to develop baselines and detect anomalies. Logs are messages that the application sends about its internal state or events that occur. Error codes, transaction identifiers, and user actions are examples of events that are logged.

 **Desired Outcome:**
+  Your application emits metrics and logs that provide insight into its health and the achievement of business outcomes.
+  Metrics and logs are stored centrally for all applications in the workload.

 **Common anti-patterns:**
+  Your application doesn't emit telemetry. You are forced to rely upon your customers to tell you when something is wrong.
+  A customer has reported that your application is unresponsive. You have no telemetry and are unable to confirm that the issue exists or characterize the issue without using the application yourself to understand the current user experience.

 **Benefits of establishing this best practice:**
+  You can understand the health of your application, the user experience, and the achievement of business outcomes.
+  You can react quickly to changes in your application health.
+  You can develop application health trends.
+  You can make informed decisions about improving your application.
+  You can detect and resolve application issues faster.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Implementing application telemetry consists of three steps: identifying a location to store telemetry, identifying telemetry that describes the state of the application, and instrumenting the application to emit telemetry.

 As an example, an ecommerce company has a microservices based architecture. As part of their architectural design process they identified application telemetry that would help them understand the state of each microservice. For example, the user cart service emitted telemetry about events like add to cart, abandon cart, and length of time it took to add an item to the cart. All microservices would log errors, warnings, and transaction information. Telemetry would be sent to Amazon CloudWatch for storage and analysis.

 **Implementation steps**

 The first step is to identify a central location for telemetry storage for the applications in your workload. If you don’t have an existing platform [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) provides telemetry collection, dashboards, analysis, and event generation capabilities.

 To identify what telemetry you need, start with the following questions:
+  Is my application healthy?
+  Is my application achieving business outcomes?

   Your application should emit logs and metrics that collectively answer these questions. If you can’t answer those questions with the existing application telemetry, work with business and engineering stakeholders to create a list of telemetry that can. You can request expert technical advice from your AWS account team as you identify and develop new application telemetry.

   Once the additional application telemetry has been identified, work with your engineering stakeholders to instrument your application. [The AWS Distro for Open Telemetry](https://aws-otel.github.io/) provides APIs, libraries, and agents that collect application telemetry. [This example demonstrates how to instrument a JavaScript application with custom metrics](https://aws-otel.github.io/docs/getting-started/js-sdk/metric-manual-instr).

   Customers that want to understand the observability services that AWS offers can work through the [One Observability Workshop](https://catalog.workshops.aws/observability/en-US) on their own or request support from their AWS account team to guide them. This workshop guides you through the observability solutions at AWS and provides hands-on examples of how they’re used.

   For a deeper dive into application telemetry, read the [Instrumenting distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/) article in the Amazon Builder’s Library. It explains how Amazon instruments applications and can serve as a guide for developing your own instrumentation guidelines.

 **Level of effort for the implementation plan:** Medium

## Resources
<a name="resources"></a>

 **Related best practices:**

[OPS04-BP02 Implement and configure workload telemetry](ops_telemetry_workload_telemetry.md) – Application telemetry is a component of workload telemetry. In order to understand the health of the overall workload you need to understand the health of individual applications that make up the workload.

[OPS04-BP03 Implement user activity telemetry](ops_telemetry_customer_telemetry.md) – User activity telemetry is often a subset of application telemetry. User activity like add to cart events, click streams, or completed transactions provide insight into the user experience.

[OPS04-BP04 Implement dependency telemetry](ops_telemetry_dependency_telemetry.md) – Dependency checks are related to application telemetry and may be instrumented into your application. If your application relies on external dependencies like DNS or a database your application can emit metrics and logs on reachability, timeouts, and other events.

[OPS04-BP05 Implement transaction traceability](ops_telemetry_dist_trace.md) – Tracing transactions across a workload requires each application to emit information about how they process shared events. The way individual applications handle these events is emitted through their application telemetry.

[OPS08-BP02 Define workload metrics](ops_workload_health_design_workload_metrics.md) – Workload metrics are the key health indicators for your workload. Key application metrics are a part of workload metrics.

 **Related documents:**
+  [AWS Builders Library – Instrumenting Distributed Systems for Operational Visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/)
+  [AWS Distro for OpenTelemetry](https://aws-otel.github.io/)
+  [AWS Well-Architected Operational Excellence Whitepaper – Design Telemetry](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/design-telemetry.html)
+  [Creating metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)
+  [Implementing Logging and Monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.html)
+  [Monitoring application health and performance with AWS Distro for OpenTelemetry](https://aws.amazon.com/blogs/opensource/monitoring-application-health-and-performance-with-aws-distro-for-opentelemetry/)
+  [New – How to better monitor your custom application metrics using Amazon CloudWatch Agent](https://aws.amazon.com/blogs/devops/new-how-to-better-monitor-your-custom-application-metrics-using-amazon-cloudwatch-agent/)
+  [Observability at AWS](https://aws.amazon.com/products/management-and-governance/use-cases/monitoring-and-observability/)
+  [Scenario – Publish metrics to CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/PublishMetrics.html)
+  [Start Building – How to Monitor your Applications Effectively](https://aws.amazon.com/startups/start-building/how-to-monitor-applications/)
+  [Using CloudWatch with an AWS SDK](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/sdk-general-information-section.html)

 **Related videos:**
+  [AWS re:Invent 2021 - Observability the open-source way](https://www.youtube.com/watch?v=vAnIhIwE5hY)
+  [Collect Metrics and Logs from Amazon EC2 instances with the CloudWatch Agent](https://www.youtube.com/watch?v=vAnIhIwE5hY)
+  [How to Easily Setup Application Monitoring for Your AWS Workloads - AWS Online Tech Talks](https://www.youtube.com/watch?v=LKCth30RqnA)
+  [Mastering Observability of Your Serverless Applications - AWS Online Tech Talks](https://www.youtube.com/watch?v=CtsiXhiAUq8)
+  [Open Source Observability with AWS - AWS Virtual Workshop](https://www.youtube.com/watch?v=vAnIhIwE5hY)

 **Related examples:**
+  [AWS Logging & Monitoring Example Resources](https://github.com/aws-samples/logging-monitoring-apg-guide-examples)
+  [AWS Solution: Amazon CloudWatch Monitoring Framework](https://aws.amazon.com/solutions/implementations/amazon-cloudwatch-monitoring-framework/?did=sl_card&trk=sl_card)
+  [AWS Solution: Centralized Logging](https://aws.amazon.com/solutions/implementations/centralized-logging/)
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US)
