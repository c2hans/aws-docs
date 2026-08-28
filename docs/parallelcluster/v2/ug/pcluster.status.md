---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.status.html
---

# `pcluster status`
<a name="pcluster.status"></a>

Pulls the current status of the cluster.

```
pcluster status [ -h ] [ -c {{CONFIG_FILE}} ] [ -r {{REGION}} ] [ -nw ] {{cluster_name}}
```

## Positional arguments
<a name="pcluster.status.posarg"></a>

**cluster\_name**
Shows the status of the cluster with the provided name.

## Named arguments
<a name="pcluster.status.namedarg"></a>

**-h, --help**
Shows the help text for `pcluster status`.

**-c {{CONFIG\_FILE}}, `--config` {{CONFIG\_FILE}}**
Specifies the alternative configuration file to use.
Defaults to `~/.parallelcluster/config`.

**-r {{REGION}}, --region {{REGION}}**
Specifies the AWS Region to use. Defaults to the AWS Region specified by using the [`pcluster configure`](pcluster.configure.md) command.

**-nw, --nowait**
Indicates not to wait for stack events after processing a stack command.
Defaults to `False`.

**Example using AWS ParallelCluster version 2.11.7:**

```
$ pcluster status -c {{path/to/config}} -r {{us-east-1}} {{mycluster}}
Status: ComputeFleetHITSubstack - CREATE_IN_PROGRESS
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
