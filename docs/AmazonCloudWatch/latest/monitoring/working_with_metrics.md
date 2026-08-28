---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html
---

# Metrics in Amazon CloudWatch
<a name="working_with_metrics"></a>

Metrics are data about the performance of your systems. Amazon CloudWatch collects metrics through two paths: AWS vended metrics from services such as Amazon EC2, Amazon EBS, and Amazon RDS, and custom metrics that you publish using the OpenTelemetry Protocol (OTLP) or the CloudWatch API.

## Overview
<a name="metrics-overview"></a>

### OpenTelemetry: open-source native metrics in CloudWatch
<a name="metrics-overview-otel-intro"></a>

CloudWatch supports OpenTelemetry as the recommended path for metric ingestion and querying. You can use vendor-agnostic, open-source instrumentation to send metrics to CloudWatch – the same OTel SDKs and collectors that work with Prometheus, Grafana, and other backends work with CloudWatch out of the box.

### Two metric models
<a name="metrics-overview-comparison"></a>

CloudWatch supports two metric models. Both are fully supported – choose based on your needs:

|  | **[OpenTelemetry Metrics (Recommended)](metrics-otel-recommended.md)** | **[CloudWatch Metrics (Classic)](metrics-classic.md)** |
| --- | --- | --- |
| **Ingestion** | OTLP endpoint (OTel SDKs, collectors) | PutMetricData API, EMF |
| **Query language** | PromQL | CloudWatch Metrics Insights (SQL) |
| **Labels / Dimensions** | Up to 150 labels per data point | Up to 30 dimensions per metric |
| **Pricing model** | Per GB ingested | Per metric per month |
| **Storage** | Up to 15 months | Up to 15 months |
| **Metric names** | Open-source native | Proprietary (CloudWatch-format) |
| **Best for** | New workloads, containers, high-cardinality | Existing integrations, low-cardinality AWS service metrics |

### Getting started
<a name="metrics-overview-getting-started"></a>
+ **New to CloudWatch metrics?** Start with [OpenTelemetry Metrics (Recommended)](metrics-otel-recommended.md).
+ **Already using PutMetricData or EMF?** See [CloudWatch Metrics (Classic)](metrics-classic.md).
+ **Want AWS service metrics in PromQL?** Enable [AWS vended metrics in OpenTelemetry format](CloudWatch-OTelEnrichment.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
