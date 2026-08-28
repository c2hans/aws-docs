---
source_url: https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-with-adot.html
---

# Using AWS Distro for OpenTelemetry as a collector
<a name="AMP-ingest-with-adot"></a>

This section describes how to configure the AWS Distro for OpenTelemetry (ADOT) Collector to scrape from a Prometheus-instrumented application, and send the metrics to Amazon Managed Service for Prometheus. For more information about the ADOT Collector, see [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/).

The following topics describe three different ways to set up ADOT as a collector for your metrics, based on whether your metrics are coming from Amazon EKS, Amazon ECS, or an Amazon EC2 instance.

**Topics**
+ [Set up metrics ingestion using AWS Distro for OpenTelemetry on an Amazon Elastic Kubernetes Service cluster](AMP-onboard-ingest-metrics-OpenTelemetry.md)
+ [Set up metrics ingestion from Amazon ECS using AWS Distro for Open Telemetry](AMP-onboard-ingest-metrics-OpenTelemetry-ECS.md)
+ [Set up metrics ingestion from an Amazon EC2 instance using remote write](AMP-onboard-ingest-metrics-remote-write-EC2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
