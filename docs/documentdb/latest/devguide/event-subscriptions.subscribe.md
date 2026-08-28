---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/event-subscriptions.subscribe.html
---

# Subscribing to Amazon DocumentDB events
<a name="event-subscriptions.subscribe"></a>

You can use the Amazon DocumentDB console to subscribe to event subscriptions, as follows:

1. Sign in to the AWS Management Console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Event subscriptions**.
![Amazon DocumentDB console navigation pane with Event Subscriptions option highlighted.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/subscribe-event-subs.png)

1. In the **Event subscriptions** pane, choose **Create event subscription**.
![Event Subscriptions pane highlighting the Create event subscription button in the upper-right corner.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/subscribe-create.png)

1. In the **Create event subscription** dialog box, do the following:
   + For **Name**, enter a name for the event notification subscription.
![The Create event subscription form showing the Details section and the Name input field.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/subscribe-name.png)
   + For **Target**, choose where you want to send notifications to. You can choose an existing **ARN** or choose **New Email Topic** to enter the name of a topic and a list of recipients.
![The Target section with options to specify where to send notifications to.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/subscribe-target.png)
   + For **Source**, choose a source type. Depending on the source type you selected, choose the event categories and the sources that you want to receive event notifications from.
![The Source section to select a source type to receive event notifications from.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/subscribe-source.png)
   + Choose **Create**.
![The Source section with the Create button in the lower-right corner.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/subscribe-create-2.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
