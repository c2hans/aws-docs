---
source_url: https://docs.aws.amazon.com/chatbot/latest/adminguide/bedrock-converse.html
---

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Conversing with your Amazon Bedrock Agent connectors using Amazon Q Developer in chat applications
<a name="bedrock-converse"></a>

To start a conversation with your agent, run:

`@Amazon Q ask {{connector_name}} {{your message}}`. This invokes your configured agent with your message within a new session. Your agent's response starts a new thread in your chat channel under the initial message.

Any subsequent mention of `@Amazon Q` in this thread sends the provided message directly to the agent and all interactions in this thread share the same agent and session ID. As such, you can continue to ask questions in this thread without specifying the name of your connector.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
