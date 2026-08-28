---
source_url: https://docs.aws.amazon.com/claude-platform/latest/userguide/models.html
---

# Available models
<a name="models"></a>

Claude Platform on AWS offers the same set of Claude models as the first-party Claude API.

For the current list of models, model IDs, context window sizes, and capabilities, see [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) in the Anthropic documentation.

## Model IDs
<a name="_model_ids"></a>

Model IDs on Claude Platform on AWS are identical to those used on the first-party Claude API (for example, `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-haiku-4-5`). There are no Bedrock-style ARNs or `anthropic.` prefixes — use the model ID exactly as Anthropic publishes it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Claude Platform on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query claude-platform` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
