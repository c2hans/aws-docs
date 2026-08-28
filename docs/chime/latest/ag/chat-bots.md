---
source_url: https://docs.aws.amazon.com/chime/latest/ag/chat-bots.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Integrating chatbots into the Amazon Chime desktop client
<a name="chat-bots"></a>

You can use the AWS Command Line Interface (AWS CLI), Amazon Chime API, or AWS SDK to integrate chatbots with Amazon Chime. Chatbots let you use the power of Amazon Lex, AWS Lambda, and other AWS services to streamline common tasks with intelligent conversational interfaces that are accessible to users in Amazon Chime chat rooms.

If you're an Amazon Chime Enterprise account administrator, you can use chatbots to allow users to perform such tasks as:
+ Querying their internal systems for information.
+ Automating tasks.
+ Receiving notifications for critical issues.
+ Creating support tickets.

For more information about Amazon Chime Enterprise accounts, see [Managing your Amazon Chime accounts](manage-chime-account.md).

If you administer an Amazon Chime Enterprise account, you can create up to 10 chatbots for integration with Amazon Chime. Chatbots can be used only in chat rooms created by members of your account. Only chat room administrators can add chatbots to a chat room. After a chatbot is added to a chat room, members of the chat room can interact with the bot using commands provided by the bot creator. For more information, see the next section in this topic.

Linux and macOS users can build a sample custom chatbot. For more information, see [Build custom chatbots for Amazon Chime](https://aws.amazon.com/blogs/business-productivity/build-custom-chat-bots-for-amazon-chime/).

**Topics**
+ [Using chatbots with Amazon Chime](use-bots.md)
+ [Amazon Chime events sent to chatbots](events-bots.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
