---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/investigate.html
---

# Investigate performance issues by using the Spark UI
<a name="investigate"></a>

Before you apply any best practices to tune performance of your AWS Glue jobs, we highly recommended that you profile the performance and identify the bottlenecks. This will help you focus on the right things.

For quick analysis, [Amazon CloudWatch metrics](https://docs.aws.amazon.com/glue/latest/dg/monitoring-awsglue-with-cloudwatch-metrics.html) provide a basic view of your job metrics. The [Spark UI ](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)provides a deeper view for performance tuning. To use the Spark UI with AWS Glue, you must [enable Spark UI for your AWS Glue jobs](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html). After you are familiar with the Spark UI, follow the [strategies for tuning Spark job performance](performance-tuning-strategies.md) to identify and reduce the impact of bottlenecks based on your findings.

## Identify bottlenecks by using the Spark UI
<a name="identify"></a>

When you open the Spark UI, Spark applications are listed in a table. By default, an AWS Glue job's **App Name** is `nativespark-<Job Name>-<Job Run ID>`. Choose the target Spark app based on the job run ID to open the **Jobs** tab. Incomplete job runs, such as streaming job runs, are listed in **Show incomplete applications**.

The **Jobs** tab shows a summary of all jobs in the Spark application. To determine any stage or task failures, check the total number of tasks. To find the bottlenecks, sort by choosing **Duration**. Drill down to the details of long-running jobs by choosing the link shown in the **Description** column.

![Spark Jobs tab showing duration, stages succeeded/total, and tasks succeeded/total.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/592d38b4-3c49-4bce-b4bc-84f5dde53bf9.png)

The **Details for Job** page lists the stages. On this page, you can see overall insights such as duration, the number of succeeded and total tasks, the number of inputs and outputs, and the amount of shuffle read and shuffle write.

![""](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/c00dfc5f-dc43-4166-9d48-3f47b79371af.png)

The **Executor** tab shows the Spark cluster capacity in detail. You can check the total number of cores. The cluster shown in the following screenshot contains 316 active cores and 512 cores in total. By default, each core can process one Spark task at the same time.

![Executors page summary showing the number cores for executors.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/e3186dc7-a352-4510-bb18-39d33dbd086b.png)

Based on the value  `5/5` shown on the **Details for Job** page, stage 5 is the longest stage, but it uses only 5 cores out of 512. Because the parallelism for this stage is so low, but it takes a significant amount of time, you can identify it as a bottleneck. To improve performance, you want to understand why. To learn more about how to recognize and reduce the impact of common performance bottlenecks, see [Strategies for tuning Spark job performance](performance-tuning-strategies.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
