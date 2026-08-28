---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/importing-exporting.html
---

# Importing and exporting bots in Lex V2
<a name="importing-exporting"></a>

You can export a bot definition, a bot locale or a custom vocabulary and then import it back to create a new resource or to overwrite an existing resource in an AWS account. For example, you can export a bot from a test account and then create a copy of the bot in your production account. You can also copy a bot from one AWS Region to another Region.

You can change the resources of the exported resource before importing it. For example, you can export a bot and then edit the JSON file for a slot to add or remove slot value elicitation utterances from a specific slot. After you finish editing the definition, you can import the modified file.

**Topics**
+ [Exporting bots from Lex V2](export.md)
+ [Importing bots in Lex V2](import.md)
+ [Using a password when importing or exporting](import-export-password.md)
+ [JSON format for importing and exporting bots in Lex V2](import-export-format.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
