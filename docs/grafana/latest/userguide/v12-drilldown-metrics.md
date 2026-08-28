---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/v12-drilldown-metrics.html
---

# Metrics Drilldown
<a name="v12-drilldown-metrics"></a>

The Metrics Drilldown app provides a queryless, point-and-click experience for exploring Prometheus metric data. You can quickly find related metrics without needing to write PromQL queries.

Key capabilities include:
+ Browse and discover metrics without writing queries.
+ OpenTelemetry filtering support that automates label joins for non-promoted resource attributes.
+ Native histogram support for higher-resolution visualizations.
+ Pivot from metrics to related logs to correlate signals.
+ Entry point directly from alerting rules.

To access Metrics Drilldown, choose **Drilldown** and then **Metrics** from the Grafana navigation menu.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
