---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/userguide/monitoring-cloudwatch.html
---

# Monitoring RTB Fabric metrics with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor RTB Fabric using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

For RTB Fabric, you can monitor request volume, latency, HTTP status codes, and infrastructure metrics to track the performance and health of your RTB gateways and links.

The RTB Fabric service reports metrics in the `AWS/RTBFabric` namespace.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
