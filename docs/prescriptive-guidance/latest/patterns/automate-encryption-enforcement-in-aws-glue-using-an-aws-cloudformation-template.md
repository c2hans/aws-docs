---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-encryption-enforcement-in-aws-glue-using-an-aws-cloudformation-template.html
---

# Automate encryption enforcement in AWS Glue using an AWS CloudFormation template
<a name="automate-encryption-enforcement-in-aws-glue-using-an-aws-cloudformation-template"></a>

*Diogo Guedes, Amazon Web Services*

## Summary
<a name="automate-encryption-enforcement-in-aws-glue-using-an-aws-cloudformation-template-summary"></a>

This pattern shows you how to set up and automate encryption enforcement in AWS Glue by using an AWS CloudFormation template. The template creates all the required configurations and resources for enforcing encryption. These resources include an initial configuration, a preventive control created by an Amazon EventBridge rule, and an AWS Lambda function.

## Prerequisites and limitations
<a name="automate-encryption-enforcement-in-aws-glue-using-an-aws-cloudformation-template-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Permissions to deploy the CloudFormation template and its resources

**Limitations **

This security control is regional. You must deploy the security control in each AWS Region where you want to set up encryption enforcement in AWS Glue.

## Architecture
<a name="automate-encryption-enforcement-in-aws-glue-using-an-aws-cloudformation-template-architecture"></a>

**Target technology stack  **
+ Amazon CloudWatch Logs (from AWS Lambda)
+ Amazon EventBridge rule
+ AWS CloudFormation stack
+ AWS CloudTrail
+ AWS Identity and Access Management (IAM) managed role and policy
+ AWS Key Management Service (AWS KMS)
+ AWS KMS alias
+ AWS Lambda function
+ AWS Systems Manager Parameter Store

**Target architecture**

The following diagram shows how to automate encryption enforcement in AWS Glue.

![Diagram shows how to automate encryption enforcement in AWS Glue using a CloudFormation template.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d50d0659-5592-44d0-8fcb-7a2983712640/images/272a7fb2-ecbc-41f7-a556-d555e4e39a59.png)

The diagram shows the following workflow:

1. A [CloudFormation template](https://github.com/aws-samples/aws-custom-guardrail-event-driven/blob/main/CloudFormation/aws-custom-guardrail-event-driven.yaml) creates all the resources, including the initial configuration and detective control for encryption enforcement in AWS Glue.

1. An EventBridge rule detects a state change in the encryption configuration.

1. A Lambda function is invoked for evaluation and logging through CloudWatch Logs. For non-compliant detection, the Parameter Store is recovered with an Amazon Resource Name (ARN) for an AWS KMS key. The service is remediated to compliant status with encryption enabled.

**Automation and scale**

If you’re using [AWS Organizations](https://aws.amazon.com/organizations/), you can use [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to deploy this template in multiple accounts where you want to enable encryption enforcement in AWS Glue.

## Tools
<a name="automate-encryption-enforcement-in-aws-glue-using-an-aws-cloudformation-template-tools"></a>
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you enable operational and risk auditing, governance, and compliance of your AWS account.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale.

**Code**

The code for this pattern is available in the GitHub [aws-custom-guardrail-event-driven](https://github.com/aws-samples/aws-custom-guardrail-event-driven/blob/main/CloudFormation/aws-custom-guardrail-event-driven.yaml) repository.

## Best practices
<a name="automate-encryption-enforcement-in-aws-glue-using-an-aws-cloudformation-template-best-practices"></a>

AWS Glue supports data encryption at rest for [authoring jobs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/author-job-glue.html) and [developing scripts using development endpoints](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint.html).

Consider the following best practices:
+ Configure ETL jobs and development endpoints to use AWS KMS keys to write encrypted data at rest.
+ Encrypt the metadata stored in the [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro) by using keys that you manage through AWS KMS.
+ Use AWS KMS keys to encrypt job bookmarks and the logs generated by [crawlers](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) and ETL jobs.

## Epics
<a name="automate-encryption-enforcement-in-aws-glue-using-an-aws-cloudformation-template-epics"></a>

### Launch the CloudFormation template
<a name="launch-the-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation template. | Download the `aws-custom-guardrail-event-driven.yaml` template from the GitHub [repository](https://github.com/aws-samples/aws-custom-guardrail-event-driven/blob/main/CloudFormation/aws-custom-guardrail-event-driven.yaml), and then [deploy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/deploy/index.html) the template. The `CREATE_COMPLETE` status indicates that your template was successfully deployed.The template requires no input parameters. | Cloud architect |

### Verify the encryption settings in AWS Glue
<a name="verify-the-encryption-settings-in-aws-glue"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check the AWS KMS key configurations. | 1. Sign in to the AWS Management Console and then open the [AWS Glue console](https://console.aws.amazon.com/glue/).<br />2. In the navigation pane, under **Data Catalog**, choose **Catalog settings**.<br />3. Verify that the **Metadata encryption** and **Encrypt connection passwords** settings are flagged and configured to use `KMSKeyGlue`. | Cloud architect |

### Test the encryption enforcement
<a name="test-the-encryption-enforcement"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify the encryption setting in CloudFormation. | 1. Sign in to the AWS Management Console and then open the [CloudFormation console](https://console.aws.amazon.com/cloudformation).<br />2. In the navigation pane, choose **Stacks**, and then choose your stack.<br />3. Choose the **Resources** tab.<br />4. In the **Resources** table, find the encryption setting by **Logical ID**. | Cloud architect |
| Switch the provisioned infrastructure to an uncompliant state. | 1. Sign in to the AWS Management Console and then open the [AWS Glue console](https://console.aws.amazon.com/glue/).<br />2. In the navigation pane, under **Data Catalog**, choose **Catalog settings**.<br />3. Clear the **Metadata encryption **check box.<br />4. Clear the **Encrypt connection passwords** check box.<br />5. Choose **Save**.<br />6. Refresh the AWS Glue console.The guardrail detects the uncompliant state in AWS Glue after you clear the check boxes, and then enforces compliance by automatically remediating the encryption misconfiguration. As a result, the encryption check boxes should again be selected after you refresh the page. | Cloud architect |

## Related resources
<a name="automate-encryption-enforcement-in-aws-glue-using-an-aws-cloudformation-template-resources"></a>
+ [Creating a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) (AWS CloudFormation documentation)
+ [Creating a CloudWatch Events rule that triggers on an AWS API call using AWS CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-CloudTrail-Rule.html) (Amazon CloudWatch documentation)
+ [Setting up encryption in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/set-up-encryption.html) (AWS Glue documentation)
