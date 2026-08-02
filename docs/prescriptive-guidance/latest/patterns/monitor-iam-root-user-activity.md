---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-iam-root-user-activity.html
---

# Monitor IAM root user activity
<a name="monitor-iam-root-user-activity"></a>

*JJ Sung and Mostefa Brougui, Amazon Web Services*

## Summary
<a name="monitor-iam-root-user-activity-summary"></a>

Every Amazon Web Services (AWS) account has a root user. As a [security best practice](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) for AWS Identity and Access Management (IAM), we recommend that you use the root user to complete the tasks that only the root user can perform. For the complete list, see [Tasks that require root user credentials](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html) in the *AWS Account Management Reference Guide*. Because the root user has full access to all of your AWS resources and billing information, we recommend that you don’t use this account and monitor it for any activity, which might indicate that the root user credentials have been compromised.

Using this pattern, you set up an [event-driven architecture](https://aws.amazon.com/event-driven-architecture/) that monitors the IAM root user. This pattern sets up a hub-and-spoke solution that monitors multiple AWS accounts, the *spoke *accounts, and centralizes management and reporting in a single account, the *hub* account.

When the IAM root user credentials are used, Amazon CloudWatch and AWS CloudTrail record the activity in the log and trail, respectively. In the spoke account, an Amazon EventBridge rule sends the event to the central [event bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html) in the hub account. In the hub account, an EventBridge rule sends the event to an AWS Lambda function. The function uses an Amazon Simple Notification Service (Amazon SNS) topic that notifies you of the root user activity.

In this pattern, you use an AWS CloudFormation template to deploy the monitoring and event-handling services in the spoke accounts. You use a HashiCorp Terraform template to deploy the event-management and notification services in the hub account.

## Prerequisites and limitations
<a name="monitor-iam-root-user-activity-prereqs"></a>

**Prerequisites**

1. Permissions to deploy AWS resources in your AWS environment.

1. Permissions to deploy CloudFormation stack sets. For more information, see [Prerequisites for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html) (CloudFormation documentation).

1. Terraform installed and ready to use. For more information, see [Get Started – AWS](https://learn.hashicorp.com/collections/terraform/aws-get-started) (Terraform documentation).

1. An existing trail in each spoke account. For more information, see [Getting started with AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-tutorial.html) (CloudTrail documentation).

1. The trail is configured to send events to CloudWatch Logs. For more information, see [Sending events to CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html) (CloudTrail documentation).

1. Your hub and spoke accounts must be managed by AWS Organizations.

## Architecture
<a name="monitor-iam-root-user-activity-architecture"></a>

The following diagram illustrates the building blocks of the implementation.

![An event in a spoke account creating an email notification in a hub account](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/175f356b-f9df-4d33-82fc-fe33b2c88b05/images/6147e5b5-616e-49a4-b330-dbb7e3381fe7.png)

1. When the IAM root user credentials are used, CloudWatch and CloudTrail record the activity in the log and trail, respectively.

1. In the spoke account, an EventBridge rule sends the event to the central [event bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html) in the hub account.

1. In the hub account, an EventBridge rule sends the event to a Lambda function.

1. The Lambda function uses an Amazon SNS topic that notifies you of the root user activity.

## Tools
<a name="monitor-iam-root-user-activity-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational risk of your AWS account.
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.

**Other tools and services**
+ [Terraform](https://www.terraform.io/docs) is a CLI application for provisioning and managing cloud infrastructure and resources by using code, in the form of configuration files.

**Code repository**

The source code and templates for this pattern are available in a [GitHub repository](https://github.com/aws-samples/aws-iam-root-user-activity-monitor). This pattern provides two templates:
+ A Terraform template containing the resources you deploy in the hub account
+ A CloudFormation template you deploy as a stack set instance in the spoke accounts

The repository has the following overall structure.

```
.
 |__README.md
 |__spoke-stackset.yaml
 |__hub.tf
 |__root-activity-monitor-module
     |__main.tf  # contains Terraform code to deploy resources in the Hub account
     |__iam      # contains IAM policies JSON files
         |__ lambda-assume-policy.json          # contains trust policy of the IAM role used by the Lambda function
         |__ lambda-policy.json                 # contains the IAM policy attached to the IAM role used by the Lambda function
     |__outputs  # contains Lambda function zip code
```

The *Epics* section provides step-by-step instructions for deploying the templates.

## Epics
<a name="monitor-iam-root-user-activity-epics"></a>

### Deploy resources to the hub account
<a name="deploy-resources-to-the-hub-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the sample code repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-iam-root-user-activity.html) | General AWS |
| Update the Terraform template. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-iam-root-user-activity.html) | General AWS |
| Deploy the resources to the AWS hub account. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-iam-root-user-activity.html) | General AWS |

### Deploy resources to your spoke accounts
<a name="deploy-resources-to-your-spoke-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation template. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-iam-root-user-activity.html)For more information and instructions, see [Create a stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html) (CloudFormation documentation). | General AWS |

### (Optional) Test the notifications
<a name="optional-test-the-notifications"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use the root user credentials. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-iam-root-user-activity.html) | General AWS |

## Related resources
<a name="monitor-iam-root-user-activity-resources"></a>
+ [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) (IAM documentation)
+ [Working with StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) (CloudFormation documentation)
+ [Get Started](https://learn.hashicorp.com/collections/terraform/aws-get-started) (Terraform documentation)

## Additional information
<a name="monitor-iam-root-user-activity-additional"></a>

[Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a continuous security monitoring service that analyzes and processes logs to identify unexpected and potentially unauthorized activity in your AWS environment. As an alternative to this solution, if you have enabled GuardDuty, it can alert you when the root user credentials have been used. The GuardDuty finding is `Policy:IAMUser/RootCredentialUsage`, and the default severity is **Low**. For more information, see [Managing Amazon GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/findings_management.html).
