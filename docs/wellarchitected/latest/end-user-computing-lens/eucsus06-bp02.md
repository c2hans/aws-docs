---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus06-bp02.html
---

# EUCSUS06-BP02 Implement the Cost Optimizer for Amazon WorkSpaces
<a name="eucsus06-bp02"></a>

 The [Cost Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/) analyzes your Amazon WorkSpaces usage data and automatically converts the WorkSpace to the most cost-effective billing option (hourly or monthly), depending on your individual usage.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-101"></a>

 This solution analyzes your Amazon WorkSpaces usage data and automatically converts WorkSpaces to the most cost-effective billing option (hourly or monthly). This verifies that the lowest carbon footprint and cost is associated with each individual WorkSpace instance based on the unique usage pattern for each user. This data provides the opportunity to identify usage of WorkSpaces and delete unused WorkSpaces through the definition of a rule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
