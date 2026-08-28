---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/timestream-for-influxdb-well-architected-framework/introduction.html
---

# Applying the AWS Well-Architected Framework for Amazon Timestream for InfluxDB
<a name="introduction"></a>

*Balwanth Bobilli, Amazon Web Services*

You can build time-series-based solutions on Amazon Web Services (AWS) by using [Amazon Timestream](https://docs.aws.amazon.com/timestream/). Amazon Timestream offers fully managed, purpose-built time-series database engines for workloads, from low-latency queries to large-scale data ingestion. With [Amazon Timestream for InfluxDB](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html), you can run open source InfluxDB databases on AWS for time-series applications, such as real-time alerting and monitoring infrastructure reliability, with millisecond response times. Timestream for InfluxDB provides up to 99.9 percent availability.

This guide provides prescriptive guidance for applying the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) principles when you plan your Timestream for InfluxDB deployment. The AWS Well-Architected Framework helps you build secure, high-performing, resilient, and efficient infrastructures for a variety of applications and workloads. It also provides a consistent approach for you to evaluate architectures and implement scalable designs.

The AWS Well-Architected Framework is built around the following six pillars:
+ Operational excellence
+ Security
+ Reliability
+ Performance efficiency
+ Cost optimization
+ Sustainability

This guide provides information from the AWS Well-Architected Framework design pillars. Consider using these best practices when you deploy Amazon Timestream for InfluxDB on AWS.

**Note**
Some AWS services aren't available in all AWS Regions. For Region availability, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page in the AWS documentation, and choose the link for the service.

## Intended audience
<a name="audience"></a>

This guide is intended for data engineers, solutions architects, and data analysts who design and implement solutions for time-series data on AWS.

## Objectives
<a name="objectives"></a>

This guide can help you and your organization do the following:
+ Choose from the supported deployment options, perform optimized writes, and implement fine-grained access.
+ Follow the AWS Well-Architected design patterns that help improve resiliency and security.
+ Design your queries for optimal performance.
+ Learn how to be operationally efficient when managing your Timestream for InfluxDB instance in production.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
