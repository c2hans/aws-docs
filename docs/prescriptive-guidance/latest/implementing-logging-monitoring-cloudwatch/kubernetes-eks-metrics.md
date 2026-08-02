---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/kubernetes-eks-metrics.html
---

# Metrics for Amazon EKS and Kubernetes
<a name="kubernetes-eks-metrics"></a>

Kubernetes provides a metrics API that allows you to access resource usage metrics (for example, CPU and memory usage for nodes and pods), but the API only provides point-in-time information and not historical metrics. The [Kubernetes metrics-server](https://github.com/kubernetes-sigs/metrics-server) is typically used for Amazon EKS and Kubernetes deployments to aggregate metrics, provide short-term historical information on metrics, and support features such as [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

Amazon EKS exposes control plane metrics through the Kubernetes API server [in a Prometheus format](https://docs.aws.amazon.com/eks/latest/userguide/prometheus.html) and CloudWatch can capture and ingest these metrics. CloudWatch and Container Insights can also be configured to provide comprehensive metrics capture, analysis, and alarming for your Amazon EKS nodes and pods.

## Kubernetes control plane metrics
<a name="kubernetes-control-plane-metrics"></a>

Kubernetes exposes control plane metrics in a Prometheus format by using the `/metrics` HTTP API endpoint. You should install [Prometheus](https://prometheus.io/) in your Kubernetes cluster to graph and view these metrics with a web browser. You can also [ingest the metrics exposed](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-configure.html#ContainerInsights-Prometheus-Setup-new-exporters) by the Kubernetes API server into CloudWatch.

## Node and system metrics for Kubernetes
<a name="kubernetes-node-system-metrics"></a>

Kubernetes provides the Prometheus [metrics-server](https://github.com/kubernetes-sigs/metrics-server) pod that you can [deploy and run](https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html) on your Kubernetes clusters for cluster, node, and pod-level CPU and memory statistics. These metrics are used with the [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) and [Vertical Pod Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/vertical-pod-autoscaler.html). CloudWatch can also provide these metrics.

You should install the Kubernetes Metrics Server if you use the [Kubernetes Dashboard](https://github.com/kubernetes/dashboard) or the horizontal and vertical pod autoscalers. The Kubernetes Dashboard helps you browse and configure your Kubernetes cluster, nodes, pods and related configuration, and view the CPU and memory metrics from the Kubernetes Metrics Server.

The metrics provided by the Kubernetes Metrics Server can't be used for non-auto scaling purposes (for example, monitoring). The metrics are meant for point-in-time analysis and not historical analysis. The Kubernetes Dashboard deploys the `dashboard-metrics-scraper` to store metrics from the Kubernetes Metrics Server for a short time window.

Container Insights uses a containerized version of the CloudWatch agent that runs in a Kubernetes DaemonSet to discover all running containers in a cluster and provide node-level metrics. It collects performance data at every layer of the performance stack. You can use the Quick Start from AWS Quick Starts or configure Container Insights separately. The Quick Start sets up metrics monitoring with the CloudWatch agent and logging with Fluent Bit so you only need to deploy it once for logging and monitoring.

Because Amazon EKS nodes are EC2 instances, you should capture systems-level metrics, in addition to metrics captured by Container Insights, by using the standards you defined for Amazon EC2. You can use the same approach from the [Set up State Manager and Distributor for CloudWatch agent deployment and configuration](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/install-cloudwatch-systems-manager.html#set-up-systems-manager-distributor) section of this guide to install and configure the CloudWatch agent for your Amazon EKS clusters. You can update your Amazon EKS specific CloudWatch configuration file to include metrics as well as your Amazon EKS specific log configuration.

The CloudWatch agent with Prometheus support can automatically discover and scrape the Prometheus metrics from [supported, containerized workloads and systems](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus.html). It ingests them as CloudWatch logs in embedded metric format for analysis with CloudWatch Logs Insights and automatically creates CloudWatch metrics.

### Important:
<a name="important-.2c4b1ed9-abc6-5b0e-bea0-274fa4815b46"></a>

You must [deploy a specialized version](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup.html#ContainerInsights-Prometheus-Setup-install-agent) of the CloudWatch agent to collect Prometheus metrics. This is a separate agent from the CloudWatch agent deployed for Container Insights. You can use the [prometheus\_jmx](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/examples/eks/prometheus_jmx) sample Java application, which includes the deployment and configuration files for the CloudWatch agent and Amazon EKS pod deployment to demonstrate Prometheus metrics discovery. For more information, see [Set up Java/JMX sample workload on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-javajmx.html) in the CloudWatch documentation. You can also configure the CloudWatch agent to capture metrics from other Prometheus targets running in your Amazon EKS cluster.

## Application metrics
<a name="application-metrics-eks"></a>

You can create your own custom metrics with the [CloudWatch embedded metric format.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html) To ingest embedded metric format statements, you need to send embedded metric format entries to an embedded metric format endpoint. The CloudWatch agent can be configured as a [sidecar container in your Amazon EKS pod](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.html). The CloudWatch agent configuration is stored as a Kubernetes ConfigMap and read by your CloudWatch agent sidecar container to start the embedded metric format endpoint.

You can also set up your application as a Prometheus target and configure the CloudWatch agent, with Prometheus support, to discover, scrape, and ingest your metrics into CloudWatch. For example, you can use the [open-source JMX exporter](https://github.com/prometheus/jmx_exporter) with your Java applications to expose JMX Beans for Prometheus consumption by the CloudWatch agent.

If you don't want to use the embedded metric format, you can also create and update CloudWatch metrics by using [AWS API](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/Welcome.html) or [AWS SDK](https://aws.amazon.com/developer/tools/). However, we don't recommend this approach because it mixes monitoring and the application logic.

## Metrics for Amazon EKS on Fargate
<a name="metrics-fargate-eks-workloads"></a>

Fargate automatically provisions Amazon EKS nodes to run your Kubernetes pods so you don't need to monitor and collect node-level metrics. However, you must monitor metrics for pods running on your Amazon EKS nodes on Fargate. Container Insights isn't currently available for Amazon EKS on Fargate because it requires the following capabilities that aren't currently supported:
+ DaemonSets aren't currently supported. Container Insights is deployed by running the CloudWatch agent as a DaemonSet on each cluster node.
+ HostPath persistent volumes aren't supported. The CloudWatch agent container uses hostPath persistent volumes as a prerequisite for gathering container metric data.
+ Fargate prevents privileged containers and access to host information.

You can use the [built-in log router for Fargate](https://docs.aws.amazon.com/eks/latest/userguide/fargate-logging.html) to send embedded metric format statements to CloudWatch. The log router uses Fluent Bit, which has a CloudWatch plugin that can be configured to support embedded metric format statements.

You can retrieve and capture pod-level metrics for your Fargate nodes by deploying the Prometheus server in your Amazon EKS cluster to gather metrics from your Fargate nodes. Because Prometheus requires persistent storage, you can deploy Prometheus on Fargate if you use Amazon Elastic File System (Amazon EFS) for persistent storage. You can also deploy Prometheus on an Amazon EC2 backed node. For more information, see [Monitoring Amazon EKS on AWS Fargate using Prometheus and Grafana](https://aws.amazon.com/blogs/containers/monitoring-amazon-eks-on-aws-fargate-using-prometheus-and-grafana/) on the AWS Blog.
