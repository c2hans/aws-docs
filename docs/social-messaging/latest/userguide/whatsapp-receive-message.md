---
source_url: https://docs.aws.amazon.com/social-messaging/latest/userguide/whatsapp-receive-message.html
---

# Responding to a message in AWS End User Messaging Social
<a name="whatsapp-receive-message"></a>

Before you can receive a text or media message, you must have set up your WhatsApp Business Account (WABA) and an event destination. When you receive an incoming message, an event is saved in the event destination Amazon SNS topic. To receive a notification, you must subscribe to the Amazon SNS topics endpoint.

For an example event of a received media message, see [Example WhatsApp JSON for receiving a media message](managing-event-destination-dlrs.md#managing-event-destination-dlrs-example-receive-media). For more information on configuring the AWS CLI, see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *[AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)*. For a list of supported media file types, see [Supported media file types and sizes in WhatsApp](supported-media-types.md).

**Important**
To receive incoming messages, you must have [event destinations](managing-event-destinations-add.md) enabled for the WABA. For more information, see [Add a message and event destination to AWS End User Messaging Social](managing-event-destinations-add.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
