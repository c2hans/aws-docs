---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/reasoning-capabilities.html
---

# Reasoning capabilities
<a name="reasoning-capabilities"></a>

Amazon Nova 2 Lite supports extended thinking, which is disabled by default. When enabled, the model generates internal reasoning tokens that improve response quality. In Amazon Nova 2 Lite, reasoning content is redacted in the output and displays as `[REDACTED]`, though you are still charged for these tokens.

The reasoning field is included in the response structure to preserve the option of exposing this content in future releases. For more information about extended thinking, see [Extended thinking in Amazon Nova 2](extended-thinking.md) and [Code library](code-library.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
