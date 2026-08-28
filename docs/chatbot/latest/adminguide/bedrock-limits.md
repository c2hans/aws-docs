---
source_url: https://docs.aws.amazon.com/chatbot/latest/adminguide/bedrock-limits.html
---

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Quotas for Amazon Bedrock in Amazon Q Developer in chat applications
<a name="bedrock-limits"></a>

Your AWS account has the following default quotas, formerly referred to as limits, for Amazon Bedrock.

| Name | Default | Adjustable | Description |
| --- | --- | --- | --- |
| Connectors per channel | 10 connectors. | No | The maximum number of registered connectors you can have in a channel. |
| InvokeAgent request timeout | 120 seconds. | No | The amount of time connectors allow the invokeAgent request to complete |
| InvokeAgent response truncation | 2,500 characters. | No | The maximum number of characters a response message from an agent can contain. |
| Connector names | 1-20 letters, digits, dashes or underscores | No | The maximum number of characters a valid connector name can contain. Each connector must have a unique name. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
