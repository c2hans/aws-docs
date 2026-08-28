---
source_url: https://docs.aws.amazon.com/chatbot/latest/adminguide/multiple-accounts-in-a-channel.html
---

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Enabling multiple accounts to use commands using Amazon Q Developer in chat applications
<a name="multiple-accounts-in-a-channel"></a>

You can configure Amazon Q Developer in chat applications for multiple AWS accounts in the same chat channel. When you work with Amazon Q Developer in chat applications for the first time in that channel, it asks you which account you want to use. Amazon Q Developer in chat applications remembers the account selection for 7 days.

To change the default account in the channel, enter `@Amazon Q set default-account` and select the account from the list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
