---
source_url: https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-push.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Amazon Pinpoint push notifications
<a name="channels-push"></a>

**Note**
Amazon Pinpoint has updated their user guide documentation. To get the latest information regarding how to create, configure, and manage your Push resources, see the new [AWS End User Messaging Push User Guide](https://docs.aws.amazon.com/push-notifications/latest/userguide/what-is-service.html).
The following topics have been moved:
[Setting up Amazon Pinpoint mobile push channels](https://docs.aws.amazon.com/push-notifications/latest/userguide/procedure-enable-push.html)
[Monitoring push notification activity](analytics-campaigns.md)
To monitor push notification activity, you must use a campaign. You can't monitor push notification activity outside a campaign.
[Managing mobile push channels](https://docs.aws.amazon.com/push-notifications/latest/userguide/procedure-enable-push.html)
[Sending Safari web push notifications](https://docs.aws.amazon.com/push-notifications/latest/userguide/reference-send-message.html)
[Best practices](https://docs.aws.amazon.com/push-notifications/latest/userguide/channels-push-best-practices.html)

With Amazon Pinpoint, you can engage users of your apps by sending push notifications through a push notification channel. You can send push notifications to your apps using separate channels for the following push notification services:
+ Firebase Cloud Messaging (FCM)
+ Apple Push Notification service (APNs)
**Note**
You can use APNs to send messages to iOS devices such as iPhones and iPads, as well as to the Safari browser on macOS devices, such as Mac laptops and desktops.
+ Baidu Cloud Push
+ Amazon Device Messaging (ADM)

**Note**
Amazon Pinpoint sets the push endpoints with the earliest **EffectiveDate** to `INACTIVE` if a user has 15 endpoints and you add more push endpoints. See [Older push endpoints automatically set to inactive](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-auto-inactive.html) for more information.

**Topics**
+ [Troubleshooting the push channel](channels-push-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
