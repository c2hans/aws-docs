---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/events-subscribing.html
---

# Subscribing to Neptune event notification
<a name="events-subscribing"></a>

You can use the Neptune console to subscribe to event notifications, as follows:

**To subscribe to Neptune event notification**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. In the navigation pane, choose **Event subscriptions**.

1. In the **Event subscriptions** pane, choose **Create event subscription**.

1. In the **Create event subscription** dialog box, do the following:

   1. For **Name**, enter a name for the event notification subscription.

   1. For **Send notifications to**, choose an existing Amazon SNS ARN for an Amazon SNS topic, or choose **create topic** to enter the name of a topic and a list of recipients.

   1. For **Source type**, choose a source type.

   1. Choose **Yes** to enable the subscription. If you want to create the subscription but to not have notifications sent yet, choose **No**.

   1. Depending on the source type you selected, choose the event categories and the sources that you want to receive event notifications from.

   1. Choose **Create**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
