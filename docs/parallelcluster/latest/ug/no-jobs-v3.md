---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/no-jobs-v3.html
---

# Scenario 1: Spot Instance with no running jobs is interrupted
<a name="no-jobs-v3"></a>

When this interruption occurs, AWS ParallelCluster tries to replace the instance if the scheduler queue has pending jobs that require additional instances, or if the number of active instances is lower than the [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`ComputeResources`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources) / [`MinCount`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-MinCount). If AWS ParallelCluster can't provision new instances, then a request for new instances is periodically repeated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
