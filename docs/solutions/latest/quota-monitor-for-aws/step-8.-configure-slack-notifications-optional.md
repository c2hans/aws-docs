---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-8.-configure-slack-notifications-optional.html
---

# Step 8. Configure Slack notifications (optional)
<a name="step-8.-configure-slack-notifications-optional"></a>

1. Navigate to your workspace’s Slack app.

   If required, sign in to Slack.

1. Choose **Create New App**.

1. Choose **From Scratch**.

1. Give the app a name and assign it to your workspace.

1. In the **Add features and functionality** section, select **Incoming Webhooks**.

1. Allow the feature and choose **Add New Webhook to Workspace**.

1. In the **Post to Channel** dropdown menu, select a channel.

1. Copy the WebHook URL.

1. In the AWS Systems Manager console, under **Shared Resources** in the left pane, select **Parameter Store**.

1. Select the `/QuotaMonitor/SlackHook` parameter, then choose **Edit**.

1. Update the value with your WebHook URL and choose **Save changes**.
