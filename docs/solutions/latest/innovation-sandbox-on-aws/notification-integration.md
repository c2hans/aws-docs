---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/notification-integration.html
---

# Integrate notifications with other tools

Innovation Sandbox can publish its notifications to an Amazon SNS topic, so you can deliver them to your preferred communication channels, chat applications, or ticketing systems. The solution publishes the notifications, and you build and manage the subscribers that format and deliver them. Email notifications through Amazon SES and notifications through the SNS integration topic are independent channels. You can turn on either one, both, or neither.

The Compute stack creates the topic, `ISB-<namespace>-NotificationIntegration`, in the Hub account and returns its ARN in the `NotificationIntegrationTopicArn` stack output. The topic exists even when the **SNS integration topic** setting is off. The setting controls only whether the solution publishes to the topic, so turning it on or off never changes the topic ARN or removes your subscriptions.

## Published messages
<a name="notification-integration-messages"></a>

When the **SNS integration topic** setting is on, the solution publishes the same notifications it sends by email. A notification produces one message for each audience it addresses:
+ The lease owner or assigned user.
+ Managers and Administrators.
+ Administrators only, for account cleanup failures, account drift, and group cost reports.

Some notifications address one audience; others, such as a lease frozen or terminated for budget or expiry, address two and produce two messages. The solution doesn’t publish a message for an audience with no recipients, or when a user terminates their own lease.

Each message body is a JSON document with the following fields:
+  `subject`: The notification’s subject.
+  `body`: The notification’s text content.
+  `htmlBody`: The notification’s HTML content, when the notification has one.
+  `notificationType`: The notification type, for example `LeaseRequested` or `LeaseFrozen`.
+  `recipientPersona`: The audience: `user` for the lease owner or assigned user, `manager` for Managers and Administrators, or `admin` for Administrators only.
+  `recipientEmails`: The recipients' email addresses. The SNS notification envelope delivered to Amazon SQS reports this attribute as `String.Array`. An SNS event delivered to Lambda reports it as `String`. In either case, parse the value as a JSON array, even for a single recipient.
+  `schemaVersion`: The version of the message format.
+  `awsAccountId`: The sandbox account ID, when the notification relates to an account.
+  `leaseUuid`: The lease ID, when the notification relates to a lease.

Use `notificationType` and `recipientPersona` in subscription filter policies. Read `recipientEmails`, `awsAccountId`, and `leaseUuid` in your subscriber’s code; filtering on them can exhaust the SNS limit on filter policies for a topic. For the full list of notification types, see the [notification publishing source code](https://github.com/aws-solutions/innovation-sandbox-on-aws/tree/main/source/common/isb-services/notification-publishing) on GitHub.

The schema version increases whenever the message format changes. Check it before parsing a message, and log or alert on values your subscriber doesn’t recognize instead of processing them.

## Subscribe to the integration topic
<a name="notification-integration-subscribe"></a>

The topic’s access policy grants no access to other accounts, so principals in the Hub account need IAM permissions to subscribe. The solution creates no subscriptions. To consume notifications, subscribe an endpoint, such as an Amazon SQS queue, an AWS Lambda function, or an HTTPS endpoint. To deliver notifications to another account, we recommend subscribing an endpoint in the Hub account that forwards them, which keeps the topic’s access policy unchanged.

To deliver notifications to your own tools:

1. In the AWS CloudFormation console in the Hub account, choose the Compute stack, choose the **Outputs** tab, and copy the `NotificationIntegrationTopicArn` value.

1. Subscribe your endpoint to the topic. For instructions, see [Creating a subscription to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html) in the *Amazon Simple Notification Service Developer Guide*.

1. (Optional) Add a subscription filter policy on `notificationType` or `recipientPersona`, so the subscriber receives only the notifications it needs. For example, the following filter policy delivers only notifications for Managers and Administrators:

   ```json
   {
     "recipientPersona": ["manager", "admin"]
   }
   ```

   For more information, see [Amazon SNS message filtering](https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html).

1. In the solution web UI, choose **Settings**, turn on **SNS integration topic** in the notification settings, and save.

1. Trigger a notification, for example by requesting a lease that requires approval, and confirm that your subscriber receives it.

Examples of subscribers you can build:
+  **Shared Slack or Microsoft Teams channel**: A Lambda function that formats each message and posts it to a channel webhook. To use Amazon Q Developer in chat applications, have the Lambda convert the ISB message to the [Amazon Q custom notification format](https://docs.aws.amazon.com/chatbot/latest/adminguide/custom-notifs.html) and publish it to a separate SNS topic configured for Amazon Q.
+  **Direct messages to each recipient**: A Lambda function that reads the recipient addresses, finds each person in your chat tool, and sends them a message. This requires a chat app that your workspace administrator installs.
+  **ITSM tickets**: An SQS queue that your ITSM system polls, or a Lambda function that calls its API.

With raw message delivery to Amazon SQS, a message can carry at most 10 message attributes, and SNS drops messages that exceed the limit. The solution uses up to six attributes, so its messages stay within this limit.

## Security and delivery
<a name="notification-integration-security"></a>

Every message includes the recipients' email addresses and the notification content for leases and accounts across the deployment. Anyone who can subscribe to the topic receives every notification. Treat permission to call `sns:Subscribe` on the topic as an administrative privilege, and grant it only to principals that need it. The solution grants this permission to none of the roles it creates.

The topic is encrypted at rest with the Compute stack’s AWS KMS customer managed key, and its access policy denies publish requests that don’t use TLS.

The solution retries a failed publish, then logs the failure and raises the **SNS publish failure** alarm. Email is sent independently, so an SNS failure doesn’t stop email delivery. For more information, see [Alarms deployed by the solution](monitoring-alarms.md#solution-alarms).

If your subscriber is in a different Region from the Hub account, review the Amazon SNS requirements for cross-Region delivery before you subscribe, especially for Regions that are disabled by default.
