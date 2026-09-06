---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_evaluate_new_services_review_workload.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST10-BP02 Review and analyze this workload regularly
<a name="cost_evaluate_new_services_review_workload"></a>

 Existing workloads are regularly reviewed based on for each defined processes.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

To realize the benefits of new AWS services and features, you must execute the review process on your workloads and implement new services and features as required. For example, you might review your workloads and replace the messaging component with Amazon Simple Email Service (Amazon SES). This removes the cost of operating and maintaining a fleet of instances, while providing all the functionality at a reduced cost.

**Implementation steps**
+ ** Regularly review the workload: **Using your defined process, perform reviews with the frequency specified. Verify that you spend the correct amount of effort on each component. This process would be similar to the initial design process where you selected services for cost optimization. Analyze the services and the benefits they would bring, this time factor in the cost of making the change, not just the long-term benefits.
+ ** Implement new services:** If the outcome of the analysis is to implement changes, first perform a baseline of the workload to know the current cost for each output. Implement the changes, then perform an analysis to confirm the new cost for each output.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS News Blog](https://aws.amazon.com/blogs/aws/)
+  [Types of Cloud Computing](https://aws.amazon.com/types-of-cloud-computing/)
+  [What's New with AWS](https://aws.amazon.com/new/)
