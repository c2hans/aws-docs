---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/monitoring-eml-metrics.html
---

# Monitoring channels using Amazon CloudWatch metrics
<a name="monitoring-eml-metrics"></a>

You can monitor AWS Elemental MediaLive using Amazon CloudWatch metrics. CloudWatch collects raw data that it receives from MediaLive, and processes it into readable, near real-time metrics that are kept for 15 months. You use CloudWatch to view the metrics. Metrics can help you gain a better perspective about how MediaLive is performing over the short term and long term.

You can set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [Components of a metric](eml-metrics-gen-info.md)
+ [Pricing to view MediaLive metrics](eml-metrics-pricing.md)
+ [Viewing metrics](eml-metrics-view.md)
+ [Alphabetical list of MediaLive metrics](eml-metrics-alpha-list.md)
+ [Global metrics](eml-metrics-global.md)
+ [Input metrics](eml-metrics-input-metrics.md)
+ [MQCS metrics](eml-metrics-quality-score.md)
+ [Output metrics](eml-metrics-output-metrics.md)
+ [Pipeline locking metrics](eml-metrics-output-lock.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
