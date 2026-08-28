---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/cell-design.html
---

# Cell design
<a name="cell-design"></a>

 A cell is an instance of your complete workload, with everything needed to operate independently. As an example, consider an application that is comprised by an Application Load Balancer, some EC2 instances, and an Amazon RDS database. In this case, all components are in your cell, for example, `cell 1`. If you need another cell, `cell 2`, you will have to create another deployment of these three components.

 How you define your cell boundaries has a profound impact on the resiliency, cost, and architecture of your workload. We are going to describe some ways to define your cell strategy with its pros and cons.

 In an ideal world, a cell is independent, is unaware of other cells, and does not share its state with other cells. Cells should have no dependency on each other at all (that is, no cross-cell API calls, no shared resources like databases or S3 buckets.) Even the use of separate AWS accounts is encouraged. However, depending on your workload, it is not always possible to maintain these characteristics. Cross-cell dependencies can quickly eliminate the benefits of a cellular architecture, so try to do this as little as possible, or only at specific transitory times.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
