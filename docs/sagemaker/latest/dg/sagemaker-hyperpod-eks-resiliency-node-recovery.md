---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-node-recovery.html
---

# Automatic node recovery
<a name="sagemaker-hyperpod-eks-resiliency-node-recovery"></a>

During cluster creation or update, cluster admin users can select the node (instance) recovery option between `Automatic` (Recommended) and `None` at the cluster level. If set to `Automatic`, SageMaker HyperPod reboots or replaces faulty nodes automatically.

**Important**
We recommend setting the `Automatic` option.

Automatic node recovery runs when issues are found from health-monitoring agent, basic health checks, and deep health checks. If set to `None`, the health monitoring agent will label the instances when a fault is detected, but it will not automatically initiate any repair or recovery actions on the affected nodes. This option is not recommended.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
