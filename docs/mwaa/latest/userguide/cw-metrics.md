---
source_url: https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html
---

# Monitoring and metrics for Amazon Managed Workflows for Apache Airflow
<a name="cw-metrics"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon Managed Workflows for Apache Airflow and your AWS solution. We recommend collecting monitoring data from all parts of your AWS solution so you can more easily debug a multi-point failure if one occurs. This topic describes what resources AWS provides for monitoring your Amazon MWAA environment and responding to potential events.

**Note**
Apache Airflow metrics and logging are subject to standard [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

For more information about monitoring Apache Airflow, refer to [Logging & Monitoring](https://airflow.apache.org/docs/apache-airflow/stable/logging-monitoring/index.html) in the Apache Airflow documentation website.

**Topics**
+ [Monitoring overview on Amazon MWAA](monitoring-overview.md)
+ [Accessing audit logs in AWS CloudTrail](monitoring-cloudtrail.md)
+ [Accessing Airflow logs in Amazon CloudWatch](monitoring-airflow.md)
+ [Monitoring dashboards and alarms on Amazon MWAA](monitoring-dashboard.md)
+ [Apache Airflow environment metrics in CloudWatch](access-metrics-cw.md)
+ [Container, queue, and database metrics for Amazon MWAA](accessing-metrics-cw-container-queue-db.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
