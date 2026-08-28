---
source_url: https://docs.aws.amazon.com/blocks/latest/devguide/bb-communication.html
---

# Communication
<a name="bb-communication"></a>

This section covers Blocks for sending messages to users.

## EmailClient
<a name="bb-email-client"></a>

Transactional email sending. Configure a from address and send emails with text or HTML bodies. Supports batch sending for up to 50 emails in one call.

Locally, EmailClient captures sent emails and logs them to the console for development testing. On AWS, it sends via Amazon SES. Best for signup confirmations, password resets, notifications, and any transactional communication.

For more information, see [bb-email-client on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-email-client).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Blocks. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query blocks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
