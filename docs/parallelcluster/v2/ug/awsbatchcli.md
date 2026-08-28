---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli.html
---

# AWS Batch (`awsbatch`)
<a name="awsbatchcli"></a>

For information about AWS Batch, see [AWS Batch](https://aws.amazon.com/batch/). For documentation, see the [AWS Batch User Guide](https://docs.aws.amazon.com/batch/latest/userguide/).

**AWS ParallelCluster CLI commands for AWS Batch**

When you use the `awsbatch` scheduler, the AWS ParallelCluster CLI commands for AWS Batch are automatically installed in the AWS ParallelCluster head node. The CLI uses AWS Batch API operations and permits the following operations:
+ Submit and manage jobs.
+ Monitor jobs, queues, and hosts.
+ Mirror traditional scheduler commands.

**Important**
AWS ParallelCluster doesn't support GPU jobs for AWS Batch. For more information, see [GPU jobs](https://docs.aws.amazon.com/batch/latest/userguide/gpu-jobs.html).

**Topics**
+ [`awsbsub`](awsbatchcli.awsbsub.md)
+ [`awsbstat`](awsbatchcli.awsbstat.md)
+ [`awsbout`](awsbatchcli_awsbout.md)
+ [`awsbkill`](awsbatchcli_awsbkill.md)
+ [`awsbqueues`](awsbatchcli_awsbqueues.md)
+ [`awsbhosts`](awsbatchcli_awsbhosts.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
