---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes.html
---

# Get Amazon SNS notifications when the key state of an AWS KMS key changes
<a name="get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes"></a>

*Shubham Harsora, Aromal Raj Jayarajan, and Navdeep Pareek, Amazon Web Services*

## Summary
<a name="get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes-summary"></a>

The data and metadata associated with an AWS Key Management Service (AWS KMS) key is lost when that key is deleted. The deletion is irreversible and you can't recover lost data (including encrypted data). You can prevent data loss by setting up a notification system to alert you of status changes to [key states](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html#key-state-cmk-type) of your AWS KMS keys.

This pattern shows you how to monitor status changes to AWS KMS keys by using Amazon EventBridge and Amazon Simple Notification Service (Amazon SNS) to issue automated notifications whenever the key state of an AWS KMS key changes to `Disabled` or `PendingDeletion`. For example, if a user tries to disable or delete an AWS KMS key, you will receive an email notification with details about the attempted status change. You can also use this pattern to schedule the deletion of AWS KMS keys.

## Prerequisites and limitations
<a name="get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes-prereqs"></a>

**Prerequisites**
+ An active AWS account with an AWS Identity and Access Management (IAM) user
+ An [AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html)

## Architecture
<a name="get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes-architecture"></a>

**Technology stack**
+ Amazon EventBridge
+ AWS Key Management Service (AWS KMS)
+ Amazon Simple Notification Service (Amazon SNS)

**Target architecture**

The following diagram shows an architecture for building an automated monitoring and notification process for detecting any changes to the state of an AWS KMS key.

![Architecture for building an automated monitoring and notification process](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2534df87-a6fd-4360-9b5d-4a8b1f533de3/images/0cb6a6b0-405b-4d26-ad04-2067176aa086.png)

The diagram shows the following workflow:

1. A user disables or schedules the deletion of an AWS KMS key.

1. An EventBridge rule evaluates the scheduled `Disabled` or `PendingDeletion` event.

1. The EventBridge rule invokes the Amazon SNS topic.

1. Amazon SNS sends an email notification message to the users.

**Note**
You can customize the email message to meet your organization's needs. We recommend including information about the entities where the AWS KMS key is used. This can help users understand the impact of deleting the AWS KMS key. You can also schedule a reminder email notification that's sent one or two days before the AWS KMS key is deleted.

**Automation and scale**

The AWS CloudFormation stack deploys all the necessary resources and services for this pattern to work. You can implement the pattern independently in a single account, or by using [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) for multiple independent accounts or [organizational units](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) in AWS Organizations.

## Tools
<a name="get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes-tools"></a>
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions. The CloudFormation template for this pattern describes all the AWS resources that you want, and CloudFormation provisions and configures those resources for you.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. EventBridge delivers a stream of real-time data from your own applications and AWS services, and it routes that data to targets such as AWS Lambda. EventBridge simplifies the process of building event-driven architectures.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.

**Code**

The code for this pattern is available in the GitHub [Monitor AWS KMS keys disable and scheduled deletion](https://github.com/aws-samples/aws-kms-deletion-notification) repository.

## Epics
<a name="get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes-epics"></a>

### Deploy the CloudFormation template
<a name="deploy-the-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Clone the GitHub [Monitor AWS KMS keys disable and scheduled deletion](https://github.com/aws-samples/aws-kms-deletion-notification) repository to your local machine by running the following command:<br />`git clone https://github.com/aws-samples/aws-kms-deletion-notification` | AWS administrator, Cloud architect |
| Update the template's parameters. | In a code editor, open the `Alerting-KMS-Events.yaml` CloudFormation template that you cloned from the repository, and then update the following parameters:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes.html) | AWS administrator, Cloud architect |
| Deploy the CloudFormation template. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes.html) | AWS administrator, Cloud architect |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the subscription email. | After the CloudFormation template successfully deploys, Amazon SNS sends a subscription confirmation message to the email address that you provided in the CloudFormation template.<br />To receive notifications, you must confirm this email subscription. For more information, see [Confirm the subscription](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.confirm.html) in the Amazon SNS Developer Guide. | AWS administrator, Cloud architect |

### Test the subscription notification
<a name="test-the-subscription-notification"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Disable AWS KMS keys. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes.html) | AWS administrator |
| Validate the subscription. | Confirm that you received the Amazon SNS notification email. | AWS administrator |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the CloudFormation stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes.html) | AWS administrator |

## Related resources
<a name="get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes-resources"></a>
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/) (AWS documentation)
+ [Creating a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) (AWS CloudFormation documentation)
+ [Building event-driven architectures on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/63320e83-6abc-493d-83d8-f822584fb3cb/en-US) (AWS Workshop Studio documentation)
+ [AWS Key Management Service Best Practices](https://d1.awsstatic.com/whitepapers/aws-kms-best-practices.pdf) (AWS Whitepaper)
+ [Security best practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html) (AWS KMS Developer Guide)

## Additional information
<a name="get-amazon-sns-notifications-when-the-key-state-of-an-aws-kms-key-changes-additional"></a>

Amazon SNS provides in-transit encryption by default. To align with security best practices, you can also enable server-side encryption for Amazon SNS by using an AWS KMS customer managed key.
