---
source_url: https://docs.aws.amazon.com/push-notifications/latest/userguide/load-balancer-limits.html
---

# Quotas for AWS End User Messaging Push
<a name="load-balancer-limits"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for AWS End User Messaging Push, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **Amazon Pinpoint**.

Your AWS account has the following quotas related to AWS End User Messaging Push.

| Resource | Default quota | Eligible for increase |
| --- | --- | --- |
| Maximum number of push notifications that can be sent per second in a campaign | 25,000 notifications per second | Yes, use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home) |
| Amazon Device Messaging (ADM) message payload size | 6 KB per message | No |
| Apple Push Notification service (APNs) message payload size | 4 KB per message | No |
| APNs sandbox message payload size | 4 KB per message | No |
| Baidu Cloud Push message payload size | 4 KB per message | No |
| Firebase Cloud Messaging (FCM) message payload size | 4 KB per message | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Push. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query push-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
