---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/default-agent-hold.html
---

# Default agent hold flow in Connect Customer: You are on hold
<a name="default-agent-hold"></a>

The **Default agent hold** flow is the experience the agent receives when placed on hold. During this flow, a **Loop prompt** block plays the message "You are on hold" to the agent every 10 seconds.

![The properties page of the loop prompts block, the message You are on hold.](http://docs.aws.amazon.com/connect/latest/adminguide/images/default-agent-hold-loop-prompt.png)

You can set **break time** to a maximum of 10 seconds. This means the maximum amount time you can specify between **You are on hold** messages is 10 seconds. To make the time between longer, add multiple prompts to the loop. For example, if you want 20 seconds between **You are on hold** messages:
+ The first prompt might say **You are on hold** with **break time="10s"**
+ Add another prompt with a blank message and break time="10s".

![break time = 10s in the text-to-speech box.](http://docs.aws.amazon.com/connect/latest/adminguide/images/default-agent-hold-loop-prompt-example.png)

For instructions about how to override and change a default flow, see [Change a default flow in your Connect Customer contact center](change-default-contact-flow.md).

**Tip**
Wondering if a default flow has been changed? Use [flow version control](flow-version-control.md) to view the original version of the flow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
