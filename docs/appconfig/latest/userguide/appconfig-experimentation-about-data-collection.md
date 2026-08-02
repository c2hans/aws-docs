---
source_url: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-experimentation-about-data-collection.html
---

# About data collection
<a name="appconfig-experimentation-about-data-collection"></a>

While AWS AppConfig experimentation provides aggregate metrics on your experiment, it does not provide analytics for experiment results. The experiment dashboard includes real-time monitoring of experiment traffic. You can view audience exposure levels, treatment allocation over time, and traffic distribution across treatments.

For per-user metrics analysis, you can use CloudWatch, Snowflake, Datadog, or other analytics platforms. To monitor operational metrics, choose **View in CloudWatch** from the experiment dashboard to access operational metrics directly. With CloudWatch, you can monitor key metrics such as page load time, conversion rate, and error rates during an experiment run. You can also configure CloudWatch alarms to alert you when key metrics exceed acceptable thresholds during an experiment run.

For experiment results analysis such as conversion rates, user engagement, and feature adoption, use CloudWatch or your existing analytics platforms. You can export experiment data to data warehouses such as [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html), Snowflake, or Databricks. You can also integrate with monitoring tools such as Datadog, New Relic, or Dynatrace, or use AWS services such as Amazon S3 for durable data storage and [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) to capture client-side user interactions. This approach gives you full control over how metrics are defined, collected, and interpreted.
