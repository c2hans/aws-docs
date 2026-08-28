---
source_url: https://docs.aws.amazon.com/glue/latest/dg/tuning-aws-glue-for-apache-spark.html
---

# Improving performance for AWS Glue for Apache Spark jobs
<a name="tuning-aws-glue-for-apache-spark"></a>

In order to improve AWS Glue for Spark performance, you may consider updating certain performance related AWS Glue and Spark parameters.

 For more information about specific strategies for identifying bottlenecks through metrics and reducing their impact, see [Best practices for performance tuning AWS Glue for Apache Spark jobs](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/introduction.html) on AWS Prescriptive Guidance. This guide introduces you to key topics applicable to Apache Spark in all runtime environments, such as Spark architecture and Resilient Distributed Datasets. Using those topics, the guide guides you to implement specific performance tuning strategies, such as optimizing shuffles and parallelizing tasks.

You can identify bottlenecks by configuring AWS Glue to show the Spark UI. For more information, see [Monitoring jobs using the Apache Spark web UI](monitor-spark-ui.md).

Additionally, AWS Glue provides performance features that may be applicable to the specific type of data store your job connects to. Reference information about performance parameters for data stores can be found in [Connection types and options for ETL in AWS Glue for Spark](aws-glue-programming-etl-connect.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
