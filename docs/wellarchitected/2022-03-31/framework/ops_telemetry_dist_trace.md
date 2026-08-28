---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_telemetry_dist_trace.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS04-BP05 Implement transaction traceability
<a name="ops_telemetry_dist_trace"></a>

 Implement your application code and configure your workload components to emit information about the flow of transactions across the workload. Use this information to determine when a response is required and to assist you in identifying the factors contributing to an issue.

 On AWS, you can use distributed tracing services, such as [AWS X-Ray](https://aws.amazon.com/xray/), to collect and record traces as transactions travel through your workload, generate maps to see how transactions flow across your workload and services, gain insight to the relationships between components, and identify and analyze issues in real time.

 **Common anti-patterns:**
+  You have implemented a serverless microservices architecture spanning multiple accounts. Your customers are experiencing intermittent performance issues. You are unable to discover which function or component is responsible because you lack the traces that would allow you to pinpoint where in the application the performance issue exists and what is causing the issue.
+  You are trying to determine where the performance bottlenecks are in your workload so that they can be addressed in your development efforts. You are unable to see the relationship between your application components, and the services they interact with, to determine where the bottlenecks are because you lack the traces that would allow you to drill down into the specific services and paths impacting application performance.

 **Benefits of establishing this best practice:** Understanding the flow of transactions across your workload allows you to understand the expected behavior of your workload transactions, and variations from expected behavior across your workload, enabling you to respond if necessary.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement transaction traceability: Design your application and workload to emit information about the flow of transactions across system components, such as transaction stage, active component, and time to complete activity. Use this information to determine what is in progress, what is complete, and what the results of completed activities are. This helps you determine when a response is required. For example, longer than expected transaction response times within a component can indicate issues with that component.
  +  [AWS X-Ray](https://aws.amazon.com/xray/)
  +  [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS X-Ray](https://aws.amazon.com/xray/)
+  [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
