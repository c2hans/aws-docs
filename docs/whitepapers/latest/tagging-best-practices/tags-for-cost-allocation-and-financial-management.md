---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tags-for-cost-allocation-and-financial-management.html
---

# Tags for cost allocation and financial management
<a name="tags-for-cost-allocation-and-financial-management"></a>

 One of the first tagging use cases organizations often tackle is visibility and management of cost and usage. There are usually a few reasons for this:
+  **It's typically a well understood scenario and requirements are well known.** For example, finance teams want to see the total cost of workloads and infrastructure that span across multiple services, features, accounts, or teams. One way to achieve this cost visibility is through consistent tagging of resources.
+  **Tags and their values are clearly defined.** Usually, cost allocation mechanisms already exist in an organization’s finance systems, for example, tracking by cost center, business unit, team, or organization function.
+  **Rapid, demonstrable return on investment.** It’s possible to track cost optimization trends over time when resources are tagged consistently, for example, for resources that were rightsized, auto-scaled, or put on a schedule.

 Understanding how you incur costs in AWS allows you to make informed financial decisions. Knowing where you have incurred costs at the resource, workload, team, or organization level enhances your understanding of the value delivered at the applicable level when compared to the business outcomes achieved.

 The engineering teams might not have experience with financial management of their resources. Attaching a person with a specialized skill in AWS financial management who can train engineering and development teams on the basics of AWS financial management and create a relationship between finance and engineering to foster the culture of FinOps will help achieve measurable outcomes for the business and encourage teams to build with cost in mind. Establishing good financial practices is covered in depth by the [Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) of the Well-Architected Framework, but we will touch on a few of the fundamental principles in this whitepaper.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
