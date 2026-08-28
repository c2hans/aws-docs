---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sus_sus_user_a3.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS02-BP02 Align SLAs with sustainability goals
<a name="sus_sus_user_a3"></a>

 Review and optimize workload service-level agreements (SLA) based on your sustainability goals to minimize the resources required to support your workload while continuing to meet business needs.

 **Common anti-patterns:**
+  Workload SLAs are unknown or ambiguous.
+  You define your SLA just for availability and performance.
+  You use the same design pattern (like Multi-AZ architecture) for all your workloads.

 **Benefits of establishing this best practice:** Aligning SLAs with sustainability goals leads to optimal resource usage while meeting business needs.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 SLAs define the level of service expected from a cloud workload, such as response time, availability, and data retention. They influence the architecture, resource usage, and environmental impact of a cloud workload. At a regular cadence, review SLAs and make trade-offs that significantly reduce resource usage in exchange for acceptable decreases in service levels.

 **Implementation steps**
+  Define or redesign SLAs that support your sustainability goals while meeting your business requirements, not exceeding them.
+  Make trade-offs that significantly reduce sustainability impacts in exchange for acceptable decreases in service levels.
  +  **Sustainability and reliability:** Highly available workloads tend to consume more resources.
  +  **Sustainability and performance:** Using more resources to boost performance could have a higher environmental impact.
  +  **Sustainability and security:** Overly secure workloads could have a higher environmental impact.
+  Use design patterns such as [microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html) that prioritize business-critical functions and allow lower service levels (such as response time or recovery time objectives) for non-critical functions.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Service Level Agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/?aws-sla-cards.sort-by=item.additionalFields.serviceNameLower&aws-sla-cards.sort-order=asc&awsf.tech-category-filter=*all)
+  [Importance of Service Level Agreement for SaaS Providers](https://aws.amazon.com/blogs/apn/importance-of-service-level-agreement-for-saas-providers/)

 **Related videos:**
+ [ Delivering sustainable, high-performing architectures ](https://www.youtube.com/watch?v=FBc9hXQfat0)
+ [ Build a cost-, energy-, and resource-efficient compute environment ](https://www.youtube.com/watch?v=8zsC5e1eLCg)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
