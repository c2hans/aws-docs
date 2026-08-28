---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr04-bp01.html
---

# RAIBR04-BP01 Narrow the use case
<a name="raibr04-bp01"></a>

 Identify the minimum viable use case that still delivers meaningful business value while reducing complexity and associated risks. Narrow the use case to a specific domain, industry vertical, geography, or user segment rather than attempting to solve broad, general problems. Restrict the types of inputs your system accepts and the formats of outputs it generates.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation considerations
<a name="implementation-considerations-24"></a>

1.  Evaluate current scope and identify risk reduction opportunities. For example, an AI medical diagnosis system might focus on a specific condition type rather than general diagnostics or limit analysis to structured lab results rather than free-text notes.

1.  Define specific boundaries for system application. As an example, a financial AI advisor might serve only retail investors within certain portfolio sizes, using standardized investment products rather than complex instruments. Consider expertise requirements.

1.  Document input and output restrictions to control risk exposure. Consider a customer service AI that accepts only structured inputs rather than free-text queries, which improves response reliability. Include clear guidance on system limitations and context for appropriate use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
