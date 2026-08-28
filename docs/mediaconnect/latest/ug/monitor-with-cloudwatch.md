---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-cloudwatch.html
---

# Monitoring AWS Elemental MediaConnect with Amazon CloudWatch metrics
<a name="monitor-with-cloudwatch"></a>

You can monitor AWS Elemental MediaConnect using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These metrics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. Most MediaConnect metrics can be accessed in periods as short as one second. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

You can view CloudWatch metrics for your flows directly on the MediaConnect console. On the console, you can view these metrics in periods as short as one second or as long as 30 minutes.

**Note**
MediaConnect Gateway metrics are not available in high resolution periods (one second). You must select a period of at least one minute.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
