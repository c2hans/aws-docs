---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/4-custom-metrics-removal.html
---

# Vendor and custom metrics cost reduction
<a name="4-custom-metrics-removal"></a>

Amazon CloudWatch, Prometheus, and third-party monitoring can become significant cost drivers in Amazon EKS.

## Check container insights, prometheus, ADOT (AWS Distro for OpenTelemetry) metrics
<a name="problem"></a>

For sample commands to audit Container Insights metrics and estimate cost, see the [audit-container-insights-metrics.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/08-vendor-custom-metrics-reduction/audit-container-insights-metrics.sh)

**Reduce Prometheus/ADOT Metric Cardinality**

For sample commands to identify and reduce high-cardinality Prometheus metrics, see this [reduce-prometheus-cardinality.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/08-vendor-custom-metrics-reduction/reduce-prometheus-cardinality.sh)

**Prometheus Relabeling to Drop Expensive Metrics**

For a sample Prometheus ServiceMonitor with metric relabeling to drop expensive metrics, see this [servicemonitor-cost-optimized.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/08-vendor-custom-metrics-reduction/servicemonitor-cost-optimized.yaml)

**CloudWatch Metric Streams: Cost-Effective Alternative**

Use CloudWatch metric filters to extract only the signals you need from existing log data instead of publishing continuous custom metrics, see this [cloudwatch-metric-filter.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/08-vendor-custom-metrics-reduction/cloudwatch-metric-filter.sh).

**Vendor Metrics Cost Checklist**

|
|
| **Metric Source** | **Cost Driver** | **Optimization** |
| --- |--- |--- |
| CloudWatch Container Insights | Per-metric pricing ($0.30/metric/month) | Disable enhanced metrics for non-prod |
| Amazon Managed Prometheus | Ingested samples ($0.03/10M samples) | Drop unused metrics via relabeling |
| CloudWatch Logs | Ingestion \+ storage ($0.50/GB \+ $0.03/GB) | Filter at source, reduce log verbosity |
| Third-party (Datadog, New Relic) | Per-host or per-container pricing | Use namespace-level sampling |
| Custom metrics via PutMetricData | $0.30/metric/month \+ API calls | Batch calls, reduce dimensions |

## Actions
<a name="strategy"></a>

Audit custom metrics and replace them with default metrics or built-in integrations wherever possible.

**Audit process**

For sample commands to list custom metrics, estimate their monthly cost, and identify ones that duplicate Container Insights defaults, see this [audit-custom-metrics.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/08-vendor-custom-metrics-reduction/audit-custom-metrics.sh)

### Common replacements
<a name="common-replacements.93a4227e-cc3b-52d6-9977-dcbb8877c69b"></a>

|
|
| Custom Metric | Default Alternative | Source |
| --- |--- |--- |
| Custom CPU per pod | `pod_cpu_utilization` | Container Insights |
| Custom memory per pod | `pod_memory_utilization` | Container Insights |
| Custom node count | `cluster_node_count` | Container Insights |
| Custom network bytes | `pod_network_rx_bytes` / `pod_network_tx_bytes` | Container Insights |
| Custom disk usage | `node_filesystem_utilization` | Container Insights |
| Custom request count | ALB metrics / Service Mesh | Built-in |

### Cleanup steps
<a name="cleanup-steps.40db8475-458d-5b55-aab0-3571beeea338"></a>

1. **Inventory** – List all custom metrics and their associated costs

1. **Map** – Identify which default metrics or integrations provide equivalent data

1. **Validate** – Confirm dashboards and alarms work with default metrics

1. **Remove** – Delete custom metric publishing from application configurations

1. **Monitor** – Verify no alerting gaps after removal

Audit your metric count with `aws cloudwatch list-metrics`, drop unused metrics via Prometheus relabeling, disable enhanced Container Insights in non-production clusters, and set `ttlSecondsAfterFinished` on jobs to auto-clean metric sources.

**key takeaway**: Monitoring costs scale with cluster size unless you actively manage cardinality. A 100-node cluster can easily generate thousands of metrics, most of which nobody looks at. Filter at the source, not after ingestion.

## Recommendations
<a name="recommendations"></a>
+ Enable CloudWatch Container Insights as the default observability layer, it provides comprehensive metrics at lower cost than custom metrics
+ Use the CloudWatch Metrics Calculator to estimate savings from custom metric removal
+ Retain custom metrics only when they provide unique business-level data not available from infrastructure metrics
+ Review metric publishing frequency, reduce from 1-second to 60-second resolution where real-time precision isn't required (saves on high-resolution metric charges)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
