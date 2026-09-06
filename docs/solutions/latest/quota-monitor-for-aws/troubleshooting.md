---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

The Quota Monitor for AWS logs errors, warnings, informational messages, and debugging messages for the solution’s Lambda functions. To choose the type of messages to log, find the applicable function in the Lambda console, and change the **LOG\_LEVEL** environment variable to the applicable type of message.

| Level | Description |
| --- | --- |
|  **ERROR**  | Logs will include information on anything that causes an operation to fail. |
|  **WARNING**  | Logs will include information on anything that can potentially cause inconsistencies in the function but might not cause the operation to fail. Logs will also include ERROR messages. |
|  **NFO**  | Logs will include high-level information about how the function is operating. Logs will also include `ERROR` and `WARNING` messages. |
|  **DEBUG**  | Logs will include information that might be helpful when debugging a problem with the function. Logs will also include `ERROR`, `WARNING`, and `INFO` messages. |

If these instructions don’t address your issue, see the [Contact AWS Support](contact-aws-support.md) section for instructions on opening an AWS Support case for this solution.

## Problem: Solution is not monitoring expected accounts or Regions
<a name="problem-solution-is-not-monitoring-expected-accounts-or-regions"></a>

If you’ve deployed the solution but it’s not monitoring the accounts or Regions, and the stacks are not deployed in spoke accounts, follow these steps to troubleshoot:

1. SSM parameter updates: Verify that you’ve updated the following SSM parameters after deployment:
   +  `/QuotaMonitor/OUs` (for Organizations or Hybrid deployment)
   +  `/QuotaMonitor/Accounts` (for Account or Hybrid deployment)
   +  `/QuotaMonitor/RegionsToDeploy`

1. Parameter values: Ensure the values in these parameters are correct and formatted properly (comma-separated lists).

1. Deployment model: Confirm that you’ve selected the correct deployment model (Organizations, Account, or Hybrid) when creating the stack.

1. StackSet deployments: If you’re using Organizations or Hybrid mode, check the CloudFormation StackSets console to confirm that the stacks have been created in the expected accounts and Regions.

### Resolution
<a name="resolution"></a>

If any of the above are incorrect, update the SSM parameters with the correct values. The solution should detect these changes and adjust its deployment accordingly. If issues persist, update the main stack to trigger a redeployment.

## Problem: The SNS spoke stack is not deploying in the new Region after updating the hub stack
<a name="problem-sns-spoke-stack-not-deploying-in-new-region-after-updating-hub-stack"></a>

After updating the hub stack, if the SNS spoke stack is not deploying in the new Region, follow these steps to troubleshoot:

### Resolution
<a name="resolution-sns-spoke"></a>

Ensure that you provide only one Region and update (or resave) the OUs or account’s parameter in Systems Manager Parameter Store after changing the SNS Spoke Region in the hub stack.

## Problem: Amazon CloudWatch Events bus permissions error
<a name="problem-amazon-cloudwatch-events-bus-permissions-error"></a>

If during spoke stack deployment, you received a **CREATE\_FAILED** message for the `TAWarnRule` and/or the `TASErrorRule`, verify that the CloudWatch Event Bus in the primary account allows the spoke account to send events to the monitoring account.

### Resolution
<a name="resolution-cloudwatch-events"></a>

Update the hub stack with the secondary account ID or complete the following tasks:

1. In the monitoring account, navigate to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, select **Event Buses**.

1. Select **Add Permissions**.

1. For **Principal**, enter the applicable secondary account ID.

1. Select the **Everybody()** box.

1. Choose **Add**.

## Problem: Slack notifications are not being received
<a name="problem-slack-notifications-are-not-being-received"></a>

If you don’t receive Slack notifications for WARN or ERROR events, check the CloudWatch logs for an error message.

1. In the primary account, navigate to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, select **Logs**.

1. Select the `/aws/lambda/[replaceable]`<stackname>`-SlackNotifier-`[replaceable]`<randomstring>` Log Group.

1. Select the top (most recent) Log Stream.

1. Look for the following error.

    **Example error for Quota Monitor for AWS**
![quota monitor error](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/quota-monitor-error.png)

### Resolution
<a name="resolution-1"></a>

Complete the following tasks:

1. In the primary account, navigate to the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager).

1. In the navigation pane under **Shared Resources**, select **Parameter Store**.

1. Select the `/QuotaMonitor/SlackHook` parameter and verify that the parameter shows the correct value.

## Problem: Email notifications are not being received
<a name="problem-email-notifications-are-not-being-received"></a>

If you don’t receive email notifications, confirm that you subscribed to the Amazon SNS topic.

1. In the primary account, navigate to the [Amazon SNS console](https://console.aws.amazon.com/sns/).

1. In the navigation pane, select **Topics**.

1. Select the ` {{<stackname>}}-SNSTopic-{{<randomstring>}} ` ARN value.

1. Verify that the **Subscription ID** shows an ARN value.

### Resolution
<a name="resolution-2"></a>

If the **Subscription ID** field shows `PendingConfirmation`, complete the following tasks:

1. Select the box next to **PendingConfirmation**.

1. Under **Subscriptions**, select **Request** **Confirmations**.

1. Navigate to the applicable email inbox.

1. In the subscription notification email, select the **SubscribeURL** link.

1. In the Amazon SNS console, refresh and verify that the **Subscription ID** has an ARN value.

## Problem: Hub stack creation failed
<a name="problem-hub-stack-creation-failed"></a>

If the hub stack creation failed with the following error, you haven’t allowed trusted access with Organizations:

 `You must enable organizations access to operate a service managed stack set (Service: CloudFormation, Status Code: 400, Request ID: ABCXYZ`

### Resolution
<a name="resolution-3"></a>

Allow trusted access with AWS Organizations to use service-managed permissions on AWS CloudFormation console or AWS Organizations console. See [Step 2b: Fulfill prerequisites manually](step-2b.-achieve-prerequisites-manually-optional.md) for instructions.

## Problem: Too many messages queued in the Summarizer SQS queue
<a name="problem-too-many-queue-messages"></a>

If too many messages are queued in the `QMSummarizerEventQueueQMSummarizerEventQueue` SQS queue and the number of queued messages keeps growing.

### Resolution
<a name="resolution-4"></a>

The `QMReporterQMReporterLambda` Lambda function consumes events from the queue and is invoked every five minutes by default. Try one or more of the following:
+ Increase the rate of the `QMReporterQMReporterEvents` EventBridge rule on the default bus.
+ Increase the value of the Lambda function’s `MAX_LOOPS` environmental variable.

## Problem: Identify the hub account number that centralizes quota alerts for the spoke account
<a name="hub-account-identification"></a>

In Organization/Hybrid Mode, it can be challenging to determine which hub account is responsible for centralizing quota alerts for a specific spoke account.

### Resolution
<a name="resolution-5"></a>

To identify the hub account number:

1. Log in to the spoke account.

1. Navigate to the Amazon EventBridge console.

1. Select the 'QuotaMonitorSpokeBus' event bus.

1. Look for a rule named 'QMUtilizationWarn' or 'QMUtilizationErr'.

1. Click on the identified rule.

1. Examine the target event bus ARN in the rule details.

The account number in the target event bus ARN is the hub account number.

 **Example ARN**

```
arn:aws:events:us-east-1:123456789012:event-bus/QuotaMonitorBus
```

In this example, 123456789012 is the hub account number.

## Problem: Stack failed to update due to deletion of resources outside of CloudFormation
<a name="deleted-resources-outside-cloudformation"></a>

If the solution’s resources are manually deleted outside of the CloudFormation stack, the solution will fail to update because the CloudFormation stack will not be able to find the resource.

### Resolution
<a name="resolution-6"></a>

For resolution, see the [How do I update a CloudFormation stack that’s failing because of a resource that I manually deleted?](https://repost.aws/knowledge-center/failing-stack-updates-deleted) article on AWS re:Post.
