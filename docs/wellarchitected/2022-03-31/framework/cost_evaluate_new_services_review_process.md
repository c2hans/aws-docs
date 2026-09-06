---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_evaluate_new_services_review_process.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST10-BP01 Develop a workload review process
<a name="cost_evaluate_new_services_review_process"></a>

 Develop a process that defines the criteria and process for workload review. The review effort should reflect potential benefit. For example, core workloads or workloads with a value of over 10% of the bill are reviewed quarterly, while workloads below 10% are reviewed annually.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

To ensure that you always have the most cost-efficient workload, you must regularly review the workload to know if there are opportunities to implement new services, features, and components. To ensure that you achieve overall lower costs the process must be proportional to the potential amount of savings. For example, workloads that are 50% of your overall spend should be reviewed more regularly, and more thoroughly, than workloads that are 5% of your overall spend. Factor in any external factors or volatility. If the workload services a specific geography or market segment, and change in that area is predicted, more frequent reviews could lead to cost savings. Another factor in review is the effort to implement changes. If there are significant costs in testing and validating changes, reviews should be less frequent.

Factor in the long-term cost of maintaining outdated and legacy, components and resources, and the inability to implement new features into them. The current cost of testing and validation may exceed the proposed benefit. However, over time, the cost of making the change may significantly increase as the gap between the workload and the current technologies increases, resulting in even larger costs. For example, the cost of moving to a new programming language may not currently be cost effective. However, in five years time, the cost of people skilled in that language may increase, and due to workload growth, you would be moving an even larger system to the new language, requiring even more effort than previously.

Break down your workload into components, assign the cost of the component (an estimate is sufficient), and then list the factors (for example, effort and external markets) next to each component. Use these indicators to determine a review frequency for each workload. For example, you may have webservers as a high cost, low change effort, and high external factors, resulting in high frequency of review. A central database may be medium cost, high change effort, and low external factors, resulting in a medium frequency of review.

**Implementation steps**
+  **Define review frequency: **Define how frequently the workload and its components should be reviewed. This is a combination of factors and may differ from workload to workload within your organization, it may also differ between components in the workload. Common factors include the importance to the organization measured in terms of revenue or brand, the total cost of running the workload (including operation and resource costs), the complexity of the workload, how easy is it to implement a change, any software licensing agreements, and if a change would incur significant increases in licensing costs due to punitive licensing. Components can be defined functionally or technically, such as web servers and databases, or compute and storage resources. Balance the factors accordingly and develop a period for the workload and its components. You may decide to review the full workload every 18 months, review the web servers every 6 months, the database every 12 months, compute and short-term storage every 6 months, and long-term storage every 12 months.
+ ** Define review thoroughness: **Define how much effort is spent on the review of the workload or workload components. Similar to the review frequency, this is a balance of multiple factors. You may decide to spend one week of analysis on the database component, and four hours for storage reviews.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS News Blog](https://aws.amazon.com/blogs/aws/)
+  [Types of Cloud Computing](https://aws.amazon.com/types-of-cloud-computing/)
+  [What's New with AWS](https://aws.amazon.com/new/)
