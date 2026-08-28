---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pcluster.update-compute-fleet-v3.html
---

# `pcluster update-compute-fleet`
<a name="pcluster.update-compute-fleet-v3"></a>

Updates the status of the cluster compute fleet.

```
pcluster update-compute-fleet [-h]
                 --cluster-name {{CLUSTER_NAME}}
                 --status {START_REQUESTED,STOP_REQUESTED,ENABLED,DISABLED}
                [--debug]
                [--query {{QUERY}}]
                [--region {{REGION}}]
```

## Named arguments
<a name="pcluster-v3.update-compute-fleet.namedargs"></a>

**-h, --help**
Shows the help text for `pcluster update-compute-fleet`.

**--cluster-name, -n {{CLUSTER\_NAME}}**
Specifies the name of the cluster.

**--status {START\_REQUESTED,STOP\_REQUESTED,ENABLED,DISABLED}**
Specifies the status applied to the cluster compute fleet. The statuses `START_REQUESTED` and `STOP_REQUESTED` correspond to the Slurm scheduler while the statuses `ENABLED` and `DISABLED` correspond to the AWS Batch scheduler.

**--debug**
Enables debug logging.

**--query {{QUERY}}**
Specifies the JMESPath query to perform on the output.

**--region, -r {{REGION}}**
Specifies the AWS Region to use. The AWS Region must be specified, using the `AWS_DEFAULT_REGION` environment variable, the `region` setting in the `[default]` section of the `~/.aws/config` file, or the `--region` parameter.

**Example using AWS ParallelCluster version 3.1.4:**

```
$ pcluster update-compute-fleet -n {{cluster-v3}} --status {{STOP_REQUESTED}}
{
  "status": "STOP_REQUESTED",
  "lastStatusUpdatedTime": "2022-07-12T20:19:47.653Z"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
