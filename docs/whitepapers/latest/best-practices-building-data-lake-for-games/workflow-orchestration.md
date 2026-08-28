---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/workflow-orchestration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Workflow orchestration
<a name="workflow-orchestration"></a>

 ETL operations are the backbone of a data lake. ETL workflows often involve orchestrating and monitoring the execution of many sequential and parallel data processing tasks. As the volume of data grows, game developers find they need to move quickly to process this data to ensure they make faster, well-informed design and business decisions. To process data at scale, game developers need to elastically provision resources to manage the data coming from increasing diverse sources and often end up building complicated data pipelines.

 AWS managed orchestration services such as [AWS Step Functions](https://aws.amazon.com/step-functions/) and [Amazon Managed Workflows for Apache Airflow](https://aws.amazon.com/managed-workflows-for-apache-airflow/) (MWAA) are managed workflow orchestration services that help simplify ETL workflow management that involves a diverse set of technologies. These services provide the scalability, reliability, and availability needed to successfully manage your data processing workflows

## AWS Step Functions
<a name="aws-step-functions"></a>

 [AWS Step Functions](https://aws.amazon.com/step-functions/) is a serverless orchestration service that lets you combine AWS Lambda functions and other AWS services to build to scalable, distributed applications using state machines. Step Functions is based on state machines and tasks. A *state machine* is a workflow. A *task* is a state in a workflow that represents a single unit of work that another AWS service performs. Each step in a workflow is a *state*. With the Step Functions built-in controls, you examine the state of each step in your workflow to make sure that your data processing job runs as expected.

 Step Functions scales horizontally and provides fault-tolerant workflows. You can process data faster using parallel transformations or dynamic parallelism, and it lets you easily retry failed transformations, or choose a specific way to handle errors without the need to manage a complex process. Step Functions manages state, checkpoints, and restarts for you to make sure that your workflows run in order. Step Functions can be integrated with a wide variety of AWS services including:
+  [AWS Lambda](https://aws.amazon.com/lambda/)
+  [AWS Fargate](https://aws.amazon.com/fargate/)
+  [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
+  [AWS Glue](https://aws.amazon.com/glue/)
+  [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS)
+  [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) (Amazon SQS)
+  [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS)
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), and more

 Step Functions has two workflow types:
+  **Standard** **Workflows** have exactly-once workflow transformation, and can run for up to one year.
+  **Express** **Workflows** have at-least-once workflow transformation, and can run for up to five minutes.

 Standard Workflows are ideal for long-running, auditable workflows, as they show execution history and visual debugging. Express Workflows are ideal for high-event-rate workloads, such as streaming data processing. Your state machine transformations will behave differently, depending on which Type you select. Refer to [Standard vs. Express Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html) for details.

 Depending on your data processing needs, Step Functions directly integrates with other data processing services provided by AWS, such as [AWS Batch](https://docs.aws.amazon.com/step-functions/latest/dg/connect-batch.html) for batch processing, [Amazon EMR](https://docs.aws.amazon.com/step-functions/latest/dg/connect-emr.html) for big data processing, [AWS Glue](https://docs.aws.amazon.com/step-functions/latest/dg/connect-glue.html) for data preparation, [Athena](https://docs.aws.amazon.com/step-functions/latest/dg/connect-athena.html) for data analysis, and [AWS Lambda](https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html) for compute. [Run ETL/ELT workflows using Amazon Redshift (Lambda, Amazon Redshift Data API)](https://docs.aws.amazon.com/step-functions/latest/dg/sample-etl-orchestration.html) demonstrates how to use Step Functions and the Amazon Redshift Data API to run an ETL/ELT workflow that loads data into the Amazon Redshift data warehouse. [Manage an Amazon EMR Job](https://docs.aws.amazon.com/step-functions/latest/dg/sample-emr-job.html) demonstrates Amazon EMR and AWS Step Functions integration.

 [Workflow Studio for AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-studio.html) is a low-code visual workflow designer that lets you create serverless workflows by orchestrating AWS services. It makes it easy for game developers to build serverless workflows and empowers game developers to focus on building better gameplay while reducing the time spent writing configuration code for workflow definitions and building data transformations. Use drag-and-drop to create and edit workflows, control how input and output is filtered or transformed for each state, and configure error handling. As you create a workflow, Workflow Studio validates your work and generates code.

![Sample design workflow](http://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/images/sample-design-workflow.png)

## Amazon Managed Workflows for Apache Airflow (MWAA)
<a name="amazon-managed-workflows-for-apache-airflow-mwaa"></a>

 [Apache Airflow](https://airflow.apache.org/) is an open-source tool for programmatically authoring, scheduling, and monitoring workflows. [Amazon Managed Workflows for Apache Airflow](https://aws.amazon.com/managed-workflows-for-apache-airflow/) (MWAA) is a managed orchestration service for Apache Airflow that makes it easier to build, operate, and scale end-to-end data pipelines without having to manage the underlying infrastructure for scalability, availability, and security. Amazon MWAA can help reduce operational cost and engineering overhead.

 The auto scaling mechanism of MWAA automatically increases the number of Apache Airflow workers in response to queued tasks and disposes of extra workers when there are no more tasks queued or running. You can configure task parallelism, auto scaling, and concurrency settings directly on MWAA console.

 Amazon MWAA orchestrates and schedules your workflows by using Directed Acyclic Graphs (DAGs) written in Python. To run DAGs in an Amazon MWAA environment, you copy your files to the Amazon S3, then let Amazon MWAA know where your DAGs and supporting files are located on the Amazon MWAA console. Amazon MWAA takes care of synchronizing the DAGs among workers, schedulers, and the web server.

![A diagram showing how all of the components contained in the MWAA section appear as a single Amazon MWAA environment in your account.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/images/mwaa.jpg)

 Amazon MWAA supports open-source integrations with Amazon Athena, AWS Batch, Amazon CloudWatch, Amazon DynamoDB, AWS DataSync, Amazon EMR, AWS Fargate, Amazon EKS, Amazon Data Firehose, AWS Glue, AWS Lambda, Amazon Redshift, Amazon SQS, Amazon SNS, Amazon SageMaker AI, and Amazon S3, as well as hundreds of built-in and community-created operators and sensors and third-party tools such as Apache Hadoop, Presto, Hive, and Spark to perform data processing tasks.

 Code examples are available for faster integration. For example, [Using Amazon MWAA with Amazon EMR](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-emr.html) demonstrates how to enable an integration using Amazon EMR and Amazon MWAA. [Creating a custom plugin with Apache Hive and Hadoop](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-hive.html) walks you through the steps to create a custom plugin using Apache Hive and Hadoop on an Amazon MWAA environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
