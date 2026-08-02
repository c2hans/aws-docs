---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_select_service_analyze_over_time.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST05-BP06 Perform cost analysis for different usage over time
<a name="cost_select_service_analyze_over_time"></a>

 Workloads can change over time. Some services or features are more cost effective at different usage levels. By performing the analysis on each component over time and at projected usage, the workload remains cost-effective over its lifetime.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

As AWS releases new services and features, the optimal services for your workload may change. Effort required should reflect potential benefits. Workload review frequency depends on your organization requirements. If it is a workload of significant cost, implementing new services sooner will maximize cost savings, so more frequent review can be advantageous. Another trigger for review is change in usage patterns. Significant changes in usage can indicate that alternate services would be more optimal. For example, for higher data transfer rates a direct connect service may be cheaper than a VPN, and provide the required connectivity. Predict the potential impact of service changes, so you can monitor for these usage level triggers and implement the most cost-effective services sooner.

**Implementation steps**
+ ** Define predicted usage patterns: **Working with your organization, such as marketing and product owners, document what the expected and predicted usage patterns will be for the workload.
+ ** Perform cost analysis at predicted usage:** Using the usage patterns defined, perform the analysis at each of these points. The analysis effort should reflect the potential outcome. For example, if the change in usage is large, a thorough analysis should be performed to verify any costs and changes.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Total Cost of Ownership (TCO) Calculator](https://aws.amazon.com/tco-calculator/)
+  [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/)
+  [Cloud products](https://aws.amazon.com/products/)
