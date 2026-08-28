---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/cost-effective-resources.html
---

# Cost-effective resources
<a name="cost-effective-resources"></a>

| COST 1: How do you optimize your costs?  |
| --- |
|   |

Serverless architectures are easier to manage in terms of correct resource allocation. Due to its pay-per-value pricing model and scale based on demand, serverless effectively reduces the capacity planning effort.

 As covered in the operational excellence and performance pillars, optimizing your serverless application has a direct impact on the value it produces and its cost.

 As Lambda proportionally allocates CPU, network, and storage IOPS based on memory, the faster the initiation, the cheaper and more value your function produces due to 1-ms billing incremental dimension.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
