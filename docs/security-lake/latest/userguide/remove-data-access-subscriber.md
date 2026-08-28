---
source_url: https://docs.aws.amazon.com/security-lake/latest/userguide/remove-data-access-subscriber.html
---

# Removing a data subscriber from Security Lake
<a name="remove-data-access-subscriber"></a>

If you no longer want a subscriber to consume data from Security Lake, you can remove the subscriber by following these steps.

------
#### [ Console ]

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/).

1. In the navigation pane, choose **Subscribers**.

1. Select the subscriber that you want to remove.

1. Choose **Delete** and confirm the action. This will delete the subscriber and all the associated notification settings.

------
#### [ API ]

Based on your scenario, do one of the following:
+ To delete the subscriber and all associated notification settings, use the [DeleteSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteSubscriber.html) operation of the Security Lake API. If you're using the AWS Command Line Interface (AWS CLI), run the [delete-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-subscriber.html) command.
+ To retain the subscriber but stop future notifications to the subscriber, use the [DeleteSubscriberNotification](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteSubscriberNotification.html) operation of the Security Lake API. If you're using the AWS Command Line Interface (AWS CLI), run the run the [delete-subscriber-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-subscriber-notification.html) command.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
