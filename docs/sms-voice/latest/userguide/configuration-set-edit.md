---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-edit.html
---

# Edit a configuration set in AWS End User Messaging SMS
<a name="configuration-set-edit"></a>

To edit a configuration set using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Configuration sets**.

1. On the **Configuration sets** page, choose the configuration set to edit.

1. Select the **Set settings** tab and then choose **Edit settings**.

1. In **List settings** do the following:
   + **Message type** choose either:
     + **Promotional** – Choose this option for sending marketing messages or messages promoting your business or service.
     + **Transactional** – Choose this option for sending time-sensitive messages, such as password resets or transaction alerts.
   + **Default sender ID** – Choose the default sender ID for the configuration set.
   + **Message feedback** – Choose to enable [Message feedback](message-feedback.md#message-feedback.title) for the configuration set.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
