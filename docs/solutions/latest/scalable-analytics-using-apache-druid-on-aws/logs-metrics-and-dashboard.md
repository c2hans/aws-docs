---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/logs-metrics-and-dashboard.html
---

# Logs, metrics, and dashboard
<a name="logs-metrics-and-dashboard"></a>

The guidance establishes a log group named `/aws/solutions/druid/<cluster name>` in CloudWatch for storing various logs collected from EC2 instances. These logs include:
+ Druid process logs from EC2 instances
+ ZooKeeper process logs
+ System initialization logs from EC2 instances

In addition, it also sets up a S3 bucket to store the logs gathered from AWS infrastructure and services, including:
+ VPC Flow Logs
+ ALB access logs
+ S3 bucket access logs

The guidance creates a metric namespace named `AWSSolutions/Druid` to store the metrics collected from EC2 instances. These metrics include:
+ Druid application metrics (e.g. ingestion/query throughput)
+ Operating system metrics (e.g. CPU/memory/disk utilization)

The guidance includes an Amazon CloudWatch dashboard named `druid-<cluster name>-ops-dashboard` configured to provide an overview of the health and operational status of all components in the guidance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Scalable Analytics Using Apache Druid on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
