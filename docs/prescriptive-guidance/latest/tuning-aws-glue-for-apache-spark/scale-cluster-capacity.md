---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/scale-cluster-capacity.html
---

# Scale cluster capacity
<a name="scale-cluster-capacity"></a>

If your job is taking too much time, but executors are consuming sufficient resources and Spark is creating a large volume of tasks relative to available cores, consider scaling cluster capacity. To assess if this is appropriate, use the following metrics.

## CloudWatch metrics
<a name="scaling-metrics"></a>
+ Check **CPU Load** and **Memory Utilization** to determine whether executors are consuming sufficient resources.
+ Check how long the job has run to assess whether the processing time is too long to meet your performance goals.

In the following example, four executors are running at more than 97 percent CPU load*, *but processing has not been completed after about three hours.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/bdff4ca8-7a07-4ff0-aafa-d47854d46666.png)

|
|
| Note: If CPU load is low, you probably will not benefit from scaling cluster capacity. |
| --- |

## Spark UI
<a name="scaling-spark"></a>

On the **Job** tab or the** Stage** tab, you can see the number of tasks for each job or stage. In the following example, Spark has created `58100` tasks.

![Stages for All Jobs showing one stage and 58,100 tasks.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/f528359e-a638-4fb7-91ed-be18410bb5db.png)

On the **Executor** tab, you can see the total number of executors and tasks. In the following screenshot, each Spark executor has four cores and can perform four tasks concurrently.

![Executors table showing the Cores column.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/ca6082e8-94ff-4c34-95e7-50e89698b62e.png)

In this example, the number of Spark tasks (`58100)` is much larger than the 16 tasks that the executors can process concurrently (4 executors × 4 cores ).

If you observe these symptoms, consider scaling the cluster. You can scale cluster capacity by using the following options:
+ **Enable AWS Glue Auto Scaling** – [Auto Scaling](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html) is available for your AWS Glue extract, transform, and load (ETL) and streaming jobs in AWS Glue version 3.0 or later. AWS Glue automatically adds and removes workers from the cluster depending on the number of partitions at each stage or the rate at which microbatches are generated on the job run.

  If you observe a situation where the number of workers does not increase even though Auto Scaling is enabled, consider adding workers manually. However, note that scaling manually for one stage might cause many workers to be idle during later stages, costing more for zero performance gain.

  After you enable Auto Scaling, you can see the number of executors in the CloudWatch executor metrics. Use the following metrics to monitor the demand for executors in Spark applications:
  + `glue.driver.ExecutorAllocationManager.executors.numberAllExecutors`
  + `glue.driver.ExecutorAllocationManager.executors.numberMaxNeededExecutors`

  For more information about metrics, see [Monitoring AWS Glue using Amazon CloudWatch metrics](https://docs.aws.amazon.com/glue/latest/dg/monitoring-awsglue-with-cloudwatch-metrics.html).
+ **Scale out: Increase the number of AWS Glue workers** – You can manually increase the number of AWS Glue workers. Add workers only until you observe idle workers. At that point, adding more workers will increase costs without improving results. For more information, see [Parallelize tasks](parallelize-tasks.md).
+ **Scale up: Use a larger worker type** – You can manually change the instance type of your AWS Glue workers to use workers with more cores, memory, and storage. Larger worker types make it possible for you to vertically scale and run intensive data integration jobs, such as memory-intensive data transforms, skewed aggregations, and entity-detection checks involving petabytes of data.

  Scaling up also assists in cases where the Spark driver needs larger capacity—for instance, because the job query plan is quite large. For more information about worker types and performance, see the AWS Big Data Blog post [Scale your AWS Glue for Apache Spark jobs with new larger worker types G.4X and G.8X](https://aws.amazon.com/blogs/big-data/scale-your-aws-glue-for-apache-spark-jobs-with-new-larger-worker-types-g-4x-and-g-8x/).

  Using larger workers can also reduce the total number of workers needed, which increases performance by reducing shuffle in intensive operations such as join.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
