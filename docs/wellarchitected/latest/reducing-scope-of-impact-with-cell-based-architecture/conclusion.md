---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

 Cell-based architecture can bring a higher level of isolation, predictability, and testability to your workload. It is extremely important to understand the trade-offs of using this architectural model and that not all your business workloads are going to require extreme levels of resiliency.

 This guidance focused on workload architecture of cell-based architecture, but one aspect that cannot be overlooked is operational excellence, with cells you now have dozens if not hundreds of replicas of your workload to operate and evolve. All of the operational excellence best practices recommended by the Well-architected framework should have their attention reinforced on workloads that use this architectural style.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
