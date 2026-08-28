---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/pcluster.delete-cluster-instances-v3.html
---

# `pcluster delete-cluster-instances`
<a name="pcluster.delete-cluster-instances-v3"></a>

Initiate the forced termination of all cluster compute nodes. This does not work with AWS Batch clusters.

```
pcluster delete-cluster-instances [-h]
                 --cluster-name {{CLUSTER_NAME}}
                [--debug]
                [--force {{FORCE}}]
                [--query {{QUERY}}]
                [--region {{REGION}}]
```

## Named arguments
<a name="pcluster-v3.delete-cluster-instances.namedargs"></a>

**-h, --help**
Shows the help text for `pcluster delete-cluster-instances`.

**--cluster-name, -n {{CLUSTER\_NAME}}**
Specifies the name of the cluster.

**--debug**
Enables debug logging.

**--force {{FORCE}}**
When `true`, forces the deletion by ignoring validation errors. (Defaults to `false`.)

**--query {{QUERY}}**
Specifies the JMESPath query to perform on the output.

**--region, -r {{REGION}}**
Specifies the AWS Region to use. The AWS Region must be specified, using the `AWS_DEFAULT_REGION` environment variable, the `region` setting in the `[default]` section of the `~/.aws/config` file, or the `--region` parameter.

```
$ pcluster delete-cluster-instances -n {{cluster-v3}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
