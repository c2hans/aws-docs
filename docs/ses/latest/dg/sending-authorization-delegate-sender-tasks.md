---
source_url: https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks.html
---

# Delegate sender tasks for Amazon SES sending authorization
<a name="sending-authorization-delegate-sender-tasks"></a>

As a delegate sender, you're sending emails on behalf of an identity that you don't own, but are authorized to use. Even though you're sending on the identity owner's behalf, bounces and complaints count toward the bounce and complaint metrics for your AWS account, and the number of messages you send counts toward your sending quota. You're also responsible for requesting any sending quota increases that you might need in order to send the identity owner's emails.

As a delegate sender, you must complete the following tasks:
+ [Providing information to the identity owner](sending-authorization-delegate-sender-tasks-information.md)
+ [Using delegate sender notifications](sending-authorization-delegate-sender-tasks-notifications.md)
+ [Sending emails for the identity owner](sending-authorization-delegate-sender-tasks-email.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
