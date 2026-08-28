---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli_awsbhosts.html
---

# `awsbhosts`
<a name="awsbatchcli_awsbhosts"></a>

Shows the hosts that belong to the cluster’s compute environment.

```
awsbhosts [ - h ] [ - c {{CLUSTER}} ] [ - d ] [ {{instance_ids}} [ {{instance_ids}} ... ]]
```

## Positional Arguments
<a name="awsbatchcli.awsbhosts.arguments"></a>

**{{instance\_ids}}**
Specifies a space-separated list of instances IDs. If a single instance is requested, it is shown in a detailed version.

## Named Arguments
<a name="awsbatchcli.awsbhosts.namedarguments"></a>

**-c {{CLUSTER}}, --cluster {{CLUSTER}}**
Specifies the name of the cluster to use.

**-d, --details**
Indicates whether to show the details of the hosts.
Default: False

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
