---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/awsbatchcli.awsbkill-v3.html
---

# `awsbkill`
<a name="awsbatchcli.awsbkill-v3"></a>

Cancels or terminates jobs submitted in the cluster.

```
awsbkill [-h] [-c {{CLUSTER}}] [-r {{REASON}}] {{job_ids}} [{{job_ids}} ... ]
```

## Positional Arguments
<a name="awsbatchcli.awsbkill-v3.arguments"></a>

**{{job\_ids}}**
Specifies the space-separated list of job IDs to cancel or terminate.

## Named Arguments
<a name="awsbatchcli.awsbkill-v3.namedarguments"></a>

**-c {{CLUSTER}}, --cluster {{CLUSTER}}**
Indicates the name of the cluster to use.

**-r {{REASON}}, --reason {{REASON}}**
Indicates the message to attach to a job, explaining the reason for canceling it.
Default: “Terminated by the user”

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
