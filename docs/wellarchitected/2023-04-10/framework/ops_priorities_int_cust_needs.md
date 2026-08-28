---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_priorities_int_cust_needs.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS01-BP02 Evaluate internal customer needs
<a name="ops_priorities_int_cust_needs"></a>

 Involve key stakeholders, including business, development, and operations teams, when determining where to focus efforts on internal customer needs. This will ensure that you have a thorough understanding of the operations support that is required to achieve business outcomes.

 Use your established priorities to focus your improvement efforts where they will have the greatest impact (for example, developing team skills, improving workload performance, reducing costs, automating runbooks, or enhancing monitoring). Update your priorities as needs change.

 **Common anti-patterns:**
+  You have decided to change IP address allocations for your product teams, without consulting them, to make managing your network easier. You do not know the impact this will have on your product teams.
+  You are implementing a new development tool but have not engaged your internal customers to find out if it is needed or if it is compatible with their existing practices.
+  You are implementing a new monitoring system but have not contacted your internal customers to find out if they have monitoring or reporting needs that should be considered.

 **Benefits of establishing this best practice:** Evaluating and understanding internal customer needs will inform how you prioritize your efforts to deliver business value.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Understand business needs: Business success is created by shared goals and understanding across stakeholders including business, development, and operations teams.
  +  Review business goals, needs, and priorities of internal customers: Engage key stakeholders, including business, development, and operations teams, to discuss goals, needs, and priorities of internal customers. This ensures that you have a thorough understanding of the operational support that is required to achieve business and customer outcomes.
  +  Establish shared understanding: Establish shared understanding of the business functions of the workload, the roles of each of the teams in operating the workload, and how these factors support shared business goals across internal and external customers.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Well-Architected Framework Concepts – Feedback loop](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.feedback-loop.en.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
