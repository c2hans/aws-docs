---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/identify-and-alert-when-amazon-data-firehose-resources-are-not-encrypted-with-an-aws-kms-key.html
---

# Identify and alert when Amazon Data Firehose resources are not encrypted with an AWS KMS key
<a name="identify-and-alert-when-amazon-data-firehose-resources-are-not-encrypted-with-an-aws-kms-key"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="identify-and-alert-when-amazon-data-firehose-resources-are-not-encrypted-with-an-aws-kms-key-summary"></a>

For compliance, some organizations must have encryption enabled on data delivery resources such as Amazon Data Firehose. This pattern shows a way to monitor, detect, and notify when resources are out of compliance.

To maintain the encryption requirement, this pattern can be used on AWS to provide automated monitoring and detection of Amazon Data Firehose delivery resources that aren’t encrypted with an AWS Key Management Service (AWS KMS) key. The solution sends alert notifications, and it can be extended to perform automatic remediation. This solution can be applied to an individual account or a multiple-account environment, such as an environment that uses an AWS landing zone or AWS Control Tower.

## Prerequisites and limitations
<a name="identify-and-alert-when-amazon-data-firehose-resources-are-not-encrypted-with-an-aws-kms-key-prereqs"></a>

**Prerequisites **
+ Amazon Data Firehose delivery stream
+ Sufficient permissions and familiarity with CloudFormation, which is used in this infrastructure automation

**Limitations **
+ The solution is not real time because it uses AWS CloudTrail events for detection, and there is a delay between the time an unencrypted resource is created and the notification is sent.

## Architecture
<a name="identify-and-alert-when-amazon-data-firehose-resources-are-not-encrypted-with-an-aws-kms-key-architecture"></a>

**Target technology stack  **

The solution uses serverless technology and the following services:
+ AWS CloudTrail
+ Amazon CloudWatch
+ AWS Command Line Interface (AWS CLI)
+ AWS Identity and Access Management (IAM)
+ Amazon Data Firehose
+ AWS Lambda
+ Amazon Simple Notification Service (Amazon SNS)

**Target architecture **

![Process for generating alerts when Data Firehose resources aren't encrypted.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/897ba8cf-d1c2-4149-98e7-09d3d90d13d6/images/d694f718-bd0c-4d14-a2e4-e0ea58dc048e.png)

The diagram illustrates these steps:

1. A user creates or modifies Amazon Data Firehose.

1. A CloudTrail event is detected and matched.

1. Lambda is invoked.

1. Non-compliant resources are identified.

1. Email notification is sent.

**Automation and scale**

You can use CloudFormation StackSets to apply this solution to multiple AWS Regions or accounts with a single command.

## Tools
<a name="identify-and-alert-when-amazon-data-firehose-resources-are-not-encrypted-with-an-aws-kms-key-tools"></a>
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS CLI, AWS SDKs, and API operations.
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) delivers a near real-time stream of system events that describe changes in AWS resources.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that enables you to interact with AWS services by using commands in your command line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) is a fully managed service for delivering real-time streaming data. With Firehose, you don't have to write applications or manage resources. You configure your data producers to send data to Firehose, and it automatically delivers the data to the destination that you specified.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time that you consume—there is no charge when your code isn’t running.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) is a managed service that provides message delivery from publishers to subscribers (also known as producers and consumers).

## Epics
<a name="identify-and-alert-when-amazon-data-firehose-resources-are-not-encrypted-with-an-aws-kms-key-epics"></a>

### Enforce encryption for compliance
<a name="enforce-encryption-for-compliance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy CloudFormation StackSets. | In the AWS CLI, use the `firehose-encryption-checker.yaml` template (attached) to create the stack set by running the following command.  Provide a valid Amazon SNS topic Amazon Resource Name (ARN) for the parameter. The deployment should successfully create CloudWatch Events rules, the Lambda function, and an IAM role with the necessary permissions, as described in the template.<pre>aws cloudformation create-stack-set    --stack-set-name my-stack-set   --template-body file://firehose-encryption-checker.yaml </pre> | Cloud architect, Systems administrator |
| Create stack instances. | Stacks can be created in the AWS Regions of your choice as well as in one or more accounts.  To create stack instances, run the following command. Replace the stack name, account numbers, and Regions with your own.<pre>aws cloudformation create-stack-instances     --stack-set-name my-stack-set    --accounts 123456789012 223456789012   --regions us-east-1 us-east-2 us-west-1 us-west-2     --operation-preferences FailureToleranceCount=1 </pre> | Cloud architect, Systems administrator |

## Related resources
<a name="identify-and-alert-when-amazon-data-firehose-resources-are-not-encrypted-with-an-aws-kms-key-resources"></a>
+ [Working with CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)
+ [What is Amazon CloudWatch Events?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)

## Attachments
<a name="attachments-897ba8cf-d1c2-4149-98e7-09d3d90d13d6"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/897ba8cf-d1c2-4149-98e7-09d3d90d13d6/attachments/attachment.zip)
