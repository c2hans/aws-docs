---
source_url: https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-begin.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Create a campaign
<a name="campaigns-begin"></a>

The first step in setting up a campaign is to create a new campaign. When you create a new campaign, you give the campaign a name, specify whether the campaign should be a standard campaign or an A/B test campaign, and choose the channel that you want to use to send the campaign.

**To begin creating a campaign**

1. Open the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/).

1. On the **All projects** page, choose the project that you want to create the campaign in.

1. In the navigation pane, choose **Campaigns**.

1. Choose **Create a campaign**.

1. For **Campaign name**, enter a descriptive name for the campaign. Using a descriptive name makes it faster to find or search for the campaign later.

1. For **Campaign type**, choose one of the following options:
   + **Standard campaign** – Sends a message to a segment on a schedule that you define.
   + **A/B test campaign** – Behaves like a standard campaign, but enables you to define different treatments for the campaign's message or schedule. In an A/B test campaign, you create several versions of a message or schedule to compare their performance.

1. Under **Choose a channel for this campaign**, choose the channel that you want to use to send the campaign.
**Note**
You can only choose a single channel. You can only choose the channels that are enabled for the current project. The **Custom** channel is enabled for all projects by default.

1. If you chose **In-app messaging** in the preceding step, choose a **Prioritization** for the in-app message. The value that you choose determines which message is shown in response to a trigger event.

   If you chose a different message type, proceed to the next step.

1. Choose **Next**.

**Next**
[Specify the audience for the campaign](campaigns-segment.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
