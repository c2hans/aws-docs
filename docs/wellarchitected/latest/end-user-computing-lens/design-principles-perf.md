---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/design-principles-perf.html
---

# Design principles
<a name="design-principles-perf"></a>
+  **Minimize latency**: EUC workloads are sensitive to latency. For best performance, minimize the latency between end users and EUC services, as well as between EUC instances and dependencies.
+  **Monitor performance metrics**: Use performance metrics to understand the behavior of both individual instances and the holistic health of your EUC environment. Adjust configurations to meet evolving performance requirements.
+  **Consider mechanical sympathy**: Understand the design goals of AWS EUC services and features and align them with your workload goals. For further information related to mechanical sympathy, see [Consider Mechanical Sympathy](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
