---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-amazon-ecr-repositories-for-wildcard-permissions-using-aws-cloudformation-and-aws-config.html
---

# Monitor Amazon ECR repositories for wildcard permissions using AWS CloudFormation and AWS Config
<a name="monitor-amazon-ecr-repositories-for-wildcard-permissions-using-aws-cloudformation-and-aws-config"></a>

*Vikrant Telkar, Wassim Benhallam, and Sajid Momin, Amazon Web Services*

## Summary
<a name="monitor-amazon-ecr-repositories-for-wildcard-permissions-using-aws-cloudformation-and-aws-config-summary"></a>

On the Amazon Web Services (AWS) Cloud, Amazon Elastic Container Registry (Amazon ECR) is a managed container image registry service that supports private repositories with resource-based permissions using AWS Identity and Access Management (IAM).

IAM supports the "`*`" wildcard in both the resource and action attributes, which makes it easier to automatically choose multiple matching items. In your testing environment, you can allow all authenticated AWS users to access an Amazon ECR repository by using the `ecr:*` [wildcard permission](https://docs.aws.amazon.com/lambda/latest/operatorguide/wildcard-permissions-iam.html) in a principal element for your [repository policy statement](https://docs.aws.amazon.com/AmazonECR/latest/userguide/set-repository-policy.html). The `ecr:*` wildcard permission can be useful when developing and testing in development accounts that can't access your production data.

However, you must make sure that the `ecr:*` wildcard permission is not used in your production environments because it can cause serious security vulnerabilities. This pattern’s approach helps you to identify Amazon ECR repositories that contain the `ecr:*` wildcard permission in repository policy statements.   The pattern provides steps and an AWS CloudFormation template to create a custom rule in AWS Config. An AWS Lambda function then monitors your Amazon ECR repository policy statements for `ecr:*` wildcard permissions. If it finds non-compliant repository policy statements, Lambda notifies AWS Config to send an event to Amazon EventBridge and EventBridge then initiates an Amazon Simple Notification Service (Amazon SNS) topic. The SNS topic notifies you by email about the non-compliant repository policy statements.

## Prerequisites and limitations
<a name="monitor-amazon-ecr-repositories-for-wildcard-permissions-using-aws-cloudformation-and-aws-config-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI), installed and configured. For more information about this, see [Installing, updating, and uninstalling the AWS CLI ](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)in the AWS CLI documentation.
+ An existing Amazon ECR repository with an attached policy statement, installed and configured in your testing environment. For more information about this, see [Creating a private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) and [Setting a repository policy statement](https://docs.aws.amazon.com/AmazonECR/latest/userguide/set-repository-policy.html) in the Amazon ECR documentation.
+ AWS Config, configured in your preferred AWS Region. For more information about this, see [Getting started with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) in the AWS Config documentation.
+ The `aws-config-cloudformation.template` file (attached), downloaded to your local machine.

**Limitations **
+ This pattern’s solution is Regional and your resources must be created in the same Region.

## Architecture
<a name="monitor-amazon-ecr-repositories-for-wildcard-permissions-using-aws-cloudformation-and-aws-config-architecture"></a>

The following diagram shows how AWS Config evaluates Amazon ECR repository policy statements.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01bbf5f8-27aa-4c64-9a03-7fcccc0955b8/images/49bbf14b-0a18-4d4a-86ab-162d37708e01.png)

The diagram shows the following workflow:

1. AWS Config initiates a custom rule.

1. The custom rule invokes a Lambda function to evaluate the compliance of the Amazon ECR repository policy statements. The Lambda function then identifies non-compliant repository policy statements.

1. The Lambda function sends the non-compliance status to AWS Config.

1. AWS Config sends an event to EventBridge.

1. EventBridge publishes the non-compliance notifications to an SNS topic.

1. Amazon SNS sends an email alert to you or an authorized user.

**Automation and scale**

This pattern’s solution can monitor any number of Amazon ECR repository policy statements, but all resources that you want to evaluate must be created in the same Region.

## Tools
<a name="monitor-amazon-ecr-repositories-for-wildcard-permissions-using-aws-cloudformation-and-aws-config-tools"></a>
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – AWS CloudFormation helps you model and set up your AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle. You can use a template to describe your resources and their dependencies, and launch and configure them together as a stack, instead of managing resources individually. You can manage and provision stacks across multiple AWS accounts and AWS Regions.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) – AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time.
+ [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)** **–** **Amazon Elastic Container Registry (Amazon ECR) is an AWS managed container image registry  service that is secure, scalable, and reliable. Amazon ECR supports private repositories with resource-based permissions using IAM.
+ [Amazon EventBridge ](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)– Amazon EventBridge is a serverless event bus service that you can use to connect your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your applications, software as a service (SaaS) applications, and AWS services to targets such as AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other accounts.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time that you consume—there is no charge when your code is not running.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) coordinates and manages the delivery or sending of messages between publishers and clients, including web servers and email addresses. Subscribers receive all messages published to the topics to which they subscribe, and all subscribers to a topic receive the same messages.

**Code**

The code for this pattern is available in the `aws-config-cloudformation.template` file (attached).

## Epics
<a name="monitor-amazon-ecr-repositories-for-wildcard-permissions-using-aws-cloudformation-and-aws-config-epics"></a>

### Create the AWS CloudFormation stack
<a name="create-the-aws-cloudformation-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the AWS CloudFormation stack. | Create an AWS CloudFormation stack by running the following command in AWS CLI:<pre>$ aws cloudformation create-stack --stack-name=AWSConfigECR \<br />    --template-body  file://aws-config-cloudformation.template \<br />    --parameters ParameterKey=<email>,ParameterValue=<myemail@example.com> \<br />    --capabilities CAPABILITY_NAMED_IAM</pre> | AWS DevOps |

### Test the AWS Config custom rule
<a name="test-the-aws-config-custom-rule"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the AWS Config custom rule. | 1. Sign in to the AWS Management Console, open the AWS Config console, and then choose **Resources**.<br />2. On the **Resource inventory** page, you can filter by resource category, resource type, and compliance status.<br />3. An Amazon ECR repository that contains `ecr:*` is `NON-COMPLIANT?` and an Amazon ECR repository that doesn't contain `ecr:*` is `COMPLIANT`.<br />4. The email address subscribed to the SNS topic receives notifications if an Amazon ECR repository contains non-compliant policy statements. | AWS DevOps |

## Attachments
<a name="attachments-01bbf5f8-27aa-4c64-9a03-7fcccc0955b8"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/01bbf5f8-27aa-4c64-9a03-7fcccc0955b8/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
