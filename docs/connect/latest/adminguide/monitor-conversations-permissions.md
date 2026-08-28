---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/monitor-conversations-permissions.html
---

# Assign permissions to monitor live conversations in the Connect Customer Contact Control Panel (CCP)
<a name="monitor-conversations-permissions"></a>

For managers to monitor live conversations, you assign them the **CallCenterManager** and **Agent** security profiles. To allow agent trainees to monitor live conversations, you might want to create a security profile specific for this purpose.

**To assign a manager permissions to monitor a live conversation**

1. Go to **Users**, **User management**, choose the manager, and then choose **Edit**.

1. In the Security Profiles box, assign the manager to the **CallCenterManager** security profile. This security profile also includes a setting that makes the icon to download recordings appear in the results of the **Contact search** page.

1. Assign the manager to the **Agent** security profile so they can access the Contact Control Panel (CCP), and use it to monitor the conversation.

1. Choose **Save**.

**To create a new security profile for monitoring live conversations**

1. Choose **Users**, **Security profiles**.

1. Choose **Add new security profile**.

1. Expand **Analytics and optimization**, then choose **Access metrics** and **Real-time contact monitoring**.

   **Access metrics** is needed so they can access the real-time metrics report, which is where they choose which conversations to monitor.

1. Expand **Contact Control Panel**, then choose **Access Contact Control Panel** and **Make outbound calls**.
![The contact control panel section of the security profiles page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/monitor-conversations-agent-permissions2.png)

   These permissions are needed so they can monitor the conversation through the Contact Control Panel.

1. Choose **Save**.

Next, show your managers how to monitor conversations. Continue to [Listen to live conversations or read live chats in Connect Customer](monitor-conversations-howto.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
