---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/default-prompts-from-lex.html
---

# Default prompts from Amazon Lex: Sorry
<a name="default-prompts-from-lex"></a>

If you add an Amazon Lex classic bot (not Amazon Lex V2) to your contact center, know that it also has some default prompts that it uses for error handling. For example:
+ Sorry, can you please repeat that?
+ Sorry, I could not understand. Goodbye.

**To change default Amazon Lex prompts**

1. In Amazon Lex, go to your bot.

1. On the Editor tab, choose Error Handling.

1. Change the text as needed. Choose **Save**, then **Build** and **Publish**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
