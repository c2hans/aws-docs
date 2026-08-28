---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions.html
---

# Orchestrate an ETL pipeline with validation, transformation, and partitioning using AWS Step Functions
<a name="orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions"></a>

*Sandip Gangapadhyay, Amazon Web Services*

## Summary
<a name="orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions-summary"></a>

This pattern describes how to build a serverless extract, transform, and load (ETL) pipeline to validate, transform, compress, and partition a large CSV dataset for performance and cost optimization. The pipeline is orchestrated by AWS Step Functions and includes error handling, automated retry, and user notification features.

When a CSV file is uploaded to an Amazon Simple Storage Service (Amazon S3) bucket source folder, the ETL pipeline starts to run. The pipeline validates the content and the schema of the source CSV file, transforms the CSV file to a compressed Apache Parquet format, partitions the dataset by year, month, and day, and stores it in a separate folder for analytics tools to process.

The code that automates this pattern is available on GitHub, in the [ETL Pipeline with AWS Step Functions](https://github.com/aws-samples/aws-step-functions-etl-pipeline-pattern) repository.

## Prerequisites and limitations
<a name="orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI) installed and configured with your AWS account, so that you can create AWS resources by deploying an AWS CloudFormation stack. We recommend using AWS CLI version 2. For instructions, see[ Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the AWS CLI documentation. For configuration instructions, see [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) in the AWS CLI documentation.
+ An Amazon S3 bucket.
+ A CSV dataset with the correct schema. (The [code repository](https://github.com/aws-samples/aws-step-functions-etl-pipeline-pattern/) included with this pattern provides a sample CSV file with the correct schema and data type that you can use.)
+ A web browser that supports the AWS Management Console. (See the [list of supported browsers](https://aws.amazon.com/premiumsupport/knowledge-center/browsers-management-console/).)
+ AWS Glue console access.
+ AWS Step Functions console access.

**Limitations**
+ In AWS Step Functions, the maximum limit for keeping history logs is 90 days. For more information, see [Step Functions service quotas](https://docs.aws.amazon.com/step-functions/latest/dg/service-quotas.html) in the AWS Step Functions documentation.

**Product versions**
+ Python 3.13 for AWS Lambda
+ AWS Glue version 4.0

## Architecture
<a name="orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions-architecture"></a>

![ETL process from S3 source bucket through Step Functions, AWS Glue, and Amazon SNS in 10 steps.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8eb792b0-d35b-4a63-ba2d-71eb8d2c1203/images/054c8e9d-76a2-4334-b21a-cbe76af45923.png)

The workflow illustrated in the diagram consists of these high-level steps:

1. The user uploads a CSV file into the source folder in Amazon S3.

1. An Amazon S3 notification event initiates an AWS Lambda function that starts the AWS Step Functions state machine.

1. The Lambda function validates the schema and data type of the raw CSV file.

1. Depending on the validation results:

   1. If validation of the source file succeeds, the file moves to the stage folder for further processing.

   1. If validation fails, the file moves to the error folder, and an error notification is sent through Amazon Simple Notification Service (Amazon SNS).

1. An AWS Glue crawler creates the schema of the raw file from the stage folder in Amazon S3.

1. An AWS Glue job transforms, compresses, and partitions the raw file into Parquet format.

1. The AWS Glue job also moves the file to the transform folder in Amazon S3.

1. The AWS Glue crawler creates the schema from the transformed file. The resulting schema can be used by any analytics job. You can also use Amazon Athena to run ad-hoc queries.

1. If the pipeline completes without errors, the schema file is moved to the archive folder. If any errors are encountered, the file is moved to the error folder instead.

1. Amazon SNS sends a notification that indicates success or failure based on the pipeline completion status.

All the AWS resources used in this pattern are serverless. There are no servers to manage.

## Tools
<a name="orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions-tools"></a>

**AWS services**
+ [AWS Glue](https://aws.amazon.com/glue/) – AWS Glue is a fully managed ETL service that makes it easy for customers to prepare and load their data for analytics.
+ [AWS Step Functions](https://aws.amazon.com/step-functions/) – AWS Step Functions is a serverless orchestration service that lets you combine AWS Lambda functions and other AWS services to build business-critical applications. Through the AWS Step Functions graphical console, you see your application’s workflow as a series of event-driven steps.
+ [Amazon S3](https://aws.amazon.com/s3/) – Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.
+ [Amazon SNS](https://aws.amazon.com/sns/) – Amazon Simple Notification Service (Amazon SNS) is a highly available, durable, secure, fully managed pub/sub messaging service that enables you to decouple microservices, distributed systems, and serverless applications.
+ [AWS Lambda](https://aws.amazon.com/lambda/) – AWS Lambda is a compute service that lets you run code without provisioning or managing servers. AWS Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.

**Code **

The code for this pattern is available on GitHub, in the [ETL Pipeline with AWS Step Functions](https://github.com/aws-samples/aws-step-functions-etl-pipeline-pattern) repository. The code repository contains the following files and folders:
+ `template.yml` – AWS CloudFormation template for creating the ETL pipeline with AWS Step Functions.
+ `parameter.json` – Contains all parameters and parameter values. You update this file to change parameter values, as described in the *Epics *section.
+ `myLayer/python` folder – Contains Python packages needed to create the required AWS Lambda layer for this project.
+ `lambda` folder – Contains the following Lambda functions:
  + `move_file.py` – Moves the source dataset to the archive, transform, or error folder.
  + `check_crawler.py` – Checks the status of the AWS Glue crawler as many times as configured by the `RETRYLIMIT `environment variable before it sends a failure message.
  + `start_crawler.py` – Starts the AWS Glue crawler.
  + `start_step_function.py` – Starts AWS Step Functions.
  + `start_codebuild.py` – Starts the AWS CodeBuild project.
  + `validation.py` – Validates the input raw dataset.
  + `s3object.py` – Creates the required directory structure inside the Amazon S3 bucket.
  + `notification.py` – Sends success or error notifications at the end of the pipeline.

To use the sample code, follow the instructions in the *Epics *section.

## Epics
<a name="orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions-epics"></a>

### Prepare the source files
<a name="prepare-the-source-files"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the sample code repository. | 1. Open the [ETL Pipeline with AWS Step Functions](https://github.com/aws-samples/aws-step-functions-etl-pipeline-pattern) repository.<br />2. Choose **Code** on the main repository page, above the file list, and copy the URL listed under **Clone with HTTPS**.<br />3. Change your working directory to the location where you want to store the sample files.<br />4. At a terminal or command prompt, type the command:<pre>git clone <repoURL></pre><br />where `<repoURL>` refers to the URL you copied in step 2. | Developer |
| Update parameter values. | In your local copy of the repository, edit the `parameter.json` file and update the default parameter values as follows:+ `pS3BucketName` ─ The name of the Amazon S3 bucket for storing the datasets. The template will create this bucket for you. The bucket name must be globally unique.<br />+ `pSourceFolder` ─ The name of the folder inside the Amazon S3 bucket that will be used to upload the source CSV file.<br />+ `pStageFolder` ─ The name of the folder inside the Amazon S3 bucket that will be used as the staging area during the process.<br />+ `pTransformFolder` ─ The name of the folder inside the Amazon S3 bucket that will be used to store transformed and partitioned datasets.<br />+ `pErrorFolder` ─ The folder inside the Amazon S3 bucket that the source CSV file will be moved to if it can’t be validated.<br />+ `pArchiveFolder `─ The name of the folder inside the Amazon S3 bucket that will be used to archive the source CSV file.<br />+ `pEmailforNotification` ─ A valid email address for receiving success/error notifications.<br />+ `pPrefix` ─ A prefix string that will be used in the AWS Glue crawler name.<br />+ `pDatasetSchema` ─ The dataset schema that the source file will be validated against. The Cerberus Python package is used for source dataset validation. For more information, see the [Cerberus](https://cerberus-sanhe.readthedocs.io/usage.html#type) website. | Developer |
| Upload the source code to the Amazon S3 bucket. | Before you deploy the AWS CloudFormation template that automates the ETL pipeline, you must package the source files for the template and upload them to an Amazon S3 bucket. To do this, run the following AWS CLI command with your preconfigured profile:<pre>aws cloudformation package --template-file template.yml --s3-bucket <bucket_name> --output-template-file packaged.template --profile <profile_name></pre><br />where:+ `<bucket_name>` is the name of an existing Amazon S3 bucket in the AWS Region where you want to deploy the stack. This bucket is used to store the source code package for the CloudFormation template.<br />+ `<profile_name>` is a valid AWS CLI profile that you preconfigured when you set up AWS CLI. | Developer |

### Create the stack
<a name="create-the-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation template. | To deploy the AWS CloudFormation template, run the following AWS CLI command:<pre>aws cloudformation deploy --stack-name <stack_name> --template-file packaged.template --parameter-overrides file://parameter.json --capabilities CAPABILITY_IAM --profile <profile_name></pre><br />where:+ `<stack_name>` is a unique identifier for the CloudFormation stack.<br />+ `<profile-name>` is your preconfigured AWS CLI profile. | Developer |
| Check progress. | On the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), check the progress of stack development. When the status is `CREATE_COMPLETE`, the stack has been deployed successfully. | Developer |
| Note the AWS Glue database name. | The **Outputs** tab for the stack displays the name of the AWS Glue database. The key name is `GlueDBOutput`. | Developer |

### Test the pipeline
<a name="test-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start the ETL pipeline. | 1. Navigate to the source folder (`source`, or the folder name you set in the `parameter.json` file) inside the Amazon S3 bucket.<br />2. Upload a sample CSV file to this folder. (The code repository provides a sample file called `Sample_Bank_Transaction_Raw_Dataset.csv`that you can use.) Uploading the file will start the ETL pipeline through Step Functions.<br />3. On the [Step Functions console](https://console.aws.amazon.com/states/home), check the ETL pipeline status. | Developer |
| Check for the partitioned dataset. | When the ETL pipeline completes, verify that the partitioned dataset is available in the Amazon S3 transform folder (`transform`, or the folder name you set in the `parameter.json` file). | Developer |
| Check for the partitioned AWS Glue database. | 1. On the [AWS Glue console](https://console.aws.amazon.com/glue/), select the AWS Glue database created by the stack (this is the database that you noted in the previous epic).<br />2. Verify that the partitioned table is available in the AWS Glue Data Catalog. | Developer |
| Run queries. | (Optional) Use Amazon Athena to run ad-hoc queries on the partitioned and transformed database. For instructions, see [Run SQL queries in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the AWS documentation. | Database analyst |

## Troubleshooting
<a name="orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS Identity and Access Management (IAM) permissions for the AWS Glue job and crawler | If you further customize the AWS Glue job or the crawler, be sure to grant the appropriate IAM permissions in the IAM role used by the AWS Glue job, or provide data permissions to AWS Lake Formation. For more information, see the [AWS documentatio](https://docs.aws.amazon.com/lake-formation/latest/dg/upgrade-glue-lake-formation.html)n. |

## Related resources
<a name="orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions-resources"></a>

**AWS service documentation**
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/)
+ [AWS Glue](https://docs.aws.amazon.com/glue/)
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/)
+ [Amazon S3](https://docs.aws.amazon.com/s3/)
+ [Amazon SNS](https://docs.aws.amazon.com/sns/)

## Additional information
<a name="orchestrate-an-etl-pipeline-with-validation-transformation-and-partitioning-using-aws-step-functions-additional"></a>

The following diagram shows the AWS Step Functions workflow for a successful ETL pipeline, from the AWS Step Functions **Inspector **panel.** **

![Step Functions workflow for validating the input .csv, crawling data, and running the AWS Glue job.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8eb792b0-d35b-4a63-ba2d-71eb8d2c1203/images/bd77de7b-4d04-44bb-95d2-3ec4599b3770.png)

The following diagram shows the AWS Step Functions workflow for an ETL pipeline that fails because of an input validation error, from the Step Functions **Inspector **panel.

![Step Functions workflow with failure so the file moves to the error folder.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8eb792b0-d35b-4a63-ba2d-71eb8d2c1203/images/5fd7dd79-ba4c-4c20-b1f0-ad4b5f22bdfc.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
