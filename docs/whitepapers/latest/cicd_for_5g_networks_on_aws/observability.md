---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/observability.html
---

# Observability
<a name="observability"></a>

AWS enables observability for the 5G CNFs that are deployed on AWS by default. This is enabled by Amazon CloudWatch. CloudWatch brings complete visibility to your cloud resources and applications.

Amazon CloudWatch has four major steps during this process:

1. **Collect** — Collect metrics and logs from all of your AWS resources, applications, and services that run on AWS and on-premises servers.

1. **Monitor**— Visualize applications and infrastructure with CloudWatch dashboards, correlate logs and metrics side by side to troubleshoot, and set alerts with [ CloudWatch Alarms ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html).

1. ** Act** — Automate response to operational changes with [ CloudWatch Events ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) and [AWS Auto Scaling](https://aws.amazon.com/autoscaling/).

1. **Analyze** — Up to one-second metrics, extended data retention (15 months), and real-time analysis with [ CloudWatch Metric Math ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html).

The Amazon CloudWatch agent is installed in the customer’s Kubernetes cluster. The agent supports Prometheus [configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/), discovery, and metric pull features, enriching and publishing all high fidelity Prometheus metrics and metadata as [Embedded Metric Format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html) (EMF) to [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html).

[Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) automates the discovery and collection of Prometheus metrics from containerized applications. It automatically collects, filters, and creates aggregated custom CloudWatch metrics visualized in dashboards.

Each event creates metric data points as CloudWatch custom metrics for a curated set of metric dimensions that is fully configurable. Publishing aggregated Prometheus metrics as CloudWatch custom metrics statistics reduces the number of metrics needed to monitor, alarm, and troubleshoot performance problems and failures. You can also analyze the high-fidelity Prometheus metrics using [CloudWatch Logs Insights query language](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html) to isolate specific pods and labels impacting the health and performance of your containerized environments.

AWS CloudTrail offers this visibility, recording every API call across services. [AWS Config](https://aws.amazon.com/config/) offers capability for compliance validation. AWS provides customers with additional monitoring options of metrics, logs, events for the application, infrastructure, and pipelines, using various services like [AWS X-Ray](https://aws.amazon.com/xray/) and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/).
+ AWS can natively integrate open-source metric tools like Prometheus, Fluentd, and so on.
+ [ Prometheus metrics ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-metrics.html) can be further ingested into Amazon CloudWatch or OpenSearch Service for further analysis.
+ AWS uses fluentD as a standard mechanism to collect logs from various systems. That same mechanism is used and configured for this project.

For details on how to configure this mechanism, see [Set Up FluentD as a DaemonSet to Send Logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs.html).

![A screenshot showing Amazon CloudWatch monitored metrics.](http://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g11.png)

*Example of Amazon CloudWatch monitored metrics*
