---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/cost_data_transfer_modeling.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST08-BP01 Perform data transfer modeling
<a name="cost_data_transfer_modeling"></a>

 Gather organization requirements and perform data transfer modeling of the workload and each of its components. This identifies the lowest cost point for its current data transfer requirements.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Understand where the data transfer occurs in your workload, the cost of the transfer, and its associated benefit. This allows you to make an informed decision to modify or accept the architectural decision. For example, you may have a Multi-Availability Zone configuration where you replicate data between the Availability Zones. You model the cost of structure and decide that this is an acceptable cost (similar to paying for compute and storage in both Availability Zone) to achieve the required reliability and resilience.

Model the costs over different usage levels. Workload usage can change over time, and different services may be more cost effective at different levels.

Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) or the [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) (CUR) to understand and model your data transfer costs. Configure a proof of concept (PoC) or test your workload, and run a test with a realistic simulated load. You can model your costs at different workload demands.

**Implementation steps**
+ ** Calculate data transfer costs: **Use the [AWS pricing pages](https://aws.amazon.com/pricing/) and calculate the data transfer costs for the workload. Calculate the data transfer costs at different usage levels, for both increases and reductions in workload usage. Where there are multiple options for the workload architecture, calculate the cost for each option for comparison.
+ ** Link costs to outcomes:** For each data transfer cost incurred, specify the outcome that it achieves for the workload. If it is transfer between components, it may be for decoupling, if it is between Availability Zones it may be for redundancy.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS caching solutions](https://aws.amazon.com/caching/aws-caching/)
+  [AWS Pricing](https://aws.amazon.com/pricing/)
+  [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)
+  [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/)
+  [Deliver content faster with Amazon CloudFront](https://aws.amazon.com/getting-started/tutorials/deliver-content-faster/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
