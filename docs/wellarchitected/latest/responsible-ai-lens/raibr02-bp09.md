---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr02-bp09.html
---

# RAIBR02-BP09 Choose multiple strategies to identify potential harmful events
<a name="raibr02-bp09"></a>

 In addition to assessing potential harmful events for each responsible AI dimension independently, employ complementary strategies to identify potentially harmful events and negative stakeholder impact within the context of different use environments. Check for these events at different steps of using the AI system and under different failure modes, which includes both technical failures and misuse or abuse of the AI system. Additional strategies include scenario-based analyses, system limitation assessments that surface operational constraints, choosing a risk team with diverse backgrounds, consulting with external stakeholders, and reviewing historical incidents or risk assessment results from similar systems.

 **Level of risk exposed if this best practice is not established:** High

## Implementation considerations
<a name="implementation-considerations-19"></a>

1.  Choose which strategies are appropriate to use for your design and development process and assign owners to track the progress and iterations of each employed scenario.

1.  Establish a standardized documentation process for recording identified harmful events across different contexts.

1.  Implement regular review cycles to reassess potential harms as the system evolves and establish feedback channels for continuous input from diverse team members and external stakeholders.

## Resources
<a name="resources-18"></a>

 **Related documents**
+  [Learn how to assess the risk of AI systems](https://aws.amazon.com/blogs/machine-learning/learn-how-to-assess-risk-of-ai-systems/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
