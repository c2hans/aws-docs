---
source_url: https://docs.aws.amazon.com/whitepapers/latest/containers-on-aws/logging-and-monitoring.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Observability
<a name="logging-and-monitoring"></a>

 Observability is to continuously discover actionable insights based on signals from the system under observation over time. The signals can be low-level such as CPU, memory, disk space, and higher-level such as business signals including API response times, error rates, and transactions per second. Having insight into metrics, logs, and traces, understanding what is happening not just at the cluster or host level, but also within the container runtime and application, helps organizations make better informed decisions, such as when to scale in/out nodes/tasks/pods, change Amazon EC2 instance types, and purchasing options (on-demand, reserved, and spot).

 Treating logs as a continuous stream of events instead of as static files allows you to react to the continuous nature of log generation. You can capture, store, and analyze real-time log data to get meaningful insights into the application’s performance, network, and other characteristics. An application must not be required to manage its own log files.

 You can specify the `awslogs` log driver for containers in your Amazon ECS task definition under the **logConfiguration** object to ship the `stdout` and `stderr` I/O streams to a designated log group in Amazon CloudWatch logs for viewing and archival. Additionally, FireLens for Amazon ECS enables you to use task definition parameters with the `awsfirelens` log driver to route logs to other AWS services or third-party log aggregation tools for log storage and analytics. FireLens works with **Fluentd** and **Fluent Bit**, fully compatible with Kubernetes. Using the **Fluent Bit** daemonset, you can send container logs from your Amazon EKS clusters to CloudWatch logs.

 Amazon CloudWatch is a monitoring service that you can use to collect various system, and application-wide metrics and logs, and set alarms. CloudWatch Container Insights helps you explore, aggregate, and summarize your container metrics, application logs and performance log events at the cluster, node, pod, task, and service level through automated dashboards in the CloudWatch console. Container Insights also provides diagnostic information, such as container restart failures, crashloop backoffs in an Amazon EKS cluster to help you isolate issues and resolve them quickly. Container Insights is available for Amazon Elastic Container Service (Amazon ECS, including Fargate), Amazon Elastic Kubernetes Service (Amazon EKS), and Kubernetes platforms on Amazon EC2.

 [AWS X-Ray](https://aws.amazon.com/xray/) provides a complete view of requests as they flow through your distributed applications with end-to-end tracing capabilities. You can filter visual data across payloads, functions, traces, services, APIs to easily identify performance bottlenecks, any edge case errors or issues.

 [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) helps you manage monitoring and alerting for your containerized applications and infrastructure at scale. It is fully compatible with the popular upstream open-source Prometheus. You can collect and access performance and operational data from container workloads on AWS and on-premises. It simplifies the setup of Prometheus and automates the ongoing operations and maintenance.

 [Amazon Managed Grafana](https://aws.amazon.com/grafana/) is a managed service for open-source Grafana. It simplifies interactive visualization and analysis for your data sources at scale. You can visualize, analyze, and alarm on your metrics, logs, and traces collected from multiple data sources in your observability system. This includes AWS services, third-party ISVs, and other resources in your environment.

 [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/) (ADOT) is a secure production-ready, AWS-supported distribution of the OpenTelemetry project, which provides a single set of open-source APIs, libraries, and agents to collect and correlate distributed traces and metrics. ADOT consists of SDKs, auto-instrumentation agents, collectors and exporters to send data to back-end services, including Amazon CloudWatch, X-Ray, and Amazon Managed Service for Prometheus.
