---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr01-bp01.html
---

# RAIBR01-BP01 Aggregate beneficial events into intended benefits
<a name="raibr01-bp01"></a>

 Identify the specific beneficial events that could assist each type of downstream stakeholder. Translate these events into specific intended benefits for the use case.

 **Level of risk exposed if this best practice is not established:** High

## Implementation considerations
<a name="implementation-considerations-11"></a>

1.  For each downstream stakeholder, identify examples of system interactions (input and output pairs) that you consider to be beneficial, and group the examples into different categories of benefits.

1.  Score each benefit on impact and likelihood, using your existing knowledge (from the Use Case focus area) about the workflow.

1.  Prioritize the benefits that are critical to your organization's success.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
