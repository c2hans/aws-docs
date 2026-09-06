---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/notification-center-channels.html
---

# Delivery channels
<a name="notification-center-channels"></a>

| Channel | Type | Description |
| --- | --- | --- |
| In-app |  `inApp`  | Writes a notification item to each recipient’s inbox in the Spatial Data Portal. Notifications appear in the bell icon in the portal navigation. Items expire after 90 days. |
| Slack |  `slack`  | Posts a formatted message to a Slack webhook URL stored in AWS Secrets Manager. The webhook is the destination — recipients are not used for routing. |
| Email |  `email`  | Sends an email via Amazon SES to each recipient’s address resolved from their Cognito user profile. |

Each notification rule targets exactly one channel. To deliver to multiple channels, associate multiple rules — one per channel — to the same template. Each rule retries independently.
