---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr04-bp03.html
---

# RAIBR04-BP03 Assign your potential harm mitigations to implementation strategies
<a name="raibr04-bp03"></a>

 As input to your system design, consider whether potential harms can be addressed through technical features or stakeholder guidance.

 **Level of risk exposed if this best practice is not established:** High

## Implementation considerations
<a name="implementation-considerations-26"></a>

1.  Categorize your mitigations into implementation strategies that are either built into the system (a part of the core AI system or resolved with filtering of inputs and outputs) or addressed through guidance. For example, a healthcare chatbot might reduce the risk of incorrectly responding to requests for legal advice by either customizing the underlying model or guardrails, or by warning users not to request legal advice, or both.

## Resources
<a name="resources-24"></a>

 **Related documents:**
+  [Learn how to assess the risk of AI systems](https://aws.amazon.com/blogs/machine-learning/learn-how-to-assess-risk-of-ai-systems/)
+  [Responsible AI in the generative era](https://www.amazon.science/blog/responsible-ai-in-the-generative-era)
+  [NIST Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
