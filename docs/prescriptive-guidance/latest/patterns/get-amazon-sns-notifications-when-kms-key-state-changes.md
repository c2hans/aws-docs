---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/get-amazon-sns-notifications-when-kms-key-state-changes.html
---

# Get Amazon SNS notifications when the key state of an AWS KMS key changes
<a name="get-amazon-sns-notifications-when-kms-key-state-changes"></a>

*Shubham Harsora, Aromal Raj Jayarajan, Prasobh S P, and Vishnu Unnikrishnan, Amazon Web Services*

## Summary
<a name="get-amazon-sns-notifications-when-kms-key-state-changes-summary"></a>

When you delete an [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/) key, you lose the data and metadata associated with that key. The deletion is irreversible, and you can’t recover the lost data (including encrypted data). To prevent data loss, set up a notification system that alerts you to changes in the [key states](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html#key-state-cmk-type) of your AWS KMS keys.

This pattern shows you how to monitor status changes to AWS KMS keys by using [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) and [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/) to issue automated notifications whenever the key state of an AWS KMS key changes to `Disabled` or `PendingDeletion`, and when a scheduled deletion completes. For example, if a user disables or schedules the deletion of an AWS KMS key, you receive an email notification with details about the change, such as the account, Region, caller, and key ID. If you receive a notification, you can re-enable the key or cancel the deletion before data is lost.

## Prerequisites and limitations
<a name="get-amazon-sns-notifications-when-kms-key-state-changes-prereqs"></a>

**Prerequisites**
+ An active AWS account with an AWS Identity and Access Management (IAM) role or user that can create AWS CloudFormation stacks, AWS KMS keys, Amazon SNS topics, and Amazon EventBridge rules
+ An [AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html) to use for testing
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/index.html) turned on for management events (create a trail so that failed calls and a long history are available)

**Limitations**
+ The EventBridge rules are Regional. Deploy the stack in each AWS Region where you have AWS KMS keys.
+ The notifications for disabling a key and scheduling its deletion rely on CloudTrail management events. They usually arrive within a few minutes.
+ Failed requests (for example, a request that AWS KMS denies) also send a notification. The last line of the message shows the error code. The line is empty if the request succeeded.
+ The stack creates one AWS KMS key to encrypt the Amazon SNS topic. If you disable or delete that key, the notifications stop.

## Architecture
<a name="get-amazon-sns-notifications-when-kms-key-state-changes-architecture"></a>

**Technology stack**
+ AWS CloudFormation
+ AWS CloudTrail
+ Amazon EventBridge
+ AWS Key Management Service (AWS KMS)
+ Amazon Simple Notification Service (Amazon SNS)

**Target architecture**

The following diagram shows an architecture for building an automated monitoring and notification process for detecting any changes to the state of an AWS KMS key.

![Architecture for building an automated monitoring and notification process](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2534df87-a6fd-4360-9b5d-4a8b1f533de3/images/0cb6a6b0-405b-4d26-ad04-2067176aa086.png)

The diagram shows the following workflow:

1. A user disables an AWS KMS key or schedules its deletion. When the waiting period ends, AWS KMS deletes the key and sends a separate deletion event.

1. An EventBridge rule matches the event.

1. The EventBridge rule publishes a message to an Amazon SNS topic. The topic is encrypted with an AWS KMS customer managed key that the AWS CloudFormation stack creates.

1. Amazon SNS sends an email notification to the subscribed users.

**Note**
You can customize the email message to meet your organization’s needs by changing the input transformer of each EventBridge rule. We recommend including information about the resources that use the AWS KMS key. This information helps users understand the impact of deleting the key.

**Automation and scale**

The AWS CloudFormation stack deploys all the necessary resources and services for this pattern to work. You can implement the pattern independently in a single account and Region, or deploy it to multiple accounts and Regions by using [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).

## Tools
<a name="get-amazon-sns-notifications-when-kms-key-state-changes-tools"></a>
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions. The CloudFormation template for this pattern describes all the AWS resources that you want, and CloudFormation provisions and configures those resources for you.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. EventBridge delivers a stream of real-time data from your own applications and AWS services, and it routes that data to targets such as [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/). EventBridge simplifies the process of building event-driven architectures.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you enable operational and risk auditing, governance, and compliance of your AWS account. CloudTrail records actions taken by a user, role, or AWS service as events. The AWS KMS API calls that this pattern monitors are CloudTrail events.

**Code**

The code for this pattern is available in the GitHub [Monitor AWS KMS keys disable and scheduled deletion](https://github.com/aws-samples/aws-kms-deletion-notification) repository.

## Epics
<a name="get-amazon-sns-notifications-when-kms-key-state-changes-epics"></a>

### Deploy the CloudFormation template
<a name="deploy-the-cloudformation-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Clone the GitHub [Monitor AWS KMS keys disable and scheduled deletion](https://github.com/aws-samples/aws-kms-deletion-notification) repository to your local machine by running the following command:<pre>git clone https://github.com/aws-samples/aws-kms-deletion-notification</pre> | AWS administrator, Cloud architect |
| Deploy the AWS CloudFormation template. | 1. Sign in to the AWS Management Console and open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/) in the AWS Region where you want the notifications.<br />2. Choose **Create stack**, and then choose **With new resources (standard)**.<br />3. For **Prerequisite - Prepare template**, choose **Choose an existing template**.<br />4. For **Specify template**, choose **Upload a template file**.<br />5. Choose **Choose file**, select the `Alerting-KMS-Events.yaml` file from your cloned GitHub repository, and then choose **Next**.<br />6. For **Stack name**, enter a name for your stack.<br />7. For **DestinationEmailAddress**, enter an active email address that you plan to use for receiving the Amazon SNS notification.<br />8. For **SNSTopicName**, enter a name for your Amazon SNS topic.<br />9. Choose **Next**, and then choose **Next** again on the **Configure stack options** page.<br />10. On the **Review and create** page, choose **Submit**.The stack shows `CREATE_COMPLETE` status when the resources are created. | AWS administrator, Cloud architect |

### Confirm the subscription
<a name="confirm-the-subscription"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Confirm the subscription email. | After the CloudFormation template successfully deploys, Amazon SNS sends a subscription confirmation message to the email address that you entered.<br />To receive notifications, you must confirm this email subscription. For more information, see [Confirm the subscription](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html) in the Amazon SNS Developer Guide. | AWS administrator, Cloud architect |

### Test the subscription notification
<a name="test-the-subscription-notification"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Disable an AWS KMS key. | 1. Sign in to the AWS Management Console and open the [AWS KMS console](https://console.aws.amazon.com/kms).<br />2. Make sure that you are in the AWS Region where you deployed the stack.<br />3. In the navigation pane, choose **Customer managed keys**.<br />4. Select the check box for a test AWS KMS key. Don’t use a key that your applications use.<br />5. Choose **Key actions**, and then choose **Disable**.<br />6. When you finish testing, choose **Key actions**, and then choose **Enable**. | AWS administrator |
| Schedule the deletion of an AWS KMS key (optional). | 1. Select the test AWS KMS key.<br />2. Choose **Key actions**, and then choose **Schedule key deletion**.<br />3. Enter a waiting period of 7 days, select the confirmation check box, and then choose **Schedule deletion**.<br />4. After you receive the notification, choose **Key actions**, and then choose **Cancel key deletion**. | AWS administrator |
| Validate the subscription. | Confirm that you received the Amazon SNS notification email. The email arrives within a few minutes. It shows the account ID, Region, the caller, and the key ID. | AWS administrator |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the CloudFormation stack. | 1. Sign in to the AWS Management Console and open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. In the navigation pane, choose **Stacks**.<br />3. Select the stack that you created previously, and then choose **Delete**.The AWS KMS key that encrypts the topic goes into a pending deletion period (30 days by default) and is then removed. | AWS administrator |
| Delete the test key. | If you created an AWS KMS key only for testing, schedule it for deletion in the AWS KMS console. | AWS administrator |

## Related resources
<a name="get-amazon-sns-notifications-when-kms-key-state-changes-resources"></a>
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/) (AWS documentation)
+ [Creating a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) (AWS CloudFormation documentation)
+ [Building event-driven architectures on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/63320e83-6abc-493d-83d8-f822584fb3cb/en-US) (AWS Workshop Studio documentation)
+ [AWS Key Management Service Best Practices](https://d1.awsstatic.com/whitepapers/aws-kms-best-practices.pdf) (AWS Whitepaper)
+ [Security best practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html) (AWS KMS Developer Guide)
+ [Monitor KMS keys with Amazon EventBridge](https://docs.aws.amazon.com/kms/latest/developerguide/kms-events.html) (AWS KMS documentation)
+ [Enable compatibility between event sources from AWS services and encrypted topics](https://docs.aws.amazon.com/sns/latest/dg/sns-key-management.html) (Amazon SNS documentation)
+ [Detection and monitoring best practices for AWS KMS](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/monitoring.html) (AWS Prescriptive Guidance)
+ [Monitor and remediate scheduled deletion of AWS KMS keys](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-and-remediate-scheduled-deletion-of-aws-kms-keys.html) (AWS Prescriptive Guidance)

## Additional information
<a name="get-amazon-sns-notifications-when-kms-key-state-changes-additional"></a>

The Amazon SNS topic in this pattern is encrypted with a customer managed AWS KMS key that the AWS CloudFormation template creates. EventBridge can’t publish to a topic that uses the AWS managed key `alias/aws/sns`, because you can’t change that key’s policy. The customer managed key costs about USD 1 per month plus request charges. For more information, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/). The Amazon SNS topic policy allows only the three EventBridge rules in the stack to publish, and denies requests that don’t use TLS.

Do not disable or delete the key that encrypts the topic. The rules in this stack also send a notification if that happens.
