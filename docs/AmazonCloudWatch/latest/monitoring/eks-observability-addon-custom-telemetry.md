---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/eks-observability-addon-custom-telemetry.html
---

# Custom telemetry

Besides the telemetry that Container Insights and Application Signals collect, the Amazon CloudWatch Observability add-on and Helm chart can send your own application telemetry to CloudWatch. You can correlate your application data with your infrastructure metrics, because the add-on adds Kubernetes and cloud attributes to it. For the list of attributes, see [Telemetry enrichment](eks-standard-telemetry-attributes.md).
+ [OTLP ingestion](eks-observability-addon-otlp-endpoint.md) – Your applications and collectors push metrics, traces, and logs to the CloudWatch agent over OTLP.
+ [Scraping ServiceMonitor and PodMonitor targets](eks-observability-addon-prometheus-monitors.md) – The CloudWatch agent scrapes the Prometheus targets that your ServiceMonitor and PodMonitor objects describe.

To control which of this telemetry the add-on sends, see [OpenTelemetry filters](eks-observability-addon-telemetry-filters.md). That topic lists which filters apply to each source.

**Topics**
+ [OTLP ingestion](eks-observability-addon-otlp-endpoint.md)
+ [Scraping ServiceMonitor and PodMonitor targets](eks-observability-addon-prometheus-monitors.md)
