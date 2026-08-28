---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/conversation-contexts.html
---

# Conversation context with your Lex V2 bots
<a name="conversation-contexts"></a>

*Conversation context* is information that the user, your client application, or a Lambda function provides to a Amazon Lex V2 bot to fulfill an intent. Conversation context includes slot data that the user provides, request attributes set by the client application, and session attributes that the client application and Lambda functions create.

**Topics**
+ [Setting intent context for your Lex V2 bot](context-mgmt-active-context.md)
+ [Using default slot values in intents for your Lex V2 bot](context-mgmt-default.md)
+ [Setting session attributes for your Lex V2 bot](context-mgmt-session-attribs.md)
+ [Setting request attributes for your Lex V2 bot](context-mgmt-request-attribs.md)
+ [Setting the session timeout](context-mgmt-session-timeout.md)
+ [Sharing information between intents with your Lex V2 bot](context-mgmt-cross-intent.md)
+ [Setting complex attributes in your Lex V2 bot](context-mgmt-complex-attributes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
