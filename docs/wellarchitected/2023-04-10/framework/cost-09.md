---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/cost-09.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST 9. How do you manage demand, and supply resources?
<a name="cost-09"></a>

For a workload that has balanced spend and performance, verify that everything you pay for is used and avoid significantly underutilizing instances. A skewed utilization metric in either direction has an adverse impact on your organization, in either operational costs (degraded performance due to over-utilization), or wasted AWS expenditures (due to over-provisioning).

**Topics**
+ [COST09-BP01 Perform an analysis on the workload demand](cost_manage_demand_resources_cost_analysis.md)
+ [COST09-BP02 Implement a buffer or throttle to manage demand](cost_manage_demand_resources_buffer_throttle.md)
+ [COST09-BP03 Supply resources dynamically](cost_manage_demand_resources_dynamic.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
