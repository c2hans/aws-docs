---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/awsbatchcli.awsbstat-v3.html
---

# `awsbstat`
<a name="awsbatchcli.awsbstat-v3"></a>

Shows the jobs that are submitted in the cluster’s job queue.

```
awsbstat [-h] [-c {{CLUSTER}}] [-s {{STATUS}}] [-e] [-d] [{{job_ids}} [{{job_ids}} ...]]
```

## Positional Arguments
<a name="awsbatchcli.awsbstat-v3.arguments"></a>

**{{job\_ids}}**
Specifies the space-separated list of job IDs to show in the output. If the job is a job array, all of the child jobs are displayed. If a single job is requested, it is shown in a detailed version.

## Named Arguments
<a name="awsbatchcli.awsbstat-v3.namedarguments"></a>

**-c {{CLUSTER}}, --cluster {{CLUSTER}}**
Indicates the cluster to use.

**-s {{STATUS}}, --status {{STATUS}}**
Specifies a comma-separated list of job statuses to include. The default job status is “active.”. Accepted values are: `SUBMITTED`, `PENDING`, `RUNNABLE`, `STARTING`, `RUNNING`, `SUCCEEDED`, `FAILED`, and `ALL`.
Default: “`SUBMITTED`,`PENDING`,`RUNNABLE`,`STARTING`,`RUNNING`”

**-e, --expand-children**
Expands jobs with children (both array and multi-node parallel).
Default: False

**-d, --details**
Shows jobs details.
Default: False

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
