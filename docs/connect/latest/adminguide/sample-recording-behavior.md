---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/sample-recording-behavior.html
---

# Sample recording behavior in Connect Customer
<a name="sample-recording-behavior"></a>

**Note**
This topic explains a sample flow that is included with Connect Customer. For information about locating the sample flows in your instance, see [Sample flows in Connect Customer](contact-flow-samples.md).

Type: Flow (inbound)

This flow starts by checking the channel of the contact:
+ If the contact is a task, it is transferred to the Sample inbound flow.
+ If the customer is using chat, they get a prompt that the **Set recording block** enables managers to monitor chat conversations. (To *record* chats, you only need to specify an Amazon S3 bucket where the conversation will be stored.)

  To monitor chats, the **Set recording block** is configured to record both the **Agent and Customer**.
+ If the contact is using voice, a **Get customer input** block prompts them to enter the number for who they want to record. Their entry triggers the **Set recording behavior** block with the appropriate configuration.

It ends with the customer being transferred by to the [Sample inbound flow](sample-inbound-flow.md).

For more information, see the following topics:
+ [When, what, and where for contact recordings in Connect Customer](about-recording-behavior.md)
+ [Enable contact recording](set-up-recordings.md)
+ [Enable enhanced multi-party contact monitoring in Connect Customer](monitor-conversations.md)
+ [Review recorded conversations between agents and customers using Connect Customer](review-recorded-conversations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
