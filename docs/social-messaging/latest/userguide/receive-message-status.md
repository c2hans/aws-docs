---
source_url: https://docs.aws.amazon.com/social-messaging/latest/userguide/receive-message-status.html
---

# Example of changing a message's status to read in AWS End User Messaging Social
<a name="receive-message-status"></a>

You can set the [status of the message](managing-event-destinations-status.md) to `read` to show the end user two blue check marks on their screen.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product":"whatsapp","message_id":"'{{{MESSAGE_ID}}}'","status":"read"}' --origination-phone-number-id {{{ORIGINATION_PHONE_NUMBER_ID}}} --meta-api-version v20.0
```

In the preceding command, do the following:
+ Replace {{{ORIGINATION\_PHONE\_NUMBER\_ID}}} with your phone number's ID.
+ Replace {{{MESSAGE\_ID}}} with the unique identifier of the message. Use the value of the `id` field in the message object of the Amazon SNS topic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
