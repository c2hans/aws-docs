---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/pcluster.list.html
---

# `pcluster list`
<a name="pcluster.list"></a>

Displays a list of stacks that are associated with AWS ParallelCluster.

```
pcluster list [ -h ] [ -c {{CONFIG_FILE}} ] [ -r {{REGION}} ]
```

## Named arguments
<a name="pcluster.list.namedarg"></a>

**-h, --help**
Shows the help text for `pcluster list`.

**--color**
Displays the cluster status in color.
Defaults to `False`.

**-c {{CONFIG\_FILE}}, --config {{CONFIG\_FILE}}**
Specifies the alternative configuration file to use.
Defaults to `c`.

**-r {{REGION}}, --region {{REGION}}**
Specifies the AWS Region to use. Defaults to the AWS Region specified by using the [`pcluster configure`](pcluster.configure.md) command.

Lists the name of any AWS CloudFormation stacks named `parallelcluster-*`.

**Example using AWS ParallelCluster version 2.11.7:**

```
$ pcluster list -c {{path/to/config}} -r {{us-east-1}}
mycluster            CREATE_IN_PROGRESS  2.11.7
myothercluster       CREATE_IN_PROGRESS  2.11.7
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
