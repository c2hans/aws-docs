---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/features.html
---

# Important features and concepts
<a name="features"></a>

## Logging and monitoring
<a name="logging-monitoring"></a>

AWS Glue has several [logging and monitoring](https://docs.aws.amazon.com/glue/latest/dg/logging-and-monitoring.html) options. By default, AWS Glue sends logs to the `aws-glue` log group in Amazon CloudWatch. These logs include information such as start and end time, configuration settings, and any errors or warnings that might have occurred.

Additionally, AWS Glue Spark ETL jobs provide the following options, which must be enabled for advanced monitoring:
+ [Job metrics](https://docs.aws.amazon.com/glue/latest/dg/monitoring-awsglue-with-cloudwatch-metrics.html) report job-specific metrics to the AWS Glue namespace in CloudWatch every 30 seconds. These job-specific metrics, such as processed records, total input/output data size, and runtime, provide insights into a job's performance. They can help identify bottlenecks or opportunities to optimize configurations.
+ [Continuous logging](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging.html) streams real-time Apache Spark job logs to the `/aws-glue/jobs/logs-v2` log group in CloudWatch. By using real-time logs, you can dynamically monitor AWS Glue jobs while they are running.
+ [Spark UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html) provides a Spark history server web interface for viewing information about the Spark job, such as the event timeline of each stage, a directed acyclic graph, and job environment variables. The persisted Spark UI event logs are stored in Amazon S3, and you can use them in real time or after the job is complete.
+ [Job run insights](https://docs.aws.amazon.com/glue/latest/dg/monitor-job-insights.html) simplifies job debugging and optimization by listening for common Spark exceptions, performing root cause analysis, and providing recommended actions to fix issues. The insights are stored in CloudWatch.

## Automation
<a name="automation"></a>

AWS Glue provides two main ways for you to automate ETL jobs: triggers and workflows.

### AWS Glue triggers
<a name="9999999999999999glu--triggers.ea2c4cb0-2872-5836-9b22-66eec34415af"></a>

When fired, AWS Glue triggers start specified jobs and crawlers. A trigger can be fired on demand, based on a predefined schedule, or based on specific events. You can use triggers to design a chain of dependent jobs and crawlers. For more information, see [AWS Glue triggers](https://docs.aws.amazon.com/glue/latest/dg/about-triggers.html).

### AWS Glue workflows
<a name="9999999999999999glu--workflows.7abead2f-8500-5e2e-a1ec-b03aa1d1475f"></a>

For more complex workloads, you can use AWS Glue workflows to create directed acyclic graphs and to build dependencies between separate AWS Glue entities (triggers, crawlers, and jobs). Workflows also provide a unified interface where you can share parameters, monitor progress, and troubleshoot issues across associated entities.

Setting up many associated entities within AWS Glue workflows can grow increasingly complex. Developers can create [AWS Glue blueprints](https://aws.amazon.com/blogs/big-data/simplify-data-integration-pipeline-development-using-aws-glue-custom-blueprints/) for sharing complex data pipelines with data scientists and business analysts. These templates allow for the consistent and repeatable creation of AWS Glue workflows, abstracting away the technical details.

To learn more about AWS Glue blueprints and workflows, see [Performing complex ETL activities using blueprints and workflows in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/orchestrate-using-workflows.html).

### Orchestrating AWS Glue jobs with other AWS services
<a name="orchestrating-9999999999999999glu--jobs-with-other-9999999999999999aws--services.4878a975-6d15-518d-a454-41b2b8ee77d9"></a>

For more automation options, AWS Glue integrates with other AWS services, such as AWS Lambda, AWS Step Functions, and Amazon Managed Workflows for Apache Airflow (Amazon MWAA).

For more information about the orchestration methods for AWS Glue ETL jobs, see [Orchestration in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/etl-jobs.html).

## Job bookmarks
<a name="bookmarks"></a>

Job bookmarks in AWS Glue are used to keep track of the progress of ETL jobs, which prevents the need to reprocess data in subsequent job runs. When job bookmarks are enabled, AWS Glue maintains a record of data that has already been processed. Then with each run, it processes only the new data in the data source. For more information, see [Tracking processed data using job bookmarks](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html).
