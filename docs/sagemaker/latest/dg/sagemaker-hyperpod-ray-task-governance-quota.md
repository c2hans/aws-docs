---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-task-governance-quota.html
---

# Quota and scheduling behavior for Ray workloads
<a name="sagemaker-hyperpod-ray-task-governance-quota"></a>

Task Governance accounts quota at `RayCluster` granularity. A cluster reserves quota for its full declared size when it is admitted, and holds that quota for its whole lifetime regardless of load. A long-lived cluster that sits idle still counts against your team quota until you delete it.

## Gang scheduling
<a name="sagemaker-hyperpod-ray-task-governance-quota-gang"></a>

Task Governance admits the head and all workers together. A `RayCluster` is not admitted until quota exists for the entire declared size, so a partially scheduled cluster never starts.

## Preemption
<a name="sagemaker-hyperpod-ray-task-governance-quota-preemption"></a>

When higher-priority work needs capacity, Task Governance preempts a lower-priority Ray workload. Preemption deletes the whole cluster, including the head.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
