---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-thinking-differences.html
---

# Differences in thinking across model versions
<a name="claude-messages-thinking-differences"></a>

The Messages API handles thinking differently across Claude 3.7 Sonnet and Claude 4 models, primarily in redaction and summarization behavior. The following table summarizes those differences.

| Feature | Claude 3.7 Sonnet | Claude 4 Models |
| --- | --- | --- |
| Thinking output | Returns the full thinking output | Returns summarized thinking |
| Redaction handling | Uses `redacted_thinking` blocks | Redacts and encrypts full thinking, returned in a `signature` field |
| Interleaved thinking | Not supported | Supported with a beta header |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
