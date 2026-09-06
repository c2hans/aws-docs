---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_select_service_analyze_all.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST05-BP02 Analyze all components of the workload
<a name="cost_select_service_analyze_all"></a>

 Verify every workload component is analyzed, regardless of current size or current costs. The review effort should reflect the potential benefit, such as current and projected costs.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

Perform a thorough analysis on all components in your workload. Ensure that balance between the cost of analysis and the potential savings in the workload over its lifecycle. You must find the current impact, and potential future impact, of the component. For example, if the cost of the proposed resource is $10 a month, and under forecasted loads would not exceed $15 a month, spending a day of effort to reduce costs by 50% ($5 a month) could exceed the potential benefit over the life of the system. Using a faster and more efficient data-based estimation will create the best overall outcome for this component.

Workloads can change over time, and the right set of services may not be optimal if the workload architecture or usage changes. Analysis for selection of services must incorporate current and future workload states and usage levels. Implementing a service for future workload state or usage may reduce overall costs by reducing or removing the effort required to make future changes.

[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and the [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) (CUR) can analyze the cost of a Proof of Concept (PoC) or running environment. You can also use [AWS Pricing Calculator](https://calculator.aws/#/) to estimate workload costs.

**Implementation steps**
+  **List the workload components: **Build the list of all the workload components. This is used as verification to check that each component was analyzed. The effort spent should reflect the criticality to the workload as defined by your organization’s priorities. Grouping together resources functionally improves efficiency, for example production database storage, if there are multiple databases.
+  **Prioritize component list:** Take the component list and prioritize it in order of effort. This is typically in order of the cost of the component from most expensive to least expensive, or the criticality as defined by your organization’s priorities.
+ ** Perform the analysis:** For each component on the list, review the options and services available and chose the option that aligns best with your organizational priorities.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Pricing Calculator](https://calculator.aws/#/)
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
+  [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/)
+  [Cloud products](https://aws.amazon.com/products/)
