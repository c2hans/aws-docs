---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/prompting-tools.html
---

# Use external tools
<a name="prompting-tools"></a>

Amazon Nova understanding models can be integrated with external tools and systems to enhance their capabilities and have the models complete real world tasks. Such tasks include grounding the model with accurate context by building your own Retrieval Augmented Generation (RAG) system or leveraging tool calling systems to build your own orchestration system.

The utilization of external tools is a core building block of agentic systems and the optimization of how you define those tools has a high impact on the accuracy of the system.

The following sections will walk through how you can optimize tools for different common use cases.

**Topics**
+ [Build your own RAG](prompting-tools-rag.md)
+ [Tool calling systems](prompting-tools-function.md)
+ [Troubleshooting tool calls](prompting-tool-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
