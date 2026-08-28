---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/cost_select_service_analyze_all.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST05-BP02 Analyze all components of the workload
<a name="cost_select_service_analyze_all"></a>

|  |
| --- |
| This best practice was updated with new guidance on December 6, 2023. |

 Verify every workload component is analyzed, regardless of current size or current costs. The review effort should reflect the potential benefit, such as current and projected costs.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Workload components, which are designed to deliver business value to the organization, may encompass various services. For each component, one might choose specific AWS Cloud services to address business needs. This selection could be influenced by factors such as familiarity with or prior experience using these services.

 After identifying your organization’s requirements (as mentioned in [COST05-BP01 Identify organization requirements for cost](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_requirements.html)), perform a thorough analysis on all components in your workload. Analyze each component considering current and projected costs and sizes. Consider the cost of analysis against any potential workload savings over its lifecycle. The effort expended on analyzing all components of this workload should correspond to the potential savings or improvements anticipated from optimizing that specific component. For example, if the cost of the proposed resource is $10 per month, and under forecasted loads would not exceed $15 per month, spending a day of effort to reduce costs by 50% (five dollars per month) could exceed the potential benefit over the life of the system. Using a faster and more efficient data-based estimation creates the best overall outcome for this component.

 Workloads can change over time, and the right set of services may not be optimal if the workload architecture or usage changes. Analysis for selection of services must incorporate current and future workload states and usage levels. Implementing a service for future workload state or usage may reduce overall costs by reducing or removing the effort required to make future changes. For example, using Amazon EMR Serverless might be the appropriate choice initially. However, as consumption for that service increases, transitioning to Amazon EMR on Amazon EC2 could reduce costs for that component of the workload.

 Strategic review of all workload components, irrespective of their present attributes, has the potential to bring about notable enhancements and financial savings over time. The effort invested in this review process should be deliberate, with careful consideration of the potential advantages that might be realized.

 [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and the [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) (CUR) can analyze the cost of a Proof of Concept (PoC) or running environment. You can also use [AWS Pricing Calculator](https://calculator.aws/#/) to estimate workload costs.

### Implementation steps
<a name="implementation-steps"></a>
+  **List the workload components:** Build a list of your workload’s components. This is used as verification to check that each component was analyzed. The effort spent should reflect the criticality to the workload as defined by your organization’s priorities. Grouping together resources functionally improves efficiency (for example production database storage, if there are multiple databases).
+  **Prioritize component list:** Take the component list and prioritize it in order of effort. This is typically in order of the cost of the component, from most expensive to least expensive, or the criticality as defined by your organization’s priorities.
+ ** Perform the analysis:** For each component on the list, review the options and services available, and chose the option that aligns best with your organizational priorities.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Pricing Calculator](https://calculator.aws/#/)
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
+  [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/)
+  [Cloud products](https://aws.amazon.com/products/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
