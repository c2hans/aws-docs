---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-monitoring.html
---

# Monitoring Flink Kubernetes operator and Flink jobs
<a name="jobruns-flink-monitoring"></a>

This section describes several ways that you can monitor your Flink jobs with Amazon EMR on EKS. These include integrating Flink with the Amazon Managed Service for Prometheus, using the *Flink Web Dashboard*, which provides job status and metrics, or using a monitoring configuration to send log data to Amazon S3 and Amazon CloudWatch.

**Topics**
+ [Use Amazon Managed Service for Prometheus to monitor Flink jobs](jobruns-flink-monitoring-prometheus.md)
+ [Use the Flink UI to monitor Flink jobs](jobruns-flink-monitoring-ui.md)
+ [Use monitoring configuration to monitor Flink Kubernetes operator and Flink jobs](jobruns-flink-monitoring-configuration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
