---
source_url: https://docs.aws.amazon.com/social-messaging/latest/userguide/receive-message-emoji.html
---

# Example of responding to a message with a reaction in AWS End User Messaging Social
<a name="receive-message-emoji"></a>

You can add a reaction to the message, like a thumbs up.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product":"whatsapp","recipient_type":"individual","to":"'{{{PHONE_NUMBER}}}'","type": "reaction","reaction": {"message_id": "'{{{MESSAGE_ID}}}'","emoji":"\uD83D\uDC4D"}}' --origination-phone-number-id {{{ORIGINATION_PHONE_NUMBER_ID}}} --meta-api-version v20.0
```

In the preceding command, do the following:
+ Replace {{{PHONE\_NUMBER}}} with your customer's phone number.
+ Replace {{{MESSAGE\_ID}}} with the unique identifier of the message. Use the value of the `id` field in the message object of the Amazon SNS topic.
+ Replace {{{ORIGINATION\_PHONE\_NUMBER\_ID}}} with your phone number's ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
