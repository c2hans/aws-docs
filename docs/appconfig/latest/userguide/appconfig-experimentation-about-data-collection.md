---
source_url: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-experimentation-about-data-collection.html
---

# About data collection
<a name="appconfig-experimentation-about-data-collection"></a>

Although AWS AppConfig experimentation provides aggregate treatment traffic metrics on your experiment, it does not provide analytics for experiment results. The experiment dashboard includes real-time monitoring of experiment traffic. You can view audience exposure levels, treatment allocation over time, and traffic distribution across treatments. For more information, see [Observing treatment traffic](appconfig-experimentation-observing-treatment-traffic.md).

To monitor operational metrics during a run, choose **View in CloudWatch** from the experiment dashboard. In CloudWatch, you can track metrics such as page load time, conversion rate, and error rates, and set alarms to notify you when a metric crosses a threshold.

For experiment results analysis such as conversion rates, user engagement, and feature adoption, use CloudWatch or your existing analytics platforms. You can export experiment data to data warehouses such as [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html), Snowflake, or Databricks. You can also integrate with monitoring tools such as Datadog, New Relic, or Dynatrace, or use AWS services such as Amazon S3 for durable data storage and [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) to capture client-side user interactions. This approach gives you full control over how metrics are defined, collected, and interpreted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
