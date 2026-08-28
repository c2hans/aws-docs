---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/pluster.create.html
---

# `pcluster create`
<a name="pluster.create"></a>

Creates a new cluster.

```
pcluster create [ -h ] [ -c {{CONFIG_FILE}} ] [ -r {{REGION}} ] [ -nw ] [ -nr ]
                [ -u {{TEMPLATE_URL}} ] [ -t {{CLUSTER_TEMPLATE}} ]
                [ -p {{EXTRA_PARAMETERS}} ] [ -g {{TAGS}} ]
                {{cluster_name}}
```

## Positional arguments
<a name="pluster.create.arg"></a>

**{{cluster\_name}}**
Defines the name of the cluster. The AWS CloudFormation stack name is `parallelcluster-{{cluster_name}}`.

## Named arguments
<a name="pluster.create.namedarg"></a>

**-h, --help**
Shows the help text for `pcluster create`.

**-c {{CONFIG\_FILE}}, --config {{CONFIG\_FILE}}**
Specifies the alternative configuration file to use.
Defaults to `~/.parallelcluster/config`.

**-r {{REGION}}, --region {{REGION}}**
Specifies the AWS Region to use. The priority order used to select the AWS Region for a new cluster is as follows:

1. `-r` or `--region` parameter to [`pcluster create`](#pluster.create).

1. `AWS_DEFAULT_REGION` environment variable.

1. `aws_region_name` setting in `[aws]` section of AWS ParallelCluster config file (default location is `~/.parallelcluster/config`.) This is the location updated by the [`pcluster configure`](pcluster.configure.md) command.

1. `region` setting in `[default]` section of AWS CLI config file (`~/.aws/config`.)

**-nw, --nowait**
Indicates not to wait for stack events after running a stack command.
Defaults to `False`.

**-nr, --norollback**
Disables stack rollback on error.
Defaults to `False`.

**-u {{TEMPLATE\_URL}}, --template-url {{TEMPLATE\_URL}}**
Specifies a URL for the custom AWS CloudFormation template if it was used when created.

**-t {{CLUSTER\_TEMPLATE}}, --cluster-template {{CLUSTER\_TEMPLATE}}**
Indicates the cluster template to use.

**-p {{EXTRA\_PARAMETERS}}, --extra-parameters {{EXTRA\_PARAMETERS}}**
Adds extra parameters to stack create.

**-g {{TAGS}}, --tags {{TAGS}}**
Specifies additional tags to add to the stack.

When the command is called and begins polling for the status of that call, it's safe to use "Ctrl-C" to exit. You can return to viewing the current status by calling `pcluster status mycluster`.

**Examples using AWS ParallelCluster version 2.11.7:**

```
$ pcluster create {{mycluster}}
    Beginning cluster creation for cluster: mycluster
Info: There is a newer version 3.1.4 of AWS ParallelCluster available.
Creating stack named: parallelcluster-mycluster
Status: ComputeFleetHITSubstack - CREATE_IN_PROGRESS
$ pcluster create {{mycluster}} --tags '{ {{"Key1"}} : {{"Value1"}} , {{"Key2"}} : {{"Value2"}} }'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
