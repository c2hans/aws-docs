---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-bedrock-invocation-logging-cloudformation.html
---

# Configure model invocation logging in Amazon Bedrock by using AWS CloudFormation
<a name="configure-bedrock-invocation-logging-cloudformation"></a>

*Vikramaditya Bhatnagar, Amazon Web Services*

## Summary
<a name="configure-bedrock-invocation-logging-cloudformation-summary"></a>

You can configure Amazon Bedrock to collect invocation logs, model input data, and model output data for all model invocations in your AWS account. This is a [best practice](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/) for building robust generative AI applications with Amazon Bedrock. You can store model invocation logs in an Amazon CloudWatch Logs log group, in an Amazon Simple Storage Service (Amazon S3) bucket, or in both. Having log data in CloudWatch Logs helps you create custom metric filters, alarms, and dashboards. Amazon S3 is ideal for replicating data across AWS Regions or for long-term storage, as governed by your organization's policies.

This pattern provides a sample AWS CloudFormation template that uses an infrastructure as code (IaC) approach to configure model invocation logging for Amazon Bedrock. The template configures log storage in both CloudWatch Logs and Amazon S3.

## Prerequisites and limitations
<a name="configure-bedrock-invocation-logging-cloudformation-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ The following permissions:
  + [Permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) to create CloudFormation stacks
  + [Permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-updates) to access Amazon Bedrock
  + [Permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html) to create and access Amazon S3 buckets
  + [Permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-identity-based-access-control-cwl.html) to create and access CloudWatch Logs log groups
  + [Permissions](https://docs.aws.amazon.com/lambda/latest/dg/security-iam-awsmanpol.html) to create and access AWS Lambda functions
  + [Permissions](https://docs.aws.amazon.com/kms/latest/developerguide/customer-managed-policies.html) to create and access AWS Key Management Service (AWS KMS) keys

**Limitations**

This pattern logs model invocations to both CloudWatch Logs and Amazon S3. It does not support choosing only one of these two services.

## Architecture
<a name="configure-bedrock-invocation-logging-cloudformation-architecture"></a>

**Target architecture**

The CloudFormation template provisions the following resources in your target AWS account:
+ A CloudWatch Logs log group for storing model invocation logs
+ An Amazon S3 bucket for storing model invocation logs and a corresponding bucket policy
+ An Amazon S3 bucket for storing server-side access logs and a corresponding bucket policy
+ An AWS Lambda function that configures logging settings in Amazon Bedrock
+ An AWS KMS key and a corresponding key alias
+ An AWS Identity and Access Management (IAM) service role for Amazon Bedrock

The following diagram shows how invocation logs are stored after you deploy the CloudFormation stack associated with this pattern. Amazon Bedrock publishes log data when the foundation model delivers text, an image, a video, or embedding data. As shown in the diagram, the Amazon S3 buckets and the CloudWatch Logs log group are encrypted with an AWS KMS key.

![Workflow for logging invocations of an Amazon Bedrock foundation model.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a55e7495-ec84-4d41-886e-5c37b37aac67/images/a958d52f-9072-40af-80cb-360f6c1c7fd5.png)

The diagram shows the following workflow:

1. A user submits a query to a foundation model in Amazon Bedrock.

1. Amazon Bedrock assumes the IAM service role.

1. Amazon Bedrock generates log data and stores it in an CloudWatch Logs log group and in an Amazon S3 bucket.

1. If a user reads, uploads, or deletes any files in the Amazon S3 bucket that contains the model invocation logs, those activities are logged in another Amazon S3 bucket for server-side access logs.

**Automation and scale**

To scale this solution, you can deploy the CloudFormation template as a stack set to multiple AWS Regions and AWS accounts. For more information, see [Managing stacks across accounts and Regions with StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) in the CloudFormation documentation.

## Tools
<a name="configure-bedrock-invocation-logging-cloudformation-tools"></a>

**AWS services**
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that makes high-performing foundation models (FMs) from leading AI companies and Amazon available for your use through a unified API.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all of your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is an object storage service that offers industry-leading scalability, data availability, security, and performance.

**Other tools**
+ [Git](https://git-scm.com/docs) is an open source, distributed version control system.

**Code repository**

The code for this pattern is available in the GitHub [enable-bedrock-logging-using-cloudformation](https://github.com/aws-samples/enable-bedrock-logging-using-cloudformation) repository.

## Epics
<a name="configure-bedrock-invocation-logging-cloudformation-epics"></a>

### Create the CloudFormation stack
<a name="create-the-cfnshort-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the CloudFormation template. | Download the [CloudFormation template](https://github.com/aws-samples/enable-bedrock-logging-using-cloudformation/blob/main/enable-bedrock-logging-using-cloudformation.yaml) from the GitHub repository. | Cloud architect |
| Deploy the template. | Create a stack in your target account and Region. In the **Parameters** section, specify values for the parameters that are defined in the template. For instructions, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation. | Cloud architect |

### Test the solution
<a name="test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable model access. | In Amazon Bedrock, add access to the foundation model. For instructions, see [Add or remove access to Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html) in the Amazon Bedrock documentation. | Cloud architect |
| Run a sample prompt. | In Amazon Bedrock playgrounds, run a sample prompt. For instructions, see [Generate responses in the console using playgrounds](https://docs.aws.amazon.com/bedrock/latest/userguide/playgrounds.html) in the Amazon Bedrock documentation. | Cloud architect |
| Review the logging configuration. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-bedrock-invocation-logging-cloudformation.html) | Cloud architect |
| Review the Amazon S3 bucket. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-bedrock-invocation-logging-cloudformation.html) | Cloud architect |
| Review the log group. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-bedrock-invocation-logging-cloudformation.html) | Cloud architect |

## Related resources
<a name="configure-bedrock-invocation-logging-cloudformation-resources"></a>

**AWS documentation**
+ [Accessing an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html) (Amazon S3 documentation)
+ [Creating and managing stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) (CloudFormation documentation)
+ [Monitor model invocation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) (Amazon Bedrock documentation)
+ [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) (CloudWatch Logs documentation)

**AWS blog posts**
+ [Monitoring Generative AI applications using Amazon Bedrock and Amazon CloudWatch integration](https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/)
+ [Best practices for building robust generative AI applications with Amazon Bedrock Agents – Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/)
+ [Best practices for building robust generative AI applications with Amazon Bedrock Agents – Part 2](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/)
