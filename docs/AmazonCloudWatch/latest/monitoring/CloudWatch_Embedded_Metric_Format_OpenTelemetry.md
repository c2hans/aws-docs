---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_OpenTelemetry.html
---

# Using the embedded metric format with AWS Distro for OpenTelemetry
<a name="CloudWatch_Embedded_Metric_Format_OpenTelemetry"></a>

 OpenTelemetry is an open-source initiative that removes boundaries and restrictions between vendor-specific formats for tracing, logs, and metrics by offering a single set of specifications and APIs. For more information, see [OpenTelemetry](https://opentelemetry.io/). You can use the embedded metric format as a part of the OpenTelemetry project. Using the embedded metric format with OpenTelemetry requires two components: an OpenTelemetry-compliant data source and the AWS Distro for OpenTelemetry Collector enabled for use with CloudWatch embedded metric format logs.

 We have preconfigured redistributions of the OpenTelemetry components, which AWS maintains, to make onboarding as easy as possible. For more information about using OpenTelemetry with the embedded metric format, in addition to other AWS services, see [AWS Distro for OpenTelemetry](https://aws-otel.github.io/). For additional information regarding language support and usage, see [AWS Observability on Github](https://github.com/aws-observability).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
