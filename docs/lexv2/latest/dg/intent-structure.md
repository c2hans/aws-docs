---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/intent-structure.html
---

# Intent structure
<a name="intent-structure"></a>

Intents are the goals that your users want to accomplish, such as ordering flowers or booking a hotel. Your bot must have at least one intent. An intent is made up of the following components
+ **Initial response** – The initial message sent to the user after the intent is invoked. You can set responses, initialize values, and define the next step that your bot takes to respond to the user at the beginning of the intent.
+ **Slots** – The parameters required to fulfill an intent. Each slot has a type that defines the values that can be entered in the slot. You can choose from your custom slot types or you can choose a built-in slot type.
+ **Confirmation** – After the conversation with the user is complete and the slot values for the intent are filled, you can set a confirmation prompt to ask the user if the slot values are correct.
+ **Fulfillment** – The response sent to a user during the course of fulfillment. You can set fulfillment progress updates at the start of fulfillment and continue sending periodic updates while the fulfillment is in progress. You can also set a post-fulfillment success message, a failure message, and a timeout message.
+ **Closing response** – The closing response sent to the user after their intent is fulfilled. You can set the closing response to end the conversation, or you can set it to let the user know that they can continue with another intent.

**Topics**
+ [Initial response](intent-initial.md)
+ [Slots](intent-slots.md)
+ [Confirmation](intent-confirm.md)
+ [Fulfillment](intent-fulfillment.md)
+ [Closing response](intent-closing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
