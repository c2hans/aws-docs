---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/multi-node-v3.html
---

# Scenario 3: Spot Instance running multi-node jobs is interrupted
<a name="multi-node-v3"></a>

The job fails with a state code of `NODE_FAIL`, and the job is requeued (unless `--no-requeue` was specified when the job was submitted). If the node is a static node, it's replaced. If the node is a dynamic node, the node is terminated and reset. Other nodes that were running the terminated jobs might be allocated to other pending jobs, or scaled down after the configured [`SlurmSettings`](Scheduling-v3.md#Scheduling-v3-SlurmSettings) / [`ScaledownIdletime`](Scheduling-v3.md#yaml-Scheduling-SlurmSettings-ScaledownIdletime) time has passed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
