---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/events-manage.html
---

# Managing Neptune event notification subscriptions
<a name="events-manage"></a>

If you choose **Event subscriptions** in the navigation pane of the Neptune console, you can view subscription categories and a list of your current subscriptions.

 You can also modify or delete a specific subscription.

## Modifying Neptune event notification subscriptions
<a name="events-modify-subscriptions"></a>

**To modify your current Neptune event notification subscriptions**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. In the navigation pane, choose **Event subscriptions**. The **Event subscriptions** pane shows all your event notification subscriptions.

1. In the **Event subscriptions** pane, choose the subscription that you want to modify and choose **Edit**.

1. Make your changes to the subscription in either the **Target** or **Source** section. You can add or remove source identifiers by selecting or deselecting them in the **Source** section.

1. Choose **Edit**. The Neptune console indicates that the subscription is being modified.

## Deleting a Neptune event notification subscription
<a name="events-delete-subscription"></a>

You can delete a subscription when you no longer need it. All subscribers to the topic will no longer receive event notifications specified by the subscription.

**To delete an Neptune event notification subscription**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. In the navigation pane, choose **Event subscriptions**.

1. In the **Event subscriptions** pane, choose the subscription that you want to delete.

1. Choose **Delete**.

1. The Neptune console indicates that the subscription is being deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
