---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/monitoring-tools.html
---

# Monitoring tools for Amazon EKS
<a name="monitoring-tools"></a>

This section discusses three categories of Amazon EKS monitoring tools: AWS monitoring services, open source or proprietary solutions, and specialized tools.

## AWS services
<a name="monitoring-services"></a>
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html): Comprehensive monitoring and logging service

  CloudWatch forms the backbone of AWS monitoring solutions and provides extensive capabilities for Amazon EKS environments. It delivers Container Insights for granular container and cluster metrics, so you can monitor performance, resource utilization, and application health. The service excels in log aggregation and analysis, and supports centralized logging across containers and nodes. CloudWatch integrates naturally with AWS services. It provides automated alarm configuration and supports custom metrics and dashboards, which make it an essential tool for Amazon EKS monitoring.
+ [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html): Advanced distributed tracing platform

  X-Ray elevates observability by providing sophisticated distributed tracing capabilities. Its service map visualization offers clear insights into application architecture and dependencies, and detailed request tracking helps identify performance bottlenecks across services. X-Ray can trace requests through complex microservices architectures, which makes it invaluable for troubleshooting and optimization, especially in distributed systems that span multiple AWS services.
+ [AWS Distro for OpenTelemetry](https://aws-otel.github.io/): Unified observability framework

  Distro for OpenTelemetry provides unified data collection capabilities with cross-platform support, which makes it ideal for hybrid environments. This service integrates with other AWS services, supports custom instrumentation, and offers flexibility in implementing comprehensive monitoring solutions while maintaining compatibility with industry standards.
+ [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html): Enterprise-grade visualization

  Amazon Managed Grafana provides a fully managed service for data visualization and analytics. It offers seamless integration with other AWS services, built-in security features, and enterprise-grade scalability. The service simplifies dashboard creation and management while providing advanced features such as cross-account data source access and integration with AWS IAM Identity Center.
+ [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html): Highly available, secure, managed monitoring

  Amazon Managed Service for Prometheus is a fully managed, Prometheus-compatible monitoring service. It provides automated scaling, high availability, and secure metric ingestion and querying. The service integrates seamlessly with Amazon EKS and eliminates the operational overhead of managing Prometheus servers.

## Open source or proprietary solutions
<a name="monitoring-open-source"></a>

The AWS tools described in the previous section offer seamless integration and managed services. The open source tools listed in this section complement AWS services by providing flexibility and extensive customization options. Understanding the capabilities and use cases of each tool helps you design monitoring strategies that best meet your specific requirements.
+ [Prometheus](https://docs.aws.amazon.com/eks/latest/userguide/deploy-prometheus.html): Metrics collection toolkit

  Prometheus is an open source solution for metrics collection in Kubernetes environments. Its time-series database and PromQL query language enable sophisticated metrics analyses. The platform's service discovery capabilities automatically adapt to dynamic Kubernetes environments, and its alert management system keep you informed of critical issues. Prometheus provides extensive integration options, which make it a versatile choice for comprehensive metrics monitoring.
+ [Grafana](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/kubernetes-monitoring/configuration/config-other-methods/config-aws-eks/): Advanced visualization engine

  Grafana transforms complex monitoring data into actionable insights through its visualization capabilities. The platform creates customized dashboards that combine data from multiple sources and provide a unified view of infrastructure and application metrics. Its support for various data sources and alert management features provide comprehensive monitoring. Grafana can help you visualize both real-time and historical data, so you can identify trends and make informed decisions.
+ [Fluent Bit](https://fluentbit.io/): Unified logging layer

  This logging solution provides log collection and management for Kubernetes environments. Its native Kubernetes integration ensures seamless log gathering from containers and nodes, and its support for multiple output destinations offers flexibility in log storage and analysis. Advanced features such as log parsing and filtering enable you to process and route logs based on specific requirements. The lightweight nature of Fluent Bit makes it particularly suitable for containerized environments.
+ [Datadog](https://www.datadoghq.com/blog/eks-monitoring-datadog/): Full-stack observability

  Datadog provides comprehensive monitoring capabilities with native Kubernetes support. It offers infrastructure monitoring, application performance monitoring (APM), log management, and real-time analytics. You can use the platform's automatic service discovery and extensive integration catalog for Amazon EKS monitoring, and its machine learning capabilities to detect anomalies and predict potential issues.
+ [New Relic](https://docs.newrelic.com/docs/infrastructure/amazon-integrations/connect/eks-add-on/): Application performance monitoring

  New Relic offers visibility into application performance and infrastructure health. Its Kubernetes integration provides detailed container insights, distributed tracing, and custom dashboards. The platform helps you correlate application performance with infrastructure metrics, so you can quickly identify and resolve issues.
+ [Elastic Stack (ELK Stack)](https://aws.amazon.com/opensearch-service/resources/the-benefits-of-the-elk-stack/): Log analysis and search

  The ELK Stack combines Elasticsearch, Logstash, and Kibana to provide log management and analysis capabilities. It offers advanced search functionality, visualization tools, and machine learning features. You can use the stack to handle large volumes of log data from your Amazon EKS environments.

## Specialized tools
<a name="monitoring-special"></a>

You can mix and match the following tools based on your specific monitoring requirements, scale of operations, and organizational preferences. The key is to create a monitoring stack that provides comprehensive visibility while remaining manageable and cost-effective.
+ [kube-state-metrics (KSM)](https://github.com/kubernetes/kube-state-metrics): Kubernetes state monitoring

  This add-on service listens to the Kubernetes API server and generates metrics about the state of objects. It provides insights into the health of deployments, pods, and other Kubernetes resources.
+ [Kubernetes Metrics Server](https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html): Resource metrics

  This metrics server collects resource metrics from kubelets and exposes them through the Kubernetes metrics API. It provides horizontal pod autoscaling and basic CPU and memory metrics.
+ [Kubecost](https://github.com/kubecost/cost-analyzer-helm-chart): Kubernetes cost monitoring

  Tools such as Kubecost provide detailed cost analysis and optimization recommendations for EKS clusters. They help you understand and optimize cloud spending across different namespaces, deployments, and services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
