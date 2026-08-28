---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp05.html
---

# EUCPERF10-BP05 Tune application performance where possible to optimize compute resource usage
<a name="eucperf10-bp05"></a>

 To provide the optimal access to compute resource for your applications, consider tuning the performance of applications or software where possible to reduce their compute resource utilization.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-27"></a>

 By reducing the compute resource utilization for software used to provide non-end user facing functionality, such as security agents, additional resources are made available to benefit the applications users interact with. The disabling of non-essential functionality within software can yield a performance benefit for end user software.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
