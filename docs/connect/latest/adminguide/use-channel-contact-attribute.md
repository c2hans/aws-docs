---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/use-channel-contact-attribute.html
---

# Personalize a contact's experience based on how they contact your contact center
<a name="use-channel-contact-attribute"></a>

You can personalize the customer's experience based on the channel that they use to contact you. Here's what you do:

1. Add a **Check contact attributes** block to the beginning of your flow.

1. Configure the block as shown in the following image. In the **Attribute to check** section, set **Type** to **System**, set **Attribute** to **Channel**. In the **Conditions to check** section, set it to **Equals CHAT**.
![The Attribute to check section set to Channel, the Conditions to check section set to chat.](http://docs.aws.amazon.com/connect/latest/adminguide/images/channel-attribute.png)

1. The following image of the configured Check contact attributes block shows two branches: **CHAT** and **No Match**. If the customer is contacting you through chat, specify what should happen next. If the customer is contacting you through a call (No Match), specify the next step in the flow.
![A configured Check contact attributes block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/channel-attribute-flow.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
