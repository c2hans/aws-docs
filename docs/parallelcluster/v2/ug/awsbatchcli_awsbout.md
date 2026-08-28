---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli_awsbout.html
---

# `awsbout`
<a name="awsbatchcli_awsbout"></a>

Shows the output of a given job.

```
awsbout [ - h ] [ - c {{CLUSTER}} ] [ - hd {{HEAD}} ] [ - t {{TAIL}} ] [ - s ] [ - sp {{STREAM_PERIOD}} ] {{job_id}}
```

## Positional Arguments
<a name="awsbatchcli.awsbout.arguments"></a>

**{{job\_id}}**
Specifies the job ID.

## Named Arguments
<a name="awsbatchcli.awsbout.namedarguments"></a>

**-c {{CLUSTER}}, --cluster {{CLUSTER}}**
Indicates the cluster to use.

**-hd {{HEAD}}, --head {{HEAD}}**
Gets the first {{HEAD}} lines of the job output.

**-t {{TAIL}}, --tail {{TAIL}}**
Gets the last <tail> lines of the job output.

**-s, --stream**
Gets the job output, and then waits for additional output to be produced. This argument can be used together with –tail to start from the latest <tail> lines of the job output.
Default: False

**-sp {{STREAM\_PERIOD}}, --stream-period {{STREAM\_PERIOD}}**
Sets the streaming period.
Default: 5

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
