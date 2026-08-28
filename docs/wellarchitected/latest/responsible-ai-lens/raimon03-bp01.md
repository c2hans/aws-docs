---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon03-bp01.html
---

# RAIMON03-BP01 Establish mechanisms for honoring stakeholder obligations
<a name="raimon03-bp01"></a>

 Consider how to honor obligations you many have to upstream stakeholders (such as people who contributed content to an evaluation or training dataset) and downstream stakeholders (such as workflows that have taken dependencies on your AI system).

 **Level of risk exposed if this best practice is not established:** High

## Implementation considerations
<a name="implementation-considerations-97"></a>

1.  Review your dataset registry to decide the correct way to handle each dataset, for example should it be kept for re-use, kept as a required record, or deleted.

1.  Review logs and customer agreements to identify potential downstream dependents and determine a decommissioning strategy that provides appropriate notice.

## Resources
<a name="resources-93"></a>

 **Related tools:**
+  [Overview of the decommissioning process](https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
