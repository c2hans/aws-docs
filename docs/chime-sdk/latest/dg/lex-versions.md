---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/lex-versions.html
---

# Creating Amazon Lex V2 bot versions for Amazon Chime SDK messaging
<a name="lex-versions"></a>

When you create an Amazon Lex V2 Bot, you only create a *draft* version. The draft is a working copy of the bot that you can update. By default, the draft version is associated with an alias called `TestBotAlias`, and you should only use the draft bot for manual testing.

After you finish dialog modeling and building the draft bot, you create one or more *versions*, numbered snapshots of the draft Lex bot. Versions allow you to control the implementation that your client applications use. For example, you can publish versions for use in different parts of your workflow, such as development, beta deployment, and production.

For more information about Lex bot versioning, see [Creating versions](https://docs.aws.amazon.com/lexv2/latest/dg/versions.html) in the *Amazon Lex V2 Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
