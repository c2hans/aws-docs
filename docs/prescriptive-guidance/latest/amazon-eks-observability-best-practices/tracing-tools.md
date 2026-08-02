---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/tracing-tools.html
---

# Tracing tools for Amazon EKS
<a name="tracing-tools"></a>

Amazon EKS supports several AWS and third-party options for implementing distributed tracing.

## AWS services
<a name="tracing-services"></a>
+ [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html): Advanced distributed tracing platform

  X-Ray is a fully managed AWS service that provides end-to-end tracing capabilities. It automatically instruments AWS services and provides detailed service maps and analytics for your applications that run on Amazon EKS. X-Ray is integrated with other AWS services, including Amazon CloudWatch, and offers automatic correlation of traces with AWS service calls.
+ [AWS Distro for OpenTelemetry](https://aws-otel.github.io/): Unified observability framework

  Distro for OpenTelemetry is a secure, production-ready, and AWS-supported distribution of OpenTelemetry for cloud-native applications. It offers vendor-neutral instrumentation capabilities while maintaining native AWS service integration, which makes it ideal for hybrid cloud environments. Distro for OpenTelemetry supports multiple observability backends and provides seamless integration with AWS monitoring services.

## Open source solutions
<a name="tracing-open-source"></a>
+ [OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html): Open source observability framework

  OpenTelemetry provides a standardized observability framework with comprehensive instrumentation libraries that support multiple programming languages. Its flexible backend options and vendor-neutral approach make it ideal for workloads that require consistency across different environments. The framework's extensive ecosystem ensures broad compatibility with various monitoring solutions.
+ [Jaeger](https://www.jaegertracing.io/): Open source distributed tracing platform

  Jaeger offers comprehensive tracing capabilities with real-time distributed context propagation. It provides root cause analysis and performance optimization through detailed service dependency visualization. Jaeger's architecture is designed for high scalability and supports various storage backends, which makes it suitable for large-scale Amazon EKS deployments.
+ [Grafana Tempo](https://grafana.com/docs/tempo/latest/): Distributed tracing

  Tempo is a Grafana Labs solution that provides high-scale trace storage and seamless integration with Prometheus metrics. Its cost-effective trace retention model and native integration with Grafana make it suitable for organizations that already use Grafana for visualization. Tempo's architecture is designed specifically for cloud-native environments such as Amazon EKS.
