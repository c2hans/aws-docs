---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-analytics-well-architected-framework/introduction.html
---

# Applying the AWS Well-Architected Framework for Amazon Neptune Analytics
<a name="introduction"></a>

*Michael Havey and Renuka Uttarala, Amazon Web Services*

You can build graph-based solutions on Amazon Web Services (AWS) by using [Amazon Neptune](https://aws.amazon.com/neptune/). Neptune includes [Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html), a memory-optimized graph analytics engine that can quickly analyze large amounts of graph data to get insights and find trends. It can perform analytics on data in your existing [Neptune database](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html) cluster, or you can load and analyze data from external datasets. This guide provides prescriptive guidance for applying the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) principles when you plan your Neptune Analytics deployment. [Applying the AWS Well-Architected Framework for Amazon Neptune](https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-well-architected-framework/introduction.html) covers the same topic for a Neptune database.

The AWS Well-Architected Framework helps you build secure, high-performing, resilient, and efficient infrastructures for a variety of applications and workloads. It also provides a consistent approach for you to evaluate architectures and implement scalable designs.

The AWS Well-Architected Framework is built around the following six pillars:
+ Operational excellence
+ Security
+ Reliability
+ Performance efficiency
+ Cost optimization
+ Sustainability

This guide provides information from the Well-Architected Framework design pillars and best practices, and considerations to keep in mind when you deploy Neptune Analytics on AWS.

## Intended audience
<a name="audience"></a>

This guide is intended for data engineers, solutions architects, and data analysts who design and implement solutions that use graphs on AWS.

## Objectives
<a name="objectives"></a>

This guide can help you and your organization do the following:
+ Choose from the supported deployment options.
+ Follow the AWS Well-Architected design patterns that help you improve resiliency and security.
+ Design your queries for optimal performance and cost savings.
+ Learn how to be operationally efficient when managing your Neptune Analytics graph in production.
