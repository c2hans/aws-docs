---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp01-bp03.html
---

# RAISP01-BP03 Check if design choices have introduced new risks
<a name="raisp01-bp03"></a>

 Review how design decisions affect the risk profile, determining whether additional assessment criteria must be incorporated into the testing framework.

 For example, choosing to use a third-party component instead of building your own solution might introduce new risk considerations. When you identify new risks or changes in risk likelihood, decide if you need to update your release criteria to properly test for these issues before release.

 **Level of risk exposed if this best practice is not established:** High

## Implementation considerations
<a name="implementation-considerations-63"></a>

1.  Review the AI system document, design decisions and tradeoffs for each component.

1.  Determine if the design decisions result in new risks or updates to already identified risks in terms of severity and likelihood.

1.  Update the risk assessment accordingly.

1.  Review the release criteria and determine if the release criteria sufficiently covers the identified risks.

1.  Update the release criteria accordingly.

## Resources
<a name="resources-60"></a>

 **Related documents:**
+  [ISO/IEC 42001:2023 A.6.2.3 Documentation of AI system design and development](https://www.iso.org/standard/42001)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
