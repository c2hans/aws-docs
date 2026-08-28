---
source_url: https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-event-destinations.html
---

# Message and event destinations in AWS End User Messaging Social
<a name="managing-event-destinations"></a>

An event destination is an Amazon SNS topic or Connect Customer instance that WhatsApp events are sent to. When you turn on event publishing, all of your send and receive events are sent to the message and event destination. Use events to monitor, track, and analyze the status of outbound messages and incoming customer communications.

Each WhatsApp Business Account (WABA) can have one event destination. All events from all resources associated to the WABA are logged to that event destination. For example, you could have a WABA with three phone numbers associated to it and all events from those phone numbers are logged to the one event destination.

**Topics**
+ [Add a message and event destination to AWS End User Messaging Social](managing-event-destinations-add.md)
+ [Message and event format in AWS End User Messaging Social](managing-event-destination-dlrs.md)
+ [WhatsApp message status](managing-event-destinations-status.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
