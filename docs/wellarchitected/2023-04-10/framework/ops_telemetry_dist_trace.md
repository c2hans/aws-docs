---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_telemetry_dist_trace.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS04-BP05 Implement transaction traceability
<a name="ops_telemetry_dist_trace"></a>

Implement your application code and configure your workload components to emit events, which are started as a result of single logical operations and consolidated across various boundaries of your workload. Generate maps to see how traces flow across your workload and services. Gain insight into the relationships between components, and identify and analyze issues. Use the collected information to determine when a response is required and to assist you in identifying the factors contributing to an issue.

 **Desired outcome:**
+  Collect transaction traces across your workload to gain insight into the relationship between components.
+  Generate maps to gain a better understanding of how transactions and events flow across your workload.

 **Common anti-patterns:**
+  You have implemented a serverless microservices architecture spanning multiple accounts. Your customers are experiencing intermittent performance issues. You are unable to discover which function or component is responsible because you lack transaction traceability.
+ There is a performance bottleneck in your workload. Because you lack transaction traceability, you are unable to see the relationship between your application components and identify the bottleneck.
+  The identifier used for traces is not globally unique, resulting in a tracing collision when analyzing workload behavior.

 **Benefits of establishing this best practice:**
+  Understanding the flow of transactions across your workload provides insight into the expected behavior of your workload transactions.
+  You can see variations from expected behavior across your workload and you can respond if necessary.
+  You can pinpoint transactions by their unique generated identifier independent from where they were generated.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 Design your application and workload to emit information about the flow of transactions across system components. Data to include in transactions are a globally unique transaction identifier, transaction stage, active component, and time to complete activity. Use this information to determine what is in progress, what is complete, and what the results of completed activities are.

 **Customer example**

 At AnyCompany Retail, all transactions have a globally unique UUID generated. This UUID is passed between microservices during transactions. The UUID is used to create transaction traces as users interact with the workload. A map of the workload topology is generated with the traces and is used to troubleshoot workload issues and improve performance.

 **Implementation steps**

1.  Instrument the applications in your workload to emit transaction traces. This can be done by generating a unique identifier for each transaction and passing the identifier between applications.

   1.  You can use auto-instrumentation in the [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) to implement traces in your existing applications without modifying your application code.

1.  Generate maps of your application topology. Use these maps to improve performance, gain insights, and aid in troubleshooting.

   1.  [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) can generate maps of the applications in your workload.

 **Level of effort for the implementation plan:** Medium. Implementing transaction traces may require moderate development effort.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS04-BP01 Implement application telemetry](ops_telemetry_application_telemetry.md) - Application telemetry covers transaction traceability and handling and needs to be implementing first.

 **Related documents:**
+ [ Discover application issues and get notifications with AWS X-Ray Insights ](https://aws.amazon.com/blogs/mt/discover-application-issues-get-notifications-aws-x-ray-insights/)
+ [ How Wealthfront utilizes AWS X-Ray to analyze and debug distributed applications ](https://aws.amazon.com/blogs/mt/wealthfront-utilizes-aws-x-ray-analyze-debug-distributed-applications/)
+ [ New for AWS Distro for OpenTelemetry – Tracing Support is Now Generally Available ](https://aws.amazon.com/blogs/aws/new-for-aws-distro-for-opentelemetry-tracing-support-is-now-generally-available/)

 **Related videos:**
+ [AWS re:Invent 2018: Deep Dive into AWS X-Ray: Monitor Modern Applications (DEV324) ](https://www.youtube.com/watch?v=5MQkX57eTh8)
+ [AWS re:Invent 2022 - Building observable applications with OpenTelemetry (BOA310) ](https://www.youtube.com/watch?v=efk8XFJrW2c)
+ [AWS re:Invent 2022 - Observability the open-source way (COP301-R) ](https://www.youtube.com/watch?v=2IJPpdp9xU0)
+ [ Capturing Trace Data with the AWS Distro for OpenTelemetry ](https://www.youtube.com/watch?v=837NtV0McOA)
+ [ Optimize Application Performance with AWS X-Ray](https://www.youtube.com/watch?v=5lIdNrrO_o8)

 **Related examples:**
+ [AWS X-Ray Multi API Gateway Tracing Example ](https://github.com/aws-samples/aws-xray-multi-api-gateway-tracing-example)

 **Related services:**
+  [AWS Distro for OpenTelemetry](https://aws-otel.github.io/)
+  [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
