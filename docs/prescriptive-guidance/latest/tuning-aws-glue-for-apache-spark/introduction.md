---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/introduction.html
---

# Best practices for performance tuning AWS Glue for Apache Spark jobs
<a name="introduction"></a>

*Roman Myers, Takashi Onikura, and Noritaka Sekiyama, Amazon Web Services*

AWS Glue provides different options for tuning performance. This guide defines key topics for tuning AWS Glue for Apache Spark. It then provides a baseline strategy for you to follow when tuning these AWS Glue for Apache Spark jobs. Use this guide to learn how to identify performance problems by interpreting metrics available in AWS Glue. Then incorporate strategies to address these problems, maximizing performance and minimizing costs.

This guide covers the following tuning practices:
+ [Scale cluster capacity](scale-cluster-capacity.md)
+ [Use the latest AWS Glue version](latest-version.md)
+ [Reduce the amount of data scan](reduce-data-scan.md)
+ [Parallelize tasks](parallelize-tasks.md)
+ [Optimize shuffles](optimize-shuffles.md)
+ [Optimize user-defined functions](optimize-user-defined-functions.md)
+ [Minimize planning overhead](minimize-planning-overhead.md)
