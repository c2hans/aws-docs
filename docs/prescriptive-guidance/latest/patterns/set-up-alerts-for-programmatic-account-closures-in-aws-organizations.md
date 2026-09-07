---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-alerts-for-programmatic-account-closures-in-aws-organizations.html
---

# Set up alerts for programmatic account closures in AWS Organizations
<a name="set-up-alerts-for-programmatic-account-closures-in-aws-organizations"></a>

*Richard Milner-Watts, Debojit Bhadra, and Manav Yadav, Amazon Web Services*

## Summary
<a name="set-up-alerts-for-programmatic-account-closures-in-aws-organizations-summary"></a>

The [CloseAccount API](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CloseAccount.html) for [AWS Organizations](https://aws.amazon.com/organizations/) enables you to close member accounts within an organization programmatically, without having to log in to the account with root credentials. The [RemoveAccountFromOrganization API](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RemoveAccountFromOrganization.html) pulls an account out from an organization in AWS Organizations, so it becomes a standalone account.

These APIs potentially increase the number of operators who can close or remove an AWS account. All users who have access to the organization through AWS Identity and Access Management (IAM) in the AWS Organizations management account can call these APIs, so access isn’t limited to the owner of the account's root email with any associated multi-factor authentication (MFA) device.

This pattern implements alerts when the `CloseAccount` and `RemoveAccountFromOrganization` APIs are called, so you can monitor these activities. For alerts, it uses an [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) topic. You can also set up Slack notifications through a [webhook](https://api.slack.com/messaging/webhooks).

## Prerequisites and limitations
<a name="set-up-alerts-for-programmatic-account-closures-in-aws-organizations-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An organization in AWS Organizations
+ Access to the organization management account, under the organization's root, to create the required resources

**Limitations **
+ As described in the [AWS Organizations API reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CloseAccount.html), the `CloseAccount` API allows only 10 percent of active member accounts to be closed within a rolling 30-day period.
+ When an AWS account is closed, its status is changed to SUSPENDED. For 90 days after this status transition, AWS Support can reopen the account. After 90 days the account is permanently deleted.
+ Users who have access to the AWS Organizations management account and APIs might also have permissions to disable these alerts. If the primary concern is malicious behavior instead of accidental deletion, consider protecting the resources created by this pattern with an [IAM permissions boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html).
+ The API calls for `CloseAccount `and `RemoveAccountFromOrganization` are processed in the US East (N. Virginia) Region (`us-east-1`). Therefore, you must deploy this solution in `us-east-1` in order to observe the events.

## Architecture
<a name="set-up-alerts-for-programmatic-account-closures-in-aws-organizations-architecture"></a>

**Target technology stack  **
+ AWS Organizations
+ AWS CloudTrail
+ Amazon EventBridge
+ AWS Lambda
+ Amazon SNS

**Target architecture **

The following diagram shows the solution architecture for this pattern.

![Architecture for setting up alerts in AWS Organizations for account closures](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/ba9d9db1-fab8-4e3b-a1bb-f0be91ade5c6/images/92caee55-2722-4ba2-bdd2-66f1af35dce5.png)

1. AWS Organizations processes a `CloseAccount` or `RemoveAccountFromOrganization` request.

1. Amazon EventBridge is integrated with AWS CloudTrail to deliver these events to the default event bus.

1. A custom Amazon EventBridge rule matches the AWS Organizations requests and calls an AWS Lambda function.

1. The Lambda function delivers a message to an SNS topic, which users can subscribe to for email alerts or further processing.

1. If Slack notifications are enabled, the Lambda function delivers a message to a Slack webhook.

## Tools
<a name="set-up-alerts-for-programmatic-account-closures-in-aws-organizations-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) provides a way to model a collection of related AWS and third-party resources, provision them quickly and consistently, and manage them throughout their lifecycles, by treating infrastructure as code.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that you can use to connect your applications with data from a variety of sources. EventBridge receives an event, an indicator of a change in environment, and applies a rule to route the event to a target. Rules match events to targets based on either the structure of the event, called an *event pattern*, or on a schedule.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests each day to thousands each second. You pay only for the compute time that you consume. There is no charge when your code is not running.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) helps you centrally manage and govern your environment as you grow and scale your AWS resources. Using AWS Organizations, you can programmatically create new AWS accounts and allocate resources, group accounts to organize your workflows, apply policies to accounts or groups for governance, and simplify billing by using a single payment method for all your accounts.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) monitors and records account activity across your AWS infrastructure, and gives you control over storage, analysis, and remediation actions.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication.

**Other tools**
+ [AWS Lambda Powertools for Python library](https://docs.powertools.aws.dev/lambda/python/latest/) is a set of utilities that provide tracing, logging, metrics, and event handling features for Lambda functions.

**Code **

The code for this pattern is located in the GitHub [AWS Account Closer Notifier](https://github.com/aws-samples/aws-account-closure-notifier) repository.

The solution includes a CloudFormation template that deploys the architecture for this pattern. It uses the [AWS Lambda Powertools for Python library](https://docs.powertools.aws.dev/lambda/python/latest/) to provide logging and tracing.

## Epics
<a name="set-up-alerts-for-programmatic-account-closures-in-aws-organizations-epics"></a>

### Deploy the architecture
<a name="deploy-the-architecture"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the CloudFormation template for the solution stack. | The CloudFormation template for this pattern is in the main branch of the [GitHub repository](https://github.com/aws-samples/aws-account-closure-notifier). It deploys the IAM roles, EventBridge rules, Lambda functions, and the SNS topic.<br />To launch the template:1. Clone the [GitHub repository](https://github.com/aws-samples/aws-account-closure-notifier) to obtain a copy of the solution code.<br />2. Open the AWS Management Console for the AWS Organizations management account.<br />3. Choose the US East (N. Virginia) Region (`us-east-1`), and then open the [CloudFormation console](https://console.aws.amazon.com/cloudformation).<br />4. Create the stack by using the `account-closure-notifier.yml` template and specifying the following values:  Stack name: `aws-account-closure-notifier-stack` `ResourcePrefix` parameter: `aws-account-closure-notifier``SlackNotification` parameter: If Slack notifications are required, change this setting to `true`.`SlackWebhookEndpoint` parameter: If Slack notifications are required, specify the webhook URL.<br />For more information about launching a CloudFormation stack, see the [AWS documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html). | AWS administrator |
| Verify that the solution has launched successfully. | 1. Wait for the CloudFormation stack to reach a status of CREATE\_COMPLETE.<br />2. Open the [EventBridge console](https://console.aws.amazon.com/events/) in `us-east-1`.<br />3. Verify that a new rule has been created with the name `aws-account-closure-notifier-event-rule`. | AWS administrator |
| Subscribe to the SNS topic. | (Optional) If you want to subscribe to the SNS topic:1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/v3/home) in `us-east-1`, and find the topic named `aws-account-closure-notifier-sns-topic`.<br />2. Choose the topic name, and then choose **Create subscription**.<br />3. For **Protocol**, choose **Email.**<br />4. For **Endpoint**, specify the email address that should receive the notification, and then choose **Create subscription**.<br />5. Check your email inbox for a message from AWS Notifications. Use the link in this email to confirm the subscription.<br />For more information about setting up SNS notifications, see the [Amazon SNS documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SetupSNS.html). | AWS administrator |

### Verify the solution
<a name="verify-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Send a test event to the default event bus. | The [GitHub repository](https://github.com/aws-samples/aws-account-closure-notifier) provides a sample event that you can send to the EventBridge default event bus for testing. The EventBridge rule also reacts to events that use the custom event source `account.closure.notifier`.You can’t use the CloudTrail event source to send this event, because it’s not possible to send an event as an AWS service.<br />To send a test event:1. Open the [EventBridge console](https://console.aws.amazon.com/events/) in `us-east-1`.<br />2. In the navigation pane, under **Buses**, choose **Event buses**, and then select the default event bus.<br />3. Choose **Send events**.<br />4. For **Event source**, enter `account.closure.notifier`.<br />5. For **Detail type**, enter `AWS API Call via CloudTrail`.<br />6. For **Event detail**, copy and paste the contents of `tests/dummy-event.json` from the GitHub repository into the text box.<br />7. Choose **Send **to initiate the notification workflow. | AWS administrator |
| Verify that the email notification was received. | Check the mailbox that subscribed to the SNS topic for notifications. You should receive an email with details of the account that was closed and the principal that performed the API call. | AWS administrator |
| Verify that the Slack notification was received. | (Optional) If you specified a webhook URL for the `SlackWebhookEndpoint` parameter when you deployed the CloudFormation template, check the Slack channel that is mapped to the webhook. It should display a message with details of the account that was closed and the principal that performed the API call. | AWS administrator |

## Related resources
<a name="set-up-alerts-for-programmatic-account-closures-in-aws-organizations-resources"></a>
+ [CloseAccount action](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CloseAccount.html) (AWS Organizations API reference)
+ [RemoveAccountFromOrganization action](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RemoveAccountFromOrganization.html) (AWS Organizations API reference)
+ [AWS Lambda Powertools for Python](https://docs.powertools.aws.dev/lambda/python/latest/)
