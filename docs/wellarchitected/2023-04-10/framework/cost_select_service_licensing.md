---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/cost_select_service_licensing.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST05-BP04 Select software with cost-effective licensing
<a name="cost_select_service_licensing"></a>

 Open-source software eliminates software licensing costs, which can contribute significant costs to workloads. Where licensed software is required, avoid licenses bound to arbitrary attributes such as CPUs, look for licenses that are bound to output or outcomes. The cost of these licenses scales more closely to the benefit they provide.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

The cost of software licenses can be eliminated through the use of open-source software. This can have significant impact on workload costs as the size of the workload scales. Measure the benefits of licensed software against the total cost to ensure that you have the most optimized workload. Model any changes in licensing and how they would impact your workload costs. If a vendor changes the cost of your database license, investigate how that impacts the overall efficiency of your workload. Consider historical pricing announcements from your vendors for trends of licensing changes across their products. Licensing costs may also scale independently of throughput or usage, such as licenses that scale by hardware (CPU-bound licenses). These licenses should be avoided because costs can rapidly increase without corresponding outcomes.

**Implementation steps**
+ ** Analyze license options: **Review the licensing terms of available software. Look for open-source versions that have the required functionality, and whether the benefits of licensed software outweigh the cost. Favorable terms will align the cost of the software to the benefit it provides.
+ ** Analyze the software provider: **Review any historical pricing or licensing changes from the vendor. Look for any changes that do not align to outcomes, such as punitive terms for running on specific vendors hardware or platforms. Additionally look for how they run audits, and penalties that could be imposed.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Total Cost of Ownership (TCO) Calculator](https://aws.amazon.com/tco-calculator/)
+  [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/)
+  [Cloud products](https://aws.amazon.com/products/)
