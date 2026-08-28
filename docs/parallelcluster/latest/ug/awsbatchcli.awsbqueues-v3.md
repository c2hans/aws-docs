---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/awsbatchcli.awsbqueues-v3.html
---

# `awsbqueues`
<a name="awsbatchcli.awsbqueues-v3"></a>

Shows the job queue that is associated with the cluster.

```
awsbqueues [-h] [-c {{CLUSTER}}] [-d] [{{job_queues}} [{{job_queues}} ... ]]
```

## Positional arguments
<a name="awsbatchcli.awsbqueues-v3.arguments"></a>

**{{job\_queues}}**
Specifies the space-separated list of queue names to show. If a single queue is requested, it is shown in a detailed version.

## Named arguments
<a name="awsbatchcli.awsbqueues-v3.namedarguments"></a>

**-c {{CLUSTER}}, --cluster {{CLUSTER}}**
Specifies the name of the cluster to use.

**-d, --details**
Indicates whether to show the details of the queues.
Default: False

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
