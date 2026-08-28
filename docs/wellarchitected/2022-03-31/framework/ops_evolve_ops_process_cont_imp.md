---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_evolve_ops_process_cont_imp.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS11-BP01 Have a process for continuous improvement
<a name="ops_evolve_ops_process_cont_imp"></a>

 Regularly evaluate and prioritize opportunities for improvement to focus efforts where they can provide the greatest benefits.

 **Common anti-patterns:**
+  You have documented the procedures necessary to create a development or testing environment. You could use CloudFormation to automate the process, but instead you do it manually from the console.
+  Your testing shows that the vast majority of CPU utilization inside your application is in a small set of inefficient functions. You could focus on improving them and reduce your costs but you have been tasked to create a new usability feature.

 **Benefits of establishing this best practice:** Continual improvement provides a mechanism to regularly evaluate opportunities for improvement, prioritize opportunities, and focus efforts where they can provide the greatest benefits.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Define processes for continuous improvement: Regularly evaluate and prioritize opportunities for improvement to focus efforts where they provide the greatest benefits. Implement changes to improve and evaluate the outcomes to determine success. If the outcomes do not satisfy the goals, and the improvement is still a priority, iterate using alternative courses of action. Your operations processes should include dedicated time and resources to make continuous incremental improvements possible.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
