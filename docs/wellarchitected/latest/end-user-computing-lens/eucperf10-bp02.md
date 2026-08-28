---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp02.html
---

# EUCPERF10-BP02 Enable self-service WorkSpaces Personal management capabilities, and allow users to request changes by an administrator
<a name="eucperf10-bp02"></a>

 The WorkSpaces Personal self-service options allow users to ramp up or down instance performance over time.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-24"></a>

 Enable user self-service where possible to optimize processes.
+  Identify the most flexible compute types for users to anticipate required changes in performance. Consider the following:
  +  You can change the compute type from Graphics.g4dn to GraphicsPro.g4dn, or from GraphicsPro.g4dn to Graphics.g4dn.
  +  However, you cannot change the compute type of Graphics.g4dn and GraphicsPro.g4dn to other types.
  +  You cannot change the compute type of Graphics and GraphicsPro to another type.
+  Consider these capabilities and limitations when initially configuring your users' environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
