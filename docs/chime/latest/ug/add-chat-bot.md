---
source_url: https://docs.aws.amazon.com/chime/latest/ug/add-chat-bot.html
---

# Adding chat bots to chat rooms
<a name="add-chat-bot"></a>

Chat bots provide conversational interfaces for a chat room. For example, a chat bot can answer frequently asked questions, then route users to more information about their issues. Chat bots can also enable voice conversations with the members of a chat room.

**Important**
To use chat bots, you must have an Amazon Chime Enterprise account. Also, your Amazon Chime account administrator must create the bots before you can add them to rooms. After the administrator creates the bot, get the bot's email address from the administrator.

**To add a chat bot to a chat room**

1. Obtain the email address of the chat bot from your Amazon Chime system administrator.

1. In the sidebar, open the chat room.

1. Choose the ellipsis menu located to the right of the chat room name, then choose **Manage webhooks and bots**.

1. In the **Manage incoming webhooks and bots in** *chat room name* dialog box, choose **Add bot**.

1. Enter the email address provided by your administrator.

1. Choose **Add**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
