---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/metrics-data.html
---

# Correlate Amazon ECS application performance using application metrics
<a name="metrics-data"></a>

Amazon ECS on Fargate supports collecting metrics from your applications running on Fargate and exporting them to either Amazon CloudWatch or Amazon Managed Service for Prometheus.

You can use the collected metadata to correlate application performance data with underlying infrastructure data, reducing the mean time to resolve the problem.

Amazon ECS uses an AWS Distro for OpenTelemetry sidecar container to collect and route your application metrics to the destination. The Amazon ECS console experience simplifies the process of adding this integration when creating your task definitions.

**Topics**
+ [Exporting application metrics to Amazon CloudWatch](application-metrics-cloudwatch.md)
+ [Exporting application metrics to Amazon Managed Service for Prometheus](application-metrics-prometheus.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
