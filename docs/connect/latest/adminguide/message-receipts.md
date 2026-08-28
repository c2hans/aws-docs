---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/message-receipts.html
---

# Enable notifications for chat customers in Connect Customer
<a name="message-receipts"></a>

You can enable message *Delivered* and *Read* in your [chat user interface](add-chat-to-website.md) so your customers know the status of the messages they send. This provides transparency to customers, and improves the overall chat experience.

Regardless of whether message receipts are enabled, the message receipt data and events are always sent and can be seen in the network log. Enabling and disabling message receipts in your chat user interface only affects whether the receipts appear in the communication widget transcript.

**Tip**
By default message receipts are already enabled in the [Test chat](chat-testing.md#test-chat) experience, the Contact Control Panel (CCP), and [downloadable open source example](download-chat-example.md) of the chat widget.

**To enable message receipts in your chat user interface**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Choose **Customize communications widget**.
![The configuration guide page, the customize communications widget option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/chatwidget-customize-chat-window-button.png)

1. Choose **Edit**.
![The saved communications widget customization page, the edit button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/chatwidget-edit-messagereceipt.png)

1. By default **Message receipts** is not enabled. Set to **Enabled**.
![The message receipts option, enabled.](http://docs.aws.amazon.com/connect/latest/adminguide/images/chatwidget-enable-messagereceipt.png)

Message receipts are now enabled. Customers who are using the communications widget will start seeing *Delivered* and *Read* receipts immediately.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
