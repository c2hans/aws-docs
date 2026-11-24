---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/eks-standard-telemetry-attributes.html
---

# Telemetry enrichment

The CloudWatch agent that the Amazon CloudWatch Observability add-on and Helm chart deploy adds resource attributes to the OpenTelemetry telemetry that it collects. The attributes follow the OpenTelemetry semantic conventions. For more information, see [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) on the OpenTelemetry website. For the Kubernetes and cloud attributes, see [Kubernetes resource attributes](https://opentelemetry.io/docs/specs/semconv/resource/k8s/) on the OpenTelemetry website and [Cloud resource attributes](https://opentelemetry.io/docs/specs/semconv/resource/cloud/) on the OpenTelemetry website. Because the metrics, logs, and traces of a pod carry the same resource attributes, you can correlate across these telemetry types out of the box.

The agent adds the attributes to the following telemetry:
+ [OTel Container Insights (Recommended)](container-insights-eks-otel.md) metrics and logs
+ Metrics, traces, and logs that your applications send to the [OTLP ingestion](eks-observability-addon-otlp-endpoint.md) endpoint
+ Metrics from [Scraping ServiceMonitor and PodMonitor targets](eks-observability-addon-prometheus-monitors.md), except the node labels

## Attributes that the agent adds
<a name="eks-standard-telemetry-attributes-list"></a>

The following table lists the attributes that the agent adds, grouped as cloud and host, Kubernetes, service identity, and label attributes. In the table, *pod telemetry* means the pod and container metrics, application logs, OTLP telemetry, and ServiceMonitor and PodMonitor metrics that come from a pod.

| Attribute | Description | Applies to |
| --- | --- | --- |
| cloud.provider, cloud.platform, cloud.account.id, cloud.region, cloud.availability\_zone | The account, Region, and Availability Zone of the node. | All telemetry |
| cloud.resource\_id | The ARN of the Amazon EKS cluster. | All telemetry |
| host.id, host.name, host.type, host.image.id | The Amazon EC2 instance of the node, its instance type, and its AMI. | All telemetry |
| k8s.cluster.name, k8s.node.name | The cluster and the node that the telemetry comes from. | All telemetry |
| k8s.namespace.name, k8s.pod.name, k8s.pod.uid, k8s.container.name | The namespace, pod, and container that the telemetry comes from. | Pod telemetry |
| k8s.deployment.name, k8s.statefulset.name, k8s.daemonset.name, k8s.replicaset.name, k8s.job.name, k8s.cronjob.name | The controllers that own the pod. | Pod telemetry |
| k8s.workload.name, k8s.workload.type | The workload that owns the pod, such as a Deployment or a StatefulSet. | Pod telemetry |
| service.name, service.namespace, service.version, service.instance.id, deployment.environment.name | The service identity of the pod. For more information, see [Setting the service identity](#eks-standard-telemetry-attributes-service). | Pod telemetry. For OTLP telemetry, only the attributes that the sender didn't set. |
| k8s.pod.label.{{key}} | A label of the pod. For more information, see [Adding Kubernetes labels](#eks-standard-telemetry-attributes-labels). | Pod telemetry |
| k8s.node.label.{{key}} | A label of the node. | All telemetry, except ServiceMonitor and PodMonitor metrics |

## Setting the service identity
<a name="eks-standard-telemetry-attributes-service"></a>

The agent sets the `service.*` attributes in line with the OpenTelemetry specification for [service resource attributes](https://opentelemetry.io/docs/specs/semconv/resource/service/) on the OpenTelemetry website. For more information, see [OpenTelemetry service identity](eks-observability-addon-service-identity.md).

## Adding Kubernetes labels
<a name="eks-standard-telemetry-attributes-labels"></a>

The agent adds each pod label as a `k8s.pod.label.{{key}}` attribute and each node label as a `k8s.node.label.{{key}}` attribute. By default, it adds every pod and node label except a built-in list of high-cardinality labels, such as `pod-template-hash`, `controller-revision-hash`, `topology.kubernetes.io/zone`, and the instance type labels.

Pod labels go on pod telemetry. Node labels go on all telemetry from the node, including node-level metrics and host logs, but not on ServiceMonitor and PodMonitor metrics.

To choose which labels the agent adds, set `otelFilters.podLabels` and `otelFilters.nodeLabels`. For more information, see [OpenTelemetry filters](eks-observability-addon-telemetry-filters.md).

## How attributes differ by telemetry type
<a name="eks-standard-telemetry-attributes-details"></a>
+ Host logs come from the node operating system, so they have the cluster, node, node label, cloud, and host attributes, and no pod, workload, or service identity attributes.
+ Node-level metrics have no pod attributes. The metrics of NVIDIA GPU, AWS Trainium, AWS Inferentia, and EFA devices carry the attributes of the pod that uses each device. For more information, see [Accelerated compute](container-insights-eks-otel-accelerated-compute.md).
+ For OTLP telemetry, the agent sets the service identity attributes only when the sender didn't set them.
+ Each metric carries at most 150 attributes. When a metric has more, the agent drops pod and node labels first, starting with Helm and tooling labels and ending with your own pod labels, so that it keeps the attributes that you're most likely to use in queries, such as the Kubernetes, cloud, host, and service identity attributes.
