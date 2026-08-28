---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/ops_observability_dependency_telemetry.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS04-BP04 Implement dependency telemetry
<a name="ops_observability_dependency_telemetry"></a>

 Dependency telemetry is essential for monitoring the health and performance of the external services and components your workload relies on. It provides valuable insights into reachability, timeouts, and other critical events related to dependencies such as DNS, databases, or third-party APIs. By instrumenting your application to emit metrics, logs and traces about these dependencies, you gain a clearer understanding of potential bottlenecks, performance issues, or failures that might impact your workload.

 **Desired outcome:** The dependencies your workload relies on are performing as expected, allowing you to proactively address issues and ensure optimal workload performance.

 **Common anti-patterns:**
+  Overlooking external dependencies: Focusing only on internal application metrics while neglecting metrics related to external dependencies.
+  Lack of proactive monitoring: Waiting for issues to arise instead of continuously monitoring dependency health and performance.
+  Siloed monitoring: Using multiple, disparate monitoring tools which can result in fragmented and inconsistent views of dependency health.

 **Benefits of establishing this best practice:**
+  Improved workload reliability: By ensuring that external dependencies are consistently available and performing optimally.
+  Faster issue detection and resolution: Proactively identifying and addressing issues with dependencies before they impact the workload.
+  Comprehensive view: Gaining a holistic view of both internal and external components that influence workload health.
+  Enhanced workload scalability: By understanding the scalability limits and performance characteristics of external dependencies.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Implement dependency telemetry by starting with identifying the services, infrastructure, and processes that your workload depends on. Quantify what good conditions look like when those dependencies are functioning as expected, and then determine what data is needed to measure those. With that information, you can craft dashboards and alerts that provide insights to your operations teams on the state of those dependencies. Use AWS tools to discover and quantify the impacts when dependencies cannot deliver as needed. Continually revisit your strategy to account for changes in priorities, goals, and gained insights.

### Implementation steps
<a name="implementation-steps"></a>

 To implement dependency telemetry effectively:

1.  **Identify external dependencies:** Collaborate with stakeholders to pinpoint the external dependencies your workload relies on. External dependencies can encompass services like external databases, third-party APIs, network connectivity routes to other environments, and DNS services. The first step towards effective dependency telemetry is being comprehensive in understanding what those dependencies are.

1.  **Develop a monitoring strategy:** Once you have a clear picture of your external dependencies, architect a monitoring strategy tailored to them. This involves understanding the criticality of each dependency, its expected behavior, and any associated service-level agreements or targets (SLA or SLTs). Set up proactive alerts to notify you of status changes or performance deviations.

1.  **Leverage [Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html):** It offers insights into the global internet, helping to understand outages or disruptions that might impact your external dependencies.

1.  **Stay informed with [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/):** It provides alerts and remediation guidance when AWS is experiencing events that may impact your services.

1.  **Instrument your application with [AWS X-Ray](https://aws.amazon.com/xray/):** AWS X-Ray provides insights into how applications and their underlying dependencies are performing. By tracing requests from start to end, you can identify bottlenecks or failures in the external services or components your application relies on.

1.  **Use [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/):** This machine learning-driven service identifies operational issues, predicts when critical issues might occur, and recommends specific actions to take. It's invaluable for gaining insights into dependencies and determining that they're not the source of operational problems.

1.  **Monitor regularly:** Continually monitor metrics and logs related to external dependencies. Set up alerts for unexpected behavior or degraded performance.

1.  **Validate after changes:** Whenever there's an update or change in any of the external dependencies, validate their performance and check their alignment with your application's requirements.

 **Level of effort for the implementation plan:** Medium

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS04-BP01 Identify key performance indicators](ops_observability_identify_kpis.md)
+  [OPS04-BP02 Implement application telemetry](ops_observability_application_telemetry.md)
+  [OPS04-BP03 Implement user experience telemetry](ops_observability_customer_telemetry.md)
+  [OPS04-BP05 Implement distributed tracing](ops_observability_dist_trace.md)

 **Related documents:**
+ [ What is AWS Health? ](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)
+ [ Using Amazon CloudWatch Internet Monitor ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html)
+ [AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
+ [ Amazon DevOps Guru User Guide ](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html)

 **Related videos:**
+ [ Visibility into how internet issues impact app performance ](https://www.youtube.com/watch?v=Kuc_SG_aBgQ)
+ [ Introduction to Amazon DevOps Guru ](https://www.youtube.com/watch?v=2uA8q-8mTZY)

 **Related examples:**
+ [ Gaining operational insights with AIOps using Amazon DevOps Guru ](https://catalog.us-east-1.prod.workshops.aws/workshops/f92df379-6add-4101-8b4b-38b788e1222b/en-US)
+ [AWS Health Aware ](https://github.com/aws-samples/aws-health-aware/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
