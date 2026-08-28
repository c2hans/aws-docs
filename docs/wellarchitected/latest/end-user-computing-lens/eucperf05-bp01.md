---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp01.html
---

# EUCPERF05-BP01 Understand your existing storage requirements, policies, and solutions
<a name="eucperf05-bp01"></a>

 If your EUC workload already uses storage volumes, operations policies, and vendor solutions, make sure that you not only understand what products and services they are based on, but also identify the features, advantages, and benefits associated with each in your existing workload. Decide whether these are best suited to your applications and technical goals. Otherwise, develop a set of new functional requirements and solutions that will better address your requirements.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-10"></a>

 Begin by understanding the storage requirements for each use case. Relevant requirements include the following:
+  Individual file size
+  Total data size
+  Average and peak IOPS
+  Whether storage is per-user or shared
+  File and folder permissions

 Also, consider organizational policies and existing solutions (for example, if policy dictates that users store all files in a central repository).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
