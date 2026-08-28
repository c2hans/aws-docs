---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-actions.html
---

# Keyword actions
<a name="keywords-actions"></a>

A keyword can have one of three actions associated with it. When a customer responds with the keyword the action will be performed to add or remove the user from the opt-out list or respond to the user with a message.
+ `Opt-out` – The recipient is added to the opt-out list and will not receive future messages.
+ `Opt-in` – The recipient wants to receive future messages.
+ `Automatic response` A message is sent to the recipient who send the text keyword message.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
