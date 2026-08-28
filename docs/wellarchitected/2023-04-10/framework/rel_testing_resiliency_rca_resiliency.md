---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_testing_resiliency_rca_resiliency.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL12-BP02 Perform post-incident analysis
<a name="rel_testing_resiliency_rca_resiliency"></a>

 Review customer-impacting events, and identify the contributing factors and preventative action items. Use this information to develop mitigations to limit or prevent recurrence. Develop procedures for prompt and effective responses. Communicate contributing factors and corrective actions as appropriate, tailored to target audiences. Have a method to communicate these causes to others as needed.

 Assess why existing testing did not find the issue. Add tests for this case if tests do not already exist.

 **Common anti-patterns:**
+  Finding contributing factors, but not continuing to look deeper for other potential problems and approaches to mitigate.
+  Only identifying human error causes, and not providing any training or automation that could prevent human errors.

 **Benefits of establishing this best practice:** Conducting post-incident analysis and sharing the results permits other workloads to mitigate the risk if they have implemented the same contributing factors, and allows them to implement the mitigation or automated recovery before an incident occurs.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Establish a standard for your post-incident analysis. Good post-incident analysis provides opportunities to propose common solutions for problems with architecture patterns that are used in other places in your systems.
  +  Ensure that the contributing factors are honest and blame free.
  +  If you do not document your problems, you cannot correct them.
    +  Ensure post-incident analysis is blame free so you can be dispassionate about the proposed corrective actions and promote honest self-assessment and collaboration on your application teams.
+  Use a process to determine contributing factors. Have a process to identify and document the contributing factors of an event so that you can develop mitigations to limit or prevent recurrence and you can develop procedures for prompt and effective responses. Communicate contributing factors as appropriate, tailored to target audiences.
  +  [What is log analytics?](https://aws.amazon.com/log-analytics/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [What is log analytics?](https://aws.amazon.com/log-analytics/)
+  [Why you should develop a correction of error (COE)](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
