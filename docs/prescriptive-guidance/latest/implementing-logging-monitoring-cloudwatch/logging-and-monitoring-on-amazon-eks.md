---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/logging-and-monitoring-on-amazon-eks.html
---

# Logging and monitoring on Amazon EKS
<a name="logging-and-monitoring-on-amazon-eks"></a>

Amazon Elastic Kubernetes Service (Amazon EKS) integrates with CloudWatch Logs for the Kubernetes control plane. The control plane is provided as a managed service by Amazon EKS and you can [turn on logging without installing a CloudWatch agent](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html). The CloudWatch agent can also be deployed to capture Amazon EKS node and container logs. [Fluent Bit and Fluentd](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-logs.html) are also supported for sending your container logs to CloudWatch Logs.

CloudWatch Container Insights provides a comprehensive metrics monitoring solution for Amazon EKS at the cluster, node, pod, task, and service level. Amazon EKS also supports multiple options for metrics capture with [Prometheus](https://prometheus.io/). The Amazon EKS control plane [provides a metrics endpoint](https://docs.aws.amazon.com/eks/latest/userguide/prometheus.html) that exposes metrics in a Prometheus format. You can deploy Prometheus into your Amazon EKS cluster to consume these metrics.

You can also [set up the CloudWatch agent to scrape Prometheus metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-configure.html) and create CloudWatch metrics, in addition to consume other Prometheus endpoints. [Container Insights monitoring for Prometheus](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus.html) can also automatically discover and capture Prometheus metrics from supported, containerized workloads and systems.

You can install and configure the CloudWatch agent on your Amazon EKS nodes, in a similar way to the approach used for Amazon EC2 with Distributor and State Manager, to align your Amazon EKS nodes with your standard system logging and monitoring configurations.
