---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/debug-notifications.html
---

# Debugging push notification failures for Amazon Chime SDK messaging
<a name="debug-notifications"></a>

The Amazon Chime SDK integrates with Amazon EventBridge in order to notify you of push message delivery failures. To further debug failures, you can also look into the [CloudWatch metrics](https://docs.aws.amazon.com/pinpoint/latest/userguide/monitoring-metrics.html) that Amazon Pinpoint sends for failures.

The following table lists and describes the delivery error messages.

| Message | Description |
| --- | --- |
| The request processing has failed because of an unknown error, exception or failure. | We encountered an internal error. Please try again. |
| The specified resource was not found. AppInstanceUserEndpoint will be deactivated. | The Amazon Pinpoint application does not exist. |
| Too many requests sent to Amazon Pinpoint. | Amazon Pinpoint has throttled your outgoing messages. |
| Unable to send messages. Please verify IAM Permissions Policy on ServiceRoleForAmazonChimePushNotification. | The role created for the Amazon Chime SDK does not have permission to call `mobiletargeting:SendMessages`. Please verify the IAM policy on the role. |
| Unable to send messages. Please verify IAM Trust Relationships on ServiceRoleForAmazonChimePushNotification. | The Amazon Chime SDK does not have permission to access the role for push notificiations. <br />Please verify the IAM role's trust policy contains the service principal, `messaging.chime.amazonaws.com`. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
