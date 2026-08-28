---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_hardware_a2.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS05-BP01 Use the minimum amount of hardware to meet your needs
<a name="sus_sus_hardware_a2"></a>

 Using the capabilities of the cloud, you can make frequent changes to your workload implementations. Update deployed components as your needs change.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Enable horizontal scaling, and use automation to scale out as loads increase and to scale in as loads decrease.
+  Scale using small increments for variable workloads.
+  Align scaling with cyclical utilization patterns (for example, a payroll system with intense bi-weekly processing activities) as load varies over days, weeks, months, or years.
+  Negotiate service level Agreements (SLAs) that allow for a temporary reduction in capacity while automation deploys replacement resources.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Compute Optimizer Documentation](https://docs.aws.amazon.com/compute-optimizer/index.html)
+  [Operating Lambda: Performance optimization](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-2/)
+  [Auto Scaling Documentation](https://docs.aws.amazon.com/autoscaling/index.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
