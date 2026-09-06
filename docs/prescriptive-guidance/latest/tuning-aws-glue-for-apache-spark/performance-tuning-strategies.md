---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/performance-tuning-strategies.html
---

# Strategies for tuning Spark job performance
<a name="performance-tuning-strategies"></a>

When preparing to tune parameters, use the following best practices:
+ Determine your performance goals before beginning to identify problems.
+ Use metrics to identify problems before attempting to change tuning parameters.

For the most consistent results when tuning a job, develop a baseline strategy for your tuning work.

## Baseline strategy for performance tuning
<a name="baseline"></a>

Generally, performance tuning is performed in the following workflow:

1. Determine performance goals.

1. Measure metrics.

1. Identify bottlenecks.

1. Reduce the impact of the bottlenecks.

1. Repeat steps 2-4 until you achieve the intended target.

First, determine your performance goals. For example, one of your goals might be to complete the run of an AWS Glue job within 3 hours. After you define your goals, measure job performance metrics. Identify trends in metrics and bottlenecks to meet the goals. In particular, identifying bottlenecks is most important for troubleshooting, debugging, and performance tuning. During the run of a Spark application, Spark records the status and statistics of each task in the Spark event log.

In AWS Glue, you can view Spark metrics through the [Spark Web UI](https://spark.apache.org/docs/latest/web-ui.html) that's provided by the Spark history server. AWS Glue for Spark jobs can send [Spark event logs](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html) to a location that you specify in Amazon S3. AWS Glue also provides an example [AWS CloudFormation template](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-history.html#monitor-spark-ui-history-cfn) and [Dockerfile](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-history.html#monitor-spark-ui-history-local) to start the Spark history server on an Amazon EC2 instance or your local computer, so you can use the Spark UI with event logs.

After you determine your performance goals and identify metrics to assess those goals, you can begin to identify and remediate bottlenecks by using the strategies in following sections.

## Tuning practices for Spark job performance
<a name="tuning-practices"></a>

You can use the following strategies for performance tuning AWS Glue for Spark jobs:
+ AWS Glue resources:
  + [Scale cluster capacity](scale-cluster-capacity.md)
  + [Use latest AWS Glue version](latest-version.md)
+ Spark applications:
  + [Reduce the amount of data scan](reduce-data-scan.md)
  + [Parallelize tasks](parallelize-tasks.md)
  + [Optimize shuffles](optimize-shuffles.md)
  + [Minimize planning overhead](minimize-planning-overhead.md)
  + [Optimize user-defined functions](optimize-user-defined-functions.md)

Before you use these strategies, you must have access to metrics and configuration for your Spark job. You can find this information in the [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/etl-jobs-section.html).

From the AWS Glue resource perspective, you can achieve performance improvements by adding AWS Glue workers and using the latest AWS Glue version.

From an Apache Spark application perspective, you have access to several strategies that can improve performance. If unnecessary data is loaded into the Spark cluster, you can remove it to reduce the amount of loaded data. If you have underused Spark cluster resources and you have low data I/O, you can identify tasks to parallelize. You might also want to optimize heavy data transfer operations such as joins if they are taking substantial time. You can also optimize your job query plan or reduce the computational complexity of individual Spark tasks.

To efficiently apply these strategies, you must identify when they are applicable by consulting your metrics. For more details, see each of the following sections. These techniques work not only for performance tuning but also for solving typical problems such as out-of-memory (OOM) errors.
