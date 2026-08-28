---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-well-architected-framework/introduction.html
---

# Applying the AWS Well-Architected Framework for Amazon Neptune
<a name="introduction"></a>

*Brian O'Keefe, Javed Ali, Michael Havey, Melissa Kwok, Abhishek Mishra, Sakti Mishra, Kevin Phillips, and Ganesh Sawhney, Amazon Web Services*

You can build graph-based solutions on Amazon Web Services (AWS) by using [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html). This guide provides prescriptive guidance for applying the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) principles when you plan your Neptune deployment.

The AWS Well-Architected Framework helps you build secure, high-performing, resilient, and efficient infrastructures for a variety of applications and workloads. It also provides a consistent approach for you to evaluate architectures and implement scalable designs.

The AWS Well-Architected Framework is built around the following six pillars:
+ Operational excellence
+ Security
+ Reliability
+ Performance efficiency
+ Cost optimization
+ Sustainability

This guide provides information from the AWS Well-Architected Framework design pillars and best practices, and considerations to keep in mind when deploying Neptune on AWS.

## Intended audience
<a name="audience"></a>

This guide is intended for data engineers, solution architects, and data analysts who design and implement solutions that use graphs on AWS.

## Objectives
<a name="objectives"></a>

This guide can help you and your organization do the following:
+ Choose from the supported deployment options and query languages, based on your use case and query patterns.
+ Follow the AWS Well-Architected design patterns that will help in improving resiliency and security.
+ Design your queries for optimal performance and cost savings.
+ Learn how to be operationally efficient when managing your Neptune cluster in production.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
