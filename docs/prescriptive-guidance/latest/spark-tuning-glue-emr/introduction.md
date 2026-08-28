---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/introduction.html
---

# Tuning Spark SQL queries for AWS Glue and Amazon EMR Spark jobs
<a name="introduction"></a>

*Phani Alapaty and Ravikiran Rao, Amazon Web Services*

[Spark SQL](https://spark.apache.org/sql/) is an Apache Spark module for processing structured data. [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) and [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) jobs use Spark SQL to process, transform and load data. Unlike the basic Spark resilient distributed dataset (RDD) API, the Spark SQL interfaces provide more information to Spark about the structure of both the data and the computation being performed. Internally, Spark SQL uses this extra information to perform additional query optimizations. There are several ways to interact with Spark SQL, including SQL and the Dataset API.

Joining data is one of the most common and important operations you can perform when extracting, transforming, or loading data into object stores or databases. When joining, you need to consider performance. There are multiple scenarios, such as large network transfers, when some of the join, analyze, or aggregate operations run out of memory. This can cause the AWS Glue Spark job to fail.

This guide provides best practices that help you tune Spark SQL join queries for AWS Glue or Amazon EMR jobs. Spark provides many configuration options that improve the performance of the Spark SQL workload. These adjustments can be done programmatically, or you can apply them at the global level by using the `spark-submit` command. This guide explains some of these configurations so that you can improve or fine-tune the performance of your Spark SQL queries and applications. The recommendations in this guide are based on configurations that AWS Professional Services uses to improve the performance of Spark SQL queries and applications.

## Intended audience
<a name="intended-audience"></a>

This guide helps architects, data engineers, data scientists, and developers understand the Spark SQL configuration options that improve the performance of Spark SQL queries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
