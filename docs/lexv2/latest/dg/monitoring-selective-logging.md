---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-selective-logging.html
---

# Selective conversation log capture in Lex V2
<a name="monitoring-selective-logging"></a>

The selective conversation log capture allows the user to select how conversation logs are captured with text and audio data from the live conversations.

To enable and capture the output of the selective conversation log capture feature, you must activate the feature in the Amazon Lex V2 console, and enable the required session attributes in the API settings to capture the selected output from the logs.

You can select the following options for the selective conversation log capture:
+ text only
+ audio only
+ text and audio

You can capture specific parts of the conversation, and choose if audio, text, or both are captured for the conversation log.

**Note**
Selective conversation log capture works for Amazon Lex V2 only.

**Topics**
+ [Manage selective conversation log capture](manage-selective-logging.md)
+ [Example of selective conversation log capture](example-selective-logging.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
