---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp01.html
---

# EUCPERF10-BP01 Align the instance type and instance size of a fleet with the workload
<a name="eucperf10-bp01"></a>

 As needed, user environments can be updated on a pre-determined schedule or in response to periodic changes in performance to satisfy a change in the anticipated demand for resources.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-23"></a>

 Determine the optimal instance family and size for your applications.
+  The non-graphics instance families can utilize the same image across them. This provides image portability across these instance families and the instance sizes associated with them and allows varying requirements for compute resources to be catered for.
+  Images created for a graphics instance family (for example, stream.graphics.g5) can only be associated with that family due to the specific GPU drivers for the associated GPU. Consequently, choose a graphics instance family carefully from the outset to avoid the need to create a new image for a different GPU family.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
