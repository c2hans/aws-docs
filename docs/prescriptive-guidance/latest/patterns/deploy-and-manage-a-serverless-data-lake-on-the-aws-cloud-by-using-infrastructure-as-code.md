---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-and-manage-a-serverless-data-lake-on-the-aws-cloud-by-using-infrastructure-as-code.html
---

# Deploy and manage a serverless data lake on the AWS Cloud by using infrastructure as code
<a name="deploy-and-manage-a-serverless-data-lake-on-the-aws-cloud-by-using-infrastructure-as-code"></a>

*Kirankumar Chandrashekar and Abdel Jaidi, Amazon Web Services*

## Summary
<a name="deploy-and-manage-a-serverless-data-lake-on-the-aws-cloud-by-using-infrastructure-as-code-summary"></a>

This pattern describes how to use [serverless computing](https://aws.amazon.com/serverless/) and [infrastructure as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) (IaC) to implement and administer a data lake on the Amazon Web Services (AWS) Cloud. This pattern is based on the [serverless data lake framework (SDLF)](https://sdlf.workshop.aws/) workshop developed by AWS.

SDLF is a collection of reusable resources that accelerate the delivery of enterprise data lakes on the AWS Cloud and helps with faster deployment to production. It is used to implement the foundational structure of a data lake by following best practices.

SDLF implements a continuous integration / continuous deployment (CI/CD) process throughout the code and infrastructure deployment by using AWS services such as AWS CodePipeline, AWS CodeBuild, and AWS CodeCommit.

This pattern uses multiple AWS serverless services to simplify data lake management. These include Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB for storage, AWS Lambda and AWS Glue for computing, and Amazon CloudWatch Events, Amazon Simple Queue Service (Amazon SQS), and AWS Step Functions for orchestration.

AWS CloudFormation and AWS code services act as the IaC layer to provide reproducible and fast deployments with easy operations and administration.

## Prerequisites and limitations
<a name="deploy-and-manage-a-serverless-data-lake-on-the-aws-cloud-by-using-infrastructure-as-code-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), installed and configured.
+ A Git client, installed and configured.
+ The [SDLF workshop](https://sdlf.workshop.aws/), open in a web browser window and ready to use.

## Architecture
<a name="deploy-and-manage-a-serverless-data-lake-on-the-aws-cloud-by-using-infrastructure-as-code-architecture"></a>

![Implementing and administering a data lake on the AWS Cloud.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f4fc3ad2-1c4f-45ea-bc86-2db13105a173/images/e0cfff30-f0f8-4fc1-8e84-a152ef615c58.png)

 The architecture diagram illustrates an event-driven process with the following steps.

1. After a file is added to the raw data S3 bucket, an Amazon S3 event notification is placed in an SQS queue. Each notification is delivered as a JSON file, which contains metadata such as the S3 bucket name, object key, or timestamp.

1. This notification is consumed by a Lambda function that routes the event to the correct extraction, transformation, and loading (ETL) process based on the metadata. The Lambda function can also use contextual configurations stored in an Amazon DynamoDB table. This step enables decoupling and scaling to multiple applications in the data lake.

1. The event is routed to the first Lambda function in the ETL process, which transforms and moves data from the raw data area to the staging area for the data lake. The first step is to update the comprehensive catalog. This is a DynamoDB table that contains all the file metadata of the data lake. Each row in this table holds operational metadata about a single object stored in Amazon S3. A synchronous call is made to a Lambda function that performs a light transformation, which is a computationally inexpensive operation (such as converting a file from one format to another), on the S3 object. Because a new object has been added to the staging S3 bucket, the comprehensive catalog is updated and a message is sent to the SQS queue waiting for the next phase in the ETL.

1. A CloudWatch Events rule triggers a Lambda function every 5 minutes. This function checks if messages were delivered to the SQS queue from the previous ETL phase. If a message was delivered, the Lambda function begins the second function from [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/sample-start-workflow.html) in the ETL process.

1. A heavy transformation is then applied on a batch of files. This heavy transformation is a computationally expensive operation, such as a synchronous call to an AWS Glue job, AWS Fargate task, Amazon EMR step, or Amazon SageMaker notebook. Table metadata is extracted from the output files by using an AWS Glue crawler, which updates the AWS Glue catalog. File metadata is also added to the comprehensive catalog table in DynamoDB. Finally, a data quality step leveraging [Deequ](https://github.com/awslabs/deequ) is also run.

**Technology stack  **
+ Amazon CloudWatch Events
+ AWS CloudFormation
+ AWS CodePipeline
+ AWS CodeBuild
+ AWS CodeCommit
+ Amazon DynamoDB
+ AWS Glue
+ AWS Lambda
+ Amazon S3
+ Amazon SQS
+ AWS Step Functions

## Tools
<a name="deploy-and-manage-a-serverless-data-lake-on-the-aws-cloud-by-using-infrastructure-as-code-tools"></a>
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) – CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS resources.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – CloudFormation helps create and provision AWS infrastructure deployments predictably and repeatedly.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) – CodeBuild is a fully managed build service that compiles your source code, runs unit tests, and produces artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) – CodeCommit is a version control service hosted by AWS that you can use to privately store and manage assets (such as source code and binary files).
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) – CodePipeline is a continuous delivery service that you can use to model, visualize, and automate the steps required to release your software changes continuously.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) – DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with scalability.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) – AWS Glue is a fully managed ETL service that makes it easier to prepare and load data for analytics.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – Lambda supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html) – Amazon Simple Storage Service (Amazon S3) is a highly scalable object storage service. Amazon S3 can be used for a wide range of storage solutions, including websites, mobile applications, backups, and data lakes.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) - AWS Step Functions is a serverless function orchestrator that makes it easy to sequence AWS Lambda functions and multiple AWS services into business-critical applications.
+ [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) – Amazon Simple Queue Service (Amazon SQS) is a fully managed message queuing service that helps you decouple and scale microservices, distributed systems, and serverless applications.
+ [Deequ](https://github.com/awslabs/deequ) – Deequ is a tool that helps you compute data quality metrics for large datasets, define and verify data quality constraints, and stay informed about changes in the data distribution.

**Code repository**

The source code and resources for the SDLF are available in the [AWS Labs GitHub repository](https://github.com/awslabs/aws-serverless-data-lake-framework/).

## Epics
<a name="deploy-and-manage-a-serverless-data-lake-on-the-aws-cloud-by-using-infrastructure-as-code-epics"></a>

### Set up the CI/CD pipeline to provision IaC
<a name="set-up-the-ci-cd-pipeline-to-provision-iac"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the CI/CD pipeline to manage IaC for the data lake. | Sign in to the AWS Management Console and follow the steps from the [Initial setup](https://sdlf.workshop.aws/en/10-deployment/100-setup.html) section of the SDLF workshop. This creates the initial CI/CD resources, such as CodeCommit repositories, CodeBuild environments, and CodePipeline pipelines that provision and manage IaC for the data lake. | DevOps engineer |

### Version-control the IaC
<a name="version-control-the-iac"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the CodeCommit repository on your local machine. | Follow the steps from the [Deploying the foundations ](https://sdlf.workshop.aws/en/10-deployment/200-foundations.html)section of the SDLF workshop. This helps you clone the Git repository that hosts IaC into your local environment. <br />For more information, see [Connecting to CodeCommit repositories ](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-connect.html)from the CodeCommit documentation. | DevOps engineer |
| Modify the CloudFormation templates. | Use your local workstation and a code editor to modify the CloudFormation templates according to your use cases or requirements. Commit them to the locally cloned Git repository. <br />For more information, see [Working with AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) from the AWS CloudFormation documentation. | DevOps engineer |
| Push the changes to the CodeCommit repository.  | Your infrastructure code is now under version control and modifications to your code base are tracked. When you push a change to the CodeCommit repository, CodePipeline automatically applies it to your infrastructure and delivers it to CodeBuild. If you use the AWS SAM CLI in CodeBuild, run the `sam package` and `sam deploy` commands. If you use AWS CLI, run the `aws cloudformation package` and `aws cloudformation deploy` commands. | DevOps engineer |

## Related resources
<a name="deploy-and-manage-a-serverless-data-lake-on-the-aws-cloud-by-using-infrastructure-as-code-resources"></a>

**Set up the CI/CD pipeline to provision IaC**
+ [SDLF workshop – Initial setup](https://sdlf.workshop.aws/en/10-deployment/100-setup.html)

**Version-control the IaC **
+ [SDLF workshop – Deploying the foundations](https://sdlf.workshop.aws/en/10-deployment/200-foundations.html)
+ [Connecting to CodeCommit repositories](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-connect.html)
+ [Working with AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html)

**Other resources**
+ [AWS serverless data analytics pipeline reference architecture](https://aws.amazon.com/blogs/big-data/aws-serverless-data-analytics-pipeline-reference-architecture/)
+ [SDLF documentation](https://sdlf.readthedocs.io/en/latest/)
