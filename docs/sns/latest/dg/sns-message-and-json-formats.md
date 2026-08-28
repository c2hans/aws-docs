---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-message-and-json-formats.html
---

# Parsing Amazon SNS message formats
<a name="sns-message-and-json-formats"></a>

When Amazon SNS sends messages to HTTP/HTTPS endpoints, they contain both HTTP headers and a JSON message body. These messages follow a structured format that includes metadata such as the message type, topic ARN, timestamps, and digital signatures. By correctly parsing Amazon SNS messages, you can determine whether a message is a subscription confirmation, notification, or unsubscribe confirmation, extract relevant data, and verify authenticity using signature validation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
