---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/provider-generated-notifications.html
---

# Provider-generated notifications in AWS Data Exchange
<a name="provider-generated-notifications"></a>

As a provider in AWS Data Exchange, you can send provider-generated notifications to inform your subscribers about important events related to your data sets. You can contact your subscribers in a structured manner and help them to process their entitled data related events in a consistent manner across providers.

Using provider-generated notifications, you do the following to help your subscribers:
+ Send notifications for data updates, delays, schema changes, and deprecations using the AWS Data Exchange Console or the AWS SDK.
+ Include comments and expected actions for subscribers to follow.

**To send provider-generated notifications to subscribers, follow these steps:**

1. Open and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. From the left navigation pane, choose **Send notification**.

1. Select your **Notification type** from the dropdown menu. Notification types include:
   + **Data update** – the data source has been updated.
   + **Data delay** – the data source hasn’t updated as expected.
   + **Schema change** – the data source will include a structural change.
   + **Deprecation** – the data source will no longer be updated.

1. Select the impacted data set from the dropdown menu and view your **Notification details** for the **date**, **time**, and **list** of subscriber actions. You can also provide location metadata for specifying what is affected by this event.

1. Choose **Preview notification** and publish your notification.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
