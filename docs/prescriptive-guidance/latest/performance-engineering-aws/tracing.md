---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/tracing.html
---

# Tracing
<a name="tracing"></a>

Tracing involves the specialized use of logging information about a program's processes. Insights from the logs can help engineers debug individual transactions and identify bottlenecks. Tracing can be enabled automatically or by using manual instrumentation.

Because an application integrates with different services, it's important to identify how the application and its underlying services are performing. Tracing works with traces and spans. A *trace* is the complete request process, and each trace is made up of spans. A *span* is a tagged time interval and is the activity within a system's individual components or services. Traces provide the big picture of what happens when a request is made to an application.

## Application team
<a name="tracing-app-team"></a>

Application developers instrument their applications by sending trace data for inbound and outbound requests and other events within the application, along with metadata about each request. To generate traces, an application must be instrumented to generate traces. Instrumentation can be automatic or manual.

### Automatic instrumentation
<a name="automatic-instrumentation.2cffa046-4381-506f-83f4-17e946e65c6d"></a>

You can collect telemetry from an application by using [automatic instrumentation](https://opentelemetry.io/docs/concepts/instrumentation/automatic/) without having to modify the source code. Automatic instrumentation agents can generate application traces of an application or service. Typically, you use configuration changes to add the agent or another mechanism.

Library instrumentation involves making minimal application code changes to add prebuilt instrumentation. The instrumentation targets specific libraries or frameworks, such as the AWS SDK, Apache HTTP clients, or SQL clients.

### Manual instrumentation
<a name="manual-instrumentation.acca1486-2693-58c9-b43b-fdbbeca8e3c0"></a>

In this approach, application developers add instrumentation code to the application at each location where they want to collect trace information. For example, use aspect-oriented programming (AOP) to collect AWS X-Ray tracing data. Developers can use SDKs to instrument their applications.

### Sampling
<a name="sampling.9ef01224-9b9a-52d1-b3ed-cfbd890b49d4"></a>

Trace data is often generated in large volumes. It's important to have a mechanism to determine whether the trace data should be exported or not. Sampling is the process of determining what data should be exported. This is generally done to save cost. By customizing sampling rules, you can control the amount of data that you record. You can also change sampling behavior without changing and redeploying your code. It's important to control the sampling rate to generate the right amount of traces.

Application developers can annotate the traces by adding metadata as key-value pairs. The annotations enrich the traces and help to refine filtering in the backend.

## DevOps team
<a name="tracing-devops-team"></a>

DevOps engineers are often asked to set up a tracing environment for the application developer to visualize traces for infrastructure and applications. Tracing environment setup involves collecting trace data from different sources and sending it to a central store for visualizing.

## Tracing backend
<a name="tracing-backend"></a>

A tracing backend is a service such as AWS X-Ray that collects data about requests that your application serves. It provides tools that you can use to view, filter, and gain insights into that data to identify issues and opportunities for optimization. For any traced request to your application, you can see detailed information about the request and response, and about other calls that your application makes to downstream AWS resources, microservices, databases, and web APIs.

## Automating tracing
<a name="tracing-automation"></a>

Because different applications have different tracing requirements, it's important to automate the configuration and operation of the tracing infrastructure. Use IaC tools to provision the tracing infrastructure's backend.

Use CD pipelines to automate the following:
+ Deploy the tracing infrastructure on demand and tear down it when it isn't required.
+ Deploy the tracing configuration across applications.

## Tracing tools
<a name="tracing-tools"></a>

AWS provides the following services for tracing and its associated visualization:
+ AWS X-Ray receives traces from your application, in addition to traces from AWS services your application uses that are already integrated with X-Ray. There are several SDKs, agents, and tools that can be used to instrument your application for X-Ray tracing. For more information, see the [AWS X-Ray documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html).

  Developers can also use AWS X-Ray SDKs to send traces to X-Ray. AWS X-Ray provides SDKs for Go, Java, Node.js, Python, .NET, and Ruby. Each X-Ray SDK provides the following:
  + Interceptors to add to your code to trace incoming HTTP requests
  + Client handlers to instrument AWS SDK clients that your application uses to call other AWS services
  + An HTTP client to instrument calls to other internal and external HTTP web services

  X-Ray SDKs also support instrumenting calls to SQL databases, automatic AWS SDK client instrumentation, and other features. Instead of sending trace data directly to X-Ray, the SDK sends JSON segment documents to a daemon process listening for UDP traffic. The [X-Ray daemon](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html) buffers segments in a queue and uploads them to X-Ray in batches. For more information about instrumenting your application by using an X-Ray SDK, see the [X-Ray documentation](https://docs.aws.amazon.com/xray/latest/devguide/xray-instrumenting-your-app.html).
+ Amazon OpenSearch Service is an AWS managed service for running and scaling OpenSearch clusters, which can be used to centrally store logs, metrics, and traces. The Observability plugin provides a unified experience for collecting and monitoring metrics, logs, and traces from common data sources. Data collection and monitoring in one place provides full-stack, end-to-end observability of your entire infrastructure. For implementation information, see the [OpenSearch Service documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability.html).
+ AWS Distro for OpenTelemetry (ADOT) is an AWS distribution based on the Cloud Native Computing Foundation (CNCF) OpenTelemetry project. ADOT currently includes automatic-instrumentation support for [Java](https://aws-otel.github.io/docs/getting-started/java-sdk/auto-instr) and [Python](https://aws-otel.github.io/docs/getting-started/python-sdk/auto-instr). In addition, ADOT supports automatic instrumentation of AWS Lambda functions and their downstream requests using Java, Node.js, and Python runtimes, through [ADOT Managed Lambda Layers](https://aws-otel.github.io/docs/getting-started/lambda). Developers can use the ADOT collector to send traces to different backends, including AWS X-Ray and Amazon OpenSearch Service.

  For a reference example of how to instrument your application by using the ADOT SDK, see the [documentation](https://aws-otel.github.io/docs/getting-started/java-sdk/auto-instr). For a reference example of how to use the ADOT SDK to send data to Amazon OpenSearch Service, see the [OpenSearch Service documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/trace-analytics.html).

  For a reference example of how to instrument your application running on Amazon EKS, see the blog post [Metrics and traces collection using Amazon EKS add-ons for AWS Distro for OpenTelemetry](https://aws.amazon.com/blogs/containers/metrics-and-traces-collection-using-amazon-eks-add-ons-for-aws-distro-for-opentelemetry/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
