---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/commands.html
---

# AWS ParallelCluster CLI commands
<a name="commands"></a>

`pcluster` and `pcluster-config` are the AWS ParallelCluster CLI commands. You use `pcluster` to launch and manage HPC clusters in the AWS Cloud and `pcluster-config` to update your configuration.

To use `pcluster`, you must have an IAM role with the [permissions](iam.md#example-parallelcluser-policies) required to run it.

```
pcluster [ -h ] ( create | update | delete | start | stop | status | list |
                  instances | ssh | dcv | createami | configure | version ) ...
 pcluster-config [-h] (convert) ...
```

**Topics**
+ [`pcluster`](pcluster.md)
+ [`pcluster-config`](pcluster-config.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
