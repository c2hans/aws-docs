---
source_url: https://docs.aws.amazon.com/wellarchitected/2025-02-25/framework/cost-mandem.html
---

# Manage demand and supply resources
<a name="cost-mandem"></a>

 When you move to the cloud, you pay only for what you need. You can supply resources to match the workload demand at the time they’re needed, this decreases the need for costly and wasteful over provisioning. You can also modify the demand, using a throttle, buﬀer, or queue to smooth the demand and serve it with less resources resulting in a lower cost, or process it at a later time with a batch service.

 In AWS, you can automatically provision resources to match the workload demand. Auto Scaling using demand or time-based approaches permit you to add and remove resources as needed. If you can anticipate changes in demand, you can save more money and validate that your resources match your workload needs. You can use Amazon API Gateway to implement throttling, or Amazon SQS to implementing a queue in your workload. These will both permit you to modify the demand on your workload components.

 The following question focuses on these considerations for cost optimization.

| COST 9:  How do you manage demand, and supply resources? |
| --- |
| For a workload that has balanced spend and performance, verify that everything you pay for is used and avoid significantly underutilizing instances. A skewed utilization metric in either direction has an adverse impact on your organization, in either operational costs (degraded performance due to over-utilization), or wasted AWS expenditures (due to over-provisioning). |

 When designing to modify demand and supply resources, actively think about the patterns of usage, the time it takes to provision new resources, and the predictability of the demand pattern. When managing demand, verify you have a correctly sized queue or buﬀer, and that you are responding to workload demand in the required amount of time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
