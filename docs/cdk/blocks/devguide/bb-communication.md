---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/bb-communication.html
---

# Communication

This section covers AWS CDK Blocks for sending messages to users.

## EmailClient
<a name="bb-email-client"></a>

Transactional email sending. Configure a from address and send emails with text or HTML bodies. Use `sendBatch()` to send many emails at once. It takes up to 100 messages per call by default (`maxBatchSize`) and sends them to SES in groups of 50. Each message can have at most 50 recipients (To, CC, and BCC combined). Both `send()` and `sendBatch()` check every address, the recipient count, and the message size (40 MB) before calling SES.

Locally, EmailClient writes emails to an outbox file (`.bb-data/<id>/emails.json`, where `<id>` is the CDK Block’s full ID) instead of sending them, so you can inspect them during development. On AWS, it sends via Amazon SES. Best for signup confirmations, password resets, notifications, and any transactional communication.

Before you deploy, verify the sender’s domain or address as an identity in Amazon SES. A new account starts in the SES sandbox, which sends only to verified email addresses and domains and limits sending (200 messages per 24 hours, 1 per second) until you request production access. Sandbox status is per AWS Region. EmailClient grants your app’s execution role only `ses:SendEmail` and `ses:SendBulkEmail`.

For more information, see [bb-email-client on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-email-client).
