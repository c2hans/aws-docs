---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-app-monitoring.html
---

# Application monitoring

Application monitoring provides a real-time view of how your services are performing. It combines topology data stored in OpenSearch with time-series RED metrics (Rate, Errors, Duration) from Amazon Managed Service for Prometheus to surface health, latency, throughput, and error information across your distributed system.

To access application monitoring, in OpenSearch UI navigate to **Observability** > **Application Monitoring**. The sidebar shows two views:
+ **Application Map** – Interactive topology graph of service dependencies
+ **Services** – Catalog of all instrumented services with filtering, detail views, and correlation links

**Topics**
+ [Prerequisites](#observability-app-monitoring-prereqs)
+ [How it works](#observability-app-monitoring-how-it-works)
+ [Ingesting application telemetry](observability-ingestion.md)
+ [Services](observability-app-services.md)
+ [Application Map](observability-app-map.md)

## Prerequisites
<a name="observability-app-monitoring-prereqs"></a>

Before you can use application monitoring, you must have the following resources configured.
+ [OTLP trace data flowing from your OTel Collectors to OpenSearch Ingestion](observability-ingestion.md) (metrics and logs are optional)
+ [Amazon Managed Service for Prometheus configured to receive remote write from OpenSearch Ingestion](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-prometheus.html)
+ An OpenSearch UI workspace with Observability enabled

An observability stack meets the second prerequisite automatically, so it applies only when you set up the pipeline yourself.

## How it works
<a name="observability-app-monitoring-how-it-works"></a>

The following diagram shows the end-to-end architecture for application monitoring.

![Architecture diagram showing microservices sending OTLP data through OTel Collector to OpenSearch Observability Stack components.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/otel-sdk-service.png)

1. Your applications and infrastructure emit telemetry through OpenTelemetry SDKs, auto-instrumentation, or the OTel API to the OTel Collector.

1. The OTel Collector forwards trace data to OpenSearch Ingestion over OTLP.

1. The OpenSearch Ingestion `otel_apm_service_map` processor extracts service-to-service relationships and computes RED metrics.

1. Topology and raw trace data are indexed into OpenSearch. RED metrics are exported to Amazon Managed Service for Prometheus through remote write.

1. OpenSearch UI queries both stores to render the Application Map, Services catalog, and service detail views.
