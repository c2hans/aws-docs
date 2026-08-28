---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-data-pipeline-to-ingest-transform-and-analyze-google-analytics-data-using-the-aws-dataops-development-kit.html
---

# Build a data pipeline to ingest, transform, and analyze Google Analytics data using the AWS DataOps Development Kit
<a name="build-a-data-pipeline-to-ingest-transform-and-analyze-google-analytics-data-using-the-aws-dataops-development-kit"></a>

*Anton Kukushkin and Rudy Puig, Amazon Web Services*

## Summary
<a name="build-a-data-pipeline-to-ingest-transform-and-analyze-google-analytics-data-using-the-aws-dataops-development-kit-summary"></a>

This pattern describes how to build a data pipeline to ingest, transform, and analyze Google Analytics data by using the AWS DataOps Development Kit (AWS DDK) and other AWS services. The AWS DDK is an open-source development framework that helps you build data workflows and modern data architecture on AWS. One of the main objectives of the AWS DDK is to save you the time and effort that's typically devoted to labor-intensive data pipeline tasks, such as orchestrating pipelines, building infrastructure, and creating the DevOps behind that infrastructure. You can offload these labor-intensive tasks to AWS DDK so that you can focus on writing code and other high-value activities.

## Prerequisites and limitations
<a name="build-a-data-pipeline-to-ingest-transform-and-analyze-google-analytics-data-using-the-aws-dataops-development-kit-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An Amazon AppFlow connector for Google Analytics, [configured](https://docs.aws.amazon.com/appflow/latest/userguide/google-analytics.html)
+ [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/cli/pip_download/) (Python’s package manager)
+ Git, installed and [configured](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
+ AWS Cloud Development Kit (AWS CDK), [installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install)

**Product versions**
+ Python 3.7 or later
+ pip 9.0.3 or later

## Architecture
<a name="build-a-data-pipeline-to-ingest-transform-and-analyze-google-analytics-data-using-the-aws-dataops-development-kit-architecture"></a>

**Technology stack**
+ Amazon AppFlow
+ Amazon Athena
+ Amazon CloudWatch
+ Amazon EventBridge
+ Amazon Simple Storage Service (Amazon S3)
+ Amazon Simple Queue Service (Amazon SQS)
+ AWS DataOps Development Kit (AWS DDK)
+ AWS Lambda

**Target architecture**

The following diagram shows the event-driven process that ingests, transforms, and analyzes Google Analytics data.

![Ingesting, transforming, and analyzing Google Analytics data with AWS services.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/edf40222-2867-4d4a-9153-ab29785b6662/images/8c38b472-153b-4497-982c-8efb97d2f7a5.png)

The diagram shows the following workflow:

1. An Amazon CloudWatch scheduled event rule invokes Amazon AppFlow.

1. Amazon AppFlow ingests Google Analytics data into an S3 bucket.

1. After the data is ingested by the S3 bucket, event notifications in EventBridge are generated, captured by a CloudWatch Events rule, and then put into an Amazon SQS queue.

1. A Lambda function consumes events from the Amazon SQS queue, reads the respective S3 objects, transforms the objects to Apache Parquet format, writes the transformed objects to the S3 bucket, and then creates or updates the AWS Glue Data Catalog table definition.

1. An Athena query runs against the table.

## Tools
<a name="build-a-data-pipeline-to-ingest-transform-and-analyze-google-analytics-data-using-the-aws-dataops-development-kit-tools"></a>

**AWS tools**
+ [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html) is a fully-managed integration service that enables you to securely exchange data between software as a service (SaaS) applications.
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon S3 by using standard SQL.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is a framework for defining cloud infrastructure in code and provisioning it through CloudFormation.
+ [AWS DataOps Development Kit (AWS DDK)](https://github.com/awslabs/aws-ddk) is an open-source development framework to help you build data workflows and modern data architecture on AWS.

**Code**

The code for this pattern is available in the GitHub [AWS DataOps Development Kit (AWS DDK)](https://github.com/awslabs/aws-ddk) and [Analyzing Google Analytics data with Amazon AppFlow, Amazon Athena, and AWS DataOps Development Kit](https://github.com/aws-samples/aws-ddk-examples/tree/main/google-analytics-data-using-appflow/python) repositories.

## Epics
<a name="build-a-data-pipeline-to-ingest-transform-and-analyze-google-analytics-data-using-the-aws-dataops-development-kit-epics"></a>

### Prepare the environment
<a name="prepare-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the source code. | To clone the source code, run the following command:<pre>git clone https://github.com/aws-samples/aws-ddk-examples.git</pre> | DevOps engineer |
| Create a virtual environment. | Navigate to the source code directory, and then run the following command to create a virtual environment:<pre>cd google-analytics-data-using-appflow/python && python3 -m venv .venv</pre> | DevOps engineer |
| Install the dependencies. | To activate the virtual environment and install the dependencies, run the following command:<pre>source .venv/bin/activate && pip install -r requirements.txt</pre> | DevOps engineer |

### Deploy the application that uses your data pipeline
<a name="deploy-the-application-that-uses-your-data-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Bootstrap the environment. | 1. Confirm that the AWS CLI is set up with valid credentials for your AWS account. For more information, see [Using named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles) in the AWS CLI documentation.<br />2. Run the `cdk bootstrap --profile [AWS_PROFILE]` command. | DevOps engineer |
| Deploy the data. | To deploy the data pipeline, run the `cdk deploy --profile [AWS_PROFILE]` command. | DevOps engineer |

### Test the deployment
<a name="test-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate stack status. | 1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. On the **Stacks** page, confirm that the status of the stack `DdkAppflowAthenaStack` is `CREATE_COMPLETE`. | DevOps engineer |

## Troubleshooting
<a name="build-a-data-pipeline-to-ingest-transform-and-analyze-google-analytics-data-using-the-aws-dataops-development-kit-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Deployment fails during the creation of an `AWS::AppFlow::Flow` resource and you receive the following error: `Connector Profile with name ga-connection does not exist` | Confirm that you created an Amazon AppFlow connector for Google Analytics and named it `ga-connection`.<br />For instructions, see [Google Analytics](https://docs.aws.amazon.com/appflow/latest/userguide/google-analytics.html) in the Amazon AppFlow documentation. |

## Related resources
<a name="build-a-data-pipeline-to-ingest-transform-and-analyze-google-analytics-data-using-the-aws-dataops-development-kit-resources"></a>
+ [AWS DataOps Development Kit (AWS DDK)](https://github.com/awslabs/aws-ddk) (GitHub)
+ [AWS DDK Examples](https://github.com/aws-samples/aws-ddk-examples) (GitHub)

## Additional information
<a name="build-a-data-pipeline-to-ingest-transform-and-analyze-google-analytics-data-using-the-aws-dataops-development-kit-additional"></a>

AWS DDK data pipelines are composed of one or many stages. In the following code examples, you use `AppFlowIngestionStage` to ingest data from Google Analytics, `SqsToLambdaStage` to handle data transformation, and `AthenaSQLStage` to run the Athena query.

First, the data transformation and ingestion stages are created, as the following code example shows:

```
        appflow_stage = AppFlowIngestionStage(
            self,
            id="appflow-stage",
            flow_name=flow.flow_name,
        )
        sqs_lambda_stage = SqsToLambdaStage(
            self,
            id="lambda-stage",
            lambda_function_props={
                "code": Code.from_asset("./ddk_app/lambda_handlers"),
                "handler": "handler.lambda_handler",
                "layers": [
                    LayerVersion.from_layer_version_arn(
                        self,
                        id="layer",
                        layer_version_arn=f"arn:aws:lambda:{self.region}:336392948345:layer:AWSDataWrangler-Python39:1",
                    )
                ],
                "runtime": Runtime.PYTHON_3_9,
            },
        )
        # Grant lambda function S3 read & write permissions
        bucket.grant_read_write(sqs_lambda_stage.function)
        # Grant Glue database & table permissions
        sqs_lambda_stage.function.add_to_role_policy(
            self._get_glue_db_iam_policy(database_name=database.database_name)
        )
        athena_stage = AthenaSQLStage(
            self,
            id="athena-sql",
            query_string=[
                (
                    "SELECT year, month, day, device, count(user_count) as cnt "
                    f"FROM {database.database_name}.ga_sample "
                    "GROUP BY year, month, day, device "
                    "ORDER BY cnt DESC "
                    "LIMIT 10; "
                )
            ],
            output_location=Location(
                bucket_name=bucket.bucket_name, object_key="query-results/"
            ),
            additional_role_policy_statements=[
                self._get_glue_db_iam_policy(database_name=database.database_name)
            ],
        )
```

Next, the `DataPipeline` construct is used to "wire" the stages together by using EventBridge rules, as the following code example shows:

```
        (
            DataPipeline(self, id="ingestion-pipeline")
            .add_stage(
                stage=appflow_stage,
                override_rule=Rule(
                    self,
                    "schedule-rule",
                    schedule=Schedule.rate(Duration.hours(1)),
                    targets=appflow_stage.targets,
                ),
            )
            .add_stage(
                stage=sqs_lambda_stage,
                # By default, AppFlowIngestionStage stage emits an event after the flow run finishes successfully
                # Override rule below changes that behavior to call the the stage when data lands in the bucket instead
                override_rule=Rule(
                    self,
                    "s3-object-created-rule",
                    event_pattern=EventPattern(
                        source=["aws.s3"],
                        detail={
                            "bucket": {"name": [bucket.bucket_name]},
                            "object": {"key": [{"prefix": "ga-data"}]},
                        },
                        detail_type=["Object Created"],
                    ),
                    targets=sqs_lambda_stage.targets,
                ),
            )
            .add_stage(stage=athena_stage)
        )
```

For more code examples, see the GitHub [Analyzing Google Analytics data with Amazon AppFlow, Amazon Athena, and AWS DataOps Development Kit](https://github.com/aws-samples/aws-ddk-examples/tree/main/google-analytics-data-using-appflow/python) repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
