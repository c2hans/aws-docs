---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots.html
---

# Using AppInstanceBots as intelligent channel agents for Amazon Chime SDK messaging
<a name="appinstance-bots"></a>

You can use `AppInstanceBots` as intelligent channel agents. The agents recognize key phrases sent via `ChannelMessages` by channel members. The bot's natural language understanding model resolves the messages. In turn, that allows one or more channel members to engage in a natural language dialog defined by the bot's model. You supply the bots, so you control the depth of dialog and integration with your enterprise systems.

**Prerequisites**
+ Knowledge of basic Amazon Chime SDK functionality, such as creating `AppInstanceUsers`, managing channels, and sending and receiving messages.
+ The ability to invoke the Amazon Chime SDK Messaging APIs.
+ Knowledge of basic Amazon Lex V2 functionality, such as creating an Amazon Lex V2 Bot, modeling intents and slots, creating bot versions, aliases, using session state, and Lambda hook integration.

**Important**
Use of Amazon Lex V2 is subject to the [AWS Service Terms](https://aws.amazon.com/service-terms/), including the terms specific to the AWS Machine Learning and Artificial Intelligence Services.

**Topics**
+ [Creating an Amazon Lex V2 bot for Amazon Chime SDK messaging](create-lex-bot.md)
+ [Setting up AppInstance bots for Amazon Chime SDK messaging](appinstance-bot-setup.md)
+ [Creating a channel membership for an AppInstanceBot for Amazon Chime SDK messaging](channel-membership.md)
+ [Sending messages to an AppInstanceBot for Amazon Chime SDK messaging](message-appinstancebot.md)
+ [Processing messages from Amazon Lex for Amazon Chime SDK messaging](process-from-lexv2.md)
+ [Processing responses from an AppInstanceBot for Amazon Chime SDK messaging](process-response.md)
+ [Using rules to send events to Amazon EventBridge for Amazon Chime SDK messaging](event-bridge-alerts.md)
+ [Troubleshooting AppInstanceBots configured with Amazon Lex V2 bots for Amazon Chime SDK messaging](troubleshoot-lex-bots.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
