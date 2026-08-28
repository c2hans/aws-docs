---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/introduction.html
---

# Monitoring and alerting tools and best practices for Amazon RDS for MySQL and MariaDB
<a name="introduction"></a>

*Igor Obradovic, Amazon Web Services*

Database monitoring is the process of measuring, tracking, and assessing the availability, performance, and functionality of a database. Monitoring and alerting solutions help organizations ensure that their database services, and therefore their associated applications and workloads, are secure, high-performing, resilient, and efficient. On AWS, you can collect and analyze your workload logs, metrics, events, and traces in order to understand the health of your workload and to gain insights from operations over time.

You can monitor your resources to ensure that they are performing as expected, and to detect and remediate any issues before they impact your customers. You should use the metrics, logs, events, and traces that you monitor to raise alarms when thresholds are breached.

This guide describes database observability and monitoring tools and best practices for Amazon Relational Database Service (Amazon RDS) databases. The guide focuses on MySQL and MariaDB databases, although most of the information also applies to other Amazon RDS database engines.

This guide is for solutions architects, database architects, DBAs, senior DevOps engineers, and other team members who engage in designing, implementing, and managing monitoring and observability solutions for their database workloads running in the AWS Cloud.

## Attachments
<a name="attachments-9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
