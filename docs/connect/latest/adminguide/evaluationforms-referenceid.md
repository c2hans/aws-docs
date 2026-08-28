---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/evaluationforms-referenceid.html
---

# Use a reference ID to represent questions in a report about contact center agent performance
<a name="evaluationforms-referenceid"></a>

A *reference ID* is a token that appears in the JSON output file. It represents a specific question. When building reports, you can use it in place of the exact wording of a question.

For example, a question might be "Did agents stick to the script?" but the next day the question might be changed to "Was there good script adherence?" Regardless of how the question is worded, the reference ID always stays the same.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
