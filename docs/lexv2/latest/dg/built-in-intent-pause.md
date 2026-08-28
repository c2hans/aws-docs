---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-pause.html
---

# AMAZON.PauseIntent
<a name="built-in-intent-pause"></a>

Responds to words and phrases that enable the user to pause an interaction with a bot so that they can return to it later. Your Lambda function or application needs to save intent data in session variables, or you need to use the [GetSession](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_GetSession.html) operation to retrieve intent data when you resume the current intent.

Common utterances:
+ pause
+ pause that

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
