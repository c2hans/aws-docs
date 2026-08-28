---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/ops_evolve_ops_process_cont_imp.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS11-BP01 Have a process for continuous improvement
<a name="ops_evolve_ops_process_cont_imp"></a>

Evaluate your workload against internal and external architecture best practices. Conduct workload reviews at least once per year. Prioritize improvement opportunities into your software development cadence.

 **Desired outcome:**
+  You analyze your workload against architecture best practices at least yearly.
+  Improvement opportunities are given equal priority in your software development process.

 **Common anti-patterns:**
+ You have not conducted an architecture review on your workload since it was deployed several years ago.
+ Improvement opportunities are given a lower priority and stay in the backlog.
+  There is no standard for implementing modifications to best practices for the organization.

 **Benefits of establishing this best practice:**
+  Your workload is kept up to date on architecture best practices.
+  Evolving your workload is done in a deliberate manner.
+  You can leverage organization best practices to improve all workloads.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 On at least a yearly basis, you conduct an architectural review of your workload. Using internal and external best practices, evaluate your workload and identify improvement opportunities. Prioritize improvement opportunities into your software development cadence.

 **Customer example**

 All workloads at AnyCompany Retail go through a yearly architecture review process. They developed their own checklist of best practices that apply to all workloads. Using the AWS Well-Architected Tool’s Custom Lens feature, they conduct reviews using the tool and their custom lens of best practices. Improvement opportunities generated from the reviews are given priority in their software sprints.

 **Implementation steps**

1.  Conduct periodic architecture reviews of your production workload at least yearly. Use a documented architectural standard that includes AWS-specific best practices.

   1.  We recommend you use your own internally defined standards it for these reviews. If you do not have an internal standard, we recommend you use the AWS Well-Architected Framework.

   1.  You can use the AWS Well-Architected Tool to create a Custom Lens of your internal best practices and conduct your architecture review.

   1.  Customers can contact their AWS Solutions Architect to conduct a guided Well-Architected Framework Review of their workload.

1.  Prioritize improvement opportunities identified during the review into your software development process.

 **Level of effort for the implementation plan:** Low. You can use the AWS Well-Architected Framework to conduct your yearly architecture review.

### Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS11-BP02 Perform post-incident analysis](ops_evolve_ops_perform_rca_process.md) - Post-incident analysis is another generator for improvement items. Feed lessons learned into your internal list of architecture best practices.
+  [OPS11-BP08 Document and share lessons learned](ops_evolve_ops_share_lessons_learned.md) - As you develop your own architecture best practices, share those across your organization.

 **Related documents:**
+ [AWS Well-Architected Tool - Custom lenses ](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-custom.html)
+ [AWS Well-Architected Whitepaper - The review process ](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-review-process.html)
+ [ Customize Well-Architected Reviews using Custom Lenses and the AWS Well-Architected Tool](https://aws.amazon.com/blogs/mt/customize-well-architected-reviews-using-custom-lenses-and-the-aws-well-architected-tool/)
+ [ Implementing the AWS Well-Architected Custom Lens lifecycle in your organization ](https://aws.amazon.com/blogs/architecture/implementing-the-aws-well-architected-custom-lens-lifecycle-in-your-organization/)

 **Related videos:**
+ [ Well-Architected Labs - Level 100: Custom Lenses on AWS Well-Architected Tool](https://www.wellarchitectedlabs.com/well-architectedtool/100_labs/100_custom_lenses_on_watool/)

 **Related examples:**
+ [ The AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
