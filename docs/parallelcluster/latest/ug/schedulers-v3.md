---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/schedulers-v3.html
---

# Schedulers supported by AWS ParallelCluster
<a name="schedulers-v3"></a>

 AWS ParallelCluster supports Slurm and AWS Batch schedulers, which are set using the [`Scheduler`](Scheduling-v3.md#yaml-Scheduling-Scheduler) setting. The following topics will describe each scheduler and how to use them. Starting with AWS ParallelCluster version 3.16.0, AWS Batch as a scheduler is no longer supported.

**Topics**
+ [Slurm Workload Manager (`slurm`)](slurm-workload-manager-v3.md)
+ [Using AWS Batch (`awsbatch`) scheduler with AWS ParallelCluster](awsbatchcli-v3.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
